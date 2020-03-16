import unittest

from mutex import SpinLock ,WaitLock, RLock
from threading import Thread

class Count():
    def __init__(self, lock_class):
        self.count = 0
        self.lock = lock_class()

    def increase(self):
        try:
            self.lock.acquire()

            self.count += 1
            return self.count
        finally:
            self.lock.release()

class MyTestCase(unittest.TestCase):
    def create_threads(self, func, argu, n = 10):
        ans = []

        for i in range(n):
            t = Thread(target=func, args=(argu, str(i)))
            ans.append(t)

        return ans

    def inc(self, count, thread_id):
        for i in range(10):
            ans = count.increase()
            print("threadId={0}|count={1}".format(thread_id, ans))

    def test_spinlock(self):
        count = Count(SpinLock)

        threads = self.create_threads(self.inc, count)
        for t in threads:
            t.start()

    def test_waitlock(self):
        count = Count(WaitLock)

        threads = self.create_threads(self.inc, count)
        for t in threads:
            t.start()

    def test_RLock_reentrance(self):

        def func():
            lock = RLock()
            lock.acquire()
            print("enter into the first level")
            lock.acquire()
            print("enter into the second level")
            lock.release()
            lock.release()


        t = Thread(target=func)
        t.start()

    def test_Rlock_fucntion(self):
        count = Count(RLock)

        threads = self.create_threads(self.inc, count)
        for t in threads:
            t.start()

if __name__ == '__main__':
    unittest.main()
