with traveldata as 
(
  select *
  from {{ source('staging','dev_load_data_to_gcs_transform_data_v1') }}
  where year = 2023
)

select * from traveldata