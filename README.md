# MoviePy Editing Automation
An application which can automate videos together in a simple manner. Idea based off of [Devon Crawford's attempt](https://github.com/DevonCrawford/Video-Editing-Automation) in which he is using the [ffmpeg](https://ffmpeg.org/) library.

## How It Works
This project uses the [ffmpeg-python](https://github.com/kkroening/ffmpeg-python) library to handle video processing and the [PIL](http://www.pythonware.com/products/pil/) for image processing. To run this you'll need to first [install ffmpeg](https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg) and ffmpeg-python

## Directory Guide
- **src/** (source code)
- **frames/** (where color and gray frames are stored for editing. **Might take up a lot of space**)
- **imports/** (directory for all videos you want edited)
- **exports/** (this is where the final edited video is placed)

### **Do Not's**
1. **Do not** set the framerate too high if you do not have a large amount of RAM. Too many loaded frames will take up all of it.
2. **Do not** use videos that are short as it cannot yet choose the last frame if the ideal last frame is not in the video.
3. **Do not** place videos with wildly different base framerates and use a even different framerate- the program will essentially cut it out by accident.
4. **Do not** put a folder into the imports folder as it will read that but cannot access those files
5. **Do not** open up the folders created in frames/ until the program finishes as the command prompt will deny access to that folder and break

### How to Use
1. Delete all .gitkeep's in directories
2. Place desired videos into **imports/**
3. Run **editor.py** and select any variables desired
4. Wait for edited video to be created
5. Enjoy your new video