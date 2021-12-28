import sys
import re
filename = f"problems\text.txt"
array = []
address = 0000
old_line = ""
with open(filename) as f:
    for line in f:
        if re.match(r'[ \t]', line):  # replace 2tabs to 1tab
            line = line.replace("\t\t", "\t")
        if(line.split("\t")[1] == "START"):  # start
            address = line.split("\t")[2]
            old_line = line.split("\t")  # to delay by 1 line
        elif(old_line[1] == "START"):  # skip second line
            print("")
        elif(old_line[1] == "RESW"):
            address += int(old_line[2])*3
        elif(old_line[1] == "BYTE"):
            try:
                # get the char before '
                charRegex = re.findall("(.*?)'", old_line[2])
                if(charRegex[0] == "c"):
                    address += str(charRegex[1]).__len__()
                else:
                    address += str(charRegex[1]).__len__()/2
            except:
                print()
        else:
            address = int(address)+3

        # convert address to hex
        line += "\t"+str(hex(int(address))[2:].zfill(4))
        line = line.replace("\n", "").replace(
            ".", "").replace("â€™", "").split("\t")
        old_line = line
        print(line)
        array.append(list(map(str, line)))  # make line string type
    if not(array[-1]):  # remove last element if empty
        array.pop()

# for i in range(0, array.__len__()):
#     try:
#         print(array[i])
#     except:
#         print("NULL")

        #######coded_with_❤_by_marwaneldesouki#######
