SELECT
    title
FROM
    movies
WHERE
    id IN(
        SELECT
            movie_id
        FROM
            stars
        WHERE
            person_id IN(
                SELECT
                    id
                FROM
                    people
                WHERE
                    name = "Chadwick Boseman"
            )
    )
LIMIT 5;