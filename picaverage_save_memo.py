import Image
from picaverage_save import *

im = Image.open('samp.png').convert('RGB')

def main():
    w, h = im.size

    data = [picaverage(x, y, im) for y in range(0, h) for x in range(0, w)]
    im.putdata(data)

    im.save('samp2.png')
    
if __name__ == '__main__':
    main()
