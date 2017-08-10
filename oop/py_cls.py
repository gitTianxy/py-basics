# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
# Python从设计之初就已经是一门面向对象的语言。
# 构建python类时关注如下几个概念：
    1. 类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
    2. 继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
    4. 实例化：创建一个类的实例，类的具体对象。
    5. 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

    6. 数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
    7. 类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
    8. 实例变量：定义在方法中的变量，只作用于当前实例的类。

    9. 方法：类中定义的函数。
    3. 方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
# 类关键字
    * class
    * self
    * instances.__class__
    * object: 公共父类
    * super(Child, self): 访问父类
# python命名规则
    * name: public
    * _name: protected
    * __name: private
    * __name__: special/python_built-in
# Python内置类属性
    * __dict__ : 类的属性（包含一个字典，由类的数据属性组成）
    * __doc__ :类的文档字符串
    * __name__: 类名
    * __module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
    * __bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
# Python基础重载方法
    * __init__(self[,args...])
    * __str__(self)
    * __del__(self)
    * __cmp__(self,x)
# Python垃圾回收
    * 引用计数
    * 循环引用排查
    * 大对象排查
# 动态创建类:
    * python是动态语言, 天然支持动态创建类.
    * python中类也是对象, 所以可以通过操作对象/类实例一样操作类:
        1. type: 动态创建类
        2. 动态添加属性(ClsName.new_attr=...即可)
        3. metaclass: 动态改变类的方法
"""

import gc


class Employee:
    # 类变量
    empCount = 0
    publicVar = None
    _protectedVar = None
    __privateVar = None

    # 构造函数
    def __init__(self, name, salary):
        self.name = name  # 实例变量
        self.salary = salary
        Employee.empCount += 1

    def __del__(self):
        print 'method exec when the object on GC'

    def displayCount(self):
        # print "Employee count: %d" % Employee.empCount
        print "Employee count: %d" % self.__class__.empCount

    def displayEmployee(self):
        print "Employee: name_", self.name, ", salary_", self.salary

    def publicMethod(self):
        pass

    def _protectedMethod(self):
        pass

    def __privateMethod(self):
        pass


class Parant(object):
    """
    parent class
    """
    parentAttr = None
    _parentAttr = None
    __parentAttr = None

    def __init__(self):
        self.__class__.parentAttr = 'parentAttr'
        self.__class__._parentAttr = '_parentAttr'
        self.__class__.__parentAttr = '__parentAttr'
        print 'call parent constructor'

    def parentMethod(self):
        print 'call public parent method'

    def _parentMethod(self):
        print 'call protected parent method'

    def __parentMethod(self):
        print 'call private parent method'


class Child(Parant):
    """
    child class
    """
    childAttr = None

    def __init__(self):
        super(Child, self).__init__()  # 调用此方法则父类中必须写object
        print 'call child constructor'

    def childMethod(self):
        print 'call child method'


class DynamicClsDemo:
    """
    动态语言本身支持运行期动态创建类，而静态语言在编译时创建类; 要在静态语言运行期创建类，
    必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。
    """

    def __init__(self):
        tpc = self.type_cls()
        print type(tpc)
        tp = tpc()
        tp.method_a()
        tp.method_b('B')

        MyList = self.meta_cls()
        ml = MyList()
        ml.add('a')
        ml.add('b')
        print ml
        ml.delete('a')
        print ml

    def type_cls(self):
        """
        type()用于动态创建'类'
        TIPS:
            1. 通过type()函数创建的类和直接写class是完全一样的:
        因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
            2. 注意定义的函数中要至少带一个self参数
        """

        def cls_method_a(self):
            print 'class method A'

        def cls_method_b(self, arg):
            print 'class method %s' % arg

        cls_name = 'TypeCls'
        parent_cls = (object,)
        cls_methods = dict(method_a=cls_method_a, method_b=cls_method_b)
        return type(cls_name, parent_cls, cls_methods)

    def meta_cls(self):
        """
        class 定义了 instance 的行为，metaclass 则定义了 class 的行为。可以说，class是metaclass的instance。
        instance 创建的时候会调用 __init__ 函数，类似的，class 创建的时候会调用 __new__ 函数。因此通过自定义 __new__ 函数，
        你可以在创建类的时候做些额外的事情：把这个类注册到某个地方作为记录或者后续的查询，给类注入一些属性，或者干脆替换成另外一个类。
        """

        class MyList(list):
            __metaclass__ = DynamicClsDemo.MyListMetaCls

        return MyList

    class MyListMetaCls(type):
        def __new__(cls, name, bases, attrs):
            attrs['add'] = lambda self, value: self.append(value)
            attrs['delete'] = lambda self, value: self.remove(value)
            return type.__new__(cls, name, bases, attrs)


if __name__ == "__main__":
    print '类基本操作 ------------------'
    # 创建
    e = Employee('kevin', '11K')
    # 访问方法
    e.displayCount()
    e.displayEmployee()
    # 访问属性--直接访问+内置函数访问
    e.salary = "14K"
    print 'salary after reset: ', e.salary
    del Employee.empCount
    try:
        print 'empCount after delete: ', Employee.empCount
    except Exception, e:
        print 'empCount is deleted', e.args

    while True:
        if hasattr(e, "name"):
            print "name: ", getattr(e, "name")
            setattr(e, "name", "xinyu")
            print "name after reset: ", getattr(e, "name")
            delattr(e, "name")
        else:
            print "name has been deleted"
            break
    # GC
    gc.enable()
    del e
    gc.collect()

    print '类继承------------------'
    c = Child()
    c.parentMethod()
    c._parentMethod()
    c.childMethod()

    print '动态生成类------------------'
    DynamicClsDemo()
