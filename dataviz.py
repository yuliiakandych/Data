import csv
import numpy as np
import matplotlib.pyplot as plt

categories = [] #strip out the first row of text
install = []
rating = []

with open("data/googeplaystore.csv") as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            print("pushing test row to categories array")
            categories.append(row)
            line_count += 1
        else:
            #print('collect the rest')
            installData = row[5]
            installData = installData.replace(",", "")
            installData = installData.replace("Free", "0")
            installs.append(int(np.char.strip(installData, "+")))
            line_count += 1

print("processed", line_count, "rows of data")
print("first line:", installs[0])
print("last line:", installs[-1])