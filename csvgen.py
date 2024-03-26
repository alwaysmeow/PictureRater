import os
import csv

headers = ["Filename", "Mark"]

filenames = os.listdir('static')

data = []

for filename in filenames:
    data.append((filename, -1))

with open("markup.csv", 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(headers)
    csvwriter.writerows(data)