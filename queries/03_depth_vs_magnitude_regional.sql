SELECT AVG(magnitude) AS avg_magnitude,
    CASE
        WHEN depth < 70 THEN 'Shallow'
        WHEN depth >70 AND depth < 300 THEN 'Intermediate'
        WHEN depth > 300 THEN 'Deep'
    END AS depth_group
    FROM nepal_earthquakes
    GROUP BY depth_group;
    