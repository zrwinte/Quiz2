#Created by Zach Winters, TEC 284 Quiz 2
#Importing the required libraries
#from gpiozero import Button, LED
from gpiozero import Button, RGBLED
from time import sleep

# Setting up the GPIO pins
red_button = Button(17)
green_button = Button(27)
blue_button = Button(22)

rgb_led = RGBLED(red=23, green=24, blue=25)

# Creating my function to check button states to ensure colors display/mix accordingly!
def check_buttons():
    red = red_button.is_pressed
    green = green_button.is_pressed
    blue = blue_button.is_pressed
