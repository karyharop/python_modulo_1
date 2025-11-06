print("\n")
print("=" * 40)
print("RETO OPERADORES")
print("=" * 40)
print("\n")

print("=== CALCULADORA DE IMC ===\n")

# 1. Declara dos variables: 'peso' con valor 70 (en kilogramos) y 'altura' con valor 1.75 (en metros)
peso = 70 "kg"

altura = 1.75 "m"

print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")

print("\n=== CÁLCULO DEL IMC ===")

# 2. Calcula el IMC utilizando la fórmula: peso / (altura ** 2)
IMC = peso / (altura ** 2) 
# significa elevar al cuadrado

# 3. Almacena el resultado en una variable llamada 'imc'
print(f"IMC: {IMC}")

# 4. Redondea el resultado a dos decimales usando la función round()
resultado = round(IMC, 2)

print("=== RESULTADO ===")
# 5. Imprime el resultado con un mensaje descriptivo
print(f"Tu Índice de Masa Corporal (IMC) es: {resultado}")

