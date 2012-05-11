#!/usr/bin/env python
# coding: utf-8
import Image

def picaverage(x, y, filename):
  im = Image.open(filename)
  for i in range(-2,4):
    for j in range(-2,4):
      pixel = im.getpixel(x + i, y + j)
      totalpixel += list(pixel)

  averagepixel = totalpixel / len(i) * len(j)
  
  return averagepixel
  
  


