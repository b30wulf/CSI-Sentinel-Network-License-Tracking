contents = open("output1.txt","r")
from datetime import datetime
from datetime import date
today = date.today()
d2 = today.strftime("%B %d, %Y")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
with open("license.html", "w") as e:
    e.write("<img src='https://glotmansimpson.com/wp-content/uploads/2020/03/Glotman-Simpson-Logo-1-1024x178.jpg' alt='Simply Easy Learning' width='512' height='89'>")
    e.write("<pre><b> Refreshed : " + str(d2) + " at "+ str(current_time) + "</b></pre>")
    for lines in contents.readlines():
        if "Licenses being used" in lines:
            e.write("<pre><b>" + lines + "</b></pre> \n")
        else :
            e.write("<pre>" + lines + "</pre> \n")
