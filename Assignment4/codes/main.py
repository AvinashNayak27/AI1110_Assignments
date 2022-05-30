# CBSE Probability Grade 12
# Exercise 13.5 q10

# Name: Avinash MAlothu
# Roll number: AI21BTECH11018

""" Problem Statement
A person buys a lottery ticket in 50 lotteries ,in each of which his chance of winning a prize is 1/100.What is the probability that he will win a prize
(a)at least once
(b)exactly once   
(c)at least twice
"""

import matplotlib.pyplot as plt
from scipy.stats import binom

n = 5
p = 1/6

# Computing the probabilities
print(f'Hence the probability of getting six twice in 5 rolls is {(binom.pmf(2,n,p))}')
