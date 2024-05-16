with traveldata as 
(
  select *
  from {{ source('staging','active_travel_counts_2022_2023') }}
  where year = 2022
)

select * from traveldata