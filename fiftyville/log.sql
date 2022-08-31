-- Keep a log of any SQL queries you execute as you solve the mystery.
--for description about the crime.
SELECT
    description
from
    crime_scene_reports
where
    year = 2021
    and month = 7
    and day = 28
    and street = "Humphrey Street"
union all
select
    transcript
from
    interviews
where
    year = 2021
    and month = 7
    and day = 28;
select 