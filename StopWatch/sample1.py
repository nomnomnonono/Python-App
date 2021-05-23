import time

import StopWatch

stop_watch = StopWatch.StopWatch()
stop_watch.start()

for i  in range(10):
    time.sleep(1.55)
    print("lap" + str(i) + " : " + stop_watch.lap())
    print("split : " + stop_watch.split())

stop_watch.stop()

print("elapsed : " + stop_watch.result())
