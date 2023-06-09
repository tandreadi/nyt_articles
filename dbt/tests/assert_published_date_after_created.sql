SELECT article_id
FROM {{ ref('stg_nytarticles__metadata') }}
WHERE published_date < created_date
