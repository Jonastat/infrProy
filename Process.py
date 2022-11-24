import time
class Process:
    startTime=-1
    stopTime=-1

    def __init__(self,timeNeeded,processName):
        self.startTime = time.time()
        self.timeNeeded = timeNeeded
        self.processName = processName


    def showInfo(self):
        print(f" startTime {self.startTime}  timeNeeded {self.timeNeeded} process name {self.processName}" )
    #metodo que verifica si el proceso ya termino y ya no necesita mas al procesador
    def isDone(self):
        print(f"time needed  {self.timeNeeded}")
        if(self.timeNeeded<0):
            return True
        return False
    #reduce el tiempo que necesita el proceso al procesador
    def addWorkTime(self,workTime):
        self.timeNeeded -= workTime
        print(f" tiempo que necesita el proceso para empezar {self.timeNeeded}")
    #metodo que setea el tiempo de inicio del proceso
    def setStartTime(self, startTime):
        self.startTime = startTime
    #metodo que setea el tiempo de detencion del proceso
    def setStopTime(self, stopTime):
        self.stopTime = stopTime
    def timeService(self):
        timeService = self.stopTime - self.startTime
        print(f"tiempo de servicio del proceso {self.processName} : {timeService}")

    

