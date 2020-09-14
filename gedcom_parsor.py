"""Created by Nikhil Kalyan
            Date: 09/12/2020 11:20PM
        Program that reads the GEDCOM file and Prints every input line of GEDCOM in this format 
        <-- <level>|<tag>|<valid?> : Y or N|<arguments>"""


def ged_reader(path):
    """Function that Read the input file write the given format to the file"""
    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        print("Cannot open {}".format(path))
    else:
        all_lines = fp.readlines()
        fp = open(path, 'w')

        for line in all_lines[2:]:
            line = line.rstrip('\n')
            print("--> " + line)
            fp.write("--> " + line + '\n')
            line_lst = line.split(' ', 2)
            line_str = check_item(line_lst)
            print("<-- " + line_str)
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
    string = str()
    try:
        string = lst[0] + lst[1] + lst[2]
    except IndexError:
        string = lst[0] + lst[1]
    return string


def main():
    "Main method call all the functions"
    path = input("Enter path:")
    ged_reader(path)


if __name__ == '__main__':
    main()
