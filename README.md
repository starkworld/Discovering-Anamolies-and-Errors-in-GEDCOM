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


All lines (or records) begin with a level numberthat is used to group the information from multiple records. Records with level numbers 1 and 2are always in the form: <level_number> <tag> <arguments>Lines with level number 0have one of twodifferent forms.  The first has the form0 <id> <tag>where<tag>isINDI orFAM.  The <id>field between the "0" and the tag is a unique identifier used to identify an individual or a family.The second versionof level 0 records hasthe form0 <tag><arguments that may be ignored>where<tag>isHEAD, TRLR, orNOTE.For example,0 p1 INDIbegins the definition of a new person with id ‘p1’.  The definition may include any number of records of level 1 or 2.
  
#### (Sprint 1):
During this sprint I have got to know some user stories they are:
#### StoryID: US01                  
#### StoryName: Dates before current date                   
#### StoryDescription: Dates(birth,marriage,divorce,death)should not be after the current date

#### StoryID: US02                  
#### StoryName: Birth before marriage                  
#### StoryDescription: Birth should occur before marriage of an individual

Apart of this here I displayed data of an each individual and families in pretty tables
![Alt text](https://github.com/starkworld/Discovering-Anamolies-and-Errors-in-GEDCOM/blob/master/Screen%20Shot%202020-09-20%20at%2010.59.12%20PM.png)

![Alt text](https://github.com/starkworld/Discovering-Anamolies-and-Errors-in-GEDCOM/blob/master/Screen%20Shot%202020-09-20%20at%2010.59.28%20PM.png)
