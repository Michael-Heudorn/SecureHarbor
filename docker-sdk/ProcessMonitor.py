from Monitor import Monitor
from docker.models.containers import Container
from threading import Thread


class ProcessMonitor(Monitor):
    def run(self, container: Container):
        print("[*] Starting Process Monitor")

    def stop(self, container: Container):
        print("[*] Stopping Process Monitor")

    def runInThread(self, container: Container):
        thread = Thread(target=self.run(container))
        thread.start()
