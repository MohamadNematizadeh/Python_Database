import time
from PySide6.QtCore import *
from timy import Mytime

class Thread_timer(QThread):
    timer_signal = Signal(Mytime)
    def __init__(self,h,m,s):
        super().__init__()
        self.timer_time = Mytime(h,s,m)

    def run(self):
        while True:
            self.timer_time.minus()
            self.timer_signal.emit(self.timer_time)
            time.sleep(1)