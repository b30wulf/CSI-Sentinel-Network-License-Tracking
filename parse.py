h = open("temp.txt", 'a')
h.truncate(0)
g = open("output.txt", "a")
g.truncate(0)
f = open(r"G:/license parsing bot/test.txt",'r')
j = open("output1.txt","a")
j.truncate(0)
irofile = iter(f)
NUM_PROGRAMS = 22
NUM_LICENSE_ALLIGN = 14
NUM_USER_ALLIGN = 17
NUM_TOTAL_ALLIGN = 30
address1 = 0
counter = [0]*NUM_PROGRAMS
max = [0]*NUM_PROGRAMS
for line in f:
    if "   |- Feature name" in line:
        linePoint1=line
        line5 = line.replace("   |- Feature name                   : ","")
        line6 = line5.replace("\n","")
        clean_line = line6.replace(" ","")
        line = next(irofile)
        line3 = line.replace("   |- Feature version                : ","")
        cleaner_line = clean_line + line3
        line4 = cleaner_line.replace("\"","")
        h.write(line4)
        linePoint1 = next(irofile)
        linePoint1 = next(irofile)
        linePoint1 = next(irofile)
        linePoint1 = next(irofile)
        linePoint1 = next(irofile)
        linePoint1 = next(irofile)
        if "   |- Maximum concurrent user(s)     : " in linePoint1:
            line10 = linePoint1.replace("   |- Maximum concurrent user(s)     : ", "")
            line11 = line10.replace("\n", "")
            nums = int(line11)
            max[address1] = nums
            address1 = address1 + 1
        else :
            print("didn't find")

    
    if "     |- User name" in line:
        linePoint = line
        clean_line = line.replace("|- User name                      : ", "")
        line2 = clean_line.replace("\n","")
        line = next(irofile)
        if len(line2) < NUM_USER_ALLIGN:
            for x in range(NUM_USER_ALLIGN-len(line2)):
                line2 = line2 + " "
        line2 = line2 + " : "
        cleaner_line = line.replace("     |- Host name                      : ", "")
        liner = line2 + cleaner_line
        if len(liner) < NUM_TOTAL_ALLIGN:
            for x in range(NUM_TOTAL_ALLIGN-len(liner)):
                liner = liner + " "
        linePoint = next(irofile)
        linePoint = next(irofile)
        linePoint = next(irofile)
        linePoint = next(irofile)
        linePoint = next(irofile)
        if "     |- Token shared by                : " in linePoint:
            line7 = linePoint.replace("     |- Token shared by                : ", "")
            num = int(line7[0])
            num = num + 1
            line8 = liner.replace("\n","")
            if num <= 3:
                line8 = line8 + " : " + str(num) + "/3"+ " Allowed windows open\n"
                h.write(line8)
            else :
                line8 = line8 + " : 3/3"+ " Allowed windows open\n"
                h.write(line8)
                line8 = line8 + " : " + str(num-3) + "/3"+ " Allowed windows open\n"
                h.write(line8)
        else :
            line9 = liner.replace("\n","")
            line9 = line9 + " : 1/3 Allowed windows open\n"
            h.write(line9)

h.write(" ")
h.close()
h = open("temp.txt", 'r')
irofile2 = iter(h)
temp = {}
for line in h:
    if (not line in temp.keys()):
        temp[line] = line
        g.write(line)
g.close()
g = open("output.txt", 'r')
irofile3 = iter(g)
count = 0
address = -1
for line in g:
    if "     " in line:
        count = count + 1
    else:
        if address >= 0 :
            counter[address] = count
            count = 0
            address = address + 1
        else :
            address = 0
g.close()  
g = open("output.txt", 'r')
irofile3 = iter(g)
address2 = 0
for line in g:
    if (not "     " in line):
        if address2 < NUM_PROGRAMS:
            line10 = line.replace("\n","")
            line11 = line10.replace("	", " ")
            line12 = line11.replace("	"," ")
            if len(line12) < NUM_LICENSE_ALLIGN :
                for x in range (NUM_LICENSE_ALLIGN - len(line12)):
                    line12 = line12 + " " 
            line12 = line12 + "     "+ str(counter[address2]) + "/" + str(max[address2]) + " Licenses being used:\n" 
            j.write(line12)
            address2 = address2 + 1
    else :
        j.write(line)

j.close()


print(max)
print(counter)



