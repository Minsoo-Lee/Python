class SalesWorker:
    def __init__(self, name):
        self.__name = name
    def work(self):
        print(self.__name, "sale things.")

class DevWorker(SalesWorker):
    def __init__(self, name):
        super().__init__(name)
        self.__name = name
    def work(self):
        print(self.__name,"develop things")

if __name__ == "__main__":
    worker1 = SalesWorker("Dave")
    worker2 = DevWorker("minsoo")
    
    workers = [worker1, worker2]
    
    for worker in workers:
        worker.work()