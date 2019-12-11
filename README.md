# ChuteAI
Bi-directional feedback system for bouldering chute classification

Bouldering is a term associated with rock climbing without the use of ropes. Whether it be outdoor bouldering or indoor bouldering, there are crash pads under the climber which will cushion the impact from a potential fall. However, even with pads present it is incredibly important to have the correct form while falling and landing in order to avoid injury. A lot of amateur climbers are not familiar with the proper technique, which has resulted in severe injuries in the past. ChuteAI is a platform which diagnoses a rock climber’s falling technique, while also allowing the user to define what it means to have a correct falling technique. In this sense, it is a dual-feedback system. It allows experienced climbers to tell the AI what it means to fall and land correctly, while also giving inexperienced climbers the opportunity to understand how they can better improve their own technique. The implementation of such a platform in the rock climbing industry could significantly reduce an amateur climber’s chance of injury.

There are two primary modes of operation for a user of this system. The first is the testing and user feedback mode. This can be used by an amateur climber that would like some feedback about how their fall performance was, based on their own sensor input. Their performance is separated into two scores: the falling and landing scores. Each of these scores is accompanied by some feedback comments so that the user is able to understand how they can improve their technique. They also include some information as to how the AI came to determine those scores. The second is the training and AI feedback mode. Although the AI is already trained, we want to give a user the ability to input their own data and re-train the network. This could be used by a professional climber or instructor who might like to input their own training data, turning this AI into an interactive learner that learns from demonstration. The climber in this case would determine how well the AI is able to classify their data based on the output analysis, then correct and retrain the AI if the classification is not accurate enough. If they agree with the classification, they can retrain the AI with that same data and labeled outputs, thereby reinforcing it.

ChuteAI helps the users and the users help ChuteAI. It's a powerful diagnostic tool, which can also be reinforced and improved.


### Data Acquisition

ChuteAI uses a battery-powered Adafruit Feather 32u4 Adalogger for data acquisition. This is connected to an MPU6050 IMU via I2C to collect gyroscope and accelerometer data, which is stored on a Micro-SD card. These are mounted on a breadboard and attached to a belt, which the user mounts to their midriff with the SD card pointed down. When the Adalogger is reset, the onboard LED will flash 3 times, indicating that data collection is starting. On the fourth flash the LED stays on, and 4 seconds of data is collected as the user falls and lands. The LED turns off when data acquisition is complete.

<img src="https://github.com/loicmaxwell17/ChuteAI/blob/master/Images/IMG_5147.JPG" width="300"/>
<img src="https://github.com/loicmaxwell17/ChuteAI/blob/master/Images/IMG_5148.JPG" width="300"/>

Once data is collected, the SD card is removed. The data stored in the .csv file in the SD card will be transferred to a local directory in a PC for analysis.

### Data Analysis

The backend server is written using Flask framework. The user can open the flask_interface.py by typing in 
    
    set FLASK_APP=flask_interface.py
    flask run

to initialize it. Then in a web browser navigate to localhost:5000 to open the frontend UI. The UI looks like this.


On the left handside is the User Performance UI which demonstrate how the user performs in a particular fall; on the right handside is the AI retrain UI from which ChuteAI gets new corrected data and get itself retrained. The user can click the button at the center bottom to select the directory of the .csv data file. And on the User Performance interface click the "Show Performance" button, and waveform and the comments regarding the performance of the falling will appear. The waveform consists of acceleration in y-direction and gyroscope reading in x and z-direction and the user can switch between them by clicking on the waveform graph. The grading system is defined as the following:
    
   Falling - left, right, center (center being good, left and right are bad)
   Landing - good, bad, N/A (N/A when the fall was bad)
   
Despite the grading, the user will also receive feedback from ChuteAI including the suggestion to the next fall and how ChuteAI interpret the waveform graph (i.e. what kind of waveform does ChuteAI see as a good fall/land). If the user thinks that his performance is different than what ChuteAI has interperted, he can easily make changes to retrain ChuteAI by typing in the grading classification he thinks is correct on the right UI and click the "Retrain" button. Once the retrain process is successful, a "retrain successful" message will pop up and the user can use the retrained AI for further analysis. Usually, this retrain process is done by a professional climber, and amateur users only need the User Performance UI on the left side.

### Built With

Python 3.6-language for backend server
Flask-framework for backend server
Tensorflow-model for the AI
HTML5, CSS3, JavaScript-language for frontend UI
Jquery-library for frontend UI
Pycharm-project management

### Authors

Loic Maxwell-AI building, training, and data collection
Weiting Ji-frontend UI designing and building
