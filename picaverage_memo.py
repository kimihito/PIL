#!/usr/bin/env python
# coding: utf-8
import Image

class memoized:
  def __init__(self, f):
    self.f = f
    self.cache = {}
  
  def __call__(self, *args):
    if self.cache.has_key(args):
      return self.cache[args]
    result = self.f(*args)
    self.cache[args] = result
    return result

@memoized
def picaverage_v(x, y, im):
  w, h = im.size
  upper, lower = y - 2, y + 2

  totalpixels = [0, 0, 0]  
  pixels = im.crop((x, upper, x+1, lower)).getdata()
  for pixel in pixels:
    totalpixels[0] += pixel[0]
    totalpixels[1] += pixel[1]
    totalpixels[2] += pixel[2]

  if upper < 0:
    upper = 0
  if lower > h:
    lower = h

  l = len(pixels)
  totalpixels[0] /= l
  totalpixels[1] /= l
  totalpixels[2] /= l

  return tuple(totalpixels)

def picaverage(x, y, im):
  w, h = im.size
  if x < 0 or y < 0 or w < x or h < y or im.mode != 'RGB':
    raise Exception('argument error')

  left, upper, right, lower = x - 2, y - 2, x + 2, y + 2

  if left < 0:
    left = 0
  if right > w:
    right = w
  
  totalpixels = [0, 0, 0]
  for n in range(left, right):
    r = picaverage_v(n, y, im)
    totalpixels[0] += r[0]
    totalpixels[1] += r[1]
    totalpixels[2] += r[2]

  l = (right - left)
  totalpixels[0] /= l
  totalpixels[1] /= l
  totalpixels[2] /= l

  return tuple(totalpixels)
