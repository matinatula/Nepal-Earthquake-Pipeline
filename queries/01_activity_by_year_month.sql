SELECT 
    EXTRACT(YEAR FROM time) AS year, 
    EXTRACT(MONTH FROM time) AS month, 
    COUNT(id) AS count
    FROM nepal_earthquakes
    GROUP BY year, month
    ORDER BY count DESC
    LIMIT 5;