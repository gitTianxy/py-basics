
print "------python use 'try-except' to CATCH exception, and use 'raise' to THROW exception-----"

try:
    try:
        1 / 0
    except:
        print 'here is when exception happens'
        raise ArithmeticError('calculation error')
    else:
        print 'here is when exception not happens'
    finally:
        print 'here is when all the block above finished'
except ArithmeticError, e:
    print e.args
