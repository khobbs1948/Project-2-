Project 2:
Extract, Transform, and Load
The US has witnessed several mass shootings. With recent news of yet another two mass shootings in the past month and much debate ongoing on gun regulations at a state and national level, the team decided to set up a data set exploring mass shooting data and corresponding gun regulations by state and year.

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

The final database is in PostgreSQL, a relational database and consists of two data tables.

The objective of the data engineering project is to combine the data to potentially analyze relationships between the following:
Gun regulations and subsequent levels of mass shootings in each state
Mass shootings and subsequent gun regulations in each state or surrounding state
Number of mass shootings and the number of gun regulations over time in each state
Trend in gun regulations and mass shootings over time in each state

Transform data
--------------
(1) US Mass Shooting data lists the location as "city,state" of the mass shooting. Parse out state into a separate column and remove spaces before the "state" name. Create an additional column, the cumulative sum of shootings per state over time. Extract desired columns, the state, year, and a unique summary. Use the groupby function to determine the number of mass shootings by state and year. 

(2)Firearm provisions data lists each provision as a column with identifying boolean values (1 or 0) to indicate if the state has the provision or not. The total number of provisions for the state is totaled in a final column. 
Extract desired columns, the state, year, and number of total gun regulations

The team created two data tables from the dataset. 
A first table, mass_shootings_outer, was created through an outer join to merge the mass shooting data with the number of gun regulations present per state.
This was completed in jupyter notebook under the dataframe name "df". This table consists of all years of data in the table, even though corresponding firearm provision data was not available from the periods of 1982-1990 and 2018-2022.

A second table, mass_shootings_inner, was created through an inner join to merge the mass shooting data with the number of gun regulations present per state.
This was also completed in jupyter notebook under the dataframe name "df_cleaned". The table is the overlap between the mass shooting data set and the gun regulations, so it consists of the total gun regulations only where there was a mass shooting. 
Therefore, data is shown only from 1991-2017, where both datasets had data.

Load data
-------------
Create a connection to the PostgreSQL database.
Create two tables, mass_shootings_outer and mass_shootings_inner, to prepare loading the dataframe into SQL.
Load the data and check that all data is there and looks correctly merged.
