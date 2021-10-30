from time import sleep
import csv
import os
import cv2
import pytesseract
from requests import get
from time import sleep
import urllib


writer = csv.writer(open('a2.csv', 'a', encoding='utf-8')) 



with open("2.csv") as f:
    reader = csv.reader(f)
    a = 1
    for row in reader:
        a += 1 
        
        
        try:
            print(row[5])
            

            name = f'{a}.png'
            v = urllib.request.urlopen(row[5])
            with open(name ,"wb") as file : file.write(v.read())
            
            # sleep(1)
            name = f"{a}.png"
            img = cv2.imread(name)
            text = ''
            text = pytesseract.image_to_string(img)
            print(text)

            writer.writerow([ row[0],row[1] ,row[2],row[3]  ,row[4],row[5] ,row[6], text])
        except:
            print("xxxxx")

        print(f"NUMBER OF PHOTO : {a}")