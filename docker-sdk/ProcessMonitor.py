from Monitor import Monitor
from docker.models.containers import Container
from multiprocessing import Process


class ProcessMonitor(Monitor):
    def run(self, container: Container):
        print("[*] Starting Process Monitor")
        print(container.top())

    def stop(self, container: Container):
        print("[*] Stopping Process Monitor")

    def runInThread(self, container: Container) -> Process:
        process = Process(target=self.run, args=(container,))
        process.start()
        return process
