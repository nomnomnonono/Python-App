import StopWatch

stop_watch = StopWatch.StopWatch()

stop_watch.start()
count = 0

for i in range(10000000):
    if (i % 10000 == 0):
        count += 1
        print("lap" + str(count) + " : " + stop_watch.lap())
        print("split : " + stop_watch.split())

stop_watch.stop()

print("elapse : " + stop_watch.result())
