

  create or replace view `nytarticles`.`nyt_articles_dataset`.`int_authors_flattened`
  OPTIONS()
  as WITH

nyt_articles_metadata AS (

    SELECT * FROM `nytarticles`.`nyt_articles_dataset`.`stg_nytarticles__metadata`

),

flattened_authors AS (

    SELECT
        article_id,
        section,
        subsection,
        title,
        organisation_facet,
        material_type_facet,
        item_type,
        title_length,
        abstract_length,
        ARRAY(
            SELECT CAST(elem AS string)
            FROM UNNEST(SPLIT(authors, ",")) AS elem) AS author
    FROM nyt_articles_metadata

)

SELECT * FROM flattened_authors;

