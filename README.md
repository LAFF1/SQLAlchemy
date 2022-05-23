# SQLAlchemy
Surfs Up Repository 

### Overview

Create a webpage to display Hawaii weather information from a SQLite database and return a json response, using Python and Flask. There is a main page, and responses both json and error responses are returned on a separate page. 

## Home Page 

![image](https://user-images.githubusercontent.com/98897041/169849001-f662375e-fd2b-4217-92ac-b25eb4365dc4.png)

## Precipitation Analysis
Preciptaion is a hyperlink to a Json response of the last 12 months of precipitation records.

![image](https://user-images.githubusercontent.com/98897041/169850180-fc3157d9-bd08-491e-ba3a-1863d2fd160a.png)

## Station Analysis
Stations is a hyperlink that returns a json resonse of all of the reporting stations in the database.

![image](https://user-images.githubusercontent.com/98897041/169850652-de98e1f9-817c-4ea3-b0bb-a91ecc7f3c20.png)

Most active station information, is determined by counting the number of reports by each station and then the station id is returned to the page and displayed. 

Most active station is a hyperlink that returns a json response of all the temperatur observations for the most active station in the database.

![image](https://user-images.githubusercontent.com/98897041/169851502-797104dc-3b02-4b10-8fdb-c77a44422e9e.png)

## Temperature Observations  

Temperature observations returns the minimum, average and maximum temperatures for a date. There are two paths the first provides a json response for a year beggining with the date that is entered. The second allows a date range to be selected, and provides a json reponse for each date in the range. If a date is not entered or is invalid - and error message is returned and the date and/or date range may be corrected and requested again. 

12 month period beginning with date entered:      Response  
![image](https://user-images.githubusercontent.com/98897041/169853271-9057aab1-03dc-4415-825b-bc7231b96ffc.png)
![image](https://user-images.githubusercontent.com/98897041/169853401-3bfd6275-de38-414d-9083-6f97c547b665.png)

Date range inclusive of dates entered:            Response  
![image](https://user-images.githubusercontent.com/98897041/169854335-d5a11cd2-b40f-44fe-9166-0542afc1f30f.png)
![image](https://user-images.githubusercontent.com/98897041/169854440-6f7734c5-e9d1-4203-93cf-5cab38254152.png)
