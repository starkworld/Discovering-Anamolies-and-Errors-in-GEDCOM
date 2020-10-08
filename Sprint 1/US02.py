"""
Author: Nikhil Kalyan
Time: 04 Oct, 202o 7:15PM
Implementing user story 2 which identified children birth before parents marriage
"""
from typing import Dict
from famclass import gedFileParse

individual, family = gedFileParse("/Users/nikhilkalyan/Discovering-Anamolies-and-Errors-in-GEDCOM/CFMT.ged")

dateList = []


def getMarriedDateUsingID(famListData, id):
    for i in famListData:
        if (i[0] == id):
            return i[3]


def birthBeforeMarriage(indiListData, famListData):
    for i in indiListData:
        birthDate = i[3]
        if i[5] != 0:
            for j in i[5]:
                if birthDate > getMarriedDateUsingID(famListData, j):  # We call the function here to get the dates
                    dateList.append(i[1])
                    print(i[1] + " have their marriage dates before birth date")
                    break
    if len(dateList) == 0:
        print("There is no individual having birth dates after marriage dates :)")
    else:
        print("These people have birth dates after their marriage dates :( ")
        print(dateList)



print(individual)
print(family)

birthBeforeMarriage(individual, family)
