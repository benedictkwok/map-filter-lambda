# exercise using map and filter, lambda  by importing functools
# 1) add two lists
# 2) add list and tuple ; list is mutable while tuple is imutable
import functools
class Solution(object):
# Driver code
    list1 = [1,2,3,4]
    list2 = [4,5,6,7]
    list3 = [1,9,9,4]
    tuple1 = (7,8,9,0)
    res1= list(map(lambda x, y: x + y, list1, list2))
    print (list(res1))

    res2 = list(map(lambda x,y: x + y, list1,tuple1))
    print (list(res2))

    res3 = list(filter(lambda x: x < 3, list3))
    print (list(res3))

# finding intersection of two lists
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print (list(filter(lambda x: x in a, b)))  # [2, 3, 5, 7]
print (list(filter(lambda y: y in [1,2,3,4], [4,5,6,7])))  # [4]
