# simple_mutex
A simple implementation of spinlock, lock, reentrant lock. Implement an atomic operations test and set based on Python Lock object.

Test and set operation is simulated by Python Lock object.
# SpinLock

Implement a spinlock based on test and set atomic operation, a thread will be busy waiting until getting the lock.

## code
```
lock = SpinLock()

lock.acquire()
lock.release()
```

# Lock
Implement a Lock based on test and set atomic operation, a thread will be blocked until getting the lock

## code

```
lock =WaitLock()

lock.acquire()
lock.release()
```

# Reentrant lock
Implement a  Reentrant lock based on WaitLock Object, if a thread owns a lock, it can reenter the lock without release.

```
lock =RLock()

lock.acquire()
lock.release()
```

# Peterson algorithm
Implement a mutex lock based on peterson algorithm

## Code 
```
from person_mutex import PetersonMutex

mutex = PetersonMutex()
mutex.enter_region()
mutex.leave_region()
```
