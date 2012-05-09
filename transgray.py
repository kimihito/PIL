#!/usr/bin/env python
# coding: utf-8
import Image
import ImageOps
img1 = Image.open("img/sample.png")
img2 = ImageOps.grayscale(img1)
img2.save("sampgray.png")
