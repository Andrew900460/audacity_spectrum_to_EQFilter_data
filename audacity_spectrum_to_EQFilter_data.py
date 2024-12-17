import math
import sys

fileInput = sys.argv[1]
print("")

with open(fileInput,"r") as file:
    content = file.read()

lines = content.splitlines()
total_points = len(lines)
skip = 0
# We have to limit how many points we use, becuse it seems that the Filter Curve only allows a limited number of points.
# Idk what the actual limit is, but it appeared to be about 200. Hence that number.
if(total_points > 200):
    skip = math.ceil(total_points / 200)

new_total_points = total_points//skip

lines2 = []

i2 = 0
for i in range(0,total_points,skip):
    tabIndex = lines[i].index('\t')
    freq = lines[i][0:tabIndex]
    vol = lines[i][tabIndex+1:]
    lines2.append("f"+str(i2)+"=\""+freq+"\" v"+str(i2)+"=\""+vol+"\"")
    i2+=1

print(" ".join(lines2))
