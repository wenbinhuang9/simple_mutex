from threading import  Thread
"""a presentation of strict alternation """
"""the drawback of this solution is that it embeds the mutual exclusion code into process or thread"""
turn = [0]
count = [0]

def run1(thread_id, turn, count):
    for i in range(100):
        while turn[0] != 0: pass
        count[0] += 1
        print("thread_id={0}|count={1}".format( thread_id, count[0]))

        turn[0] = 1

def run2(thread_id):
    for i in range(100):
        while turn[0] != 1: pass
        count[0] += 1
        print("thread_id={0}|count={1}".format( thread_id, count[0]))

        turn[0] = 0

t1 = Thread(target=run1, args=("1", turn, count))
t2 = Thread(target=run2, args=("2",))
t1.start()
t2.start()