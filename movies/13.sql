select
    name
from
    people where id in(
        select person_id from stars where movies_id in(
            select id from movies where id in(
                select person_id from stars where person
            )
        )
    )