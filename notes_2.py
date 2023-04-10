'''
Created on Apr 10, 2023

@author: hayam

7/22 in https://www.youtube.com/watch?v=kdA4PtfYxU0&list=PLI4OVrCFuY57b_16D8xs7-hmABHncVD_w&index=7
'''
import threading
'''
- multitasking: executing multiple tasks at the same time
- types of multitasking:
    process based multitasking:
        each task is an independent program/task
        used in OS level
        
    thread based multitasking
        each task is an independent thread (separate part of program)
        used in programmatic level
 - Thread:
    - example: if a class of 100 students is divided to 4 batches where each batch studies for an hour, that takes 4 hours for all the students to learn
    but if each batch was taught by a prof in a diff hall, then all 100 will be done within 1 hour
    in this example: teacher is thread, hall is memory.
    
    - python objects of threading.Thread() class
    
    * so a thread is operating system ibject that executes instructions/program. It is a seperate flow of execution in program. It represents task/subprogram.
    
    * need: 
        consider a simple calculator with 4 functions. withour threading, if each function needs 0.01 sec, a 100 calls of fcts would be 1s
        if we have 4 threads (main, thread1, thread2, thread3) then if all 4 worked parallally, a 100 calls would be 0.25 sec.
        aka to make programs faster
        
        or if you have an application and many user, if the program has to wait tfor each user to consult the database to check for the next user, that would take forever. If every user had a thread, multiple users can be inspecting database at the same time
        
    * adv:
        - improve performance
        - reduce response time
        - increase flow(normal = 1 flow, n threads = n flows)

- threading module:
    * MainThread: created by PVM and is the defualt thread that is used when running
    * fcts: threading.
        1) current_thread(): returns which thread is currently being rand and thread ID (TID)
        2) current_thread().name: returns name of current thread
        3) current_thread().ident: returns id of current thread
        4) current_thread().is_alive(): returns boolean if thread is running
        - creating threads:
            * way 1: using Thread class from threading module
            5) Thread(target = fct_name,args=()): to create a thread obj
            6) start(): to call the thread created
            * way 2: extending Thread class
    '''

#fcts 1-4:
'''
import threading

print(threading.current_thread())
print(threading.current_thread().name)
print(threading.current_thread().ident)
print(threading.current_thread().is_alive())
'''

#creating threads method 1:

#import 
from threading import Thread, current_thread
from time import  sleep

'''
#create fct that will be executed parallaly
def display():
    for i in range(4):
        print("hello world")
        
#create object of thread class:
t1 = Thread(target = display,args=())
#start method
t1.start()

#another ex
def display2(n,msg):
    for i in range(n):
        print(msg)        
t2 = Thread(target = display2,args=(3,"hello!"))
t2.start()

#another ex
def display3(n):
    for i in range(n):
        print("hi")        
t3 = Thread(target = display3,args=(3,)) #has to have the comma here
t3.start()

#another ex
def display4(n):
    for i in range(n):
        print("Hi!")        
t4 = Thread(target = display4,kwargs={'n':2}) #keyword arguments
t4.start()

#another ex
def display5(n,msg):
    for i in range(n):
        print(msg)        
t5 = Thread(target = display5,kwargs={'n':5, 'msg': "hey"}) 
t5.start()



for i in range(4):
    print("this happens in main thread")
'''
'''

def display():
    print("t1 thread details: ",current_thread())
    for i in range(4):
        print("hello world")
        
#create object of thread class:
t1 = Thread(target = display,args=())
#start method
t1.start()
for i in range(4):
    print("this happens in main thread")
'''
'''
#how to create threads for methods:
class Example:
    @classmethod
    # if it is @staticmethod, class thread wont work only main thread, to make it work, remove 'self' from class arg
    def display(self,n):
        for i in range(5):
            print("hello")

e1 = Example()
#t1 = Thread(target=e1.display, args =(5,))
#or:
t1 = Thread(target=Example.display, args =(5,))
t1.start()    
for i in range(5):
    print("welcome")
'''

#creating threads method 2: advantage: you can access data created by threads
'''
class MyThread(Thread):
    def run(self):
        print("trial")

t1 = MyThread()
t1.start()
'''
#time and sleep.
'''
videos = ['OOP', 'constructor', 'destructor', 'file handling']
#t1
class MyClass(Thread):
    def run(self):
        for vid in videos:
            print(f"{vid} started uploading...")
            #will print, wait 3 sec then print again
            sleep(3)
            print(f"{vid} uploaded")


t1 = MyClass()
t1.start()

#t1 will start, main will wait 0.5 then start, t1 will continue

#main thread
for i in range(4):
    sleep(0.5)
    print("Check copyright")
'''
'''
videos = ['OOP', 'constructor', 'destructor', 'file handling']
class MyClass(Thread):
    def __init__(self,val): #will be executed before anything else
        print("constructor called")
        self.kid = val
        Thread.__init__(self)
    
    def compression(self):
        print(".zip file")

    def run(self):
        self.compression()
        if self.kid:
            print("Suitable for kids")
        for vid in videos:
            print(f"{vid} started uploading...")
            #will print, wait 3 sec then print again
            sleep(3)
            print(f"{vid} uploaded")


t1 = MyClass(True) #arg here is the value of the variable val
t1.start()

#t1 will start, main will wait 0.5 then start, t1 will continue

#main thread
for i in range(4):
    sleep(0.5)
    print("Check copyright")
'''

def display():
    a = 10
    b = 20
    return a+b

t1 = Thread(target=display)
print(t1.start()) #none bc you cant display results of one thread in main like this.

#you can do it this way:
'''
videos = ['OOP', 'constructor', 'destructor', 'file handling']
class MyClass(Thread):
    def __init__(self,val): #will be executed before anything else
        print("constructor called")
        self.kid = val
        Thread.__init__(self)
    
    def compression(self):
        print(".zip file")

    def run(self):
        a = 10
        b = 20
        self.temp = a+b
        self.compression()
        if self.kid:
            print("Suitable for kids")
        for vid in videos:
            print(f"{vid} started uploading...")
            #will print, wait 3 sec then print again
            sleep(3)
            print(f"{vid} uploaded")
            
        


t1 = MyClass(True) #arg here is the value of the variable val
t1.start()
print("result is: ",t1.temp)

#t1 will start, main will wait 0.5 then start, t1 will continue

#main thread
for i in range(4):
    sleep(0.5)
    print("Check copyright")
'''

#for timings errors:
'''
videos = ['OOP', 'constructor', 'destructor', 'file handling']
class MyClass(Thread):
    def __init__(self,val): #will be executed before anything else
        print("constructor called")
        self.kid = val
        Thread.__init__(self)
    
    def compression(self):
        print(".zip file")

    def run(self):
        a = 10
        b = 20
        
        self.compression()
        if self.kid:
            print("Suitable for kids")
        for vid in videos:
            print(f"{vid} started uploading...")
            #will print, wait 3 sec then print again
            sleep(3)
            print(f"{vid} uploaded")
        self.temp = a+b    
        


t1 = MyClass(True) #arg here is the value of the variable val
t1.start()
sleep(20) #this here will delay the timings to let the program reach the self.temp variable before main thread is executed
print("result is: ",t1.temp)

#t1 will start, main will wait 0.5 then start, t1 will continue

#main thread
for i in range(4):
    sleep(0.5)
    print("Check copyright")
'''

