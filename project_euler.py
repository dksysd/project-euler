import time
#import sys

start_time = time.time()
Fibo = [1, 1, 0]
res = []
min_num = 12345678999
max_num = 99987654321

j = int(0)
while j < max_num:
    temp = Fibo[0] + Fibo[1]
    Fibo[2] = temp
    if temp >= min_num and temp <= max_num:
        res.append(temp)
    elif temp > max_num:
        break
    temp = Fibo[1] + Fibo[2]
    Fibo[0] = temp
    if temp >= min_num and temp <= max_num:
        res.append(temp)
    elif temp > max_num:
        break
    temp = Fibo[0] + Fibo[2]
    Fibo[1] = temp
    if temp >= min_num and temp <= max_num:
        res.append(temp)
    elif temp > max_num:
        break
    j += 3

#sys.stdout = open('result.txt', 'a')
print('result::', res)

result = 0
for z in res:
    result += z
print('sum::', result)
print('runtime::', round(time.time()-start_time, 6))
