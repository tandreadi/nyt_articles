select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select article_id
from `nytarticles`.`nyt_articles_dataset`.`stg_nytarticles__metadata`
where article_id is null



      
    ) dbt_internal_test