# This is simple script is use to get images
# from the Android App IPWebcam
# Developer: Michael Jalloh
############################################
# Special thanks to Peter Lunk on hackster.io


import urllib
import cv2
import time
import numpy as np
import pygame
import requests as r

pygame.init()



class IPWEBCAM(object):
    def __init__(self,root_url='192.168.2.109:8080', width=400, height=400):
        self.url = 'http://'+root_url
        self.width = width
        self.height = height
        self.resolutions = {
                "0" : "1920x1080",
                "1" : "1280x720",
                "2" : "960x720",
                "3" : "720x480",
                "4" : "640x480",
                "5" : "352x288",
                "6" : "320x240",
                "7" : "256x144",
                "8" : "176x144"
                }

    def get_image(self):
        # Get our image from the phone
        imgResp = urllib.request.urlopen(self.url + '/shot.jpg')

        # Convert our image to a numpy array so that we can work with it
        imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)

        # Convert our image again but this time to opencv format
        img = cv2.imdecode(imgNp,-1)

        return img


    def get_image_string(self,img):
        # return the image as a string, but also give out its shape(width,height) and color_space
        return (img.tostring(), img.shape[1::-1], 'RGB')

    def get_pygame_image(self):
        # Get the image
        img = self.get_image()

        # split our image color_space into blue, green, red components
        b,g,r = cv2.split(img)

        # compose our image back but this time as red, green and blue
        img = cv2.merge([r,g,b])

        # get our image in string format and also the size and color_space for pygame to Use
        img,shape,color_space = self.get_image_string(img)

        # create the pygame image from the string, size and color space
        img = pygame.image.frombuffer(img,shape,color_space)

        # resize the image
        img = pygame.transform.scale(img, (self.width, self.height))

        return img

    def swap_camera(self, option: str ="on"):
        # swap the camera from thte back to the front
        # option: on / off
        return r.get(self.url+"/settings/ffc?set={}".format(option))

    def overlay(self, option: str ="off"):
        # turn on of off the text overlay
        # option: on / off
        return r.get(self.url+"/settings/overlay?set={}".format(option))

    def led(self, option: str ="off"):
        # turn on or off the flash light
        if option =="on":
            return r.get(self.url+"/enabletorch")
        return r.get(self.url+"/disabletorch")

    def set_quality(self,option: int = 50):
        # Set the quality of the image
        # from 0 to 100
        if option > 100:
            option = 100
        if option < 0:
            option = 0
        return r.get(self.url +"/settings/quality?set={}".format(option))

    def set_orientation(self, orientation: int = 0):
        # Set the camera orientation
        # Landscape = 0
        # Portait = 1
        # Upside down = 2
        # Upside down portait = 3
        
        if orientation == 0:
            return r.get(f"{self.url}/settings/orientation?set=landscape")
        elif orientation == 1:
            return r.get(f"{self.url}/settings/orientation?set=portait")
        elif orientation == 2:
            return r.get(f"{self.url}/settings/orientation?set=upsidedown")
        elif orientation == 3:
            return r.get(f"{self.url}/settings/orientation?set=upsidedown_portait")

    def set_resolution(self, option: str = "0"):
        if option in self.resolutions:
            return r.get(f"{self.url}/settings/video_size?set={self.resolutions[option]}")

    def zoom(self, option: int = 0):
        if option < 0:
            option = 0
        if option > 100:
            option = 100
        return r.get(f"{self.url}/ptz?zoom={option}")
        
