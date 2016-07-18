#!/usr/bin/python3
# Script to backup the MinecraftPi worlds and then upload them to an FTP server
# By Winkleink (July 2016)
# https://github.com/winkleink/MinecraftPi_backup
# MIT Licence
# This is a quick fix so use at your peril
import os
import zipfile
import datetime

import ftplib

now = datetime.datetime.now()
year= str(now.year)
month = str(now.month)
day = str(now.day)
hour = str(now.hour)
minute= str(now.minute)

uploadfile = "minecraft"+year+"-"+month+"-"+day+"-_-"+hour+"-"+minute+".tar.gz"

print(uploadfile)
os.system ("tar zcvf " + uploadfile + " /home/pi/.minecraft/games/com.mojang")

# Enter your FTP Server Name or IP address, Username and Password in the following line
session = ftplib.FTP("FTP SERVER NAME/IP ADDRESS","USERNAME","PASSWORD")
file = open("/home/pi/"+uploadfile, "rb")
session.storbinary("STOR " + uploadfile, file)
file.close()
session.quit()
print("Done")



