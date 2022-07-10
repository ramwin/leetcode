#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


# 执行用时： 48 ms , 在所有 Python3 提交中击败了 85.19% 的用户
# 内存消耗： 15 MB , 在所有 Python3 提交中击败了 96.83% 的用户


from threading import Lock


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_lock = Lock()

        self.foo_lock.acquire()

        self.bar_lock = Lock()


    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(0, self.n):
            self.bar_lock.acquire()
            printFoo()
            self.foo_lock.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(0, self.n):
            self.foo_lock.acquire()
            printBar()  # outputs "bar". Do not change or remove this line.
            self.bar_lock.release()
        self.foo_lock.release()
