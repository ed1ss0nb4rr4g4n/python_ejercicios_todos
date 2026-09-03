while True:
    edad=int(input("Digite la edad de una persona: "))
    if edad<0:
        print("La edad no puede ser negativa")
        continue
    if edad>=0:
        categoria="Niño"
    elif edad>=13:
        categoria="Adolescente"   
    elif edad>=18 and edad<=59:
        categoria="Adulto"
    else:
        categoria="Adulto mayor"

    print (f"La persona es un: {categoria}")
    break
