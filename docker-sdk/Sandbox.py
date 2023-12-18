class Sandbox:
    def __init__(self, container, monitors):
        self.container = container
        self.monitors = monitors
        self.processes = []

    def runMonitors(self):
        for monitor in self.monitors:
            # TODO Run them in parallel
            process = monitor.runInThread(self.container)
            self.processes.append(process)

    def terminate(self):
        for process in self.processes:
            process.terminate()

        self.container.stop()
