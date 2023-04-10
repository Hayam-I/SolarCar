'''
Created on Apr 8, 2023

@author: hayam
'''
import threading
import time
#prints the number of active threads (running threads)
#print(threading.active_count())
#will return 1 bc only main thread is running
#prints a list of running threads
#print(threading.enumerate())
#will return only MainThread in list for now

#example on how to make threads run at the same time:

#this method will take 3 seconds to be fully executed
def eat_breakfast():
    time.sleep(3)
    print("you eat breakfast")

#this method will take 4 seconds to be fully executed
def drink_coffee():
    time.sleep(4)
    print("you drink coffee")
    
#this method will take 5 seconds to be fully executed    
def study():
    time.sleep(5)
    print("you finish study")

'''
#this program will take 12 (3+4+5) seconds to complete  
eat_breakfast()
#only after eat_breakfast() is fully executed, is the drink_cofee() allowed to be executed
drink_coffee()
#same here
study()

#these tasks were completed sequentially, not concurenlty, for you to start another method, you have to finish the one before it
#however, with multithreading, these functions would be executed at the same time, like we would multitask
#if you notice here, the trhead count is still 1 and the main thread is responsible for running these three methods
print(threading.active_count())
print(threading.enumerate())
'''
    
#to make 3 additional threads for each function:
x=threading.Thread(target=eat_breakfast, args=())
x.start()
#if you have a function with args: x=threading.Thread(target=eat_breakfast, args=(1,))

y=threading.Thread(target=drink_coffee, args=())
y.start()

z=threading.Thread(target=study, args=())
z.start()

'''
print(threading.active_count())
print(threading.enumerate())
'''

#now the whole program took around 5 seconds bc all three threads are happening at the same time.
#notice how the print methods were shown before the functions? thats bec the main thread wont wait till the rest of the threads are done, it has its own set of instructions to do
#main thread is not in charge of running these functions, the program will handle these functions through the other 3 threads
#main thread finished before the other three so it gets printed first
#main thread's responsibility: create new threads, print out number and list

#this method will tell you how long it takes for the main thread to be finished with instructions
print(time.perf_counter())

#thread synchronization: when a calling thread waits for another thread to finish before acting out its own instructions
#these threads are joined which means the main thread will not work until x,y,and z are done. when printing the thread count it will be 1 bc the threads will be over.
x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())