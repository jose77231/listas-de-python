cadenaLarga = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce velit metus, bibendum et dolor ac, sollicitudin commodo metus. Etiam ut vehicula metus, quis venenatis dui. Praesent quis fermentum leo, vel sollicitudin elit. Fusce in est non ligula accumsan ornare. Donec tincidunt lobortis tellus fermentum rhoncus. Sed pulvinar auctor tellus in dignissim. Ut sagittis eleifend felis, id rhoncus felis. Aliquam erat volutpat. Vestibulum interdum nunc elementum est pharetra imperdiet.

Fusce velit leo, imperdiet in elit sed, vehicula aliquam ligula. Etiam convallis sem id accumsan finibus. Nulla eget augue congue, fermentum ligula eu, volutpat nisl. Maecenas a varius ante. Praesent dignissim nulla rutrum lorem congue aliquet vel congue augue. Proin posuere ex et diam ullamcorper, non venenatis odio viverra. Vivamus nec ultricies felis. Etiam facilisis tortor eget justo posuere, non posuere metus sollicitudin.

Nulla tempor neque a arcu posuere tincidunt. Curabitur iaculis velit sed luctus accumsan. In vel imperdiet turpis. Proin dolor velit, accumsan eget nunc ut, tempus varius eros. Nam semper sollicitudin orci. Donec a faucibus metus. Aliquam ut felis imperdiet, eleifend est blandit, tristique tellus. Nam consequat nisi mattis pretium venenatis. Curabitur viverra viverra magna, ac consectetur ligula commodo nec.

Morbi bibendum a tellus vel lobortis. Sed vitae velit tortor. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod purus id quam dapibus semper. Integer mauris massa, sollicitudin eu lacinia ut, volutpat eget ante. Donec nec mollis est, id dictum justo. Sed elementum tempor massa. In id sapien id turpis tristique tempor at nec sem. Nullam et enim neque. Nam eget malesuada nisi, eu condimentum ligula. Vestibulum sit amet porta lorem.

Praesent at arcu arcu. Proin ac mi at risus bibendum tempus. Phasellus sit amet libero eu est mattis sagittis. Cras sagittis lobortis nunc, in condimentum est volutpat ut. Curabitur nec magna volutpat, venenatis enim et, molestie lectus. Sed fringilla nulla at tempus porta. Etiam tristique neque non dui maximus, vitae interdum ante faucibus. Curabitur libero metus, lobortis nec libero a, tempus commodo leo. Sed lobortis magna enim. Sed non magna semper, ultricies ex in, placerat diam. Sed mattis gravida fringilla. Aliquam erat volutpat.
"""

caracteres = ['a', 'e', 'i', 'o', 'u', ' ', ',','.']

# Definir una función para contar caracteres
def contar_caracteres(parrafo):
    total_caracteres = len(parrafo)
    total_letras = sum(parrafo.count(caracter) for caracter in caracteres[:-2]) # Excluyendo espacios y comas
    total_vocales = sum(parrafo.count(vocal) for vocal in caracteres[:-2])
    total_espacios = parrafo.count(' ')
    total_comas = parrafo.count(',')
    total_puntos = parrafo.count('.')

    # Conteo de vocales individuales
    total_vocales_a = parrafo.count('a')
    total_vocales_e = parrafo.count('e')
    total_vocales_i = parrafo.count('i')
    total_vocales_o = parrafo.count('o')
    total_vocales_u = parrafo.count('u')

    # Imprimir estadísticas del párrafo
    print("Total de caracteres:", total_caracteres)
    print("Total de letras (incluyendo vocales):", total_letras)
    print("Total de vocales:", total_vocales)
    print("Total de vocales a:", total_vocales_a)
    print("Total de vocales e:", total_vocales_e)
    print("Total de vocales i:", total_vocales_i)
    print("Total de vocales o:", total_vocales_o)
    print("Total de vocales u:", total_vocales_u)
    print("Total de espacios:", total_espacios)
    print("Total de comas:", total_comas)
    print("Total de puntos:", total_puntos)
    print("Total de palabras:", len(parrafo.split()))

# Separar la cadena en párrafos
parrafos = cadenaLarga.split('\n\n')

# Iterar sobre los párrafos y calcular estadísticas
for i, parrafo in enumerate(parrafos, start=1):
    print("Párrafo", i, ":")
    contar_caracteres(parrafo)
    print()
