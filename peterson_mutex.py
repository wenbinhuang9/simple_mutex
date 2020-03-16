from threading import Thread
class PetersonMutex():
    def __init__(self):
        self.turn = 0
        self.interested = [False, False]

    def enter_region(self, process):
        other = 1 - process
        self.turn = process
        self.interested[process] = True

        """busy waiting until getting the lock"""
        while self.turn == process and self.interested[other] == True: pass

    def leave_region(self, process):
        self.interested[process] = False

"""Begin testing peterson algorithm"""
class Count():

    def __init__(self):
        self.count = 0
        self.mutex = PetersonMutex()
    def inc(self, process):
        try:
            self.mutex.enter_region(process)
            self.count += 1
            return self.count
        finally:
            self.mutex.leave_region(process)

count = Count()

def run(count, thread_id):
    for i in range(10):
        ans = count.inc(thread_id)
        print("thread_id={0}|count={1}".format(thread_id, ans))

t1 = Thread( target=run, args=(count, 0,) )
t2 = Thread( target=run, args=(count, 1,) )
t1.start(), t2.start()
