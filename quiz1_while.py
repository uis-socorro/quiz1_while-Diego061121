# Input 

C1 = int(input("Valor del capital 1: "))
C2 = int(input("Valor del capital 2: "))
C3 = int(input("Valor del capital 3: "))
meses = 0 

# Processing 

while C3 > C1 + C2: 
    C1 = C1 + (C1 * 0.03)
    c2 = C2 * 0.04 
    C2 = C2 + c2 
    meses =  meses + 1 

# Output 

print("El numero de meses para que el capital sea el necesario es: ", meses)


