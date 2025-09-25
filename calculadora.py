import math

def calculadora():
    while True:
        print("\n=== CALCULADORA CIENTÍFICA ===")
        print("Selecciona una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("6. Raíz cuadrada")
        print("7. Logaritmo (base e)")
        print("8. Logaritmo en base 10")
        print("9. Funciones trigonométricas (sen, cos, tan)")
        print("10. Salir")
        
        opcion = input("Opción: ")

        if opcion == "1":
            a, b = map(float, input("Ingresa dos números separados por espacio: ").split())
            print(f"Resultado: {a + b}")
        
        elif opcion == "2":
            a, b = map(float, input("Ingresa dos números separados por espacio: ").split())
            print(f"Resultado: {a - b}")

        elif opcion == "3":
            a, b = map(float, input("Ingresa dos números separados por espacio: ").split())
            print(f"Resultado: {a * b}")

        elif opcion == "4":
            a, b = map(float, input("Ingresa dos números separados por espacio: ").split())
            if b != 0:
                print(f"Resultado: {a / b}")
            else:
                print("Error: División entre cero")

        elif opcion == "5":
            base, exponente = map(float, input("Ingresa la base y el exponente separados por espacio: ").split())
            print(f"Resultado: {math.pow(base, exponente)}")

        elif opcion == "6":
            a = float(input("Ingresa un número: "))
            if a >= 0:
                print(f"Resultado: {math.sqrt(a)}")
            else:
                print("Error: No se puede calcular la raíz cuadrada de un número negativo")

        elif opcion == "7":
            a = float(input("Ingresa un número: "))
            if a > 0:
                print(f"Resultado: {math.log(a)}")
            else:
                print("Error: El logaritmo solo está definido para números positivos")

        elif opcion == "8":
            a = float(input("Ingresa un número: "))
            if a > 0:
                print(f"Resultado: {math.log10(a)}")
            else:
                print("Error: El logaritmo solo está definido para números positivos")

        elif opcion == "9":
            angulo = float(input("Ingresa un ángulo en grados: "))
            rad = math.radians(angulo)
            print(f"sen({angulo}) = {math.sin(rad)}")
            print(f"cos({angulo}) = {math.cos(rad)}")
            print(f"tan({angulo}) = {math.tan(rad)}")

        elif opcion == "10":
            print("Saliendo de la calculadora... ¡Hasta luego!")
            break

        else:
            print("Opción inválida, intenta de nuevo.")

# Ejecutar la calculadora
if __name__ == "__main__":
    calculadora()
