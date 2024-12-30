import cv2
import os
from tqdm import tqdm
def create_video_from_frames(sample_video_path, frames_folder, output_video_path):
    # Open the sample video to get the frame rate and frame size
    cap = cv2.VideoCapture(sample_video_path)
    
    if not cap.isOpened():
        print("Error: Unable to open sample video.")
        return
    
    # Get the frame rate (fps) and frame size from the sample video
    fps = cap.get(cv2.CAP_PROP_FPS)
    # frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_files = sorted([f for f in os.listdir(frames_folder) if f.endswith(('.png', '.jpg', '.jpeg'))])
    first_frame_path = os.path.join(frames_folder, frame_files[0])
    first_frame = cv2.imread(first_frame_path)
    
    if first_frame is None:
        print(f"Error: Couldn't read the first frame at {first_frame_path}")
        return
    frame_height, frame_width, _ = first_frame.shape
    cap.release()  # Close the video file

    # Get a list of image files in the frames folder, sorted by name

    if not frame_files:
        print("Error: No images found in the folder.")
        return

    # Create a VideoWriter object to write the frames into a video file
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 video
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    # Loop through the image files and write them to the video
    for frame_file in tqdm( frame_files):
        frame_path = os.path.join(frames_folder, frame_file)
        frame = cv2.imread(frame_path)
        
        if frame is None:
            print(f"Warning: Couldn't read frame {frame_file}. Skipping.")
            continue
        
        frame = cv2.resize(frame, (frame_width, frame_height))  # Resize to match video resolution
        out.write(frame)

    # Release the VideoWriter object and finalize the video file
    out.release()
    print(f"Video saved to {output_video_path}")

# Example usage
# create_video_from_frames("./ac75088a634c44ac390aee0c819c89d4.mp4", "image-2-ascii-frames", "output_videoji.mp4")
