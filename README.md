# Discovering-Anamolies-and-Errors-in-GEDCOM
This project is Common line program which discover errors and anomalies in GEDCOM genealogy files

GEDCOM is a standard format for genealogy data developed by The Church of Jesus Christ of Latter-day Saints. GEDCOM identifies two major entities: individuals and families.  GEDCOM allows you to describe the following characteristics of individuals:
#### •Unique individual ID
#### •Name
#### •Sex/Gender
#### •Birth date
#### •Death date
#### •Unique Family ID where the individual is a child
#### •Unique Family ID where the individual is a spouseLikewise,

GEDCOM allows you to describe the following characteristics of a family:
#### •Unique family ID
#### •Unique individual ID of husband
#### •Unique individual ID of wife
#### •Unique individual ID of each child in the family
#### •Marriage date
#### •Divorce date,

if appropriateGEDCOMis a line-oriented text file format where each line has three parts separated by blank space:
#### 1.level number(0, 1, or 2) 
#### 2.tag(a string of 3 or 4 characters) 
#### 3.arguments(an optional character string) 


All lines (or records) begin with a level numberthat is used to group the information from multiple records. Records with level numbers 1 and 2are always in the form: <level_number> <tag> <arguments>Lines with level number 0have one of twodifferent forms.  The first has the form0 <id> <tag>where<tag>isINDI orFAM.  The <id>field between the "0" and the tag is a unique identifier used to identify an individual or a family.The second versionof level 0 records hasthe form0 <tag><arguments that may be ignored>where<tag>isHEAD, TRLR, orNOTE.For example,0 p1 INDIbegins the definition of a new person with id ‘p1’.  The definition may include any number of records of level 1 or 2.  The definition of person ‘p1’ ends either at the end of the GEDCOM file, or with the next level 0 record.0 f207 FAMbegins the definition of a new family with id ‘f207’.0 NOTE this is commentdefines a new comment.Level numbers provide a mechanism for grouping records in hierarchical groups: all records with larger level numbers than the current record belong to theentity headed by that entity. For example, all of the records from the first level 0 record, up to, but not including the “0 F32 FAM” record, belong to the group headed by the first record(with level 0)that describes the individual with ID “I27”. The DATE record with level number 2 is associated withthe previous BIRT record with level number 1.0 I27INDI1 NAME Mark /Ardis/1 SEX M 1 BIRT2 DATE 7 APR 19491 FAMC F320 NOTE end of individual Mark ArdisThe first level 0 record identifies a new individual with id “I27”.All following records with levelgreater than 0, until the next level 0 record,identify characteristics of individual I27.The “1 NAME”record specifies thatthe nameof individual I27is ‘Mark Ardis’.   (The individual’s last name is surrounded by slashes.) The ‘1 SEX M’ record specifies that the gender of individual I27is male.  The ‘1 BIRT’ recordis the first of two records that specify individual I27’s birthdate.  The ‘2 DATE 7 APR 1949’record specifies the date and since level 2 is greater than level 1, the DATE record is associated with the preceding BIRT record.   Finally, the ‘1 FAMC F32’ record tells us that the preceding DATE and BIRT records are complete and that the current individual is a child in family F32(Note that F32may or may not be defined when this record is parsed.)Finally, the ‘0 NOTE’record tells us that the definition of individual I27is complete (because we found another level 0 record).   Note that IDs of both individuals and families are arbitrary strings.  You should NOTassume that all IDs have any specific format.I will test your program with you a variety of id formats.The Wikipedia entry for GEDCOM <http://en.wikipedia.org/wiki/GEDCOM> has a nice introduction with pointers to more information. Family Echo <http://www.familyecho.com> and Geni <http://www.geni.com> allow you to create your family tree online and export it later in GEDCOM format. They are free, but they require you to create an account. Geni has a social networking component to its product. It will email you with reminders of birthdays and anniversaries of your relatives. You may want to try out one of these systems to see how informationis recorded in GEDCOM files. For this project,we are going to work with a subset of GEDCOM, and we will assume that all records are syntactically well-formed. That is, all records will start with a level number in the first character of the record, havea legal tag, and will have arguments in the proper format. Also, only one blank space will be used to separate all fields. 
