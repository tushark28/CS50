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
union
all
select
    transcript
from
    interviews
where
    year = 2021
    and month = 7
    and day = 28;

select
    *
from
    bakery_security_logs
where
    year = 2021
    and month = 7
    and day = 28
    and hour = 10
    and minute <= 25;

select
    *
from
    atm_transactions
where
    year = 2021
    and month = 7
    and day = 28
    and atm_location = "Leggett Street";

select
    *
from
    people
where
    id in(
        select
            *
        from
        where
            account_number in(
                select
                    account_number
                from
                    atm_transactions
                where
                    year = 2021
                    and month = 7
                    and day = 28
                    and atm_location = "Leggett Street"
            )
    );