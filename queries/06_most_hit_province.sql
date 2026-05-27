SELECT
    COUNT(*) AS num_earthquakes,
    CASE
        WHEN ((latitude >= 26.25 AND latitude <=28.10) AND (longitude >= 86.05 AND longitude <=88.12)) THEN 'Koshi Province (East)'
        WHEN ((latitude >= 26.35 AND latitude <=27.25) AND (longitude >= 84.50 AND longitude <=86.25)) THEN 'Madhesh Province'
        WHEN ((latitude >= 27.05 AND latitude <=28.25) AND (longitude >= 84.10 AND longitude <=86.35)) THEN 'Bagmati Province (Central)'
        WHEN ((latitude >= 27.20 AND latitude <=29.20) AND (longitude >= 82.50 AND longitude <=85.00)) THEN 'Gandaki Province'
        WHEN ((latitude >= 27.15 AND latitude <=28.35) AND (longitude >= 81.45 AND longitude <=83.40)) THEN 'Lumbini Province'
        WHEN ((latitude >= 28.05 AND latitude <=30.15) AND (longitude >= 81.05 AND longitude <=83.45)) THEN 'Karnali Province (Mid-West)'
        WHEN ((latitude >= 26.55 AND latitude <=30.20) AND (longitude >= 80.04 AND longitude <=81.35)) THEN 'Sudurpashchim Province (Far-West)'
        ELSE 'None'
    END AS province
    FROM nepal_earthquakes
    GROUP BY province
    ORDER BY num_earthquakes DESC;

    