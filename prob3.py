#!/usr/bin/env python3
from functools import reduce
mylist = [1,2,3,8,4,5,6]

high = reduce(lambda x,y: x if (x>y) else y, mylist)

print(high)