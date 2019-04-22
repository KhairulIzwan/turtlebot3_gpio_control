# turtlebot3_gpio_control

# IMPORTANT! (FIRST STEP)
##  RPi.GPIO Installation
### Raspbian Wheezy
1.  sudo apt-get update
2.  sudo apt-get install python-rpi.gpio python3-rpi.gpio

### Other Distributions
1.  sudo apt-get update
2.  sudo pip install RPi.GPIO

## Installing the turtlebot3_gpio_control
1.  cs -- or -- cd ~/catkin_ws/src
2.  git clone https://github.com/KhairulIzwan/turtlebot3_gpio_control.git
3.  cm -- or -- cd ~/catkin_ws/
4.  rospack profile ---> to ensure the package; executed node available (updated)

### In-case get error; due to package dependencies, run:
1.  rosdep install --from-paths src --ignore-src -r -y
2.  cm -- or -- cd ~/catkin_ws/ 
### This usecase shows even more powerful feature of rosdep. This command magically installs all the packages that the packages in your catkin workspace depend upon but are missing on your computer.


# LED Blink Example:
## RasPi Pinout
![alt text](https://cdn.sparkfun.com/assets/learn_tutorials/4/2/4/header_pinout.jpg)

1.  Connect the LED (Cathode -- Ground (PIN#06), Anode -- GPIO18 (PIN#12))
2.  roscore (REMOTE PC) ---
3.  rosrun turtlebot3_gpio_control blink_LED.py (RasPi -- TURTLEBOT3 PC)
4.  rostopic pub /led_blink ool "data: false" --- turn "OFF" the LED
### or
4.  rostopic pub /led_blink ool "data: true" --- turn "ON" the LED
