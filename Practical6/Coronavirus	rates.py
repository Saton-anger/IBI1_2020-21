import matplotlib.pyplot as plt
# build a list of country and a dictionary of the number of people in different countries
Country = ['USA', 'India', 'Brazil', 'Russia', 'UK']
People = {'USA': 29862124, 'India': 11285561, 'Brazil': 11205972, 'Russia': 4360823, 'UK': 4234924}
# output the dictionary "People"
print(People)
# build pie chart
number = [29862124, 11285561, 11205972, 4360823, 4234924]
explode = (0, 0, 0, 0, 0)
plt.pie(number, explode=explode, labels=Country, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')
plt.show()
