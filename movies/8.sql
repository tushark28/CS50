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
    );