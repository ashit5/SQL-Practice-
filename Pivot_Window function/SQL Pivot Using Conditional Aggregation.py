# SQL Pivot Using Conditional Aggregation
# This query transforms row-based occupation data into column format (Doctor, Professor, Singer, Actor).
# How it works:
#ROW_NUMBER() assigns a sequence number to each name within its occupation after sorting alphabetically.
#PARTITION BY Occupation ensures numbering is done separately for each occupation.
#The outer query groups records by row number so that names in the same position appear in the same row.
#CASE WHEN filters names for each occupation.
#MAX() is used to extract the non-NULL value, effectively pivoting rows into columns.
#NULL is displayed automatically where an occupation has fewer names.
#This approach allows pivoting data without using database-specific PIVOT functions and works across most SQL databases.

SELECT 
    MAX(CASE WHEN Occupation = 'Doctor' THEN Name END) AS Doctor,
    MAX(CASE WHEN Occupation = 'Professor' THEN Name END) AS Professor,
    MAX(CASE WHEN Occupation = 'Singer' THEN Name END) AS Singer,
    MAX(CASE WHEN Occupation = 'Actor' THEN Name END) AS Actor
FROM (
    SELECT 
        Name,
        Occupation,
        ROW_NUMBER() OVER (
            PARTITION BY Occupation
            ORDER BY Name
        ) AS rn
    FROM OCCUPATIONS
) t
GROUP BY t.rn
ORDER BY t.rn;
