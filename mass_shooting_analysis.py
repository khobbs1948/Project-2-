#!/usr/bin/env python
# coding: utf-8

# ETL: Extract, Transform, Load
# -------------------------------------------
# In the following code, we will extract two sources of data (US Mass Shootings from 1982-2022 and Firearm Provisions in US States per year from 1991-2017). 
# We will then clean and transform the data to be able to merge the files on state and year. 
# We will generate two dataframes listing each state, year, number of gun regulations present in that state at that year, and number of mass shootings that took place in that state and year. One table will be an inner join and one table will be an outer join.
# An additional column called "state cumulative shootings" is added to show the cumulative number of mass shootings in a state over the years.
# Finally, we will create a connection to SQL to load the dataframe into a data table to be displayed and turned over for data analysis.

#import dependencies
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

#read in mass shooting data by location
#mass shooting data starts at 1982 and goes through 2022
csv_file = "mass_shootings.csv"
mass_shootings_df = pd.read_csv(csv_file)

#separate city from state using .apply function
mass_shootings_df["state"] = mass_shootings_df["location"].apply(lambda x:x.split(",")[1])

#get rid of spaces before and after the state so that merge will work later
mass_shootings_df['state'] = mass_shootings_df['state'].str.strip()

#choose columns that you want to keep in dataframe
#keep summary as a unique column to do groupby later
ms_df = mass_shootings_df[["state","year","summary"]]

#group by state and year to get number of shootings per state and year
summary_ms = ms_df.groupby(["state","year"]).count()
summary_ms = summary_ms.sort_values(["year"], ascending=True)
summary_ms

#value counts to check data
summary_ms.value_counts()

#rename column "summary" to "shootings"
shootings_df = summary_ms.rename(columns={"summary":"shootings"})
shootings_df = shootings_df.reset_index()

#calculate the cumulative number of shootings per state in sequential order
shootings_df['state_cumulative_shootings'] = shootings_df[['state', 'shootings']].groupby('state').cumsum()
shootings_df

#read in data set showing gun regulations by state by year (restricting gun ownership)
#gun laws start at 1991 and goes through 2017
csv_file = "gun_laws.csv"
gun_laws_df = pd.read_csv(csv_file)
gun_laws_df

#keep desired columns: state, year, and total number of laws
laws_df = gun_laws_df[["state","year","lawtotal"]]
laws_df

#do an outer join to merge data frames on year and state, so that the law total is added per state and year
df = pd.merge(shootings_df, laws_df, how="outer",on=["year","state"])

#do an inner join to merge data frames on year and state, so that the law total is added only per state and year with a mass shooting
df_cleaned = pd.merge(shootings_df, laws_df, how="inner",on=["year","state"])
df_cleaned

#sort dataframe from oldest year to most recent year
df = df.sort_values(["year"], ascending=True)
df = df.rename(columns= {"lawtotal": "number_gun_regulations"})
df.set_index(["state", "year"],inplace=True)

#sort dataframe from oldest year to most recent year
df_cleaned = df_cleaned.sort_values(["year"], ascending=True)
df_cleaned = df_cleaned.rename(columns= {"lawtotal": "number_gun_regulations"})
df_cleaned.set_index(["state", "year"], inplace=True)

#establish the connection to postgresql
protocol = 'postgresql'
username = 'postgres'
password = 'admin'
host = 'localhost'
port = 5432
database_name = 'mass_shootings_db'
rds_connection_string = f'{protocol}://{username}:{password}@{host}:{port}/{database_name}'
engine = create_engine(rds_connection_string)

#create table in sql
#check table exists
#engine.table_names()

#upload dataframes into sql
df.to_sql(name='mass_shootings_outer', con=engine, if_exists='append', index=True)

df_cleaned.to_sql(name='mass_shootings_inner', con=engine, if_exists='append', index=True)

#Confirm the data has been added in the mass_shootings_outer table (all data)
#pd.read_sql_query("select * from mass_shootings_outer", con=engine)

#Confirm the data has been added in the mass_shootings_inner table (cleaned database)
#pd.read_sql_query("select * from mass_shootings_inner", con=engine)

