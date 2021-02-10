import pygame
import time
from .node import Node
from .ids import TIMER


class Timer(Node):
    def __init__(self, wait_time, autostart=False, start_now=False, **kwargs):
        super(Timer, self).__init__(id=kwargs.get("id", TIMER))
        self.wait_time = wait_time
        self.autostart = autostart
        self.start_time = None
        self.end_time = None
        self.past_time = 0

        if start_now:
            self.start()
    
    def start(self):
        self.start_time = time.perf_counter()
    
    def is_done(self):
        return self.past_time >= self.wait_time
    
    def get_time(self):
        return self.past_time
    
    def on_update(self):
        self.end_time = time.perf_counter()

        if self.start_time is not None and self.end_time is not None:
            self.past_time = self.end_time - self.start_time
        
        if self.past_time >= self.wait_time:
            if self.autostart:
                self.start()
