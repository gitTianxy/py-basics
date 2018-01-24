# encoding=utf-8
"""
random choice from list
random generation within a range
shuffle/disorderordered list
"""
import random

# random choice from list
nums = range(1, 6)
print "randomly choice an element from %s: %s" % (nums, random.choice(nums))
print "randomly choice an element from %s: %s" % (range(0, 10), random.randrange(0, 10))
print "randomly choice an element from %s: %s" % (range(0, 10, 2), random.randrange(0, 10, 2))

# random generation within a range
print "randomly generate a number within [0, 1):", random.random()

# shuffle ordered list
nums = range(0, 10)
print "shuffle an array. before:", nums
random.shuffle(nums)
print "shuffle an array. after:", nums
