select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      SELECT article_id
FROM `nytarticles`.`nyt_articles_dataset`.`stg_nytarticles__metadata`
WHERE published_date < created_date
      
    ) dbt_internal_test