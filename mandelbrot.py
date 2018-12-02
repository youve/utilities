#! /usr/bin/python3
# -*- coding: utf-8 -*
import cmath, readline

def mandelbrot(z):
    '''Just take a point called z in the complex plane.
    Let z1 be z0 squared plus z
    and z2 is z1 squared plus z
    and z3 is z2 squared pluz z
    and so on
    if the series of z's will always stay close to z and never trend away
    that point is in the Mandelbrot set -- Jonathan Coulton
    
    Convert the complex number to polar coordinates. The r coordinate gives
    the radius from 0. If that stays less than 2 for 1000 tries, it's probably
    in the Mandelbrot set. If it ever gets bigger than 2, then squaring it will make it
    rapidly approach infinity and is definitely not in the Mandelbrot set."
    '''
    newz = z**2 + z
    bailout = 1000
    while cmath.polar(newz)[0] < 2 and bailout > 0:
        newz = newz**2 + z
        bailout = bailout - 1
        print(newz)
    answer = ""
    if bailout < 1:
        answer = "It is probably in the Mandelbrot set"
    else:
        answer = "It escaped in " + str(1001-bailout) + " tries"
    return answer

while 1:
    try:
        z = ''
        z = complex(input("Complex number (Eg: .25+.1j) or ctrl-c: "))
        print(mandelbrot(z))
    except ValueError:
        print("Exactly as written with no spaces, and it has to be decimals not fractions.")
