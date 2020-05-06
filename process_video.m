function [out] = process_video(v)

% v = "/Users/srishtirawal/Documents/IS/videos/TheArtOfSheepMovement-DMiC_3894lk/5/processed/output (Converted).mov"
% load video by using
 v = VideoReader(v)

% nFrames = v.NumberOfFrames;
nFrames = 50;
for i=2:nFrames
    % frame i-1
    fixed = rgb2gray(read(v,i-1));
    
    %frame i
    moving = rgb2gray(read(v,i));
    
    % apply imregdemons
    dxy{i} = imregdemons(moving,fixed,'DisplayWaitbar',false);
    
    w = waitbar(i/nFrames);
end
close(w)

out.dxy = dxy;

% compute vector norms sqrt(dx^2+dy^2)
for i=2:length(dxy)
    dr(:,:,i) = vecnorm(dxy{i},2,3);
end
    
out.dr = dr;

% compute moving average
avgWindow = 15;

for i = avgWindow:length(dxy)
    drm(:,:,i) = mean(dr(:,:,(i-avgWindow+1):i),3);
end

out.drm = drm;
out.avgWindow = avgWindow;

end