# Motion Detection with Alarm using OpenCV

A simple motion detection system that analyzes webcam feed and triggers an alarm sound when movement is detected. Built with **OpenCV** and **Python**.

---

## Features

- Detects motion using frame differencing and contour analysis.
- Draws bounding boxes around detected motion.
- Plays an alarm sound when movement is detected.
- Displays real-time video feed with motion highlights.
- Easy to extend for buzzer control (Arduino/Raspberry Pi GPIO).

---

##  Requirements

- Python 3.x  
- Webcam  
- Alarm sound file (`alarm.mp3`)

### Python Libraries
Install dependencies:
```bash
pip install opencv-python playsound
```

## Setup

1-Clone or download this repository.

2-Place an alarm sound file named alarm.mp3 in the project directory.

3- Run the program:

```bash
python motion_detector.py
```
4-Press q to quit the program.

## How It Works

The script captures video feed from your webcam.

It compares two consecutive frames to detect differences.

The difference image is processed to find contours of moving objects.

If a contour exceeds a set area threshold, motion is detected.

The script draws bounding boxes around motion and plays an alarm sound.


## Customization

Contour Area Threshold:
Change 2000 in the script to make motion detection more or less sensitive.

Alarm Sound:
Replace alarm.mp3 with your preferred sound file.
