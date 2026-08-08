# Real-Time Object Detection and Tracking

This project detects and tracks multiple objects in real time using YOLOv8, OpenCV, and DeepSORT.

The system takes video from a webcam, detects objects such as people, cars, bottles, chairs, etc., and assigns a unique ID to each detected object. The same ID is maintained while the object is being tracked.

## Features

- Real-time object detection
- Object tracking using DeepSORT
- Unique ID for every tracked object
- Displays object name along with tracking ID
- Works with webcam input
- Saves the processed video as `output.mp4`
- Uses a pre-trained YOLOv8 model

## Technologies Used

- Python
- OpenCV
- YOLOv8
- DeepSORT
- NumPy

## How It Works

The project works in the following steps:

1. OpenCV captures frames from the webcam.
2. YOLOv8 processes each frame and detects objects.
3. YOLO provides the bounding box, confidence score, and object class.
4. The detections are passed to DeepSORT.
5. DeepSORT tracks the detected objects across different frames.
6. Each tracked object receives a unique ID.
7. The object name and ID are displayed on the video.
8. The processed video is saved as `output.mp4`.

### Project Flow

Webcam
   |
   v
OpenCV
   |
   v
Video Frames
   |
   v
YOLOv8
   |
   v
Object Detection
   |
   v
DeepSORT
   |
   v
Object Tracking
   |
   v
Object Name + ID
   |
   v
Display / Save Output


## Requirements

Make sure Python is installed on your computer.

Check the Python version:

python --version

The project requires the following Python libraries:

ultralytics
opencv-python
deep-sort-realtime
numpy

## Install the required libraries
pip install ultralytics
pip install opencv-python
pip install deep-sort-realtime
pip install numpy

You can also install all dependencies together:

pip install -r requirements.txt
## requirements.txt

The requirements.txt file contains:

ultralytics
opencv-python
deep-sort-realtime
numpy
## Running the Project

Run the following command from the project folder:

python main.py

The webcam will open and the system will start detecting and tracking objects.

To stop the program, press:

ESC
Example Output

The system displays bounding boxes around detected objects.

Example:

person ID:1
person ID:2
bottle ID:3
chair ID:4

The ID helps identify the same object across different video frames.

Using a Video File

The project can also work with a video file instead of a webcam.

Place your video file inside the project folder:

ObjectTrackingProject/
│
├── main.py
├── requirements.txt
├── video.mp4
└── yolov8n.pt

In main.py, change:

cap = cv2.VideoCapture(0)

to:

cap = cv2.VideoCapture("video.mp4")

Then run:

python main.py
Output Video

The processed video is automatically saved as:

output.mp4

The output contains the detected objects, bounding boxes, object names, and tracking IDs.

YOLOv8 Model

This project uses the pre-trained:

yolov8n.pt

The model is downloaded automatically by Ultralytics when it is used for the first time.

YOLOv8 is used for object detection, while DeepSORT is used for tracking.

## Understanding the Main Components
OpenCV

OpenCV is used to:

Capture video from the webcam
Read video frames
Draw bounding boxes
Display the processed video
Save the output video
YOLOv8

YOLOv8 is responsible for detecting objects in each frame.

It provides:

Object class
Bounding box coordinates
Confidence score

For example:

Person
Confidence: 0.92
DeepSORT

DeepSORT is used to track objects between frames.

For example:

Frame 1 → Person ID:1
Frame 2 → Person ID:1
Frame 3 → Person ID:1

Even when the person moves, the tracker attempts to maintain the same ID.

## Project Structure
ObjectTrackingProject/
│
├── main.py
├── requirements.txt
├── video.mp4
├── output.mp4
└── yolov8n.pt

## File Description
| File               | Description                      |
| ------------------ | -------------------------------- |
| `main.py`          | Main Python program              |
| `requirements.txt` | Required Python libraries        |
| `video.mp4`        | Input video, if using video mode |
| `output.mp4`       | Processed output video           |
| `yolov8n.pt`       | YOLOv8 pre-trained model         |


## Applications

This type of object detection and tracking system can be used in:

Security and surveillance
Traffic monitoring
People counting
Smart city systems
Retail monitoring
Crowd analysis
Autonomous systems
Video analytics

## Future Improvements

Some possible improvements are:

Add object counting
Add line-crossing detection
Track specific object classes
Add people counting
Improve tracking accuracy
Add a graphical user interface
Use a larger YOLO model for better detection accuracy
Add real-time FPS display
Add multiple camera support

## Limitations

Performance depends on computer hardware.
Detection speed may decrease on low-end systems.
Objects can sometimes lose their tracking ID.
Poor lighting or heavy object overlap can affect detection and tracking.
The project currently uses a webcam as the default input.

## Conclusion

This project demonstrates how object detection and object tracking can be combined to process video in real time.

YOLOv8 is used to detect objects, OpenCV handles the video processing, and DeepSORT tracks the detected objects and assigns unique IDs.

The project provides a basic foundation for building more advanced computer vision applications.

## Author

Harsh Sharma
Electronics and Communication Engineering Student