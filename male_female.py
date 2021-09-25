import csv

import matplotlib.pyplot as plt
import numpy as np

# Dictionary for string (Country) - float (Value) Pairs
dic = {}

# First line which contains data
start_line = 8

# last line which contains data
end_line = 295

# Max number of values in the diagram
max_entries = 5

# Index of the csv table which is used for the value in the diagram
index = 13

# True  - Will show the max_entries highest values in the diagram
# False - Will instead display the max_entries lowest values in the diagram
highest = False

with open('./exec.csv', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0

    for row in csv_reader:

        # only evaluate lines defined by star and end line
        if line_count <= start_line: line_count+=1; continue
        if line_count >= end_line: break


        try:

            country = row[0]
            year = row[1]
            val = float( row[index].replace(",", ".") )

            # Only evaluate lines from the year 2019
            if year != '2019': continue

            print('%s - %f' % (country, val))


            dic[country] = val
            line_count += 1

        except:
            continue

print(dic)

arr = []

for key in dic:
    arr.append([key, dic[key]])


arr2 = []
oecd_added = False

# Find the lowest or highest values
for ii in range(max_entries):

    current_country = ''
    current_value = ''
    current_index = -1

    for i in range(len(arr)):
        if arr[i][0] == 'OECD-Durchschnitt' and not oecd_added:
            arr2.append([arr[i][0], arr[i][1]])
            oecd_added = True
            continue

        if i == 0:
            current_country = arr[i][0]
            current_value = arr[i][1]
            current_index = i

        if arr[i][1] >= current_value if highest else arr[i][1] <= current_value:
            current_country = arr[i][0]
            current_value = arr[i][1]
            current_index = i


    arr2.append([current_country, current_value])
    del(arr[current_index])


labels = []
values = []

for val in arr2:
    labels.append(val[0])
    values.append(val[1])

x = np.array(labels)
y = np.array(values)

plt.rcParams.update({'font.size': 16})
plt.bar(x, y,)

for index, value in enumerate(y):
    plt.text(index, value, str(value))

plt.show()