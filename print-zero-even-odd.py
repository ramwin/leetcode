#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang <ramwin@qq.com>


from threading import Lock


class ZeroEvenOdd:

    def __init__(self, n):
        self.n = n
        self.zero_lock = Lock()
        self.even_lock = Lock()
        self.odd_lock = Lock()

        self.zero_lock.acquire()
        self.even_lock.acquire()
        self.odd_lock.acquire()

        self.even_lock.acquire()
        self.odd_lock.acquire()


	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(n):
            self.zero_lock.acquire()
            printNumber(0)
            self.zero_lock.release()


    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(0, n, 2):
            self.zero_lock.acquire()
            self.odd_lock.acquire()
            printNumber(i)
            self.even_lock.release()
            self.zero_lock.release()



    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, n, 2):
            self.zero_lock.acquire()
            self.even_lock.acquire()
            printNumber(i)
            self.odd_lock.release()
            self.zero_lock.release()
