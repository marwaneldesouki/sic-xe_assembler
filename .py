import sys
filename = f"G:\gam3a\System Programming\Lab\Project\\sic.txt"
array = []
with open(filename) as f:
    for line in f: 
        linex = map(str,line.replace("\n","").replace(".","").replace("â€™","").split("\t")) 
        array.append(list(filter(None, linex)))
    if not(array[-1]):
        array.pop()#remove last empty elemnt
for i in range(0,array.__len__()):
    try:
        print(array[i])
    except:
        print("NULL")