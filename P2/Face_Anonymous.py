import cv2
import os
import mediapipe as mp

def detect_and_blur_faces(input_data, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Initialize MediaPipe face detection module
    mp_face_detection = mp.solutions.face_detection

    with mp_face_detection.FaceDetection(min_detection_confidence=0.5, model_selection=0) as face_detection:
        # Check if input_data is a video or image
        if isinstance(input_data, str) and input_data.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
            # Process video
            cap = cv2.VideoCapture(input_data)
            if not cap.isOpened():
                print("Error: Unable to open video.")
                return
            
            frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            out = cv2.VideoWriter(os.path.join(output_dir, "output_video.avi"),
                                  cv2.VideoWriter_fourcc(*'XVID'), fps, (frame_width, frame_height))
            
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                frame = process_frame(frame, face_detection)

                # Write the modified frame to the output video
                out.write(frame)

                cv2.imshow("Processed Video", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            out.release()
            cv2.destroyAllWindows()
            print(f"Processed video saved at: {os.path.join(output_dir, 'output_video.avi')}")

        elif isinstance(input_data, str) and input_data.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            # Process image
            img = cv2.imread(input_data)
            img = process_frame(img, face_detection)

            cv2.imshow("Processed Image", img)
            cv2.waitKey(0)

            # Save the modified image
            output_path = os.path.join(output_dir, "output_image.jpg")
            cv2.imwrite(output_path, img)
            print(f"Processed image saved at: {output_path}")

        else:
            print("Error: Unsupported input format. Please provide a video file or an image.")

def process_frame(frame, face_detection):
    H, W, _ = frame.shape
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)

    if out.detections is not None:
        for detection in out.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box

            x1, y1, w, h = int(bbox.xmin * W), int(bbox.ymin * H), int(bbox.width * W), int(bbox.height * H)

            # Blur the detected face region
            frame[y1:y1 + h, x1:x1 + w, :] = cv2.blur(frame[y1:y1 + h, x1:x1 + w, :], (50, 50))
    return frame

# Paths
input_path = os.path.join(".", "images", "Man.jpeg")  # Change to your input image or video
output_directory = "./output"

# Detect and blur faces in the image or video
detect_and_blur_faces(input_path, output_directory)
