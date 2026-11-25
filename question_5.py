class Tarea:
    def __init__(self, titulo, prioridad="baja", completada=False):
        self.titulo = titulo
        self.prioridad = prioridad
        self.completada = completada

    def marcar_completada(self):
        self.completada = True

class ListaTareas:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def listar_pendientes(self):
        return [tarea for tarea in self.tareas if not tarea.completada]

    def contar_por_prioridad(self, prioridad):
        return len([tarea for tarea in self.tareas if tarea.prioridad == prioridad])

t1 = Tarea("Tomar agua", "alta")
t2 = Tarea("Llamar a Octavio")
t3 = Tarea("Investigar PC", "media", True)
t1.marcar_completada()

lt = ListaTareas("Planificación del día")
lt.agregar_tarea(t1)
lt.listar_pendientes()
lt.agregar_tarea(t3)
lt.contar_por_prioridad("baja")
