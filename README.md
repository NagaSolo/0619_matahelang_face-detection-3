*to be moved to wiki*

### Overview
- June 19th, 2020
- repo: github.co/NagaSolo/0619_matahelang_face-detection-3
- face detection computer vision, for all time sake; completed it once in a tinkerer way

### Idea
- Computer Vision Project Idea – Face detection is a technique to find the location of the human faces in an image. 
- Computers use various types of algorithms to detect if the shape in the image resembles a face or not. 
- Build an app to automatically detect faces and capture the image in our system.

### Opportunity
- Many uses

### Progress
- download library from here: *http://libccv.org/tutorial/* -> `DONE`
    - library is full of bug
- use library -> `WIP`
- finding alternatives to `OpenCV`
    - `libcvv` too buggy
    - from scratch cv `not enough resources`

### wuhukai:
- available source on github, implementing dlib face detection and for face swap with color correction

cmd:
`python main.py --src test_imgs/src/filename.ext --dst test_imgs/dest/filename.ext --out results/output.ext --correct_color --warp_2d`

- Completing kivy app

### dlib_only
- g2geek implementation of dlib face detection on single image and on real time

cmd:
- for single images
`python face_det_img.py ––shape-predictor models/shape_predictor_68_face_landmarks.dat ––image test_imgs/src/image_name.ext`

- for rt
`python face_det_rt.py`