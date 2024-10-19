-- DuckDB SQL preprocess query 
WITH movies AS (
     SELECT 
         movie_title AS title
         ,director_name AS director
         ,title_year AS year
         ,CONCAT(actor_1_name,'|',actor_2_name,'|', actor_3_name) AS actors
         ,GREATEST(actor_1_facebook_likes,actor_2_facebook_likes,actor_3_facebook_likes) AS max_fb_likes
         ,duration
         ,genres
         ,plot_keywords
         ,budget
         ,gross
         ,imdb_score AS imdb
         ,num_voted_users
         ,country
         ,content_rating
         ,ROW_NUMBER() OVER (PARTITION BY movie_title,director_name  ORDER BY title_year) AS row_num --used to remove duplicates

    FROM 'data/clean.csv'
    WHERE genres NOT IN ['Documentary', 'History', 'Biography', 'Sport']
        AND title_year > 1999
        AND language = 'English'
        AND LENGTH(director_name) <> 0
        AND LENGTH(content_rating) <> 0
        AND aspect_ratio <> 0
        AND budget <> 0
        AND gross <> 0
)
    SELECT 
      *
    FROM movies
    WHERE row_num = 1 --removes duplicates
        ORDER BY year DESC 
