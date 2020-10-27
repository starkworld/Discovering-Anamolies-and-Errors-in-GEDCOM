"""Created by Nikhil Kalyan
            Date: 09/12/2020 11:20PM
        Program that reads the GEDCOM file and Prints every input line of GEDCOM in this format 
        <-- <level>|<tag>|<valid?> : Y or N|<arguments>"""
from typing import List


def ged_reader(path):
    """Function that Read the input file write the given format to the file"""
    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        print("Cannot open {}".format(path))
    else:
        all_lines = fp.readlines()
        fp = open('/Users/nikhilkalyan/Discovering-Anamolies-and-Errors-in-GEDCOM/output.txt', 'w')

        for line in all_lines[2:]:
            line = line.rstrip('\n')
            fp.write("--> " + line + '\n')
            line_lst = line.split(' ', 2)
            line_str = check_item(line_lst)
            fp.write("<-- " + line_str + '\n')
        fp.close()


def check_item(line_lst):
    """Function that takes file lines as input list and compare with exisitng file"""
    top_level_1 = {'HEAD', 'TRLR', 'NOTE'}
    top_level_2 = {'INDI', 'FAM'}
    tag_indi = {'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS'}
    tag_fam = {'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV'}
    tag_date = {'DATE'}
    tmp = line_lst

    if tmp[0] == '0':
        if tmp[1].isupper() and tmp[1] in top_level_1:
            tmp[1] = "|{}|Y|".format(tmp[1])
            return to_str(tmp)
        if tmp[2].isupper():
            tmp[1], tmp[2] = tmp[2], tmp[1]
            if tmp[1] in top_level_2:
                tmp[1] = "|{}|Y|".format(tmp[1])
            return to_str(tmp)
        tmp[1] = "|{}|N|".format(tmp[1])
        return to_str(tmp)

    if tmp[0] == '1':
        if tmp[1] in tag_indi or tmp[1] in tag_fam:
            tmp[1] = "|{}|Y|".format(tmp[1])
            return to_str(tmp)
        else:
            tmp[1] = "|{}|N|".format(tmp[1])
            return to_str(tmp)

    if tmp[0] == '2':
        if tmp[1] in tag_date:
            tmp[1] = "|{}|Y|".format(tmp[1])
            return to_str(tmp)
        else:
            tmp[1] = "|{}|N|".format(tmp[1])
            return to_str(tmp)
    else:
        tmp[1] = "|{}|N|".format(tmp[1])
    return to_str(tmp)


def to_str(lst):
    """Method that returns list of given line of file"""
    try:
        string = lst[0] + lst[1] + lst[2]
    except IndexError:
        string = lst[0] + lst[1]
    return string


def findParents(id: int, listFam: List) -> str:
    found: str = ""
    for fam in listFam:
        if id in fam[-1:]:
            found: str = fam
            break
    return found


def checkIfSiblings(fam1: List, fam2: List, listFam: List) -> bool:
    """just makes sure siblings aren't married, if they are return false"""
    if fam1[0] == fam2[0]:
        return False
    husb1fam: str = findParents(fam1[1], listFam)
    husb2fam: str = findParents(fam2[1], listFam)
    wife1fam: str = findParents(fam1[2], listFam)
    wife2fam: str = findParents(fam2[2], listFam)

    if husb1fam:
        if husb2fam:
            if husb1fam[0] == husb2fam[0]:
                return True
        elif wife2fam:
            if husb1fam[0] == wife2fam[0]:
                return True
    elif wife1fam:
        if husb2fam:
            if wife1fam[0] == husb2fam[0]:
                return True
        elif wife2fam:
            if wife1fam[0] == wife2fam[0]:
                return True

    return False


def main():
    """Main method call all the functions"""
    path = input("Enter path:")
    ged_reader(path)


if __name__ == '__main__':
    main()
