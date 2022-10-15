from ast import arg
import threading
import time
import multiprocessing

def longSquare(n, results):
    time.sleep(1)
    results[n]=n**2

#print([longSquare(n) for n in range (0,5 ) ])

results = {}
t1 = threading.Thread(target=longSquare, args=(1,results))
t2 = threading.Thread(target=longSquare, args=(2,results))
t1.start()
t2.start()
t1.join()
t2.join()
print(results)

resultsData = {}
threads = [threading.Thread(target=longSquare, args=(n, resultsData)) for n in range (0, 100)]
[t.start() for t in threads]
[t.join() for t in threads]
print(resultsData)

#resultProcess = {}
#p1 = multiprocessing.Process(target=longSquare, args=(1, resultProcess))
#p2 = multiprocessing.Process(target=longSquare, args=(2, resultProcess))
#p1.start()
#p2.start()
#p1.join()
#p2.join()

#print(resultProcess)