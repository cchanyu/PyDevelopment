'''
Week 1 Homework - Find the average height of the men

Name: Chanyu Choung

Class: CMP414

Homework due date: Feb 8th, 2021 (Monday)

Years = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980]

Heights = [170, 172.1, 173.1, 173.4, 176.1, 177.1, 177.3, 178.3, 179]
'''

# %%
Years = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980]
Heights = [170, 172.1, 173.1, 173.4, 176.1, 177.1, 177.3, 178.3, 179]
Average = []

# 1900 - 1910 : Given formula calculation
calc1 = (Heights[1]-Heights[0])
calc2 = (calc1 / Heights[0]) * 100
print("%.3f" % calc2 + "%")

print("-------------------------")

# Looping through the list
b = len(Years) - 1
for i, v in enumerate(Years):
  if i < b:
    calc1 = (Heights[i+1] - Heights[i])
    calc2 = (calc1 / Heights[i]) * 100
    print("Years:", Years[i], "-", Years[i+1])
    print("Growth Average: " + "%.3f" % calc2 + "%")
    print("")
    Average.append(calc2)

maxi = max(Average)
pos = Average.index(maxi)
print("The largest growth:", "%.3f" % maxi + "%")
print("During the years:", Years[pos], "-", Years[pos+1])
# %%
