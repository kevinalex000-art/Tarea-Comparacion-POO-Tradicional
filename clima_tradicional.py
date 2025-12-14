# Tarea Práctica - Programación Tradicional (Funcional)
# Archivo: clima_tradicional.py

def obtener_temperaturas_diarias():
    """
    Solicita las 7 temperaturas diarias y las retorna en una lista.
    """
    temperaturas = []
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    
    print("--- 🌡️ Ingreso de Temperaturas Diarias (Tradicional) ---")
    
    for dia in dias:
        while True:
            try:
                temp = input(f"Ingrese la temperatura del {dia} (°C): ")
                temperaturas.append(float(temp))
                break
            except ValueError:
                print("Error: Por favor, ingrese un valor numérico válido.")
                
    return temperaturas

def calcular_promedio_semanal(lista_temperaturas):
    """
    Calcula el promedio aritmético de la lista de temperaturas.
    """
    if not lista_temperaturas:
        return 0.0
        
    suma_total = sum(lista_temperaturas)
    cantidad_dias = len(lista_temperaturas)
    promedio = suma_total / cantidad_dias
    
    return promedio

def programa_tradicional_clima():
    # 1. Entrada
    temps = obtener_temperaturas_diarias()
    
    # 2. Procesamiento
    promedio = calcular_promedio_semanal(temps)
    
    # 3. Salida
    print("\n--- ✅ Resultado ---")
    print(f"El promedio semanal de la temperatura es: {promedio:.2f} °C") 

# Ejecución
if __name__ == "__main__":
    programa_tradicional_clima()