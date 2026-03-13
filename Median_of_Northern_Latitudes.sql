#This project contains a SQL solution to compute the median of Northern Latitude (LAT_N) values from the STATION table.
#Since many SQL databases do not provide a built-in MEDIAN() function, the query uses window functions (ROW_NUMBER() and COUNT() OVER()) to determine the middle position(s) after sorting the latitude values.
#The query then calculates the average of the middle row(s) to derive the median and rounds the result to four decimal places.
select round(Avg(LAT_N),4)
from(select LAT_N,
        Row_Number() Over(order by LAT_N) As Rn,
        Count(*) over() as total_rows
        from STATION) t
        where Rn in (
            floor ((total_rows+1)/2),
            floor((total_rows+2)/2)
        );
