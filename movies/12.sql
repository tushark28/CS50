SELECT
    count(title)
FROM
    movies
WHERE
    id in(
        select
            movie_id
        from
            stars
        where
            person_id in(
                select
                    id
                from
                    people
                where
                    name in("Johnny Depp","Helena Bonham Carter")
            )

    )