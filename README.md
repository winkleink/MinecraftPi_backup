# MinecraftPi_backup
Backup MinecraftPi worlds on exit

My kids love building houses and cities in Minecraft on the Raspberry Pi and I'd forget to manually backup their work before re-imaging the SD because of something I want to do losing all their hard work.

These files with a change to the menu item in Raspbian will solve the problem
minec.sh is the script that runs minecraft and then after minecraft is shutdown it runs the backup script

ftpzipminecraft.py is the backup script
It first does a recursive archiving of the .minecraft directory to a single file with the name 
Filename minecraft followed by year, month, day, hour, minutes
In this way each backup will be unique

Then the file is ftp to another server so that even if the SD card is reformatted the backup will be preserved.

