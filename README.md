# ChuteAI
Bi-directional feedback system for bouldering chute classification

Bouldering is a term associated with rock climbing without the use of ropes. Whether it be outdoor bouldering or indoor bouldering, there are crash pads under the climber which will cushion the impact from a potential fall. However, even with pads present it is incredibly important to have the correct form while falling and landing in order to avoid injury. A lot of amateur climbers are not familiar with the proper technique, which has resulted in severe injuries in the past. ChuteAI is a platform which diagnoses a rock climber’s falling technique, while also allowing the user to define what it means to have a correct falling technique. In this sense, it is a dual-feedback system. It allows experienced climbers to tell the AI what it means to fall and land correctly, while also giving inexperienced climbers the opportunity to understand how they can better improve their own technique. The implementation of such a platform in the rock climbing industry could significantly reduce an amateur climber’s chance of injury.

There are two primary modes of operation for a user of this system. The first is the testing and user feedback mode. This can be used by an amateur climber that would like some feedback about how their fall performance was, based on their own sensor input. Their performance is separated into two scores: the falling and landing scores. Each of these scores is accompanied by some feedback comments so that the user is able to understand how they can improve their technique. They also include some information as to how the AI came to determine those scores. The second is the training and AI feedback mode. Although the AI is already trained, we want to give a user the ability to input their own data and re-train the network. This could be used by a professional climber or instructor who might like to input their own training data, turning this AI into an interactive learner that learns from demonstration. The climber in this case would determine how well the AI is able to classify their data based on the output analysis, then correct and retrain the AI if the classification is not accurate enough. If they agree with the classification, they can retrain the AI with that same data and labeled outputs, thereby reinforcing it.

ChuteAI helps the users and the users help ChuteAI. It's a powerful diagnostic tool, which can also be reinforced and improved.


### Data Acquisition

ChuteAI uses a battery-powered Adafruit Feather 32u4 Adalogger for data acquisition. This is connected to an MPU6050 IMU via I2C to collect gyroscope and accelerometer data, which is stored on a Micro-SD card. These are mounted on a breadboard and attached to a belt, which the user mounts to their midriff with the SD card pointed down. When the Adalogger is reset, the onboard LED will flash 3 times, indicating that data collection is starting. On the fourth flash the LED stays on, and 4 seconds of data is collected as the user falls and lands. The LED turns off when data acquisition is complete.

<img src="https://github.com/loicmaxwell17/ChuteAI/blob/master/Images/IMG_5147.JPG" width="300"/>
<img src="https://github.com/loicmaxwell17/ChuteAI/blob/master/Images/IMG_5148.JPG" width="300"/>

Once data is collected, the SD card is removed
