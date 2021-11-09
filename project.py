import sys
import re
filename = f"G:\gam3a\System Programming\Lab\Project\\sic.txt"
array = []

with open(filename) as f:
    for line in f:
        if re.match(r'[ \t]', line):
            line = line.replace("\t\t","\t")
        linex = map(str, line.replace("\n", "").replace(
            ".", "").replace("â€™", "").split("\t"))
        array.append(list(linex))
    if not(array[-1]):
        array.pop()  # remove last empty elemnt

for i in range(0, array.__len__()):
    try:
        print(array[i])
    except:
        print("NULL")

        ######coded_with_❤_by_marwaneldesouki######
