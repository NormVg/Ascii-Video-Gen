import cv2
import os


def video_to_frames(video_path, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Capture the video
    video = cv2.VideoCapture(video_path)
    success, frame_number = True, 0

    while success:
        success, frame = video.read()
        if success:
            # Save the frame as an image
            frame_filename = os.path.join(output_dir, f"frame_{frame_number:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            print(f"Saved {frame_filename}")
            frame_number += 1

    video.release()
    print("Finished extracting frames.")

# # Example usage
# video_path = "ac75088a634c44ac390aee0c819c89d4.mp4"
# output_dir = "frames_output"
# video_to_frames(video_path, output_dir)
