import time
import random

class Remote controller():
    def __init__(self, tv_STATUS = "off",TV_volume = =, CHANNEL_LIST=["KTN"],Channel_Name = "KTN"):


        print ("creating a remote controller..")

        self.TV_status = TV_status
        self.TV_Volume = TV_Volume
        self.Channel_List = Channel_List
        self.Channel_Name = Channel_Name

    def TV_on(self):

        if self.TV_Status == "ON":
            print("TV IS ALREDY ON...")

        else:
            print("tv is turning on...")
            self.TV_status = "ON"

    def TV_off(self):

        if self.TV_status == "OFF":
            print("TV IS ALREADY OFF..")

        else:
            print("TV iis turning off..")
            self.TV_status == "OFF"
             