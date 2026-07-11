{{ config(materialized='table') }}

SELECT
    employee,
    project,
    date,
    start,
    finish,
    hours_worked,
    comments
FROM stg_hours