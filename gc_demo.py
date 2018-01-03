# encoding=utf-8
"""
python内存管理机制及GC API
-----------------
* 引用计数: ref count
    - 在Python中，每个对象都有存有指向该对象的引用总数，即引用计数(reference count).
    - 我们可以使用sys包中的getrefcount()，来查看某个对象的引用计数。
    - 当使用某个引用作为参数，传递给getrefcount()时，参数实际上创建了一个临时的引用。
因此，getrefcount()所得到的结果，会比期望的多1。
    - 'del var': 表示取消变量'var'对应的引用; 当某个对象的所有引用都被取消后, 它将被GC回收.

* 分代回收
    - Python将所有的对象分为0，1，2三代。
    - 垃圾回收启动时，一定会扫描所有的0代对象; 如果0代经过一定次数垃圾回收，那么就启动对0代和1代的扫描清理;
    当1代也经历了一定次数的垃圾回收后，那么会启动对0，1，2，即对所有对象进行扫描。
    - 上述自动回收的启动阈值可以通过'gc.get_threshold()'方法获得, 默认为(700, 10, 10);
    用'gc.set_threshold(t_0, t_1, t_2)'设置.
    -

"""
import gc
from sys import getrefcount
import time


def refcount_demo():
    a = [1, 2, 3]
    b = a
    print "'a':%s, ref count of 'a':%s" % (a, getrefcount(a))
    print "'b':%s, ref count of 'b':%s" % (b, getrefcount(b))

    time.sleep(1)
    del a
    # print "'a':%s, ref count of 'a'(after 'del a'):%s" % (a, getrefcount(a))
    print "'b':%s, ref count of 'b'(after 'del a'):%s" % (b, getrefcount(b))

    time.sleep(1)
    a = [1, 2]
    print "'a':%s, ref count of 'a':%s" % (a, getrefcount(a))
    print "'b':%s, ref count of 'b':%s" % (b, getrefcount(b))


def gc_threshold_demo():
    print 'gc threshold:', gc.get_threshold()
    gc.set_threshold(500, 10, 5)
    print "gc threshold (after 'gc.set_threshold(500, 10, 5)'):", gc.get_threshold()


def gc_demo(g=None):
    if g:
        gc.collect(g)
    else:
        gc.collect()


if __name__ == '__main__':
    refcount_demo()
    gc_threshold_demo()
    gc_demo()
