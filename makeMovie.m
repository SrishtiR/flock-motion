function [] = makeMovie(v,out,filename)

w = VideoWriter(filename);
open(w)
v = VideoReader(v)
nFrames = 50;

figure,
for i = out.avgWindow:nFrames
    
    imshow(read(v,i))
    hold on
    imagesc(-out.drm(:,:,i),'AlphaData',0.5)
    colormap hot
    
    frame = getframe;
    writeVideo(w,frame);
    
end


close(w)


end

