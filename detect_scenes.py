import cv2
import csv, os
import argparse
import scenedetect
from scenedetect.video_manager import VideoManager
from scenedetect.scene_manager import SceneManager
from scenedetect.frame_timecode import FrameTimecode
from scenedetect.stats_manager import StatsManager
from scenedetect.detectors import ContentDetector

MAX_FRAMES = 100

def get_frames_from_scenes(video_name, frame_number_start, frame_number_end, frames_path, index):
    """
    Function that generates a set of images from a video based on frame number
    Params: starting frame number and ending frame number
    """
    video_dir = "".join(video_name.split(".")[0]).replace(" ", "")
    if not os.path.exists(video_dir):
        os.makedirs(video_dir)
    frames_path = os.getcwd() + "/" + video_dir + "/" + str(index)
    if not os.path.exists(frames_path):
        os.makedirs(frames_path)
    print(f"Generating frames from scenes in path: {frames_path}")
    cap = cv2.VideoCapture(video_name)
    total_frames = cap.get(7)
    i = frame_number_start
    while i < frame_number_start + MAX_FRAMES:
        try:
            cap.set(1, i)
            ret, frame = cap.read()
            cv2.imwrite(f"{frames_path}/frame_"+str(i-frame_number_start)+".jpg", frame)
            i += 1
        except cv2.error as e:
            break

def video_scene_detect(video_name, stats_file_name, file_name, video_path):
    """
    returns a list of scenes
    https://pyscenedetect.readthedocs.io/en/latest/examples/usage-python/
    https://github.com/Breakthrough/PySceneDetect/blob/master/scenedetect/video_manager.py
    """
    os.chdir(video_path)
    os.system(f"scenedetect --input \
    '{video_name}' --stats {stats_file_name} \
    detect-content --threshold 27")
    video_manager = VideoManager([video_name])
    stats_manager = StatsManager()
    scene_manager = SceneManager(stats_manager)
    scene_manager.add_detector(ContentDetector())
    base_timecode = video_manager.get_base_timecode()

    try:
        if os.path.exists(stats_file_name):
            with open(stats_file_name, 'r') as stats_file:
                stats_manager.load_from_csv(stats_file, base_timecode)
        start_time = base_timecode + 10    # set start time
        end_time = base_timecode + 200000.0 #set end_time
        video_manager.set_duration(start_time=start_time, end_time=end_time)
        video_manager.set_downscale_factor()
        video_manager.start()
        scene_manager.detect_scenes(frame_source=video_manager)
        scene_list = scene_manager.get_scene_list(base_timecode)
        final_scene_list = []
        for i, scene in enumerate(scene_list):
            print('Scene %2d: Start %s / Frame %d, End %s / Frame %d' % (
                i+1,
                scene[0].get_timecode(), scene[0].get_frames(),
                scene[1].get_timecode(), scene[1].get_frames(),))
            final_scene_list.append({
                "scene_num": i+1,
                "start": scene[0].get_timecode(),
                "end": scene[0].get_frames(),
                "start_frame": scene[0].get_frames(),
                "end_frame": scene[1].get_frames()
            })
        if stats_manager.is_save_required():
            with open(file_name, 'w') as stats_file:
                stats_manager.save_to_csv(stats_file, base_timecode)
    finally:
        video_manager.release()
    return final_scene_list

def main():
    parser = argparse.ArgumentParser(
        description="TODO")
    parser.add_argument("--video-name",
                        type=str,
                        required=True)
    parser.add_argument("--video-path",
                        type=str,
                        help="The path of video",
                        required=False)
    args = parser.parse_args()
    video_name = args.video_name
    video_path = args.video_path
    stats_file_name_extension = video_name.split(".")[0].replace(" ", "")
    file_name = f'{stats_file_name_extension}.csv'
    scene_file_name = f'{stats_file_name_extension}.txt'
    cwd = os.getcwd()
    scene_list = video_scene_detect(video_name, file_name, scene_file_name, video_path)
    for each in range(len(scene_list)):
        get_frames_from_scenes(video_name, scene_list[each]["start_frame"], scene_list[each]["end_frame"], cwd, each)
    # get_frames_from_scenes(video_name, scene_list[5]["start_frame"], scene_list[5]["end_frame"], cwd, 5)
    # get_video(frame_folder)
    # https://github.com/AdamSpannbauer/python_video_stab

if __name__ == "__main__":
    main()

