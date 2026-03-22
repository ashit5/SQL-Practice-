#  Harry Potter and his friends are at Ollivander's with Ron, finally replacing Charlie's old broken wand.
# Hermione decides the best way to choose is by determining the minimum number of gold galleons needed to buy each non-evil wand of high power and age. 
# Write a query to print the id, age, coins_needed, and power of the wands that Ron's interested in, sorted in order of descending power.
# If more than one wand has same power, sort the result in order of descending age.

Select 
w.id,
wp.age,
w.coins_needed,
w.power
from Wands w
join Wands_Property wp on w.code=wp.code
where wp.is_evil = 0
And w.coins_needed=(
    Select min(w2.coins_needed)
    from Wands w2
    join Wands_Property wp2 on w2.code=wp2.code
    where wp2.is_evil = 0
    And w.power=w2.power
    And wp.age=wp2.age
    
)
order by 
w.power Desc,
wp.age Desc;
