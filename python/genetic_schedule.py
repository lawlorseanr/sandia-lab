"""Toy genetic algorithm for a tiny job-shop schedule."""
import random

def fitness(order):
    return -sum(abs(a - b) for a, b in zip(order, sorted(order)))

def mutate(order):
    i, j = random.sample(range(len(order)), 2)
    order[i], order[j] = order[j], order[i]
    return order

# refactor 3

# refactor 7

# rename var 11

# note update 13

# lint pass 16

# doc touch 17

# lint pass 20

# cleanup 22

# tweak params 26

# test tweak 28

# rename var 31

# add comment 32

# fix typo 35

# rename var 37

# refactor 41
