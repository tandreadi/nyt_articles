select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select title
from `nytarticles`.`nyt_articles_dataset`.`stg_nytarticles__metadata`
where title is null



      
    ) dbt_internal_test