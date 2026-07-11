{{ config(materialized='table') }}
SELECT
    Employee as employee,
    Project as project,
    CAST(STRPTIME(Date || '-' || RIGHT(Month, 4), '%d-%b-%Y') as DATE) as date,
    CAST(Start as TIME) as start,
    CAST(Finish as TIME) as finish,
    make_time(
        CAST(SPLIT_PART(Time, ':', 1) as INTEGER),
        CAST(SPLIT_PART(Time, ':', 2) as INTEGER),
        0) as time,
    CAST(SPLIT_PART(Time, ':', 1) AS DECIMAL) +
        CAST(SPLIT_PART(Time, ':', 2) AS DECIMAL) / 60 as hours_worked,
    Comments as comments
FROM raw_data