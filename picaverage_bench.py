# import pyximport; pyximport.install(pyimport = True)
from multiprocessing import Pool
import profile
import Image
from picaverage import *

im = Image.open('samp.png').convert('RGB')
w, h = im.size

def picave(tup):
    x, y = tup
    return picaverage(x, y, im)

def main():
    p = Pool(8)
    return p.map(picave, [(x, y) for y in range(0, h) for x in range(0, w)])

profile.run('main()')
