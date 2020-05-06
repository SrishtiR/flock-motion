# flock-motion
Project for analyzing flock motion

# Description
This repository contains the pipeline for analyzing vidoes containing flock motion. The videos are extracted from
youtube using a keyword and count. Followed by this, different scenes detected from the each video. Each of the videos
is then analyzed to detect motion.

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

# References

# Future work
* Remove camera motion
* Extract only top view videos
