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
