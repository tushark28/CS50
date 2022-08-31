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
select
    transcript
from
    interviews
where
    year = 2021
    and month = 7
    and day = 28;
union all
select
    license_plate
from
    bakery_security_logs
where
    year = 2021
    and month = 7
    and day = 28
    and hour = 10
    and minute = 15;