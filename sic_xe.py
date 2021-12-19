import sys
import re
filename = f"G:\gam3a\System Programming\Lab\Project\\sic_xe.txt"
array = []
old_line = ""
instructions_op = [["ADD","18"],["LDB","68"],["+JSUB","48"],["JSUB","48"],["LDA","00"],["COMP","28"],["JEQ","30"],["J","3C"],["STA","0C"],["CLEAR","B4"],["LDT","74"],["TD","E0"],["RD","D8"],["COMPR","A0"],["STCH","54"],["TIXR","B8"],["LDCH","50"],["WD","DC"],["JLT","38"],["STL","14"]]
n=i=x=b=p=e= 0


def op_translation(op_code):
    res=""
    for i in range(0,instructions_op.__len__()):
        if(op_code==instructions_op[i][0]):
            res = "{0:08b}".format(int(instructions_op[i][1], 16))
            res = res[:-2]
            break
    return res
with open(filename) as f:
    for line in f:
        if re.match(r'[ \t]', line):  # replace 2tabs to 1tab
            line = line.replace("\t\t", "\t")
        if(line.split("\t")[1] == "START"): #start
            old_line = line.split("\t") #to delay by 1 line
        elif(old_line[1] == "START"):  # skip second line
           print
        
        try:
            if(line.split("\t")[1].__contains__("+")):
                e = 1
                n_moseba =1
                n=i=1
            if(line.split("\t")[1].__contains__("+") and line.split("\t")[2].__contains__("#")):
                n=0
            if(line.split("\t").__len__()==2):
                index = 1
            else:
                index = 2
            if(line.split("\t")[index].__contains__("#")):
                i= 1
                n_moseba = 1
                if(re.search(r'\d', line.split("\t")[index])):
                    p=b=0
                else:
                    p=1
            elif(line.split("\t")[index].__contains__("@")):
                p=n=1;
                n_moseba = 1
            elif(line.split("\t")[index].__contains__(",X")):
                x=i=n=p=1
                n_moseba = 1
            if(n_moseba!= 1 ):
                n=i=p=1
        except:
            print
        addressing_mode=  str(n)+str(i)+str(x)+str(b)+str(p)+str(e)
        line += "\t"+op_translation(line.split("\t")[1]) +str(int(addressing_mode))
        line = line.replace("\n", "").replace(
            ".", "").replace("â€™", "").split("\t")
        n=i=x=b=p=e= 0
        n_moseba= 0
        array.append(list(map(str, line)))  # make line string type
    if not(array[-1]):  # remove last element if empty
        array.pop()
    
    
for  i in range(0, array.__len__()):
    try:
        print(array[i])
    except:
        print("NULL")