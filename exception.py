# encoding=utf-8
"""
1. try-except
2. self-defined exception
"""


class TryExceptDemo:
    """
    python use 'try-except' to CATCH exception, and use 'raise' to THROW exception
    """

    def __init__(self):
        print "try-except demo-----------"
        TryExceptDemo.demo()

    @staticmethod
    def demo():
        try:
            try:
                1 / 0
            except:
                print 'here is when exception happens'
                raise ArithmeticError('calculation error. top:%s, bottom:%s' % (1, 0))
            else:
                print 'here is when exception not happens'
            finally:
                print 'here is when all the block above finished'
        except ArithmeticError, e:
            print "ArithmeticError: ", e.message
            try:
                raise RuntimeError('*err happens in except.')
            except Exception, ex:
                print ex
        except Exception, e:
            print "Exception: ", e.message


class MyExceptionDemo:
    """
    TIP: str(e)==e.message
    """
    def __init__(self):
        print "self-defined exception demo-----------"
        try:
            msg = 'test'
            err = 'my-exception'
            raise MyExceptionDemo.MyException(msg, err)
        except Exception, e:
            print '%s: type=%s, msg=%s, err=%s' % (e, type(e).__name__, e.message, e.errors)

    class MyException(Exception):
        def __init__(self, message, errors):
            Exception.__init__(self, message)
            self.errors = errors


if __name__ == "__main__":
    TryExceptDemo()
    MyExceptionDemo()
