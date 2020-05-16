# latihan konversi satuan temperatur

''' Program Konversi Temperatur '''
print("++++++++Program Konversi Temperatur++++++++")
print("1. Celcius")
print("2. Reamur")
print("3. Fahrenheit")
print("4. kelvin")
pilih = int(input("Masukkan pilihan anda = "))
print(" ")

if pilih == 1:
    print("==Celcius==")
    suhu_celcius = float(input("Suhu celcius = "))
    print("Mau diubah ke satuan suhu yang mana ?")
    print("1. Reamur")
    print("2. Fahrenheit")
    print("3. Kelvin")
    pilih = int(input("Pilih = "))
    print(" ")
    if pilih == 1:
        suhu_reamur = (4*suhu_celcius)/5
        print("Suhu reamur = ",suhu_reamur)
    elif pilih == 2:
        suhu_fahrenheit = ((9*suhu_celcius)/5) + 32
        print("Suhu fahrenheit = ",suhu_fahrenheit)
    elif pilih == 3:
        suhu_kelvin = suhu_celcius + 273
        print("Suhu Kelvin = ", suhu_kelvin)

elif pilih == 2:
    print("==Reamur==")
    suhu_reamur = float(input("Suhu Reamur = "))
    print("Mau diubah ke satuan suhu yang mana ?")
    print("1. Celcius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    pilih = int(input("Pilih = "))
    print(" ")
    if pilih == 1:
        suhu_celcius = (5*suhu_reamur)/4
        print("Suhu celcius = ", suhu_celcius)
    elif pilih == 2:
        suhu_fahrenheit = ((9*suhu_reamur)/4) + 32
        print("Suhu fahrenheit = ", suhu_fahrenheit)
    elif pilih == 3:
        suhu_kelvin = ((5*suhu_reamur)/4) + 273
        print("Suhu Kelvin = ", suhu_kelvin)

elif pilih == 3:
    print("==Fahrenheit==")
    suhu_fahrenheit = float(input("Suhu Fahrenheit = "))
    print("Mau diubah ke satuan suhu yang mana ?")
    print("1. Celcius")
    print("2. Reamur")
    print("3. Kelvin")
    pilih = int(input("Pilih = "))
    print(" ")
    if pilih == 1:
        suhu_celcius = ((suhu_fahrenheit - 32)*5)/9
        print("Suhu celcius = ", suhu_celcius)
    elif pilih == 2:
        suhu_reamur = ((suhu_fahrenheit-32)*4)/9
        print("Suhu reamur = ", suhu_reamur)
    elif pilih == 3:
        suhu_kelvin = (((suhu_fahrenheit - 32)*5)/9) + 273
        print("Suhu kelvin = ", suhu_kelvin)

elif pilih == 4:
    print("==Kelvin==")
    suhu_kelvin = float(input("Suhu Kelvin = "))
    print("Mau diubah ke satuan suhu yang mana ?")
    print("1. Celcius")
    print("2. Reamur")
    print("3. Fahrenheit")
    pilih = int(input("Pilih = "))
    print(" ")
    if pilih == 1:
        suhu_celcius = suhu_kelvin - 273 
        print("Suhu celcius = ", suhu_celcius)
    elif pilih == 2:
        suhu_reamur = ((suhu_kelvin - 273)*4)/5
        print("Suhu reamur = ", suhu_reamur)        
    elif pilih == 3:
        suhu_fahrenheit = (((suhu_kelvin-273)*9)/5) + 32
        print("Suhu fahrenheit = ", suhu_fahrenheit)        