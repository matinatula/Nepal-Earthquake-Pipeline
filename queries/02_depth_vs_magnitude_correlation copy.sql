SELECT 
    ( (COUNT(*) * SUM(depth * magnitude))- (SUM(depth) * SUM(magnitude)) ) / 
    SQRT ((COUNT(*)* SUM(POWER(depth,2)) - (POWER(SUM(depth),2))) * 
    (COUNT(*)* SUM(POWER(magnitude,2)) - POWER(SUM(magnitude),2)))
    AS correlation_coefficient
    FROM nepal_earthquakes