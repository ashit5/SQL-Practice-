## Company Hierarchy SQL Query

#This project contains an SQL solution to analyze a company's hierarchical structure.  
#The query retrieves the `company_code`, `founder`, and the total number of **lead managers, senior managers, managers, and employees** associated with each company.

#The solution uses **LEFT JOINs** to combine multiple tables representing different levels of the organization and applies **COUNT(DISTINCT)** to avoid duplicate records. Results are grouped by company and ordered by `company_code` in ascending string order.

#This problem demonstrates the use of:
#- SQL joins
#- Aggregation functions
#- Handling duplicate records
#- Working with hierarchical organizational data

Select c.company_code , c.founder , count(distinct lm.lead_manager_code ),count(distinct sm.senior_manager_code),count(distinct m.manager_code),count(distinct e.employee_code)

from company c
 left join Lead_Manager lm on c.company_code=lm.company_code
 left join Senior_Manager sm on c.company_code=sm.company_code
 left join Manager m on c.company_code=m.company_code
 left join Employee e on c.company_code=e.company_code
 Group by c.company_code,c.founder
 order by c.company_code;
 
