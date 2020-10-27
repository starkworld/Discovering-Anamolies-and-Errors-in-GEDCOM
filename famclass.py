"""Author: Nikhil Kalyan
    Created on 09/20/20 9:00PM
    Program is about parsing GEDCOM file and getting individual info and family info in two different tables
    We are using prettytable module for this task I will create two tables one is viewing individual info and other for 
    Viewing family info"""

from prettytable import PrettyTable
from typing import List, Tuple, TextIO


def familyList() -> List[int]:
    """Method which creates list of length 5 to store family info"""
    family_list: List = [0 for _ in range(6)]
    family_list[5] = []
    return family_list


def individualList() -> List[int]:
    """Method creates list for storing individual info"""
    return [0 for _ in range(7)]


def lastName(s: str) -> str:
    """Method strips slashes in last name return last name"""
    data: str = ''
    for i in s:
        if i != '/':
            data += i
    return data


def getNameUsingID(individualList: List, ID: int) -> List[str]:
    """Method takes ID as arg and returns associated name to that ID"""
    for i in individualList:
        if i[0] == ID:
            return i[1]


def gedFileParse(fileName: str) -> Tuple[List[str], List[str]]:
    global famValue
    readFile: TextIO = open(fileName, 'r')
    individualValue: int = 0
    familyValue: int = 0
    individual: List = []
    family: List = []
    individualData: List = individualList()
    familyData: List = familyList()
    for line in readFile:
        each_line: List[str] = line.split()
        if each_line:
            if each_line[0] == '2':
                if each_line[1] == 'DATE':
                    date: str = each_line[4] + " " + each_line[3] + " " + each_line[2]
                    if dateID == 'BIRT':
                        individualData[3]: str = date
                    if dateID == 'DEAT':
                        individualData[4]: str = date
                    if dateID == 'MARR':
                        familyData[3]: str = date
                    if dateID == 'DIV':
                        familyData[4]: str = date

            if each_line[0] == '1':
                if each_line[1] == 'NAME':
                    individualData[1]: str = each_line[2] + " " + lastName(each_line[3])
                if each_line[1] == 'SEX':
                    individualData[2]: str = each_line[2]
                if each_line[1] == 'BIRT':
                    dateID: str = 'BIRT'
                if each_line[1] == 'DEAT':
                    dateID: str = 'DEAT'
                if each_line[1] == 'MARR':
                    dateID: str = 'MARR'
                if each_line[1] == 'DIV':
                    dateID: str = 'DIV'
                if each_line[1] == 'FAMS':
                    individualData[5]: str = each_line[2]
                if each_line[1] == 'FAMC':
                    individualData[6]: str = each_line[2]
                if each_line[1] == 'HUSB':
                    familyData[1]: str = each_line[2]
                if each_line[1] == 'WIFE':
                    familyData[2]: str = each_line[2]
                if each_line[1] == 'CHIL':
                    familyData[5]: str = each_line[2]

            if each_line[0] == '0':
                if individualValue == 1:
                    individual.append(individualData)
                    individualData: List = individualList()
                    individualValue: int = 0
                if familyValue == 1:
                    family.append(familyData)
                    familyData: List = familyList()
                    familyValue: int = 0
                if each_line[1] in ['NOTE', 'HEAD', 'TRLR']:
                    pass
                else:
                    if each_line[2] == 'INDI':
                        individualValue: int = 1
                        individualData[0]: str = each_line[1]
                    if each_line[2] == 'FAM':
                        familyValue: int = 1
                        familyData[0]: str = each_line[1]
    return individual, family


def prettyPrint(individual: List[str], family: List) -> None:
    """Prints the pretty tables of family info and individual info"""
    
    print("<-------------------     Individual Info    ------------------->")
    table: PrettyTable = PrettyTable(["ID", "Name", "Gender", "Birth Date", "Death Date", "Child", "Spouse"])
    for i in individual:
        table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])
    print(table)

    table1: PrettyTable = PrettyTable(["ID", "Married", "Divorced", "Husband ID", "Husband's Name", "Wife ID", "Wife's Name", "Children"])
    print("<-----------------------------------  Family Info  -------------------------------------->")
    for i in family:
        table1.add_row([i[0], i[3], i[4], i[1], getNameUsingID(individual, i[1]), i[2], getNameUsingID(individual, i[2]), i[-1]])
    print(table1)


def main() -> None:
    """Main function calls the all methods"""
    individual, family = gedFileParse("/Users/nikhilkalyan/Discovering-Anamolies-and-Errors-in-GEDCOM/CFMT.ged")
    print(individual)
    individual.sort()
    family.sort()
    # prettyPrint(individual, family)


if __name__ == '__main__':
    """Calls main to start execution"""
    main()