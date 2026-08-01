import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

# ==========================
# Load YOLO Model
# ==========================
model = YOLO("yolov8n.pt")

# Class names
class_names = model.names

# ==========================
# Initialize DeepSORT
# ==========================
tracker = DeepSort(max_age=30)

# ==========================
# Video Source
# ==========================
# Webcam:
cap = cv2.VideoCapture(0)

# For video file use:
# cap = cv2.VideoCapture("video.mp4")

# Check video source
if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()

# ==========================
# Video Writer
# ==========================
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps = cap.get(cv2.CAP_PROP_FPS)

# Webcam sometimes returns 0 FPS
if fps == 0:
    fps = 30

out = cv2.VideoWriter(
    "output.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (width, height)
)

print("Press ESC to quit.")

# ==========================
# Main Loop
# ==========================
while True:

    ret, frame = cap.read()

    if not ret:
        print("Video finished.")
        break

    # ======================
    # YOLO Detection
    # ======================
    results = model(frame, verbose=False)[0]

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

    # ======================
    # DeepSORT Tracking
    # ======================
    tracks = tracker.update_tracks(
        detections,
        frame=frame
    )

    # ======================
    # Draw Results
    # ======================
    for track in tracks:

        if not track.is_confirmed():
            continue

        track_id = track.track_id

        x1, y1, x2, y2 = map(
            int,
            track.to_ltrb()
        )

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"ID: {track_id}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    # ======================
    # Show Output
    # ======================
    cv2.imshow(
        "Real-Time Object Detection & Tracking",
        frame
    )

    # Save Output Video
    out.write(frame)

    # ESC key to quit
    if cv2.waitKey(1) & 0xFF == 27:
        break

# ==========================
# Cleanup
# ==========================
cap.release()
out.release()
cv2.destroyAllWindows()

print("Output saved as output.mp4")