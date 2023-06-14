
    
    

with dbt_test__target as (

  select article_id as unique_field
  from `nytarticles`.`nyt_articles_dataset`.`stg_nytarticles__metadata`
  where article_id is not null

)

select
    unique_field,
    count(*) as n_records

from dbt_test__target
group by unique_field
having count(*) > 1


