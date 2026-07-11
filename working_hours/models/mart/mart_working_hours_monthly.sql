{{ config(materialized='table') }}

SELECT
    employee,
    extract('year' FROM date) as year,
    MONTH(date) as month_num,
    MONTHNAME(date) as month_name,
    SUM(hours_worked) as hours_worked_sum,
    CASE WHEN
        hours_worked_sum - 150 < 0
    THEN
        0
    ELSE
        ROUND((hours_worked_sum - 150), 2)
    END as bonus_hours,
    bonus_hours * 25 as bonus
FROM stg_hours
GROUP BY
    employee,
    year,
    month_num,
    month_name
ORDER BY month_num