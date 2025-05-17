# # --------------------------YAMILA (PARTE 1/3)------------------------------------------------------
import random

palabras = ["manzana", "bicicleta", "guitarra", "elefante", "montaña", "pelota"]

def jugar(): 
    # Mostrar integrantes
    try:
        with open("integrantes.txt", "r", encoding="utf-8") as archivo:
            print("\n⭐⭐⭐ INTEGRANTES DEL GRUPO ⭐⭐⭐")
            print(archivo.read())
    except FileNotFoundError:
        print("⚠️ No se encontró el archivo 'integrantes.txt'.")

    palabra = random.choice(palabras)
    letras_adivinadas = []
    letras_incorrectas = []
    vidas = 6
    jugando = True

    print("\n🎮 ¡Bienvenidos al juego Adivina la palabra!")
    print(f"La palabra tiene {len(palabra)} letras. Podés ingresar una letra o arriesgar la palabra completa.\n")
    
# # --------------------------BELEN (PARTE 2/3)
    while jugando:
        mostrar = ""
        for letra in palabra:
            if letra in letras_adivinadas:
                mostrar += letra + " "
            else:
                mostrar += "_ "

        print("\nPalabra:", mostrar.strip())
        print("Vidas restantes:", vidas)
        print("Letras incorrectas:", ", ".join(letras_incorrectas))

        entrada = input("➡️ Ingresá una letra o la palabra completa (o escribí 'salir' para rendirte): ").lower()

        if entrada == "salir":
            print(f"\n🫡 Te diste por vencido. La palabra era: {palabra}")
            break
# --------------------------VILMA (PARTE 3/3)-------------------------------------------------------
        if len(entrada) > 1:
            if entrada == palabra:
                print(f"\n🎉 ¡Increíble! Adivinaste la palabra completa: {palabra}")
                break
            else:
                print("❌ Esa no es la palabra. Perdés 2 vidas.")
                vidas -= 2
                if vidas <= 0:
                    print(f"\n💀 Te quedaste sin vidas. La palabra era: {palabra}")
                    break
                continue

        if len(entrada) != 1:
            print("⚠️ Solo podés ingresar **una letra** o arriesgar toda la palabra.")
            continue
        if not entrada.isalpha():
            print("⚠️ Solo se permiten letras.")
            continue
        if entrada in letras_adivinadas or entrada in letras_incorrectas:
            print("❗ Ya usaste esa letra. Probá con otra.")
            continue

        if entrada in palabra:
            print("✅ ¡Bien! La letra está en la palabra.")
            letras_adivinadas.append(entrada)
        else:
            print("❌ Esa letra no está.")
            letras_incorrectas.append(entrada)
            vidas -= 1

        if all(letra in letras_adivinadas for letra in palabra):
            print(f"\n🎉 ¡Felicidades! Adivinaste la palabra: {palabra}")
            break
        if vidas <= 0:
            print(f"\n💀 Te quedaste sin vidas. La palabra era: {palabra}")
            break

    respuesta = input("\n¿Querés jugar otra vez? (s/n): ").lower()
    if respuesta == "s":
        jugar()
    else:
        print("👋 Gracias por jugar. ¡Nos vemos!")
        
jugar()  
