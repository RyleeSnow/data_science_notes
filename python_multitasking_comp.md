### 1. 基本概念

##### 1.1 并发 Concurrency

并发指的是计算机“看似”可以同时进行很多不同的任务。比如，即使你的计算机只有一个CPU，但因为你可以迅速切换在这个CPU上运行的程序，从而造成一种假象，让人感觉这些程序真的在同时运行。

与并发相对的是“顺序 Sequential”，指的是只有当上一个执行的任务完成后，当前任务才能开始执行。但是在并发的场景下，无论上一个开始执行的任务是否完成，当前任务都可以开始执行。

##### 1.2 并行 Parallelism

并行指的是计算机“确实”可以同时进行很多不同的任务，这需要你的计算机配有多个CPU，每个CPU可以从物理层面就可以执行不同的任务。

与并行相对的是“串行 Serial”，指的是从物理上就只能一个任务、一个任务地执行。

##### 1.3 并发与并行

了解以上概念，就应该明白，并发与并行并不矛盾。并发关注的是抽象层面的任务安排，而并行关注的是物理层面的任务安排。同时，可以想象，并行时一定可以同时允许并发，但并发并不一定需要并行。

##### 1.4 进程 Process & 线程 Thread

- 进程是操作系统“分配资源”的最小单元（任一时刻，CPU总是只能运行一个**进程**，其他进程处于非运行状态），线程是操作系统“调度”的最小单元。
- 一个应用程序至少包括1个进程，而1个进程包括1个或多个线程。每个进程在执行过程中拥有独立的内存单元，而一个进程的多个线程在执行过程中共享内存。
- 虽然线程可以进行内存共享，但是：

  - 有时候需要防止多个线程同时读写某一块内存区域，同一时刻只能有一个线程使用这块内存。这个时候，则需要在这块内存上添加“互斥锁（Mutual exclusion, Mutex）”。
  - 有时候，虽然可以多个线程同时使用某一块内存区域，但需要限制线程的个数。这个时候，则需要添加“信号量 Semaphore”。
  - 虽然后者可以替代前者（设置线程限制为1），但是因为Mutex较为简单且销量很高，所以资源独占时一般还是直接采用。

##### 1.5 为什么常有人说 Python 中的多线程没有实际作用？- 全局解释器锁 GIL

GIL的全称是 Global Interpreter Lock，是python设计之初为了数据安全考虑所作的设计。

由于GIL，在Python中每个线程的执行方式是（1）获取GIL（2）执行代码（3）释放GIL。而因为每个Python进程有且只有一个GIL，这就导致**一个Python进程永远只能同时执行一个线程**。这也是为什么有人会说，Python中的多线程是鸡肋。

但这并不代表Python中的多线程是完全没有意义的。要讲明白这件事，需要理解一点补充知识。

- CPU密集型（CPU-bound）/ 计算密集型
  - 指的是系统的**硬盘、内存**性能相对CPU要好很多。IO读写在很短的时间就可以完成，而CPU还有许多运算要处理，造成IO等待CPU，CPU Loding会很高。
  - 大部份时间用来做**计算、逻辑判断**等CPU动作的程序称之CPU密集型。对于计算密集型任务，最好用C语言编写。
- IO密集型（I/O bound）
  - 指的是系统的**CPU**性能相对硬盘、内存要好很多。此时，计算很简单，但是有大量的数据读写操作，那么CPU就总是在等待IO，CPU Loading并不高。
  - 针对这类人物，用运行速度极快的C语言替换用Python这样运行速度极低的脚本语言，完全无法提升运行效率。对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C语言最差。

所以，对于CPU密集型的任务来说，Python的多线程基本没有任何实际意义。但是对于IO密集型任务（比如文件处理、网络爬虫）来说，多线程能够有效提升效率：单线程下有IO操作会进行IO等待，造成不必要的时间浪费，而开启多线程能在线程A等待时，自动切换到线程B，可以不浪费CPU的资源，从而能提升程序执行效率。

另外，对于CPU密集型的任务来说，多核多线程比单核多线程更差，原因是单核下多线程，每次释放GIL，唤醒的那个线程都能获取到GIL锁，所以能够无缝执行，但多核下，CPU0释放GIL后，其他CPU上的线程都会进行竞争，但GIL可能会马上又被CPU0拿到，导致其他几个CPU上被唤醒后的线程会醒着等待到切换时间后又进入待调度状态，这样会造成线程颠簸(thrashing)，导致效率更低。因此，多核下，想做并行提升效率，比较通用的方法是使用多进程，能够有效提高执行效率。

### 2. 多进程 - 实际应用和代码

Python多进程可以选择两种创建进程的方式：

- Fork：
  - 直接复制一份自己给子进程运行，并把自己所有资源的 handle 都让子进程继承
  - 创建速度很快，但更占用内存资源。
- Spawn：
  - 只会把必要的资源的 handle 交给子进程
  - 创建速度稍慢
  - 通常高性能计算需要让程序运行很久，因此为了节省内存以及进程安全，建议选择 Spawn

```python
multiprocessing.set_start_method('spawn')  # default on WinOS or MacOS
multiprocessing.set_start_method('fork')   # default on Linux (UnixOS)
```


#### 2.1 简单实现子进程

**多进程的主进程一定要写在程序入口 if __name__ =='__main__': 内部**

```python
from multiprocessing import Process

def task(id):  # 这里是子进程
    print(f'id {id}')

def run__process():  # 这里是主进程
    process = [Process(target=task, args=(1,)),
               Process(target=task, args=(2,)), ]
    [p.start() for p in process]  # 开启了两个进程
    [p.join() for p in process]   # 等待两个进程依次结束

# run__process()  # 主线程不建议写在 if外部。由于这里的例子很简单，你强行这么做可能不会报错
if __name__ =='__main__':
    run__process()  # 正确做法：主线程只能写在 if内部
```


这里只是简单实现了子进程，并未进行进程通信。试想，如果把一个串行任务（任务间有依赖关系）编排成多进程时，那么还需要进程通信：

- 进程池 Pool：
  - 可以让主程序获得子进程的计算结果
  - 不太灵活，适合简单任务
- 管道 Pipe / 队列 Queue
  - 可以让进程之间进行通信
  - 足够灵活。
- 共享值 Value / 共享数组 Array / 共享内容 shared_memory




#### 2.2 进程池 Pool


```python
import time

def func2(args):  # multiple parameters (arguments)
    # x, y = args
    x = args[0]  # write in this way, easier to locate errors
    y = args[1]  # write in this way, easier to locate errors

    time.sleep(1)  # pretend it is a time-consuming operation
    return x - y


def run__pool():  # main process
    from multiprocessing import Pool

    cpu_worker_num = 3
    process_args = [(1, 1), (9, 9), (4, 4), (3, 3), ]

    print(f'| inputs:  {process_args}')
    start_time = time.time()
    with Pool(cpu_worker_num) as p:
        outputs = p.map(func2, process_args)
    print(f'| outputs: {outputs}    TimeUsed: {time.time() - start_time:.1f}    \n')

    '''Another way (I don't recommend)
    Using 'functions.partial'. See https://stackoverflow.com/a/25553970/9293137
    from functools import partial
    # from functools import partial
    # pool.map(partial(f, a, b), iterable)
    '''

if __name__ =='__main__':
    run__pool()
```




#### 2.3 管道 Pipe

顾名思义，管道Pipe 有两端，因而 main_conn, child_conn = Pipe() ，管道的两端可以放在主进程或子进程内，我在实验中没发现主管道口main_conn 和子管道口child_conn 的区别。两端可以同时放进去东西，放进去的对象都经过了深拷贝：用 conn.send()在一端放入，用 conn.recv() 另一端取出，管道的两端可以同时给多个进程。conn是 connect的缩写。

```
import time

def func_pipe1(conn, p_id):
    print(p_id)

    time.sleep(0.1)
    conn.send(f'{p_id}_send1')
    print(p_id, 'send1')

    time.sleep(0.1)
    conn.send(f'{p_id}_send2')
    print(p_id, 'send2')

    time.sleep(0.1)
    rec = conn.recv()
    print(p_id, 'recv', rec)

    time.sleep(0.1)
    rec = conn.recv()
    print(p_id, 'recv', rec)


def func_pipe2(conn, p_id):
    print(p_id)

    time.sleep(0.1)
    conn.send(p_id)
    print(p_id, 'send')
    time.sleep(0.1)
    rec = conn.recv()
    print(p_id, 'recv', rec)


def run__pipe():
    from multiprocessing import Process, Pipe

    conn1, conn2 = Pipe()

    process = [Process(target=func_pipe1, args=(conn1, 'I1')),
               Process(target=func_pipe2, args=(conn2, 'I2')),
               Process(target=func_pipe2, args=(conn2, 'I3')), ]

    [p.start() for p in process]
    print('| Main', 'send')
    conn1.send(None)
    print('| Main', conn2.recv())
    [p.join() for p in process]

if __name__ =='__main__':
    run__pipe()
```


```
conn1, conn2 = multiprocessing.Pipe()  # 管道有两端，某一端放入的东西，只能在另一端拿到
queue = multiprocessing.Queue()        # 队列只有一个，放进去的东西可以在任何地方拿到。
```



#### 2.4 管道 Pipe

```python
def task_1(i):
    time.sleep(1)
    print(f'args {i}')

def task_2(i):
    time.sleep(1)
    print(f'args {i}')

def task_3(i):
    time.sleep(1)
    print(f'args {i}')

def run__queue():
    from multiprocessing import Process, Queue

    queue = Queue(maxsize=4)  # the following attribute can call in anywhere
    queue.put(True)
    queue.put([0, None, object])  # you can put deepcopy thing
    queue.qsize()  # the length of queue
    print(queue.get())  # First In First Out
    print(queue.get())  # First In First Out
    queue.qsize()  # the length of queue

    process = [Process(target=func1, args=(queue,)),
               Process(target=func1, args=(queue,)), ]
    [p.start() for p in process]
    [p.join() for p in process]

if __name__ =='__main__':
    run__queue()
```
