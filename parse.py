h = open("temp.txt", 'a')
h.truncate(0)
g = open("output.txt", "a")
g.truncate(0)
f = open(r"G:/license parsing bot/test.txt",'r')
irofile = iter(f)

for line in f:
    if "   |- Feature name" in line:
        line5 = line.replace("   |- Feature name                   : ","")
        line6 = line5.replace("\n","")
        clean_line = line6.replace(" ","")
        line = next(irofile)
        line3 = line.replace("   |- Feature version                : ","")
        cleaner_line = clean_line + line3
        line4 = cleaner_line.replace("\"","")
        h.write(line4)
    if "     |- User name" in line:
        clean_line = line.replace("|- User name                      : ", "")
        line2 = clean_line.replace("\n","")
        line = next(irofile)
        cleaner_line = line.replace("     |- Host name                     ", "")
        liner = line2 + cleaner_line
        h.write(liner)
h.close()
h = open("temp.txt", 'r')
irofile2 = iter(h)
temp = {}
for line in h:
    if (not line in temp.keys()):
        temp[line] = line
        g.write(line)


g.close()


