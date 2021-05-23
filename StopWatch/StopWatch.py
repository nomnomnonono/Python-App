import time
import math


class StopWatch:
    """
    Attributes
    ----------
    t_start: float
        starting time
    t_end: float
        stopped time
    lap_start: float
        Starting time of the lap
    """
    def __init__(self):
        """initialization of attributes"""
        self.t_start = 0
        self.t_end = 0
        self.lap_start = 0

    def start(self):
        """start the StopWatch"""
        self.t_start = time.time()
        self.lap_start = self.t_start

    def stop(self):
        """stop the StopWatch"""
        self.t_end = time.time()

    def lap(self):
        """measure the elapsed time of the current lap"""
        now = time.time()
        before = self.lap_start
        self.lap_start = now
        return self.get(round(self.lap_start - before, 3))

    def split(self):
        """measure the elapsed time to present"""
        now = time.time()
        return self.get(round(now - self.t_start, 3))

    def result(self):
        """return the elapsed time from start to stop"""
        return self.get(round(self.t_end - self.t_start, 3))

    def get(self, elapsed):
        """
        process into a readable format and output the elapsed time given by parameter

        Parameter
        ---------
        elapsed: float
            elapsed time calculated by each function(lap, split, result)

        """
        f, i = math.modf(elapsed)
        hour = math.floor(i / 3600)
        minute = math.floor((i % 3600) / 60)
        second = math.floor(i % 60)
        ms = math.floor(f * 1000)
        # H: hour, M: minute, S: second, MS: millisecond
        return str(hour).zfill(2) + "H : " + str(minute).zfill(2) + "M : " + str(second).zfill(2) + "S : " \
               + str(ms).zfill(3) + "MS"

