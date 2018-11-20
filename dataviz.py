import csv
import numpy as np
import matplotlib.pyplot as plt

categories = [] #strip out the first row of text
installs = []
ratings = []

with open("includes/googeplaystore.csv") as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            print("pushing test row to categories array")
            categories.append(row)
            line_count += 1
        else:
            #cllecting the ratings info
            ratingsData = row [2]
            ratingsData = ratingsData.replace("NaN", "0")
            ratings.append(float(ratingsData));

            #print('collect the rest')
            installData = row[5]
            installData = installData.replace(",", "")
            installData = installData.replace("Free", "0")
            installs.append(int(np.char.strip(installData, "+")))
            line_count += 1

print("processed", line_count, "rows of data")
print("first line:", ratings[0])
print("last line:", ratings[-1])

np_ratings = np.array(ratings)

popular_apps = np_ratings > 4
pop_pct = int(len(np_ratings[popular_apps]) / len(np_ratings) * 100)
print(pop_pct)

np_ratings = np.array(ratings)

unpopular_apps = np_ratings < 2
not_pop_pct = int(len(np_ratings[unpopular_apps]) / len(np_ratings) * 100)
print(not_pop_pct)

mid_apps = 100 - (pop_pct + not_pop_pct)
print(mid_apps)

#now we can plot stuff
labels = "Sucks, Meh, Love it"
sizes = [not_pop_pct, mid_apps, pop_pct]
colors = ["yellowgreen", "lightcoral", "lightskyblue"]
explode = (0.1, 0.1, 0.15)

plt.pie(sizes, explode=explode, colors=colors, autopct="%1.1f%%", shadow=True, startangle=140)
plt.axis("equal")

plt.legend(labels, loc=1)
plt.title("Do we Loves our Apps?")
plt.xlabel("User Ratings - Gooogle Play Store App Installs")
plt.show()
