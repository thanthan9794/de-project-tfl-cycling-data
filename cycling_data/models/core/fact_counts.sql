{{
    config(
        materialized='table'
    )
}}

with data22 as (
    select *
    from {{ ref('active_travel_data_2022') }}
),
data23 as (
    select *
    from {{ ref('active_travel_data_2023') }}
),
data_unioned as (
    select * from data22
    union all
    select * from data23
),
locations as (
    select * from {{ ref('locations_data') }}
)

select data_unioned.* 
    ,locations.Location_description as location
    ,locations.Borough as borough
    ,locations.Functional_area_for_monitoring as functional_area
    ,locations.Road_type as road_type
    ,locations.Latitude as latitude
    ,locations.Longitude as longitude
from data_unioned
inner join locations on data_unioned.UnqID = locations.Site_ID