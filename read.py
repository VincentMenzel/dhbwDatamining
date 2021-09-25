import csv

import matplotlib.pyplot as plt
import numpy as np

dic = {}

with open('./data1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:



        try:
            country = row[0]
            valText = row[3].replace(",", ".")
            val = float(valText)

            print('%s - %f - %s' % (valText, val, country))

            if country not in dic or val > dic[country]:
                dic[country] = val

            line_count += 1
        except:
            continue

print(dic)

labels = []
values = []

for key in dic:
    labels.append(key)
    values.append(float(dic[key]))

x = np.array(labels)
y = np.array(values)

plt.bar(x, y)
plt.show()

input("close?")
