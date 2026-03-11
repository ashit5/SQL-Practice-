#This SQL query analyzes a Binary Tree stored in a table BST, where N represents a node and P represents its parent. 
#The task is to classify each node as Root, Inner, or Leaf based on its relationship with other nodes. 
#A node is labeled Root if it has no parent (P IS NULL), Leaf if it has no children, and Inner if it has both a parent and at least one child. 
#The final output lists each node along with its type, ordered by the node value.

Select N,
    case
        when P is null then 'Root'
        when N not in (select P from BST where P is not Null) then 'Leaf'
        Else 'Inner'
    END As Nodetype
From BST
Order by N;
