class Libro:
    def __init__(self, titulo, autor, paginas, leidas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self._progreso = leidas

    def leer(self, cantidad):
        if cantidad < 0 or self._progreso + cantidad > self.paginas:
            print("Cantidad inválida")
        else:
            self._progreso += cantidad

    def progreso(self):
        return f"{(self._progreso / self.paginas) * 100}%"


    def resumen(self):
        porcentaje = (self._progreso / self.paginas) * 100
        return f"({self.titulo} {self.autor} ({porcentaje}%): {self._progreso} el total de páginas leídas es de {self.paginas})"

l1 = Libro("Pachinko", "Min Jin Lee", 496, 193)
l2 = Libro("El Conde de Monte Cristo", "Alexander Dumas", 1276)

l1.leer(200)           
l1._progreso

l1.progreso()

l1.resumen()
l2.resumen()