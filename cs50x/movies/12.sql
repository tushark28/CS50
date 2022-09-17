SELECT
    title
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
                    name = "Johnny Depp"
            )
    )
intersect
SELECT
    title
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
                    name = "Helena Bonham Carter"
            )
    )