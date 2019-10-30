# exercise using map and filter, lambda  by importing functools
import functools
class Solution(object):
# Driver code
    lis1 = [1,2,3,4]
    lis2 = [4,5,6,7]
    lis3 = [1,9,9,4]
    tuple1 = (7,8,9,0)
# 1) add two lists
    res1= list(map(lambda x, y: x + y, lis1, lis2))
    print (list(res1))   #[5,7,9,11]

#add list and tuple list is mutable while tuple is imutable
    res2 = list(map(lambda x,y: x + y, lis1,tuple1))
    print (list(res2))    #[8,10,12,4]
#filter num >2
    res3 = list(filter(lambda x: x < 3, lis3))
    print (list(res3))   #[1]

# finding intersection of two lists
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
c = [2,7,3,4]
print (list(filter(lambda x: x in a, b)))  # [2, 3, 5, 7]
print (list(filter(lambda y: y in [1,2,3,4], [4,5,6,7])))  # [4]

#reduce, this sum up the list of element
print (list(a), end=' ')
print (functools.reduce(lambda x,y: x+y, a))   #27
print (sum(a))  # 27  -doing the same using sum

#reduce, print the max element of a list1
print (list(c), end=' ')
print (functools.reduce(lambda a,b : a if a > b else b, c))

#  list with 3 rows and 4 columns
list4=[[1,2,3,4],[2,3,4,5],[5,6,7,8]]
print (list(list4))
#zip, print the total of each column using zip
print(list(map(sum, zip(*list4))))   #[8,11,14,17]


#map, print the total of column 2 using map
print(sum(map(lambda x : int(x[1]), list4))) #11

#reduce, print the total of column 2 using reduce
print(functools.reduce(lambda x,y:x+int(y[1]), list4,0)) #init 0
