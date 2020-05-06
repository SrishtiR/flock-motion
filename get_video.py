import cv2
import os
import argparse

def get_video(frame_folder):
    """
    Given path of the frame folder,
    retrieves all frames and generates video

    For the frames to be read in correct order, they 
    are named: frame0.jpg, frame1.jpg, frame2.jpg etc
    """
    os.chdir(frame_folder)
    img_array = []
    print(f"Generating video from frames in path {frame_folder}")
    for count in range(len(os.listdir(frame_folder))-1):
        filename = f"{frame_folder}/frame_{str(count)}.jpg"
        print("Reading file:", filename)
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
        out = cv2.VideoWriter('output.avi',0,5, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

def main():
    parser = argparse.ArgumentParser(
        description="TODO")
    parser.add_argument("--frames-folder",
                        type=str,
                        required=True)
    args = parser.parse_args()
    frame_folder = args.frames_folder
    get_video(frame_folder)

if __name__ == "__main__":
    main()