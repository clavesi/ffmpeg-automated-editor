# MoviePy Editing Automation
An application which can automate videos together in a simple manner. Idea based off of [Devon Crawford's attempt](https://github.com/DevonCrawford/Video-Editing-Automation) in which he is using the [ffmpeg](https://ffmpeg.org/) library.

## How It Works
This project uses the [ffmpeg-python](https://github.com/kkroening/ffmpeg-python) library to handle video processing and the [PIL](http://www.pythonware.com/products/pil/) for image processing. To run this you'll need to first [install ffmpeg](https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg) and ffmpeg-python

## Directory Guide
- **src/** (source code)
- **frames/** (where color and gray frames are stored for editing. **Might take up a lot of space while program runs, deletes automatically when finished**)
- **imports/** (directory for all videos you want edited)
- **exports/** (this is where the final edited video is placed)

### **Do Not's**
1. **Do not** place videos with wildly different base framerates and use a even different framerate- the program will essentially cut it out by accident.
2. **Do not** put a folder into the imports folder as it will read that but cannot access those files
3. **Do not** open up the folders created in frames/ until the program finishes as the command prompt will deny access to that folder and break

### How to Use
1. Place desired videos into **imports/**, ensuring that the filenames have **no spaces**
2. Run **editor.py** and select any variables desired
3. Wait for edited video to be created
4. Enjoy your new video

### Arguments
| Arg      | Desc          |
| -------- |:-------------:|
| -fps     | framerate of the video [int] <br> default=30|
| -cs      | size for each frame chunk, <br>xth out of every y pixels, <br>smaller will take longer [x:y]<br> default=5:9|
| -r       | resolution of the final video [w:h]  <br> default=30 |