import requests
import os
from multiprocessing.pool import ThreadPool

input_file = raw_input("Your website list: ")
output_file = raw_input("Result filename: ")
num_threads = int(raw_input("Thread (number): "))

url_list = []

with open(input_file) as f:
    for line in f:
        url_list.append(line.strip())

def check_url(url):
    try:
        response = requests.get('https://' + url, timeout=10)
        with open(output_file, 'a') as f:
            f.write('https://' + url + '\n')
            print('https://' + url + ' [SUCCESS]')
    except:
        try:
            response = requests.get('http://' + url, timeout=10)
            with open(output_file, 'a') as f:
                f.write('http://' + url + '\n')
                print('http://' + url + ' [SUCCESS]')
        except:
            print(url + ' [FAILED]')

if not os.path.exists(output_file):
    open(output_file, 'w').close()

pool = ThreadPool(num_threads)
pool.map(check_url, url_list)
pool.close()
pool.join()

print("HttpEZ Done")
