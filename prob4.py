#!/usr/bin/env python3

l1 = [1,3,4,5,7,9]
l2 = [2,4,5,6,8,10]

same = list(filter(lambda x: x in l1, l2))
print(same)