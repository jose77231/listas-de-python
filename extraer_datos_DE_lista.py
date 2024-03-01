lista2 = ["pantalla", "teclado", "bocinas", "mouse", "usb", "cd", "quemador", "impresora", "microfono", "webcam"]

# 1. Extraer 'mouse', 'usb', 'cd', 'quemador', 'impresora' con indices
sublista_1 = lista2[3:8]
print("1. ", sublista_1)

# 2. Extraer 'mouse', 'usb', 'cd', 'quemador', 'impresora', 'microfono', 'webcam'
sublista_2 = lista2[3:]
print("2. ", sublista_2)

# 3. Extraer 'pantalla', 'teclado', 'bocinas', 'mouse', 'usb', 'cd', 'quemador', 'impresora'
sublista_3 = lista2[:8]
print("3. ", sublista_3)

# 4. Extraer 'pantalla', 'bocinas', 'usb', 'quemador', 'microfono'
sublista_4 = [lista2[0], lista2[2], lista2[4], lista2[6], lista2[8]]
print("4. ", sublista_4)

# 5. Programar para extraer de lista2, la sublista equipo = ['mouse', 'cd', 'microfono', 'cargador'] , que aparezca sú número de índice de cada uno
equipo = ['mouse', 'cd', 'microfono', 'cargador']
for elemento in equipo:
    if elemento in lista2:
        print("Indice", lista2.index(elemento), ":", elemento)
    else:
        print(elemento, "NO encontrado en lista2")
