import commands 

CMD = "ls -l" 

status, output = commands.getstatusoutput(CMD)

print output
