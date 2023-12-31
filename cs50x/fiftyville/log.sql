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
            person_id
        from
            bank_accounts
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
    )

select * from phone_calls where year = 2021 and month = 7 and day = 28 and duration <= 60;

select * from flights where year = 2021 and month = 7 and day = 29;

select * from passengers where flight_id = 36;

select * from airports where id = 4;

select * from phone_calls where caller like "(367)%" and year = 2021 and month = 7 and day = 28;

select * from people where phone_number = "(375) 555-8161";