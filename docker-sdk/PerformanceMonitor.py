from Monitor import Monitor
from docker.models.containers import Container
from threading import Thread
import json


class PerformanceMonitor(Monitor):
    def run(self, container: Container):
        print("[*] Starting Performance Monitor")
        for stats in container.stats(decode=True):
            data = {
                "Type" : "Performance",
                "ContainerID" : container.id,
                "data" : stats
            }

            json_data = json.dumps(data)
            # TODO Distribute Data to Frontend and Classifier

    def stop(self, container: Container):
        print("[*] Stopping Performance Monitor")

    def runInThread(self, container: Container):
        thread = Thread(target=self.run(container))
        thread.start()
