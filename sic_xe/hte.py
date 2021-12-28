import sys
import re
filename = f"problems\hte.txt"
array = []
#H/NAME:6BITS/START:6BITS/LENGTH:6BITS(MAIN_LAST_END-MAIN_FIRST_START)
#T/START:6BITS/LENGTH:2BITS(LAST_END-LAST_START)/OBJCODE
#E/START:6BITS
with open(filename) as f:
    for line in f:
        if re.match(r'[ \t]', line):  # replace 2tabs to 1tab
            line = line.replace("\t\t", "\t")
        if(line.split("\t")[1] == "START"):  # start
            array.append(["H"][line.split("\t")[1]][])