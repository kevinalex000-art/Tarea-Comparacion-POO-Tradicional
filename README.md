# Tarea Práctica: Comparación de Programación Tradicional y POO en Python

Este repositorio contiene dos soluciones en Python para el cálculo del promedio semanal del clima, implementadas bajo diferentes paradigmas.

## Tabla Comparativa

| Característica | Programación Tradicional (`clima_tradicional.py`) | Programación Orientada a Objetos (`clima_poo.py`) |
| :--- | :--- | :--- |
| **Organización Principal** | Basada en **Funciones**. El flujo se enfoca en el *procedimiento* (paso a paso). | Basada en **Clases/Objetos**. El flujo se enfoca en la *entidad* (`ReporteSemanalClima`). |
| **Datos vs. Lógica** | Los datos (lista de temperaturas) se definen fuera de las funciones y se pasan como argumentos entre ellas. Están **separados**. | Los datos (`self._temperaturas`) y la lógica (`calcular_promedio()`) están **encapsulados** dentro de la clase. |
| **Modularidad** | Baja. Si se cambia la estructura de datos, muchas funciones pueden necesitar ser modificadas. | Alta. Los cambios en la implementación interna del reporte no afectan a cómo se interactúa con el objeto. |
| **Conceptos POO Aplicados** | N/A | **Encapsulamiento** (uso del atributo `_temperaturas` para proteger los datos). |

## Conclusión

Ambos enfoques resuelven el problema de manera efectiva. Sin embargo:
* La solución **Tradicional** es más rápida y concisa para tareas muy simples y directas.
* La solución **POO** ofrece una estructura más organizada y escalable. Si el programa creciera para manejar múltiples ciudades, diferentes tipos de reportes, o almacenamiento en una base de datos, la clase `ReporteSemanalClima` facilitaría enormemente la gestión y el mantenimiento del código.