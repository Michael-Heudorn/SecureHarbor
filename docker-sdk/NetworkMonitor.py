from Monitor import Monitor
from docker.models.containers import Container
from multiprocessing import Process


class NetworkMonitor(Monitor):
    def run(self, container: Container):
        print("[*] Starting Network Monitor")

    def stop(self, container: Container):
        print("[*] Stopping Network Monitor")

    def runInThread(self, container: Container) -> Process:
        process = Process(target=self.run, args=(container,))
        process.start()
        return process
