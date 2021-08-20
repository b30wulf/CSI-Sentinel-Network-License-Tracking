f = open("test.txt",'r')#open the raw data from lsmon.exe (open for only read)
h = open("temp.txt", 'a')#first temp file (open for read/write)
h.truncate(0)#clear
g = open("output.txt", "a")#second temp file (open for read/write)
g.truncate(0)#clear
j = open("output1.txt","a")#final file ready to be converted to html (open for read/write)
j.truncate(0)#clear
irofile = iter(f) #initialize iterator for lines in a text file
#Static Variables
NUM_PROGRAMS = 22
NUM_LICENSE_ALLIGN = 14
NUM_USER_ALLIGN = 17
NUM_TOTAL_ALLIGN = 30
address1 = 0
#data lists
counter = [0]*NUM_PROGRAMS
max = [0]*NUM_PROGRAMS
#looping through raw data
for line in f:
    if "   |- Feature name" in line:
        #Parsing the name and version of the program, and combining them into one line
        linePoint1=line
        line5 = line.replace("   |- Feature name                   : ","")
        line6 = line5.replace("\n","")
        clean_line = line6.replace(" ","")
        line = next(irofile)
        line3 = line.replace("   |- Feature version                : ","")
        cleaner_line = clean_line + line3
        line4 = cleaner_line.replace("\"","")
        h.write(line4)
        #6 lines down it tells us what is the number is licenses we have.
        linePoint1 = next(irofile)
        linePoint1 = next(irofile)
        linePoint1 = next(irofile)
        linePoint1 = next(irofile)
        linePoint1 = next(irofile)
        linePoint1 = next(irofile)
        #we parse the number of licenses here, and move them into the max[] list.
        if "   |- Maximum concurrent user(s)     : " in linePoint1:
            line10 = linePoint1.replace("   |- Maximum concurrent user(s)     : ", "")
            line11 = line10.replace("\n", "")
            nums = int(line11)
            max[address1] = nums
            address1 = address1 + 1
        else :
            print("didn't find")

    
    if "     |- User name" in line:
        #we find the user name, host name, and the number of windows they have open. 
        #We then parse them into one line separated by colons
        #This is a user of the license.
        linePoint = line
        clean_line = line.replace("|- User name                      : ", "")
        line2 = clean_line.replace("\n","")
        line = next(irofile)
            #this is to allign the host name and user name for all users later on.
        if len(line2) < NUM_USER_ALLIGN:
            for x in range(NUM_USER_ALLIGN-len(line2)):
                line2 = line2 + " "
        line2 = line2 + " : "
        cleaner_line = line.replace("     |- Host name                      : ", "")
        liner = line2 + cleaner_line
            #allignment
        if len(liner) < NUM_TOTAL_ALLIGN:
            for x in range(NUM_TOTAL_ALLIGN-len(liner)):
                liner = liner + " "
        #from host name, if he has multiple windows open, he will have the "token shared by" tag
        #we will find that tag 6 lines down. We parse, allign, then add to the line. 
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
            #less than 3 windows
            if num <= 3:
                line8 = line8 + " : " + str(num) + "/3"+ " Allowed windows open\n"
                h.write(line8)
            #more than 3 windows
            else :
                line8 = line8 + " : 3/3"+ " Allowed windows open\n"
                h.write(line8)
                line8 = line8 + " : " + str(num-3) + "/3"+ " Allowed windows open\n"
                h.write(line8)
        #just one window open (no tag found)        
        else :
            line9 = liner.replace("\n","")
            line9 = line9 + " : 1/3 Allowed windows open\n"
            h.write(line9)


h.close()#close reader for mem
h = open("temp.txt", 'r') #open temp file (read only)
irofile2 = iter(h) #new iterator
temp = {} #HashMap
#filters out all duplicate users written in temp.txt
for line in h:
    if (not line in temp.keys()):
        temp[line] = line
        g.write(line)
g.close()#close reader for mem
g = open("output.txt", 'r')#open temp file (read only)
irofile3 = iter(g) #new iterator
count = 0
address = -1
#We count the number of licenses used per program after being filtered by for loop above.
for line in g:
        #found a user, increase count
    if "     " in line:
        count = count + 1
    else:
        #new program, store prev value into counter[] then reset count
        if address >= 0 :
            counter[address] = count
            count = 0
            address = address + 1
        #initial address value (list allignment)
        else :
            address = 0
g.close()  #close reader for mem
g = open("output.txt", 'r') #open temp file (read only)
irofile3 = iter(g) # new iterator
address2 = 0
for line in g:
    #for each program program line found
    if (not "     " in line):
        #We use counter[x] / max[x] to find the number of licenses used vs. the total amount of licenses.
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
    #non program line, just print users.
    else :
        j.write(line)

j.close()#close reader for mem


