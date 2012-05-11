#!/usr/bin/env python
# coding: utf-8
'''配列の場所を入力してそれから５つの値の平均をとる'''

def valueave(val):
  value = 0
  devval = 0
  
  for i in range(val,6):
   value += i
   
  devval = value / len(range(val,6))
  return devval
