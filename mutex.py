from threading import Lock, Condition
import threading

"""
mock the function of test_and_set to implement a lock
"""
class SpinLock():
    def __init__(self):
        self.lock = Lock()
        self.turn = [0]
        self.owner = None

    def acquire(self):
        """busy waiting until getting the lock"""
        while not self.__testandset(self.turn, 1):
            pass
        self.owner = threading.current_thread()
    def release(self):
        if self.owner != threading.current_thread():
            raise ValueError("current thread not owns the lock")
        self.turn[0] = 0

    def __testandset(self, var, value):
        try:
            self.lock.acquire()
            if var[0] == value:
                return False
            else:
                var[0] = value
                return True
        finally:
            self.lock.release()

"""a lock that may block the thread"""
class WaitLock():
    def __init__(self):
        self.lock = Lock()
        self.turn = [0]
        self.owner = None
        self.cond = Condition()

    def acquire(self):
        while not self.__testandset(self.turn, 1):
            """block current thread if no lock acquired"""
            with self.cond:
                self.cond.wait()
        self.owner = threading.current_thread()

    def release(self):
        if self.owner != threading.current_thread():
            raise ValueError("current thread not owns the lock")
        self.turn[0] = 0
        with self.cond:
            self.cond.notify_all()

    def __testandset(self, var, value):
        try:
            self.lock.acquire()
            if var[0] == value:
                return False
            else:
                var[0] = value
                return True
        finally:
            self.lock.release()


"""a reentrant lock that allows a lock owner gets the lock for multiple times """
class RLock():
    def __init__(self):
        self.lock = WaitLock()
        self.owner = None
        self.count = 0

    def _is_owner(self):
        cur_th = threading.current_thread()
        return self.owner == cur_th

    def acquire(self):
        if self._is_owner():
            self.count += 1
            return

        self.lock.acquire()
        me = threading.current_thread()

        self.owner = me
        self.count = 1

    def release(self):
        if not self._is_owner():
            raise ValueError("not owned the current lock")
        self.count -= 1
        if self.count <= 0:
            self.owner = None
            self.lock.release()
