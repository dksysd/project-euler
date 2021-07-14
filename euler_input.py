import time
import sys
import numpy as np


Fibo = np.array([1, 2]).astype(np.int8)
res = np.array([]).astype(np.int8)
min_num = int(input('min_num::'))
max_num = int(input('max_num::'))

i = int(2)
j = int(0)
start_time = time.time()
while i < max_num:
    temp = Fibo[i-1] + Fibo[i-2]
    Fibo = np.append(Fibo, np.array([temp]))
    print('Running...')
    if temp >= min_num and temp <= max_num:
        res = np.append(res, np.array([temp]))
        j += 1
    elif temp > max_num:
        break
    temp = Fibo[i-1] + Fibo[i]
    Fibo[i-2] = temp
    if temp >= min_num and temp <= max_num:
        res = np.append(res, np.array([temp]))
        j += 1
    elif temp > max_num:
        break
    i += 1

sys.stdout = open('result.txt', 'a')
print('result::', res)
sys.stdout = open('result.txt', 'a')
print('runtime::', time.time()-start_time)
