# intMyNumber = int(input("Ingrese un numero: "))
# intEdad = int(input("Ingrese su edad: "))
# if intMyNumber > intEdad:    
    # print("El numero " + str(intMyNumber) + " es mayor a su edad")
# else:
    # print("El numero " + str(intMyNumber) + " es menor a su edad")
# number1 = int(input("Ingrese el primer numero: "))
# number2 = int(input("Ingrese el segundo numero: "))
# # number3 = int(input("Ingrese el tercer numero: "))
# if number1 > number2 and number1 > number3:
#     print("El numero " + str(number1) + " es el mayor.") 
# elif number2 < number1 and number2 < number3:
#     print("El numero " + str(number2) + " es el mayor")
# else:
#     print("El numero " + str(number3) +  " es el mayor")
# for i in range(5):
    # print( str(i) + " si funciona :3")
# average = 0
# name = input("Ingrese su nombre: ")
# # for i in range(5):
# #     average += float(input(f"{name} ingrese la nota numero {(i + 1)}: "))
# # print(f"El promedio de {name} es: {average/5}")
# count = 1
# while count < 6:
#     average += float(input(f"{name} ingrese la nota numero {count}: "))
#     count+=1

# print(f"El promedio de {name} es: {average/5}")

# mArray = []
# mArray.append(1)
# mArray.append(1)
# mArray.append(1)
# mArray.append(1)
# mArray.append(1)
# mArray.append(1) #6
# print(str(len(mArray)))

# mArray = ["P", "A", "B", "L", "O", 0, 8, 1, 3]
# print(mArray)
# mArray.remove(8)
# print(mArray)

# mTupla = (1,2,3,4,5,6,7,8)
# print(mTupla)

# mString = "mensaje"
# print(len(mString))

# mDictionary = {
#     "id": 1,
#     "message": "mensaje",
#     "status": True,
#     "numbers": [1, 2, 3]
# }

# print(mDictionary["numbers"][1])

# data = []

# while True:
#     name = (input("Ingrese el nombre del estudiante a evaluar: "))
#     number = 0;
#     for i in range(1, 6):
#         number += int(input(f"Ingrese la nota {i} del estudiante {data[len(data)-1]['name']}: "))
#     number = number/5
#     data.append({"name": name, "grades": number})
#     end = ""
#     while True:
#         end = input("Desea finalizar el programa? [S/N]: ")
#         if end == "S" or end == "N" or end == "s" or end == "n":
#             break
#     if end == "S":
#         break

# for i in range(len(data)):
#     print(f"{i + 1}: El estudiante {data[i]['name']} obtuvo: {data[i]['grades']}")