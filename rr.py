from sys import argv

#Clase para los atributos de un proceso
class Proceso():

    def __init__(self, name, instru, estado, posic):
        self.pcb = name[0]
        self.pid = name[1]
        self.instru = instru
        self.estado = estado
        self.posic = posic


#Clase para controlar el algoritmo
class RoundRobin():

    def __init__(self, num, quantum, archivo):
        self.num = num
        self.quantum = quantum
        self.archivo = archivo
        self.buffer = []
        self.procesos = [
            Proceso(["P{}".format(i), "0{}".format(i)], 100, "N", i)
            for i in range(1, self.num + 1)
        ]
        self.titulo_buffer()
        self.cola_listo()
        self.procesar_cola()
        print("{} guardado correctamente".format(self.archivo))

    #Metodo para titulo_buffer
    def titulo_buffer(self):
        self.buffer = ["Algoritmo de planificación Round Robin\n"]
        self.buffer.append("N(Nuevo) L(Listo) E(Ejecución) T(Terminado)\n")
        self.buffer.append("Cantidad de procesos: {}\n".format(self.num))
        self.buffer.append("Quantum: {}\n".format(self.quantum))
        self.guardar_buffer()

    #Metodo para guardar_buffer
    def guardar_buffer(self):
        self.buffer.append("\nProceso")
        for proc in self.procesos:
            self.buffer.append("\t{}".format(proc.pcb))
        self.buffer.append("\nID")
        for proc in self.procesos:
            self.buffer.append("\t{}".format(proc.id))
        self.buffer.append("\nInstruc")
        for proc in self.procesos:
            self.buffer.append("\t{}".format(proc.instru))
        self.buffer.append("\nEstado")
        for proc in self.procesos:
            self.buffer.append("\t{}".format(proc.estado))
        self.buffer.append("\nPosic")
        for proc in self.procesos:
            self.buffer.append("\t{}".format(proc.posic))
        self.buffer.append("\n")
        self.guardar_archivo()

    #Metodo para cola_listo
    def cola_listo(self):
        for proc in self.procesos:
            proc.estado = "L"
        self.guardar_buffer()

    #Metodo para procesar_cola
    def procesar_cola(self):
        while self.procesos_no_terminados():
            for proc in self.procesos:
                self.trabajar_proceso(proc)
        self.reposicionar_cola()
        self.guardar_buffer()

    #Metodo para reposicionar_cola
    def reposicionar_cola(self):
        posicion = 0
        for proc in self.procesos:
            if proc.estado == "T":
                proc.posic = 0
            else:
                posicion += 1
                proc.posic = posicion

    #Metodo para procesos_no_terminados
    def procesos_no_terminados(self):
        for proc in self.procesos:
            if proc.estado != "T":
                return True
        return False

    #Metodo para trabajar_proceso
    def trabajar_proceso(self, proc):
        if proc.instru > self.quantum:
            proc.instru -= self.quantum
            proc.estado = "E"
            self.guardar_buffer()
            proc.estado = "T" if proc.instru == 0 else "L"
        elif proc.estado != "T":
            proc.instru = 0
            proc.estado = "E"
            self.reposicionar_cola()
            self.guardar_buffer()
            proc.estado = "T"

    #Metodo para guardar_archivo
    def guardar_archivo(self):
        try:
            with open(self.archivo, "a") as file:
                file.write("".join(self.buffer))
                file.close()
                self.buffer[:] = []
        except IOError:
            raise "Error al guardar {}".format(self.archivo)

RoundRobin(int(argv[1]), int(argv[2]), "pytest.txt")