print("Sistema de numeración")

def hexa_a_bin(hexadecimal):
    try:
        return bin(int(hexadecimal, 16))[2:]
    except ValueError:
        return "Error"
        
def hexa_a_dec(hexadecimal):
    try:
        return int(hexadecimal, 16)
    except ValueError:
        return "Error"

def hexa_a_oct(hexadecimal):
    try:
        return oct(int(hexadecimal, 16))[2:]
    except ValueError:
        return "Error"

def hexa_a_bcd(hexadecimal):
    try:
        decimal = int(hexadecimal, 16)
        bcd_num = ""
        while decimal > 0:
            bcd_num = str(decimal % 10) + bcd_num
            decimal //= 10
        return bcd_num 
    except ValueError:
        return "Error"

def dec_a_bin(decimal):
    try:
        return bin(decimal)[2:]
    except ValueError:
        return "Error"

def dec_a_hex(decimal):
    try:
        return hex(decimal)[2:]
    except ValueError:
        return "Error"

def dec_a_oct(decimal):
    try:
        return oct(decimal)[2:]
    except ValueError:
        return "Error"

def dec_a_bcd(decimal):
    try:
        bcd_num = ""
        while decimal > 0:
            bcd_num = str(decimal % 10) + bcd_num
            decimal //= 10
        return bcd_num 
    except ValueError:
        return "Error"

def bin_a_dec(binario):
    try:
        return int(binario, 2)
    except ValueError:
        return "Error"

def bin_a_hex(binario):
    try:
        return hex(int(binario, 2))[2:]
    except ValueError:
        return "Error"

def bin_a_oct(binario):
    try:
        return oct(int(binario, 2))[2:]
    except ValueError:
        return "Error"

def bin_a_bcd(binario):
    try:
        decimal = int(binario, 2)
        bcd_num = ""
        while decimal > 0:
            bcd_num = str(decimal % 10) + bcd_num
            decimal //= 10
        return bcd_num 
    except ValueError:
        return "Error"

def oct_a_bin(octal):
    try:
        return bin(int(octal, 8))[2:]
    except ValueError:
        return "Error"

def oct_a_dec(octal):
    try:
        return int(octal, 8)
    except ValueError:
        return "Error"
        
def oct_a_bcd(octal):
    try:
        decimal = int(octal, 8)
        bcd_num = ""
        while decimal > 0:
            bcd_num = str(decimal % 10) + bcd_num
            decimal //= 10
        return bcd_num 
    except ValueError:
        return "Error"

def oct_a_hex(octal):
    try:
        return hex(int(octal, 8))[2:]
    except ValueError:
        return "Error"
    
def bcd_a_hexa(bcd):
    try:
        decimal = int(bcd)
        hexa = hex(decimal)[2:]
        return hexa.upper()
    except ValueError:
        return "Error"

def bcd_a_octa(bcd):
    try:
        decimal = int(bcd)
        octal = oct(decimal)[2:]
        return octal
    except ValueError:
        return "Error"

def bcd_a_bin(bcd):
    try:
        decimal = int(bcd)
        binario = bin(decimal)[2:]
        return binario
    except ValueError:
        return "Error"

def bcd_a_dec(bcd):
    try:
        decimal = int(bcd)
        return decimal
    except ValueError:
        return "Error"

print("Opciones de conversión:")
print("1. Hexadecimal a Binario")
print("2. Hexadecimal a Decimal")
print("3. Hexadecimal a Octal")
print("4. Hexadecimal a BCD")
print("5. Decimal a Binario")
print("6. Decimal a Hexadecimal")
print("7. Decimal a Octal")
print("8. Decimal a BCD")
print("9. Binario a Decimal")
print("10. Binario a Hexadecimal")
print("11. Binario a Octal")
print("12. Binario a BCD")
print("13. Octal a Binario")
print("14. Octal a Decimal")
print("15. Octal a BCD")
print("16. Octal a Hexadecimal")
print("17. BCD a Hexadecimal")
print("18. BCD a Octal")
print("19. BCD a Binario")
print("20. BCD a Decimal")

Conversion = int(input("Elige la conversión que quieres realizar: "))

if Conversion == 1:
    numero_hexadecimal = input("Ingresa el número hexadecimal que deseas convertir: ")
    print("Resultado:", hexa_a_bin(numero_hexadecimal))

elif Conversion == 2:
    numero_hexadecimal = input("Ingresa el número hexadecimal que deseas convertir: ")
    print("Resultado:", hexa_a_dec(numero_hexadecimal))

elif Conversion == 3:
    numero_hexadecimal = input("Ingresa el número hexadecimal que deseas convertir: ")
    print("Resultado:", hexa_a_oct(numero_hexadecimal))

elif Conversion == 4:
    numero_hexadecimal = input("Ingresa el número hexadecimal que deseas convertir: ")
    print("Resultado:", hexa_a_bcd(numero_hexadecimal))

elif Conversion == 5:
    numero_decimal = int(input("Ingresa el número decimal que deseas convertir: "))
    print("Resultado:", dec_a_bin(numero_decimal))

elif Conversion == 6:
    numero_decimal = int(input("Ingresa el número decimal que deseas convertir: "))
    print("Resultado:", dec_a_hex(numero_decimal))

elif Conversion == 7:
    numero_decimal = int(input("Ingresa el número decimal que deseas convertir: "))
    print("Resultado:", dec_a_oct(numero_decimal))

elif Conversion == 8:
    numero_decimal = int(input("Ingresa el número decimal que deseas convertir: "))
    print("Resultado:", dec_a_bcd(numero_decimal))

elif Conversion == 9:
    numero_binario = input("Ingresa el número binario que deseas convertir: ")
    print("Resultado:", bin_a_dec(numero_binario))

elif Conversion == 10:
    numero_binario = input("Ingresa el número binario que deseas convertir: ")
    print("Resultado:", bin_a_hex(numero_binario))

elif Conversion == 11:
    numero_binario = input("Ingresa el número binario que deseas convertir: ")
    print("Resultado:", bin_a_oct(numero_binario))

elif Conversion == 12:
    numero_binario = input("Ingresa el número binario que deseas convertir: ")
    print("Resultado:", bin_a_bcd(numero_binario))

elif Conversion == 13:
    numero_octal = input("Ingresa el número octal que deseas convertir: ")
    print("Resultado:", oct_a_bin(numero_octal))

elif Conversion == 14:
    numero_octal = input("Ingresa elnúmero octal que deseas convertir: ")
    print("Resultado:", oct_a_dec(numero_octal))

elif Conversion == 15:
    numero_octal = input("Ingresa el número octal que deseas convertir: ")
    print("Resultado:", oct_a_bcd(numero_octal))

elif Conversion == 16:
    numero_octal = input("Ingresa el número octal que deseas convertir: ")
    print("Resultado:", oct_a_hex(numero_octal))

elif Conversion == 17:
    numero_bcd = input("Ingresa el número BCD que deseas convertir: ")
    print("Resultado:", bcd_a_hexa(numero_bcd))

elif Conversion == 18:
    numero_bcd = input("Ingresa el número BCD que deseas convertir: ")
    print("Resultado:", bcd_a_octa(numero_bcd))

elif Conversion == 19:
    numero_bcd = input("Ingresa el número BCD que deseas convertir: ")
    print("Resultado:", bcd_a_bin(numero_bcd))

elif Conversion == 20:
    numero_bcd = input("Ingresa el número BCD que deseas convertir: ")
    print("Resultado:", bcd_a_dec(numero_bcd))
    
else:
    print("Opción no válida. Por favor, elige una opción válida.")
