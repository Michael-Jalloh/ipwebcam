# This is simple script is use to get images
# from the Android App IP Webcam
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
    def __init__(self,root_url='192.168.43.1:8080', width=400, height=400):
        self.url = 'http://'+root_url
        self.width = width
        self.height = height

    def get_image(self):
        # Get our image from the phone
        imgResp = urllib.urlopen(self.url + '/shot.jpg')

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

    def swap_camera(self, option="on"):
        return r.get(self.url+"/settings/ffc?set={}".format(option))

    def overlay(self, option="off"):
        return r.get(self.url+"/settings/overlay?set={}".format(option))

    def led(self, option="off"):
        if option =="on":
            return r.get(self.url+"/enabletorch")
        return r.get(self.url+"/disabletorch")

    def set_quality(self,option=50):
        if option > 100:
            option = 100
        if option < 0:
            option = 0
        return r.get(self.url +"/settings/quality?set={}".format(option))

    def zoom(self, option):
        pass
