#!/bin/python3

from random import choice, randint

print("....ROCK...")
print("...PAPER...")
print("...SCISSOR...")
c1 = choice(['rock', 'paper', 'scissor'])
c2 = choice(['rock', 'paper', 'scissor'])

print("Player 1 :" + c1 )
print("Player 2 :" + c2)

if c1 == c2:
    print("Nobody wins...It's a tie.")
elif (c1 == 'rock' and c2 == 'paper') or (c1 == 'paper' and c2 == 'scissor') or (c1 == 'scissor' and c2 == 'rock'):
    print("Player 2 wins. Congratulation....!!!")
else:
    print("Player 1 wins. COngratulation...!!!")
