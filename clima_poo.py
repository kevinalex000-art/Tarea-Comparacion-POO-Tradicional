# Tarea Práctica - Programación Orientada a Objetos (POO)
# Archivo: clima_poo.py

class ReporteSemanalClima:
    """
    Clase que modela el reporte de clima semanal. 
    Aplica Encapsulamiento al mantener las temperaturas internas.
    """
    
    DIAS_SEMANA = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    
    def __init__(self):
        """Constructor. Inicializa el atributo de las temperaturas."""
        # Encapsulamiento: atributo protegido
        self._temperaturas = [] 

    def ingresar_temperaturas(self):
        """Método para ingresar las temperaturas diarias."""
        print("--- 🌡️ Ingreso de Temperaturas Diarias (POO) ---")
        self._temperaturas = [] 
        
        for dia in self.DIAS_SEMANA:
            while True:
                try:
                    temp = input(f"Ingrese la temperatura del {dia} (°C): ")
                    self._temperaturas.append(float(temp))
                    break
                except ValueError:
                    print("Error: Por favor, ingrese un valor numérico válido.")
                    
    def calcular_promedio(self):
        """Método para calcular el promedio a partir de los datos internos."""
        if not self._temperaturas:
            return 0.0
            
        suma_total = sum(self._temperaturas)
        cantidad_dias = len(self._temperaturas)
        
        return suma_total / cantidad_dias

    def mostrar_reporte(self):
        """Método para presentar el resultado final al usuario."""
        promedio = self.calcular_promedio() # Llamada al método interno
        
        print("\n--- ✅ Reporte Semanal POO ---")
        print(f"Temperaturas registradas: {self._temperaturas}")
        print(f"El promedio semanal de la temperatura es: {promedio:.2f} °C")

# Función principal POO
def programa_poo_clima():
    # 1. Crear el objeto (instancia de la clase)
    reporte = ReporteSemanalClima() 
    
    # 2. Usar los métodos del objeto
    reporte.ingresar_temperaturas()
    reporte.mostrar_reporte()

# Ejecución
if __name__ == "__main__":
    programa_poo_clima()