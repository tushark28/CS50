SELECT
    name
FROM
    people
WHERE
    id IN (
        SELECT
            movie_id
        FROM
            stars
        WHERE
            movie_id = (
                SELECT
                    id
                FROM
                    movies
                WHERE
                    title = "Toy Story"
            )
    );