import commands 

CMD = "fswebcam -r 320x240 -d /dev/video0 testpic.jpg -D2 -F0" 

status, output = commands.getstatusoutput(CMD)

print output
