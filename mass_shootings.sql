drop table mass_shootings
-- Create Table
CREATE TABLE mass_shootings(
index INT PRIMARY KEY,  
year INT,
state TEXT, 
shootings INT,
lawtotal INT,
state_cumulative_shootings INT
);

select*from mass_shootings
