import sys
import re
filename = f"sic_xe\problems\sic_xe.txt"
array = []
array_2 = []
old_line = ""
address = 0000
symbol_table = []
instructions_op = [["ADDR", "90"], ["SUBR", "94"], ["MULR", "98"], ["ADD", "18"], ["LDB", "68"], ["+JSUB", "48"], ["JSUB", "48"], ["LDA", "00"], ["COMP", "28"], ["JEQ", "30"], ["J", "3C"], ["STA", "0C"], ["CLEAR",
                                                                                                                                                                                                             "B4"], ["+LDT", "74"], ["TD", "E0"], ["RD", "D8"], ["COMPR", "A0"], ["STCH", "54"], ["TIXR", "B8"], ["LDCH", "50"], ["WD", "DC"], ["JLT", "38"], ["STL", "14"]]
registers = [["A", "0"], ["X", "1"], ["L", "2"], [
    "B", "3"], ["S", "4"], ["T", "5"], ["F", "6"]]
n = i = x = b = p = e = 0
b_gdeda = 0
p_gdeda = 0


def op_translation(op_code):
    res = ""
    for i in range(0, instructions_op.__len__()):
        if(op_code == instructions_op[i][0]):
            res = bin(int(instructions_op[i][1], 16))
            res = res[2:].zfill(8)
            res = res[:-2]
            break
    return res


def displacment(line, n, i, x, b, p, e):
    res = ""
    if(n == 0 and i == 1 and p == 0):
        charRegex = re.findall("#([^<]*)", line)
        res = hex(int(charRegex[0]))[2:].zfill(3)
        return res, 0, 0
    elif(n == i == p == 1):
        charRegex = re.findall("@([^<]*)", line)
        if charRegex:
            line = charRegex[0]
        for label in symbol_table:  # search for counter_label in symbol_table
            if(label[0] == line):  # if label_in_symbol_table == line_pass
                counter_label = label[1]  # target_address
                for i in range(0, array.__len__()):
                    if(array[i].__len__() == 4):
                        index = 2
                    else:
                        index = 1
                    if(label[0] == array[i][index]):
                        try:
                            if(array[i+1].__len__() == 4):
                                index = 3
                            else:
                                index = 2
                            counter_array = array[i+1][index]  # pc
                            # target address - pc
                            res = int(counter_label, 16) - \
                                int(counter_array, 16)
                            if(res < 0):
                                res = hex(res & (2**32-1))[6:]
                            else:
                                res = hex(res)[2:]
                            if (int(res) <= -2047 or int(res) >= 2048):  # out of range
                                print("out of range")
                                for element in array:  # find base
                                    if(element[0] == "BASE"):
                                        # search on this element in symbol_table
                                        for i in range(0, symbol_table.__len__()):
                                            if(element[1] == symbol_table[i][0]):
                                                # base
                                                base = symbol_table[i][1]
                                                res = int(
                                                    counter_label, 16)-int(base, 16)
                                                if(res < 0):
                                                    res = hex(
                                                        res & (2**32-1))[6:]
                                                else:
                                                    res = hex(res)[2:]
                                b = 1
                                p = 0
                                return res, b, p
                            return res
                        except:
                            print  # akhr element mlnash da3wa beeh
    elif(i == p == 1):
        charRegex = re.findall("@([^<]*)", line)
        hash_charRegex = re.findall("#([^<]*)", line)
        if charRegex:
            line_ = charRegex[0]
        if hash_charRegex:
            line_ = hash_charRegex[0]
        for label in symbol_table:  # search for counter_label in symbol_table
            if(label[0] == line_):  # if label_in_symbol_table == line_pass
                counter_label = label[1]  # target_address
                for i in range(0, array.__len__()):
                    if(array[i].__len__() == 4):
                        index = 2
                    else:
                        index = 1
                    if(line == array[i][index]):
                        try:
                            if(array[i+1].__len__() == 4):
                                index = 3
                            else:
                                index = 2
                            counter_array = array[i+1][index]  # pc
                            # target address - pc
                            res = int(counter_label, 16) - \
                                int(counter_array, 16)
                            res = hex(res)[2:]
                            if not(int(res) >= -2047 and int(res) <= 2048):
                                for element in array:  # find base
                                    if(element[0] == "BASE"):
                                        # search on this element in symbol_table
                                        for i in range(0, symbol_table.__len__()):
                                            if(element[1] == symbol_table[i][0]):
                                                # base
                                                base = symbol_table[i][1]
                                                res = int(
                                                    counter_label, 16)-int(base, 16)
                                                if(res < 0):
                                                    res = hex(
                                                        res & (2**32-1))[6:]
                                                else:
                                                    res = hex(res)[2:]
                                b = 1
                                p = 0
                                return res, b, p
                            return res
                        except:
                            print  # akhr element mlnash da3wa beeh
    elif(e == 1):
        for element in symbol_table:
            if(element[0] == line):
                res = element[1]
    return res


with open(filename) as f:
    for line in f:
        if re.match(r'[ \t]', line):  # replace 2tabs to 1tab
            line = line.replace("\t\t", "\t")
        if(line.split("\t")[1] == "START"):  # start
            old_line = line.split("\t")  # to delay by 1 line
        elif(old_line[1] == "START"):  # skip second line
            print
        elif(old_line[1] == "RESW"):
            address += int(old_line[2])*3
        elif(old_line[1] == "RESB"):
            address += int(old_line[2])
        elif(old_line[1] == "BYTE"):
            try:
                # get the char before ,
                charRegex = re.findall("(.*?)'", old_line[2])
                if(str(charRegex[0]).lower() == "c"):
                    address += str(charRegex[1]).__len__()
                else:
                    address += str(charRegex[1]).__len__()/2
            except:
                print()
        elif(old_line[1] == "CLEAR" or old_line[1] == "COMPR" or old_line[1] == "TIXR"):
            address = int(address)+2
        elif(old_line[1].__contains__("+")):
            address = int(address)+4
        else:
            address = int(address)+3
        if(line.split("\t")[0] != ""):  # symbol_table
            symbol_table.append(
                [line.split("\t")[0], hex(int(address))[2:].zfill(4)])

        # convert address to hex
        line += "\t"+str(hex(int(address))[2:].zfill(4))
        line = line.replace("\n", "").replace(
            ".", "").replace("â€™", "").split("\t")
        old_line = line
        array.append(list(map(str, line)))  # make line string type
        ############################################################
# print(displacment("RLOOP",1,1,0,0,1,0))

for line in array:
    try:
        if(line[1].__contains__("+")):
            e = 1
            n_moseba = 1
            n = i = 1
        if(line[1].__contains__("+") and line[2].__contains__("#")):
            n = 0
        if(line.__len__() == 2):
            index = 1
        else:
            index = 2
        if(line[index].__contains__("#")):
            i = 1
            n_moseba = 1
            if(re.search(r'\d', line[index])):
                p = b = 0
            else:
                p = 1
        elif(line[index].__contains__("@")):
            p = n = 1
            n_moseba = 1
        elif(line[index].__contains__(",X")):
            x = i = n = p = 1
            n_moseba = 1
        if(n_moseba != 1):
            n = i = p = 1
    except:
        print
    addressing_mode = str(n)+str(i)+str(x)+str(b)+str(p)+str(e)
    res = ""
    if(line.__len__() == 4):
        index = 2
    else:
        index = 1
    if(line[1] == "RESW" or line[1] == "RESB"):
        res = "noObjCode"
    elif(line[1] == "BYTE"):
        res = re.findall("'([^<]*)'", line[2])[0]
    elif(line[1] == "COMPR" or line[1] == "ADDR" or line[1] == "MULR" or line[1] == "SUBR" or line[1] == "TIXR" or line[1] == "CLEAR"):
        for element in instructions_op:
            if(element[0] == line[1]):
                res = element[1]
                if(line[2].__len__() == 3):
                    LcharRegex = re.findall("(.*?),", line[2])
                    Left_char = LcharRegex[0]
                    RcharRegex = re.findall(",([^<]*)", line[2])
                    Right_char = RcharRegex[0]
                    for element in registers:
                        if(element[0] == Left_char):
                            res += element[1]
                        if(element[0] == Right_char):
                            res += element[1]
                else:
                    for element in registers:
                        if(element[0] == line[2]):
                            res += element[1]
    else:
        try:
            res, b, p = displacment(line[index], n, i, x, b, p, e)
            addressing_mode = str(n)+str(i)+str(x)+str(b)+str(p)+str(e)
        except:
            res = displacment(line[index], n, i, x, b, p, e)
    # print("result:  "+res)
    # print(n,i,x,b,p,e)

    addressing_mode = str(n)+str(i)+str(x)+str(b)+str(p)+str(e)
    res = hex(
        int(str(op_translation(line[1])+addressing_mode), 2))[2:]+res.zfill(3)
    line.append(res)
    n = i = x = b = p = e = 0
    n_moseba = 0
    array_2.append(list(map(str, line)))  # make line string type
    if not(array_2[-1]):  # remove last element if empty
        array_2.pop()

# for  i in range(0, array.__len__()):
#    try:
#        print(array[i])
#    except:
#        print("NULL")

# H/NAME:6BITS/START:6BITS/LENGTH:6BITS(MAIN_LAST_END-MAIN_FIRST_START)
# T/START:6BITS/LENGTH:2BITS(LAST_END-LAST_START)/OBJCODE
# E/START:6BITS
hte_array = []


def HTE_(arr):
    line = arr
    length = 1  # from 1->10
    addressnumber_index = 0
    displacmentnumber_index = 0
    strx = ""
    for i in range(0, line.__len__()):
        if(line[i][1] == "START"):  # start
            strx = ""
            strx += "H."+line[i][1].zfill(6)+"."+line[i][2].zfill(
                6)+"."+hex(int(arr[-1][2], 16)-int(arr[0][3]))[2:].zfill(6)
            hte_array.append(strx.split("."))
        else:
            if(line[i].__len__() == 5):  # to check the length if elements in line
                displacmentnumber_index = 4
                addressnumber_index = 3
            else:
                displacmentnumber_index = 3
                addressnumber_index = 2
            if(length == 1):  # to start T.(temp_length).first_displacment
                if(line[i][1] != "RESW" and line[i][1] != "RESB"):
                    strx = ""
                    # the (TEMP_LENGTH) because in the end it will replaced by the length
                    strx += "T."+line[i][addressnumber_index].zfill(
                        6)+".(TEMP_LENGTH)."+line[i][displacmentnumber_index].zfill(6)+"."
                else:
                    hte_array.append(strx[:-1].split("."))
                    temp_str = hte_array[hte_array.__len__()-1][3:None]
                    temp_str = ''.join(temp_str)
                    temp_str = temp_str.__len__()/2
                    hte_array[hte_array.__len__()-1][2] = hex(int(temp_str))[2:]
            # to check on the length !=10 and line != resw or resb
            elif(length != 10 and line[i][1] != "RESW" and line[i][1] != "RESB"):
                strx += line[i][displacmentnumber_index].zfill(6)+"."
            elif(length == 10):  # the end of T
                strx += line[i][displacmentnumber_index].zfill(6)+"."
                length = 0
                hte_array.append(strx[:-1].split("."))
                temp_str = hte_array[hte_array.__len__()-1][3:None]
                temp_str = ''.join(temp_str)
                temp_str = temp_str.__len__()/2
                hte_array[hte_array.__len__()-1][2] = hex(int(temp_str))[2:]
            else:  # if line contains resw or resb the length will be 0 again
                length = 0
            length += 1
    # to handle last elements
    hte_array.append(strx[:-1].split("."))
    temp_str = hte_array[hte_array.__len__()-1][3:None]
    temp_str = ''.join(temp_str)
    temp_str = temp_str.__len__()/2
    hte_array[hte_array.__len__()-1][2] = hex(int(temp_str))[2:]
    #####
    # the E statment
    hte_array.append(["E", hte_array[0][2]])
    #####


# HTE_(array_2)
# for elem in hte_array:
#     print(elem)
# for  i in range(0, array_2.__len__()):
#    try:
#        print(array_2[i])
#    except:
#        print("NULL")
