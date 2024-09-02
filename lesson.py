grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
rev=sorted(students)
a=grades[0]
aa=sum(a)/len(a)
print(aa)
b=grades[1]
bb=sum(b)/len(b)
c=grades[2]
cc=sum(c)/len(c)
d=grades[3]
dd=sum(d)/len(d)
e=grades[4]
ee=sum(e)/len(e)
grades=[aa,bb, cc, dd, ee]
my_dict=dict(zip(rev, grades))
print(my_dict)

