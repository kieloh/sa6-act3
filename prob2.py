#!/usr/bin/env python3

strings = ['apple', 'banana', 'choco', 'candy']
strings.sort()
strings.sort(key=lambda strings: len(strings))

print(strings)