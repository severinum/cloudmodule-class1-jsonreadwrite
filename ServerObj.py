class Server:

    def __init__(self, name, cpuUsage) -> None:
        self.name = name
        self.cpuUsage = cpuUsage

    def getName(self):
        return self.name

    def getCpuUsage(self):
        return self.cpuUsage


    