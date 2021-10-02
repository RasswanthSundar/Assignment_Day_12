import queue
import random
import concurrent.futures as cf
import time
import threading


def producer(pipeline, event):
    '''
        This is a producer function which 
        will produce the data when called
    '''
    while not event.is_set():
        val = random.randint(1,100)
        print(f'Producer Storing {val}')
        pipeline.put(val)
    print('Producer Exit')

def consumer(pipeline, event):
    '''
        This is a consumer function which 
        will consume the data when called
    '''
    while not event.is_set() or not pipeline.empty():
        val = pipeline.get()
        print(f'Consumer Getting {val}')
    print('Consumer Exit')

if __name__ == '__main__':
    pipeline = queue.Queue(maxsize=1)
    event = threading.Event()
    with cf.ThreadPoolExecutor() as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        print('Event Set')
        event.set()