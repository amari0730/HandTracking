Food-Tracking Task with eECoG

*Task design
The monkey was tracking food rewards with the hand contralateral
to the implant side. ECoG data and motion data were recorded
simultaneously during the task (details in the reference). There was
no eye tracking. ECoG and motion data were sampled at 1KHz and
120Hz, respectively, with time stamps synchronized.

[Author of the database] Kentaro Shimoda
[Reference] Shimoda K, Nagasaka Y, Chao ZC, Fujii N. Decoding continuous 
three-dimensional hand trajectories from epidural electrocorticographic 
signals in Japanese macaques. J. Neural Eng. 2012 9:036015

*Locations of the markers
― LSHO: left shoulder
― LELB: left elbow
― LWRI: left wrist
― RSHO: right shoulder
― RELB: right elbow
― RWRI: right wrist

*Data Format
A. ECoG_chN.mat
ECoGData_chN: ECoG signal (μV) recorded from electrodeN (1‐64), sampled at 1kHZ.
The Location of electrode is documented in "B.png".

B. ECoG_time.mat
ECoGTime: ECoGTime is a one row-vector contains Time-stamps with the same length as ECoGData_chN.

C. Motion.mat
MotionData: MotionData is a time × marker matrix containing 3-D position of marker
-index 1, LSHO
-index 2, LELB
-index 3, LWRI
-index 4, RSHO
-index 5, RELB
-index 6, RWRI
MotionTime: MotionTime contains the corresponding time-stamps.
