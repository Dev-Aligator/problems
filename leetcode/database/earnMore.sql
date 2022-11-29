select a.name
from Employee as a , Employee as b
where a.managerId = b.Id and a.salary > b.salary
;
