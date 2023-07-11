#!/usr/bin/python3
# 8-uppercase.py

def uppercase(str):
 for c in str:
  if ord(c) >= ord('a') and ord(c) <= ord('z'):
   c = chr(ord(c) - 32)
  print("{}".format(c))
 print("")
