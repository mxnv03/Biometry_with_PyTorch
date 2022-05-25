from threading import Thread
import RunTrack


class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        if self.name == 'Tracking':
            RunTrack.run()
