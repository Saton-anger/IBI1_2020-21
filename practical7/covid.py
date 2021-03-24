import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/Users/apple/documents/practical7")
covid_data = pd.read_csv("full_data.csv")

print(covid_data.iloc[0:10:2, 0:5])

# my_columns = [True, True, False, True, False, False]
# print(covid_data.iloc[0:3, my_columns])

my = []
for i in range(7996):
    if covid_data.loc[i, 'location'] == "Afghanistan":
        my.append(True)
    else:
        my.append(False)
print(covid_data.loc[my, 'total_cases'])


a1 = []
for i in range(7996):
    if covid_data.loc[i, 'location'] == 'World':
        a1.append(True)
    else:
        a1.append(False)
world_new_cases = covid_data.loc[a1, 'new_cases']
print(world_new_cases)

print('mean:', np.mean(world_new_cases))
print('median:', np.median(world_new_cases))

# boxplot for new cases worldwide
plt.boxplot(world_new_cases,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=True,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False
)
plt.title('box plot for world new cases')
plt.show()

#world_dates = covid_data.loc[a1, 'date']
#plt.plot(world_dates, world_new_cases, 'ro')
#plt.xticks(world_dates.iloc[0:len(world_dates):6], rotation=-45)
#plt.show()



# worldwide new cases and death
world_new_deaths = covid_data.loc[a1, 'new_deaths']
world_dates = covid_data.loc[a1, 'date']
plt.plot(world_dates, world_new_cases, 'ro', label="new_cases")
plt.plot(world_dates, world_new_deaths, 'bo', label='new_deaths')

plt.xticks(world_dates.iloc[0:len(world_dates):6], rotation=-45)
plt.xlabel('world_date')

plt.title('comparison between world new cases and world new deaths')

plt.legend()
plt.show()

#  code for question:  deaths between China and world
c1 = []
for i in range(7996):
    if covid_data.loc[i, 'location'] == "China":
        c1.append(True)
    else:
        c1.append(False)
China_new_cases = covid_data.loc[c1, 'new_cases']

plt.plot(world_dates, China_new_cases, 'ro', label="China_new_cases")
plt.plot(world_dates, world_new_cases, 'bo', label='world_new_cases')

plt.xticks(world_dates.iloc[0:len(world_dates):6], rotation=-45)
plt.xlabel('world_date')

plt.title('comparison between world new cases and China new cases')

plt.legend()
plt.show()

















