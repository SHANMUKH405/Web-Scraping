from matplotlib.pyplot import cla
from nbformat import write
import requests
from bs4 import BeautifulSoup
import csv

req = requests.get("https://air-quality.com/place/india/gurugram/d2853e61?lang=en&standard=aqi_us")

soup = BeautifulSoup(req.content,"html.parser")

Pollutant_readings=[]
Pollutant_reading=soup.findAll('div',class_="pollutants")

#print(Pollutant_readings)    

with open('readings.csv','w') as csv_file:
    write=csv.writer(csv_file)
    write.writerow(Pollutant_reading)
    for i in Pollutant_reading:
       j=i.text
       Pollutant_readings.append(j)
    write.writerow(Pollutant_readings)   

print(soup.prettify)    
