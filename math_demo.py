import math_demo
import random

# basic math functions
print 'abs of -5 and -5.00: %s, %s' % (abs(-5), abs(-5.00))

print 'float abs of -5 and -5.00: %s, %s' % (math_demo.fabs(-5), math_demo.fabs(-5.00))
print 'ceil of 1.05: %s' % math_demo.ceil(1.05)
print 'floor of 1.05: %s' % math_demo.floor(1.05)
print 'round(1.05), round(1.05, 1), round(1.05, 3) of 1.05: %s, %s, %s' % (round(1.05), round(1.05, 1), round(1.05, 3))

print 'exp(1): ', math_demo.exp(1)
print 'ln(e): ', math_demo.log(math_demo.e)
print 'log10(100): ', math_demo.log(100, 10)

print "2^3, 2.0^3.0--use '**': %s, %s" % (2 ** 3, 2.0 ** 3.0)
print "2^3, 2.0^3.0--use 'math.pow()': %s, %s" % (math_demo.pow(2, 3), math_demo.pow(2.0, 3.0))
print "sqrt(4): ", math_demo.sqrt(4)

# comparison functions
print '2 is less than 3: ', cmp(2, 3) == -1
print 'max in {1,2,3,4} is: ', max(1, 2, 3, 4)
print 'min in {1,2,3,4} is: ', min(1, 2, 3, 4)

# random number generators
print "random choice of an element from {1,2,3,4,5}: ", random.choice([1, 2, 3, 4, 5]);
print "generate random num [0,1): ", random.random();
print "generate random num [0, 10): ", random.randrange(0, 10)
print "generate random num [0, 2, ..., 10): ", random.randrange(0, 10, 2)
order = [1, 2, 3, 4, 5]
print "disorder an array %s:" % order
random.shuffle(order)
print  "    ", order


# trigonometric functions
print "trigonometric functions..."

# math constant
print "PI: ", math_demo.pi
print "e: ", math_demo.e

# list generator
print 'generate a num list: ', range(0, 10, 2)