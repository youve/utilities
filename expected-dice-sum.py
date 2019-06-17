#!/usr/bin/env python3

import argparse
import fractions

parser = argparse.ArgumentParser(description='How many times do you expect to throw a fair n sided die before the sum of the rolls is evenly divisible by k?')
parser.add_argument('n', metavar='sides', type=int, help='How many sides does the die have?')
#parser.add_argument('d', metavar='dice', type=int, help='How many dice? Default is 1', default=1)
parser.add_argument('k', metavar='mod', type=int, help="What should the sum be divisible by?")
parser.add_argument('-v', '--verbose', action='store_true')

args = parser.parse_args()

n = args.n
k = args.k

remainder = n % k
quotient = n // k
dice = [quotient + (1 <= i <= remainder) for i in range(k)] # [1, 2, 2, 1, 1] if n is 7 and k is 5
last_turn = dice[:]

useFractions = True
if k > 200:
    useFractions = False

if useFractions:
    answer = [fractions.Fraction(last_turn[0], sum(last_turn))]
else:
    answer = [last_turn[0]/sum(last_turn)]

sep = '\t'
print(f'\nThrowing a {n} sided die until the sum is divisible by {k}')
if args.verbose:
    print(f'\n How likely a particular remainder is per turn:')
    print(f"Mod is: ", end='')
    print(*range(0,k), "Total", sep=sep)

while len(answer) < k:
    if args.verbose:
        print(f'Turn {len(answer)}: {sep.join(map(str, last_turn))}\t{sum(last_turn)}')
    last_turn = [sum([last_turn[j] * dice[i - j] for j in range(1,k)]) for i in range(0,k)]
    if useFractions:
        answer.append(fractions.Fraction(last_turn[0], sum(last_turn)))
    else:
        answer.append(last_turn[0]/sum(last_turn))

if useFractions:
    print('\nChance of finishing at each turn:')
    print(*range(1,k + 1), sep=sep)
    print('-'*80)
    print(*answer, sep=sep)
    print(sum(answer), '=', float(sum(answer)))
else:
    print('Total:', sum(answer))
