#!/usr/bin/env python
# coding: utf-8
import Image
from operator import *

def picaverage(x, y, im):
  w, h = im.size
  if x < 0 or y < 0 or w < x or h < y or im.mode != 'RGB':
    raise Exception('argument error')

  pixels = [im.getpixel((x + i, y + j))
            for i in range(-2, 3)
            for j in range(-2, 3)
            if 0 <= x+i < w and 0 <= y+j < h]

  rgb = zip(*pixels)
  rgb = map(lambda c: reduce(add, c, 0), rgb)
  rgb = map(lambda c: c / len(pixels), rgb)
  
  return rgb
