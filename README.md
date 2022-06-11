Project 2:
Extract, Transform, and Load

Proposal:
Extract data from two csv files on mass shootings and gun regulations by state and year.
------------
Sources of data
(1) https://www.kaggle.com/datasets/zusmani/us-mass-shootings-last-50-years
US Mass Shootings May 24 2022.csv was used for the project. (1982-2022)
This data set shows the location, date, and other details about every mass shooting in the USA from 1982-2022.A mass shooting is defined as as involving four or more victims of gun violence in a short period of time.

(2)https://www.kaggle.com/datasets/jboysen/state-firearms?select=raw_data.csv
Firearm Provisions in US States shows a list of firearm provisions across the 50 states by year. (1991-2017)
The provisions are recorded for each year.

Final production database is in PostgreSQL, a relational database.

The objective of the data engineering project is to combine the data to potentially analyze several questions: Is there a relationship between the following:
Gun regulations and subsequent levels of mass shootings in each state
Mass shootings and subsequent gun regulations in each state or surrounding state
Number of mass shootings and the number of gun regulations over time in each state
Trend in gun regulations and mass shootings over time in each state.

Transform data
--------------
(1) US Mass Shooting data lists the location as "city,state" of the mass shooting. Parse out state into a separate column and remove spaces before the "state" name. Create an additional column, the cumulative sum of shootings per state over time. Extract desired columns, the state, year, and a unique summary. Use the groupby function to determine the number of mass shootings by state and year. 

(2)Firearm provisions data lists each provision as a column with identifying boolean values (1 or 0) to indicate if the state has the provision or not. The total number of provisions for the state is totaled in a final column. 
Extract desired columns: state, year, and number of total gun regulations

Perform an outer join to merge the mass shooting data with the number of gun regulations present per state.
This was completed in jupyter notebook, but could have also been done in SQL.

Load data
-------------
Create a connection to the PostgreSQL database.
Create the table, mass_shootings, to prepare loading the dataframe into SQL.
Load the data and check that all data is there and looks correctly merged.

