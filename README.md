![image](HACK4TKM.jpeg)


# {FreshGuard} - HACK4TKM


## Team Members
[1.Kushal Partani](https://github.com/Kushal7551)   
[2.Siddharth Chauhan](https://github.com/SiddharthChauhan303)   
[3.Pranav Bhutada](https://github.com/pranav243)   
[4.Yash Gupta](enter_github_id_here)   

## Link to Project
[Embed the live link of project](live_link)

## How it Works ?
Integration of gas sensors for real-time monitoring of food freshness.

Utilization of machine learning algorithms to analyze sensor data.

Threshold-based assessment for determining food edibility.

Empowering consumers and industries with proactive food management solutions.
Embed video of project demo

## Technologies used
python 
Pytorch 
Tensorflow
Pyserial
Numpy
Pandas
Flutter
Arduino 

## How to configure
Connect the sensor pins to the multiplexer and the multiplexer pin to the 
Arduino analog pin.

Rest pins are connected with ground and VDD/5V of Arduino, 1 group sensor consisting of 4 different sensors is connected through SDA SCL pins.

Now through pyserial communications the values of arduino are stored in computer and then a python script runs the model which push the prediction(accuracy score) and the sensors values to the firebase databse.

Run the client side with the flutter dependencies to run the client side code.


## How to Run

python 1.py

flutter run

## Other Links

[Figma Design](https://www.figma.com/file/vSlhdRPibICLGY52UaBiiS/E-Nose?type=design&node-id=0%3A1&mode=design&t=WVgRZWYonVnD5Ysr-1)
