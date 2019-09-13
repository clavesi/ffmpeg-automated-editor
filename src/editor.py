import os
import ffmpeg
from PIL import Image
from statistics import mean
import subprocess
import shutil
from random import randint
import time

start_time = time.time() # how long does it take to calculate averages
videos = os.listdir('imports/')
finframe_list = [] # global variable
vidavg_list = [] # global varialbe

# TODO Take arguments
# TODO Catch errors

# Delete all .gitkeeps
if os.path.exists('exports/.gitkeep'):
    os.remove('exports/.gitkeep')
    os.remove('frames/color/.gitkeep')
    os.remove('frames/final/.gitkeep')
    os.remove('frames/gray/.gitkeep')
    os.remove('imports/.gitkeep')

# Generate colored and grayscale frames for all videos
def genframes():
    # Generate color frames
    for video in range(len(videos)):
        print(videos[video])
        if os.path.exists(f'frames/color/video-{video}'):
            shutil.rmtree(f'frames/color/video-{video}')
            os.mkdir(f'frames/color/video-{video}')
        else:
            os.mkdir(f'frames/color/video-{video}')
        subprocess.run(f'ffmpeg -i imports/{videos[video]} -vf fps=15/1 frames/color/video-{video}/frame%04d.jpg -hide_banner')

    # Generate grayscale frames
    for video in videos:
        if os.path.exists(f'frames/gray/video-{videos.index(video)}'):
            shutil.rmtree(f'frames/gray/video-{videos.index(video)}')
            os.mkdir(f'frames/gray/video-{videos.index(video)}')
        else:
            os.mkdir(f'frames/gray/video-{videos.index(video)}')
        (
            ffmpeg
            .input(f'frames/color/video-{videos.index(video)}/frame%04d.jpg')
            .hue(s=0)
            .output(f'frames/gray/video-{videos.index(video)}/frame%04d.jpg')
            .overwrite_output()
            .run()
        )
genframes()

# Calculate frame averages and return start and end value
def avgframes():
    folders = os.listdir('frames/gray')
    numframes = 0
    totalavg = []
    global finframe_list
    global vidavg_list
    framerate = 30 # FIXME set framerate equal to argparse

    # Check chunks of every frame in the frames folder
    for folder in folders:
        vidfold = os.listdir(f'frames/gray/{folder}')
        vidavg = []
        totalframes = [] # just for curosity purposes
        global vidavg_list # first frame of clip
        global finframe_list # last frame of clip
        i = 0
        print(f'Calculating frame chunks for {folder}')
        for frame in vidfold:
            chunk = [] # Reset chunks for each frame
            currentframe = Image.open(f'frames/gray/{folder}/{vidfold[i]}')
            i += 1
            pixel = currentframe.load()
            totalframes.append(currentframe)

            for y in range(currentframe.size[1]): # check every y value
                if y % 9 == 5: # but only every 5th out of 9th
                    for x in range(currentframe.size[0]):
                        if x % 9 == 5:
                            chunk.append(pixel[x, y])
            numframes += 1
            
            # Get gray value of each chunk's pixel and divide by 255 to get 0-1 scale
            chunkavg = mean([i[0] for i in chunk])/225
            vidavg.append(chunkavg)
            chunkmax = max(vidavg)
            totalavg.append(chunkavg)
        
        print('avg:', mean(totalavg))
        print('max:', chunkmax)
        print(vidavg.index(chunkmax))
        print(f'Video is {len(vidavg)} frames long')

        # Vary clip lengths
        finframe = (randint(3, 7) * framerate) + vidavg.index(chunkmax)
        finframe_list.append(finframe)
        vidavg_list.append(vidavg.index(chunkmax))
        print('Final frame would be:', finframe)

        print(f'--- {time.time() - start_time} seconds ---')
        print()

    print(mean(totalavg))
    print(max(totalavg))
    print('# of frames:', numframes)
    print(vidavg_list)
    print(finframe_list)
avgframes()

# Save all frames to the frames/final folder for combining
def saveframes():
    i = 0
    for video in videos:
        (
            ffmpeg
            .input(f'frames/color/video-{videos.index(video)}/frame%04d.jpg')
            .output(f'frames/final/vid{i}-frame%04d.jpg')
            .overwrite_output()
            .run()
        )
        i += 1
saveframes()

# Export clips and combine them
def exportvideo():
    i = 0
    # Export frames into videos
    for video in videos:
        (
            ffmpeg
            .input(f'frames/final/vid{i}-frame%04d.jpg')
            .output(f'exports/video{i+1}.mp4', framerate=30)
            .overwrite_output()
            .run()
        )
        i += 1

    # Combine all those new videos
    exports = os.listdir('exports/')
    global vidavg_list
    global finframe_list
    print(vidavg_list)
    print(finframe_list)

    for video in exports:
        exports = os.listdir('exports/')
        if not(len(exports) == 1): # Checks if the final output is the only one left
            if exports[0] == 'export.mp4':
                 # rename to allow code to continue as it cannot replace it with the same name
                os.rename(f'exports/{exports[0]}', f'exports/vid0.mp4')
                exports = os.listdir('exports/')

            if not exports[0] == 'vid0.mp4': # If two clips have NOT been combined yet
                vid0 = ffmpeg.input(f'exports/{exports[0]}', ss=vidavg_list[0]/30, t=finframe_list[0]/30 - vidavg_list[0]/30)
                vid1 = ffmpeg.input(f'exports/{exports[1]}', ss=vidavg_list[1]/30, t=finframe_list[1]/30 - vidavg_list[1]/30)
                (
                    ffmpeg
                    .concat(
                        vid0,
                        vid1,
                    )
                    .output('exports/export.mp4', framerate=30)
                    .run()
                )
                vidavg_list.pop(1) # as videos get combined,
                vidavg_list.pop(0) # remove their first and last frame positions
                finframe_list.pop(1)
                finframe_list.pop(0)
            else: # If two clips HAVE been combined
                vid0 = ffmpeg.input(f'exports/{exports[0]}')
                vid1 = ffmpeg.input(f'exports/{exports[1]}', ss=vidavg_list[0]/30, t=finframe_list[0]/30 - vidavg_list[0]/30)
                if len(vidavg_list) > 1 and len(finframe_list) > 1:
                    vidavg_list.pop(0)
                    finframe_list.pop(0)
                (
                    ffmpeg
                    .concat(
                        vid0,
                        vid1,
                    )
                    .output('exports/export.mp4', framerate=30)
                    .run()
                )
            # The newly created 'export.mp4' does not get counted yet in the exports list.
            os.remove(f'exports/{exports[1]}')
            os.remove(f'exports/{exports[0]}') # Delete [1] first so it can delete [0]
        else:
            print('All videos edited together!')
exportvideo()

def cleanup(): # TODO Delete video frame folders
    print('blank')
cleanup()