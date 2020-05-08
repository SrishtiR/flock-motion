# flock-motion
Project for analyzing flock motion

# Description
This project deals with analyzing and marking specific flocking movements from animals in general swarm behavioral videos for these animals. The project uses a plethora of Youtube videos involving swarm movements of animals including sheep, buffaloes, aquatic life etc. Then the python functions, built by the shell script, will mark the frames in the videos, with a clear view of animal flocking behavior, with a red outline around the animal flocks. The intensity of the red depicts the amount of animal movement happening in the flock.

This repository contains the pipeline for analyzing vidoes containing flock motion. The videos are extracted from
youtube using a keyword and count. Followed by this, different scenes detected from each video. Each of the videos
is then broken into frames and flocking motion is then mapped into red fragments within the video; utilizing various computer vision and video analyzing Python frameworks, in particular OpenCV and Dense Optical Video Motion Detection.



# Clone
`git clone https://github.com/SrishtiR/flock-motion.git`

# Setup
pip install -r requirements.txt

# Usage
Step 1: Give chmod 777 permissions to the shell script run.sh <br>
Step 2: From command line run the following- <br>
`python3 video_frame_generate.py --key-word "flocking sheep top view" --count 5` <br>
Step 3: Update the arguments in run.sh to suit your needs <br>
Step 4: Run run.sh from command line

For the third step, update the file paths with the new video locations prior to running run.sh, and also ensure that separate folder creation lines are included in the aforementioned shell script for frames based on the different videos downloaded. 

# Future work
* Remove camera motion
* Extract only top view videos
