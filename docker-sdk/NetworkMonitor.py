from Monitor import Monitor
from docker.models.containers import Container
from threading import Thread


class NetworkMonitor(Monitor):
    def run(self, container: Container):
        print("[*] Starting Network Monitor")

    def stop(self, container: Container):
        print("[*] Stopping Network Monitor")

    def runInThread(self, container: Container):
        thread = Thread(target=self.run(container))
        thread.start()
