#! /usr/bin/python3
# -*- coding: utf-8 -*
import cmath, readline

def mandelbrot(z):
    newz = z**2 + z
    bailout = 1000
    while cmath.polar(newz)[0]**2 + cmath.polar(newz)[1]**2 < 2**2 and bailout > 0:
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
