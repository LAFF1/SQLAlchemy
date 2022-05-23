# SQLAlchemy
Surfs Up Repository 

### Overview

Create a webpage to display Hawaii weather information from a SQLite database and return a json response, using Python and Flask. There is a main page, and responses both json and error responses are returned on a separate page.  At the bottom of this README, you can also find additional temperature analysis for the beautiful state of Hawaii.  

## Home Page 

![image](https://user-images.githubusercontent.com/98897041/169849001-f662375e-fd2b-4217-92ac-b25eb4365dc4.png)

## Precipitation Analysis
Precipitation is a hyperlink to a json response of the last 12 months of precipitation records.

![image](https://user-images.githubusercontent.com/98897041/169850180-fc3157d9-bd08-491e-ba3a-1863d2fd160a.png)

## Station Analysis
Stations is a hyperlink that returns a json response of all of the reporting stations in the database.

![image](https://user-images.githubusercontent.com/98897041/169850652-de98e1f9-817c-4ea3-b0bb-a91ecc7f3c20.png)

Most active station information, is determined by counting the number of reports by each station and then the station id is returned to the page and displayed. 

Most active station is a hyperlink that returns a json response of all the temperature observations for the most active station in the database.

![image](https://user-images.githubusercontent.com/98897041/169851502-797104dc-3b02-4b10-8fdb-c77a44422e9e.png)

## Temperature Observations  

Temperature observations returns the minimum, average and maximum temperatures for a date. There are two paths the first provides a json response for a year beginning with the date that is entered. The second allows a date range to be selected, and provides a json response for each date in the range. If a date is not entered or is invalid - and error message is returned and the date and/or date range may be corrected and requested again. 

12 month period beginning with date entered:      Response  
![image](https://user-images.githubusercontent.com/98897041/169853271-9057aab1-03dc-4415-825b-bc7231b96ffc.png)
![image](https://user-images.githubusercontent.com/98897041/169853401-3bfd6275-de38-414d-9083-6f97c547b665.png)

Date range inclusive of dates entered:            Response  
![image](https://user-images.githubusercontent.com/98897041/169854335-d5a11cd2-b40f-44fe-9166-0542afc1f30f.png)
![image](https://user-images.githubusercontent.com/98897041/169854440-6f7734c5-e9d1-4203-93cf-5cab38254152.png)



## Analysis  

Is there a significant difference in the temperature between June and December?
The two hypotheses for this particular two sample t-test are as follows:
H0: µ1 = µ2 (the two population means are equal)
HA: µ1 ≠µ2 (the two population means are not equal)

Because the p-value of our test (3.864098966773339e-194) is less than alpha = 0.05, we fail to reject the null hypothesis of the test.

![image](https://user-images.githubusercontent.com/98897041/169856331-55969915-66db-40ce-b2e4-a64f5c3e72f9.png)

Turns out the weather in Hawaii always rocks! You should definitely go!

### Trip Average Temp
Here we selected travel dates for the entire year of 2016 on the left and travel dates for the week on August 1-7.
The trip average temperature is represented in the chart below. The I line represents the difference between the lowest temperature reading and the highest temperature reading. 


![image](https://user-images.githubusercontent.com/98897041/169858965-2f61d7c1-c338-499c-a008-b4e2888801a3.png) Year 
![image](https://user-images.githubusercontent.com/98897041/169858988-cfc07154-9b95-4405-97ea-8e762fa3e57d.png) Aug 1-7

### Exploratory Precipitation Analysis
Here we take a look at rainfall over the course of a year, in this case Aug 24, 2016 to Aug 23, 2017. The chart shows the daily rainfall for each day in our range.

![image](https://user-images.githubusercontent.com/98897041/169877023-504e7dc6-5e7e-4125-9b4c-7b7735edfce2.png)


### Daily Rainfalls 
We planned this trip for August 1st through August 27th, below are the rain averages by station. You might get a little wet around station USC00516128, otherwise you can leave your unbrellas at home. 

![image](https://user-images.githubusercontent.com/98897041/169872238-c22c864b-d6ab-43d2-8a86-a823e2615a2f.png)

### Daily Normals
Also using our trip from August 1st through August 27th, we took a look at our daily normal temperatures looking at the minimum, average and maximum temperatures historically for all the years we have in our database. On the left these are shown in a staked graph and on the right they are shown in an unstacked graph. 

![image](https://user-images.githubusercontent.com/98897041/169879472-a34a1bcc-c992-4b1c-81ea-4494f2261ead.png)    
![image](https://user-images.githubusercontent.com/98897041/169879648-20b9c2a0-f244-4879-837c-0214035e264e.png)

## Temperature vs Frequency 
For our most active station we took a look at the frequency that each temperature was reported by the most active station in our database. Not surprisingly 76°F was the most reported. TOBS = Temperature observations.

![image](https://user-images.githubusercontent.com/98897041/169877971-850ebb16-1aa5-4bce-96c6-6b4fab815ec7.png)

## Conclusion

You should really enjoy your Hawaiian vacation, it really doesn't matter when you choose to go... paradise awaits. 


## Resouces 
Python/Flask/sqlalchemy  
Jupyter Notebook/Python/matplotlib/sqlalchemy/pandas/seaborn/numpy/pandas  
<sub>Credit for photo -- sean-oulashin-KMn4VEeEPR8-unsplash.jpg
Native photo url "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=873&q=80"<sub>
