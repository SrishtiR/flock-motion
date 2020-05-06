python3 detect_scenes.py --video-name "Mesmerising Mass Sheep Herding-tDQw21ntR64.mp4" --video-path "videos"
python3 detect_scenes.py --video-name "The Art Of Sheep Movement-DMiC_3894lk.mp4" --video-path "videos"

python3 get_video.py --frames-folder "/Users/srishtirawal/Documents/IS/videos/MesmerisingMassSheepHerding-tDQw21ntR64/3"
python3 dense_optical_flow.py --video-path "/Users/srishtirawal/Documents/IS/videos/MesmerisingMassSheepHerding-tDQw21ntR64/3"
python3 get_video.py --frames-folder "/Users/srishtirawal/Documents/IS/videos/MesmerisingMassSheepHerding-tDQw21ntR64/3/processed"

python3 get_video.py --frames-folder "/Users/srishtirawal/Documents/IS/videos/TheArtOfSheepMovement-DMiC_3894lk/8"
python3 dense_optical_flow.py --video-path "/Users/srishtirawal/Documents/IS/videos/TheArtOfSheepMovement-DMiC_3894lk/8"
spython3 get_video.py --frames-folder "/Users/srishtirawal/Documents/IS/videos/TheArtOfSheepMovement-DMiC_3894lk/8/processed"


python3 get_video.py --frames-folder "/Users/srishtirawal/Documents/IS/videos/TheArtOfSheepMovement-DMiC_3894lk/5"
python3 dense_optical_flow.py --video-path "/Users/srishtirawal/Documents/IS/videos/TheArtOfSheepMovement-DMiC_3894lk/5"
python3 get_video.py --frames-folder "/Users/srishtirawal/Documents/IS/videos/TheArtOfSheepMovement-DMiC_3894lk/5/processed"
