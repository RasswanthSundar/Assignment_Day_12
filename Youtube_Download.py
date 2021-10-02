import time
import os
import concurrent.futures as cf

try:
    from pytube import YouTube
except:
    print('Import Missing')
    raise ImportError


# Urls for downloading the video
urls = ['https://www.youtube.com/watch?v=eSIJddEieLI', 'https://www.youtube.com/watch?v=UCDQ-Stczw0']

def download(url, fc):
    '''
        To download the youtube video in the given url
    '''
    f = YouTube(url).streams.get_highest_resolution().download()
    os.rename(f, (fc+'.MP4'))

def with_multithread(fil_nam):
    '''
        To calculate the time difference for 
        downloading the youtube videos with 
        multithreading
    '''
    t1 = time.perf_counter()

    with cf.ThreadPoolExecutor() as executor:
        executor.map(download, urls, fil_nam)

    t2 = time.perf_counter()

    return (t2-t1)

def without_multithread(fil_nam):
    '''
        To calculate the time difference for 
        downloading the youtube videos without 
        multithreading
    '''
    t1 = time.perf_counter()

    # To call the download method for the no of urls in the list[]-urls
    for (url, fil) in zip(urls, fil_nam):
        download(url, fil)

    t2 = time.perf_counter()

    return (t2-t1)

with_multi = with_multithread(['with_multi_1', 'with_multi_2'])

without_multi = without_multithread(['without_multi_1', 'without_multi_2'])

print('Time taken for the program to execute without multithreading is = ', without_multi)

print('Time taken for the program to execute with multithreading is = ', with_multi)

# Check if without multithreading is faster and print it is faster
if ((without_multi-with_multi)<0):
    print('Without multithreading the code execute faster')

# Else print multithreading is faster
else:
    print('With multithreading the code execute faster')