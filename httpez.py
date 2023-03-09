import threading
import queue
import requests

input_file = input("Your website list: ")
output_file = input("Result filename: ")
num_threads = int(input("Thread (number): "))

url_queue = queue.Queue()

with open(input_file) as f:
    for line in f:
        url_queue.put(line.strip())

def check_url():
    while True:
        url = url_queue.get()
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
        url_queue.task_done()

for i in range(num_threads):
    t = threading.Thread(target=check_url)
    t.daemon = True
    t.start()

url_queue.join()
