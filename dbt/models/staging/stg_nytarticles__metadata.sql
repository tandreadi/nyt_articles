WITH

bq_source AS (

    SELECT * FROM {{ source('nytarticles', 'nyt_articles') }}

),

nytarticles_metadata AS (
    SELECT
        uri AS article_id,
        slug_name,
        title,
        abstract,
        url,
        des_facet,
        org_facet AS organisation_facet,
        geo_facet AS geographical_facet,
        per_facet AS person_facet,
        related_urls,
        multimedia,
        thumbnail_standard,
        source,
        updated_date,
        created_date,
        published_date,
        first_published_date,
        CHARACTER_LENGTH(title) AS title_length,
        CHARACTER_LENGTH(abstract) AS abstract_length,
        COALESCE(NULLIF(section, ''), 'Undefined section') AS section,
        COALESCE(NULLIF(subsection, ''), 'Undefined subsection') AS subsection,
        COALESCE(NULLIF(item_type, ''), 'Undefined article type') AS item_type,
        COALESCE(NULLIF(subheadline, ''), 'No subheadline') AS subheadline,
        COALESCE(
            NULLIF(material_type_facet, ''), 'Undefined material type')
            AS material_type_facet,
        COALESCE(NULLIF(REPLACE(REPLACE(byline, 'BY', ''), ' AND', ','), ''), 'No author')
            AS authors

    FROM bq_source

)

SELECT * FROM nytarticles_metadata
