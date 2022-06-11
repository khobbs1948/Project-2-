drop table mass_shootings_outer
drop table mass_shootings_inner

-- Create Table
CREATE TABLE mass_shootings_outer(
index INT PRIMARY KEY,
year INT,
state TEXT, 
shootings INT,
number_gun_regulations INT,
state_cumulative_shootings INT
);

CREATE TABLE mass_shootings_inner(
index INT PRIMARY KEY,
year INT,
state TEXT, 
shootings INT,
number_gun_regulations INT,
state_cumulative_shootings INT
);

select*from mass_shootings_outer
select*from mass_shootings_inner