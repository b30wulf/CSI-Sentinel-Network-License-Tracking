contents = open("output.txt","r")
with open("license.html", "w") as e:
    for lines in contents.readlines():
        if lines[0] == " ":
            e.write("<pre>" + lines + "</pre> \n")
        else :    
            e.write(lines + "<br> \n")