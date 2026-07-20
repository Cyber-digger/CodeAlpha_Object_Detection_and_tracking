import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

# Load YOLO model
model = YOLO("yolov8n.pt")

# Get class names
class_names = model.names

# Initialize DeepSORT
tracker = DeepSort(max_age=30)

# Open webcam
cap = cv2.VideoCapture(0)

# Video Saving Setup
width = int(cap.get(3))
height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))

if fps == 0:
    fps = 30

out = cv2.VideoWriter(
    "output.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (width, height)
)

# Dictionary to store labels for track IDs
track_labels = {}

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)[0]

    detections = []

    for box in results.boxes:

        x1, y1, x2, y2 = box.xyxy[0]

        confidence = float(box.conf[0])

        class_id = int(box.cls[0])

        label = class_names[class_id]

        detections.append(
            (
                [
                    float(x1),
                    float(y1),
                    float(x2 - x1),
                    float(y2 - y1)
                ],
                confidence,
                label
            )
        )

    tracks = tracker.update_tracks(
        detections,
        frame=frame
    )

    for track in tracks:

        if not track.is_confirmed():
            continue

        track_id = track.track_id

        x1, y1, x2, y2 = map(
            int,
            track.to_ltrb()
        )

        # Get label from DeepSORT detection info
        try:
            label = track.get_det_class()
        except:
            label = "object"

        # Store label for this track
        track_labels[track_id] = label

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"{track_labels[track_id]} ID:{track_id}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.imshow(
        "Real-Time Object Detection & Tracking",
        frame
    )

    out.write(frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Output video saved as output.mp4")