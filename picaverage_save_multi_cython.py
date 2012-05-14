from multiprocessing import Pool
import Image
from picaverage_cython import *

im = Image.open('samp.png').convert('RGB')

def picave(tup):
    x, y = tup
    return picaverage(x, y, im)

def main():
    w, h = im.size
    
    p = Pool(8)
    data = [(x, y) for y in range(0, h) for x in range(0, w)]
    im.putdata(p.map(picave, data))
    
    im.save('samp2.png')

if __name__ == '__main__':
  main()
