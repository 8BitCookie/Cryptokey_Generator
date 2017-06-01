from appJar import gui
import hashlib
import random
import csv

app=gui("Cryptokey Generator", "640x480")
app.setFont(18)
app.setSticky("news")
app.setExpand("both")

keys = []
keyCount = 0
csvfile = "keys.csv"

def genCryptokeys(btn):
    keys = []
    keyCount = 0
    global keyCount
    csvfile = str(app.getEntry("file_name")+'.csv')
    no_of_keys = int(app.getEntry("no_input"))*int(app.getEntry("no_input"))
    for i in range(no_of_keys):
        percent_done = int(((keyCount / no_of_keys)*100)+1)
        num1 = random.getrandbits(int(app.getEntry("no_input")))
        num2 = random.getrandbits(int(app.getEntry("no_input")))
        finalNum = num1*num2
        key = hashlib.sha256(str(finalNum).encode('utf-8')).hexdigest()
        key = hashlib.md5(key.encode('utf-8')).hexdigest()
        key = key.upper()

        if(key not in keys):
            keys.append(key)
            keyCount+=1
            app.setLabel("maxKeys", keyCount)
            progress_text = str(percent_done)+"%"
            app.setMeter("progress", percent_done, text= progress_text)

    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for key in keys:
            writer.writerow([key])

app.addLabel("title", "Cryptokey Generator",0,0,4)
app.addLabel("maxKeys_title", "Number Of Keys Generated",1,0,2)
app.addLabel("maxKeys", "-",1,2,2)
app.addLabel("file_name_title", "File Name",2,0,4)
app.addEntry("file_name",3,0,4)
app.addLabel("no", "Mutliplyer",4,0,4)
app.addEntry("no_input",5,0,4)
app.addButton("genKeys",genCryptokeys,6,0,4)
app.addMeter("progress",7,0,4)
app.setMeter("progress", 0, text='0%')
app.setMeterFill("progress", "blue")

app.go()
        
    
