import time
from timeit import default_timer as real_time


class Stopwatch(object):
    
    def __init__(self, timer_func):
        """ Create a stopwatch timer
        Parameters: timer_func"""
        
        self._stop_time = 0
        self._start_time = None
        self.elapsed_time = 0
        self._now = timer_func
        
    def start_timer(self):
        """Starts the timer."""
        if self.start_time is not None:
            raise RuntimeError('Timer already started')
            
        self.start_time = self._now() 
        
        return 
        
    
    def stop_timer(self):
        """ Stops the timer. Returns time of stop."""
        if self.start_time is None:
            raise RuntimeError('Timer has not been started')
        self.stop_time =  self._now()
        self.elapsed_time += self.stop_time - self.start_time
        
        self.start_time = None

        return

    
    def elapsed(self):
        """ Returns the time that has elapsed between starting the timer
            and stopping it.
        """
        
        #if it's running
        if self.start_time is not None:
            return (self._now() - self.start_time) + self.elapsed_time
        
        return self.elapsed_time
        
    def reset(self):
        """ Resets the start time to 0. """
        
        self.stop_time = 0
        self.elapsed_time = 0
        self.start_time = None
        
        return 
        
    @property
    #the getter
    def start_time(self):
        print "geting start time value"
        return self._start_time
        
    #the setter
    @start_time.setter
    def start_time(self, value):
        print "setting start time value"
        self._start_time = value
        
    @property
    #the getter
    def stop_time(self):
        "getting the stop time value"
        return self._stop_time
        
    #the setter
    @stop_time.setter
    def stop_timer(self):
        "setting the stop time value"
        self._stop_time = value
        
        
    
    #what is this? look up context managers     
    def __enter__(self):
        self.start_timer()
        return self
        
    def __exit__(self, *args):
        self.stop_timer()
 

if __name__ == '__main__':
    mytimer = Stopwatch(real_time)

