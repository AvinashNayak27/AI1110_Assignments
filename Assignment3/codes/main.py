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

n = 50
p = 0.01

# Computing the probabilities
print(f'(a) {1-(binom.pmf(0,n,p))}')
print(f"(b) {(binom.pmf(1,n,p))}")
print(f"(c) {1-(binom.pmf(0,n,p))-(binom.pmf(1,n,p))}")

# Plotting the probability mass function
X = list(range(n + 1))
Y = [binom.pmf(0,n,p), binom.pmf(1,n,p), binom.pmf(2,n,p), binom.pmf(3,n,p),binom.pmf(4,n,p),binom.pmf(5,n,p),binom.pmf(6,n,p),binom.pmf(7,n,p),binom.pmf(8,n,p),binom.pmf(9,n,p),binom.pmf(10,n,p),binom.pmf(11,n,p),binom.pmf(12,n,p),binom.pmf(13,n,p),binom.pmf(14,n,p),binom.pmf(15,n,p),binom.pmf(16,n,p),binom.pmf(17,n,p),binom.pmf(18,n,p),binom.pmf(19,n,p),binom.pmf(20,n,p),binom.pmf(21,n,p),binom.pmf(22,n,p),binom.pmf(23,n,p),binom.pmf(24,n,p),binom.pmf(25,n,p),binom.pmf(26,n,p),binom.pmf(27,n,p),binom.pmf(28,n,p),binom.pmf(29,n,p),binom.pmf(30,n,p),binom.pmf(31,n,p),binom.pmf(32,n,p),binom.pmf(33,n,p),binom.pmf(34,n,p),binom.pmf(35,n,p),binom.pmf(36,n,p),binom.pmf(37,n,p),binom.pmf(38,n,p),binom.pmf(39,n,p),binom.pmf(40,n,p),binom.pmf(41,n,p),binom.pmf(42,n,p),binom.pmf(43,n,p),binom.pmf(44,n,p),binom.pmf(45,n,p),binom.pmf(46,n,p),binom.pmf(47,n,p),binom.pmf(48,n,p),binom.pmf(49,n,p),binom.pmf(50,n,p)]
plt.stem(X, Y, linefmt='r-', markerfmt='ro', basefmt='k--')
plt.title('Probability Mass Function')
plt.xticks(X)
plt.xlabel('$Y$')
plt.ylabel('Probability')
plt.show()
