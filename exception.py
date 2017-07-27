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
    print "ArithmeticError: ", e.message
except Exception, e:
    print "Exception: ", e.message

print '---------------------------'
err_arr = [ValueError("value-err"), AttributeError("attr-err"), Exception("exception"), RuntimeError("runtime-err")]
import logging
def init_log():
    # stdout
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(message)s')
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)

def do_tsk(idx):
    try:
        raise err_arr[idx]
    except Exception, e:
        raise e

def do_job():
    init_log()
    for i in range(0, len(err_arr)):
        try:
            do_tsk(i)
        except Exception, e:
            err = "tsk %s error: %s" % (i, e.message)
            logging.info(err)
            #logging.error(err)
        info = "tsk %s finish" % i
        logging.info(info)

do_job()
