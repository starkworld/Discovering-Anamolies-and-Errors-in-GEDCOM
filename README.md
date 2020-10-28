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
![Alt text](https://github.com/starkworld/Discovering-Anamolies-and-Errors-in-GEDCOM/blob/master/images/Screen%20Shot%202020-09-20%20at%2010.59.12%20PM.png)

![Alt text](https://github.com/starkworld/Discovering-Anamolies-and-Errors-in-GEDCOM/blob/master/images/Screen%20Shot%202020-09-20%20at%2010.59.28%20PM.png)

### Planning Sprint 1:
##### User Stories to Achieve during sprint 1 showned below:
##### This describe there are 16 user stories to achieve during sprint one and it will take time to do so. 
![Alt text](https://github.com/starkworld/Discovering-Anamolies-and-Errors-in-GEDCOM/blob/master/images/Screen%20Shot%202020-09-22%20at%203.02.29%20AM.png)

#### Burndown Chart for the project
##### The burndown is a chart that shows how quickly you and your team are burning through your customer's user stories. It shows the total effort against the amount of work we deliver each iteration
![Alt text](https://github.com/starkworld/Discovering-Anamolies-and-Errors-in-GEDCOM/blob/master/images/Screen%20Shot%202020-09-22%20at%203.06.39%20AM.png)
##### We can see the total effort on the left, our team velocity on the right. But look what else this simple graphs gives us.

* Work done each iteration
* Work remaining
* Work done so far
* When we can expect to be done

Till date 6User stories are implemented in sprint 1 and code reviews are doing after completion of each user story

* Sprint 1 is completed and took 15days to complete all user stories and code reviews and fixes are been done

#### Sprint 2
* Sprint two plaaning is taken place and started working on sprint 2:
##### BurnDown Chart
![Alt text](https://github.com/starkworld/Discovering-Anamolies-and-Errors-in-GEDCOM/blob/master/images/Burndown.png)



