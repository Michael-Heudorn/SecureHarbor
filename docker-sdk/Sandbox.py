class Sandbox:
    def __init__(self, container, monitors):
        self.container = container
        self.monitors = monitors

    def runMonitors(self):
        for monitor in self.monitors:
            # TODO Run them in parallel
            monitor.runInThread(self.container)

    def terminate(self):
        for monitor in self.monitors:
            monitor.stop(self.container)

        self.container.stop()
