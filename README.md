# operadores logicos
Los operadores lógicos en Python **nos permiten combinar y evaluar múltiples condiciones.** Estos operadores nos ayudan a tomar decisiones basadas en la veracidad o falsedad de las condiciones. Aquí tienes un resumen de los operadores lógicos en Python, junto con algunos ejemplos:
 
## 1. Operador "and":
 
- El operador **"and"** devuelve True si ambas condiciones son verdaderas, y False en cualquier otro caso.
- Ejemplo:
```python
edad = 25
tiene_licencia = True
if edad >= 18 and tiene_licencia:
    print("Puede conducir")
 ```
##  2. Operador "or":

- El operador **"or"** devuelve True si al menos una de las condiciones es verdadera, y False solo si ambas condiciones son falsas.
- Ejemplo:
```python
es_estudiante = True
es_empleado = False
if es_estudiante or es_empleado:
    print("Es parte de la comunidad educativa")
 ```
## 3. Operador "not":
 
- El operador **"not"** invierte el valor de una condición, es decir, devuelve True si la condición es falsa, y False si la condición es verdadera.
- Ejemplo:
```python
es_sabado = False
if not es_sabado:
    print("No es sábado")
 ```
