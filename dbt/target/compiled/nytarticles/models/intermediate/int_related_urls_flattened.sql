WITH

nyt_articles_metadata AS (

    SELECT * FROM `nytarticles`.`nyt_articles_dataset`.`stg_nytarticles__metadata`

),

flattened_related_urls AS (

    SELECT
        nyt.article_id,
        nyt.title,
        nyt.url,
        nyt.section,
        nyt.subsection,
        ru.url AS reffering_url
    FROM nyt_articles_metadata AS nyt, UNNEST(related_urls) AS ru

)

SELECT * FROM flattened_related_urls