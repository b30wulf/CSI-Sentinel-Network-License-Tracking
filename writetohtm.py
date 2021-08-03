contents = open("output1.txt","r")
with open("license.html", "w") as e:
    e.write("<img src='https://glotmansimpson.com/wp-content/uploads/2020/03/Glotman-Simpson-Logo-1-1024x178.jpg' alt='Simply Easy Learning' width='512' height='89'>")
    for lines in contents.readlines():
            e.write("<pre>" + lines + "</pre> \n")
