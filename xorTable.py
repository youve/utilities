#!/usr/bin/python3

from PIL import Image
import random

def xorTable(size, width=None):
    if not width:
        width = len(str(size)) + 1
    print('XOR TABLE'.center(size*(width+1), '='))
    print(' '*width, end=' ')
    for i in range(0, size):
        print(str(i).rjust(width), end=' ')
    print('\n', '-'*size*width*2)
    for x in range(0, size ):
        print(str(x).rjust(width), end='|')
        for y in range(0, size):
            print(str(x ^ y).rjust(width), end=" ")
        print('\n')

def xorImage(size):
    im = Image.new('L', (size,size), 'white')
    for x in range(0,size):
        for y in range(0,size):
            im.putpixel((x, y), x^y)
    im.save('xor.png')

def randXor(size):
    im = Image.new('1', (size,size), 'white')
    row = []
    for x in range(size):
        row.append(random.getrandbits(1))
    y = 0
    while y < size:
        for x in range(len(row)):
            im.putpixel((x, y), row[x])
            try: 
                row[x] = row[x] ^ row[x+1] 
            except:
                row[x] = row[x] ^ row[0]
        y = y + 1
    im.save('randxor.png')


#xorTable(16)
xorImage(255)
#randXor(255)