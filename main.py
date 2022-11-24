from Process import Process
import time 

#velocidad del procesador
processorSpeed = 3
def fcfs():
    print("has elegido fcfs")
    totalProcess = int(input("Ingrese la cantidad de procesos :"))
    processList = []
    for i in range(totalProcess):
        timeNeeded = float(input("ingrese el tiempo necesario para el proceso(en segundos )  :"))
        processName = input("ingrese el nombre  del proceso  :")
        processList.append(Process(timeNeeded,processName))

    for process in processList:
        process.setStartTime(time.time())
        while (not(process.isDone())):
            print(f"el procesador da atencion a {process.processName}")
            attentionTimeStart = time.time()
            time.sleep(processorSpeed)
            attentionTimeStop = time.time()
            totalAttentionTime = attentionTimeStop - attentionTimeStart
            process.addWorkTime(totalAttentionTime)
            print(f"el procesador quita atencion a {process.processName}, total atencion brindada {totalAttentionTime}")

        print(f"el proceso{process.processName} ha terminado su tarea, estadisticas:")
        process.setStopTime(time.time())
        process.timeService()
        #falta pone la ecuacion  pero es igual que el time service
        #process.waitTime()

       
    

def main():
    userOption = int(input("Elige el algoritmo de planificación de procesos \n1:FCFS \n:"))
    if(userOption == 1):
        fcfs()
main()
