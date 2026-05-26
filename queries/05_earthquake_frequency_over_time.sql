SELECT COUNT(*), 
    EXTRACT(YEAR FROM time) AS year
    FROM nepal_earthquakes
    GROUP BY year
    ORDER BY year ;