#!/usr/bin/env python
# coding: utf-8
import Image

def picaverage(x, y, im):
  w, h = im.size
  if x < 0 or y < 0 or w < x or h < y or im.mode != 'RGB':
    raise Exception('argument error')

  left, upper, right, lower = x - 2, y - 2, x + 2, y + 2

  if left < 0:
    left = 0
  if upper < 0:
    upper = 0
  if right > w:
    right = w
  if lower > h:
    lower = h

  data = im.getdata()
  for y in range(left, right + 1):
    for x in range(upper, lower + 1):
      pixel = data[y * w + x]
  totalpixels = [0, 0, 0]
  pixels = 
  for pixel in pixels:
    totalpixels[0] += pixel[0]
    totalpixels[1] += pixel[1]
    totalpixels[2] += pixel[2]

  l = len(pixels)
  totalpixels[0] /= l
  totalpixels[1] /= l
  totalpixels[2] /= l

  return tuple(totalpixels)
