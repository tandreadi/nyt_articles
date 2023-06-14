

  create or replace view `nytarticles`.`nyt_articles_dataset`.`int_daily_metadata`
  OPTIONS()
  as WITH

nyt_articles_metadata AS (

    SELECT * FROM `nytarticles`.`nyt_articles_dataset`.`stg_nytarticles__metadata`

),

daily_metadata AS (

    SELECT
        published_date,
        item_type,
        section,
        material_type_facet,
        COUNT(article_id) AS number_of_articles,
        AVG(title_length) AS average_title_length,
        AVG(abstract_length) AS average_abstract_length
    FROM nyt_articles_metadata
    GROUP BY published_date, item_type, section, material_type_facet

)

SELECT * FROM daily_metadata;

