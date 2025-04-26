import random
import time
from collections import OrderedDict

# Configuración del juego
PERSONAJES = OrderedDict([
    ("Dra. Elena Rojas", "Médico forense"),
    ("Prof. Carlos Mendoza", "Catedrático de historia"),
    ("Ing. Laura Vélez", "Ingeniera de software"),
    ("Sr. Antonio Cruz", "Magnate inmobiliario"),
    ("Sra. Isabel Fuentes", "Dueña de galería de arte")
])

LOCACIONES = [
    "Biblioteca",
    "Invernadero",
    "Sala de billar",
    "Observatorio",
    "Cocina profesional"
]

ARMAS = [
    "Candelabro de plata",
    "Cuerda de seda",
    "Revólver antiguo",
    "Tubo de plomo",
    "Veneno exótico"
]

# Historias del juego
HISTORIAS = {
    1: {
        "titulo": "El Misterio del Candelabro Perdido",
        "introduccion": "Durante la cena anual de la Sociedad Histórica, en medio de un apagón, " +
                       "se escuchó un grito desgarrador. Cuando las luces volvieron, el " +
                       "Director del Museo yacía muerto en la biblioteca.",
        "pistas": [
            "Hay huellas de barro que llevan hacia la sección de botánica",
            "El candelabro que iluminaba la habitación ha desaparecido",
            "Se encontró un pañuelo con iniciales bordadas cerca del cuerpo"
        ],
        "culpable": "Prof. Carlos Mendoza",
        "arma": "Candelabro de plata",
        "locacion": "Biblioteca",
        "motivo": "El profesor descubrió que el director planeaba vender artefactos históricos en el mercado negro"
    },
    
    2: {
        "titulo": "Veneno entre las Rosas",
        "introduccion": "Durante la exhibición de flores exóticas en el invernadero, " +
                       "la famosa botánica Dra. Hernández colapsó repentinamente. " +
                       "El examen preliminar sugiere envenenamiento.",
        "pistas": [
            "Se encontró un frasco vacío de un raro veneno vegetal",
            "Las huellas digitales en el vaso de la víctima fueron borradas",
            "Había una nota amenazante escondida entre las plantas"
        ],
        "culpable": "Sra. Isabel Fuentes",
        "arma": "Veneno exótico",
        "locacion": "Invernadero",
        "motivo": "La víctima iba a exponer el plagio de sus investigaciones sobre especies raras"
    },
    
    3: {
        "titulo": "Silencio en la Sala de Billar",
        "introduccion": "El torneo anual de billar terminó en tragedia cuando el campeón " +
                       "fue encontrado muerto en la sala de billar, con un golpe fatal en la cabeza.",
        "pistas": [
            "El trofeo del torneo está manchado con sangre",
            "Se escuchó una fuerte discusión minutos antes del incidente",
            "El reloj de la víctima se detuvo a las 9:15 pm"
        ],
        "culpable": "Sr. Antonio Cruz",
        "arma": "Tubo de plomo",
        "locacion": "Sala de billar",
        "motivo": "La víctima tenía pruebas de sus negocios ilegales con propiedades"
    },
    
    4: {
        "titulo": "El Secreto del Observatorio",
        "introduccion": "Durante la observación del eclipse lunar, el astrónomo jefe fue " +
                       "encontrado muerto en el observatorio, estrangulado con un fino hilo.",
        "pistas": [
            "El diario de investigación de la víctima tiene páginas arrancadas",
            "Se encontró un pendrive escondido en el telescopio",
            "El reloj astronómico fue manipulado para detenerse a una hora específica"
        ],
        "culpable": "Ing. Laura Vélez",
        "arma": "Cuerda de seda",
        "locacion": "Observatorio",
        "motivo": "La víctima descubrió que había hackeado el sistema de satélites gubernamentales"
    },
    
    5: {
        "titulo": "Muerte entre Sabores",
        "introduccion": "Durante la grabación del famoso programa de cocina 'Sabores Exquisitos', " +
                       "el chef invitado murió repentinamente después de probar su propia creación.",
        "pistas": [
            "El análisis muestra cianuro en los ingredientes",
            "La receta original fue alterada",
            "Las cámaras de seguridad fueron saboteadas durante el incidente"
        ],
        "culpable": "Dra. Elena Rojas",
        "arma": "Revólver antiguo",
        "locacion": "Cocina profesional",
        "motivo": "La víctima había descubierto su esquema de tráfico de medicamentos"
    }
}

def mostrar_personajes():
    print("\n🔍 Personajes sospechosos:")
    for i, (nombre, profesion) in enumerate(PERSONAJES.items(), 1):
        print(f"{i}. {nombre} - {profesion}")

def mostrar_menu_investigacion(pistas_descubiertas, pistas_totales):
    print("\n¿Qué deseas hacer?")
    print("1. Investigar otra pista")
    print("2. Hacer una acusación")
    print("3. Ver personajes sospechosos")
    print("4. Ver pistas descubiertas")
    
    if len(pistas_descubiertas) < pistas_totales:
        print(f"\nPistas disponibles: {len(pistas_descubiertas)}/{pistas_totales}")
    else:
        print("\n¡Has descubierto todas las pistas!")

def jugar_partida():
    # Seleccionar historia aleatoria
    historia_num = random.randint(1, 5)
    historia = HISTORIAS[historia_num]
    
    print(f"\n{'='*50}")
    print(f"CASO: {historia['titulo']}")
    print(f"{'='*50}\n")
    
    # Mostrar introducción
    print(historia['introduccion'])
    print("\nTu misión es descubrir al culpable, el arma y la locación del crimen.")
    
    # Preparar variables del juego
    pistas_descubiertas = []
    personajes_disponibles = list(PERSONAJES.keys())
    pistas_restantes = historia['pistas'].copy()
    
    while True:
        mostrar_menu_investigacion(pistas_descubiertas, len(historia['pistas']))
        
        opcion = input("\nElige una opción (1-4): ")
        
        if opcion == "1":  # Investigar pista
            if pistas_restantes:
                pista = pistas_restantes.pop(0)
                pistas_descubiertas.append(pista)
                print(f"\n🔎 Nueva pista: {pista}")
                time.sleep(2)
            else:
                print("\n¡No hay más pistas por descubrir!")
                time.sleep(1)
                
        elif opcion == "2":  # Hacer acusación
            print("\n💀 REALIZAR ACUSACIÓN")
            
            # Seleccionar personaje
            mostrar_personajes()
            try:
                num_personaje = int(input("\nNúmero del personaje culpable: ")) - 1
                personaje = list(PERSONAJES.keys())[num_personaje]
            except (ValueError, IndexError):
                print("Selección inválida. Intenta de nuevo.")
                continue
                
            # Seleccionar arma
            print("\n🛠 Armas posibles:")
            for i, arma in enumerate(ARMAS, 1):
                print(f"{i}. {arma}")
                
            try:
                num_arma = int(input("\nNúmero del arma utilizada: ")) - 1
                arma = ARMAS[num_arma]
            except (ValueError, IndexError):
                print("Selección inválida. Intenta de nuevo.")
                continue
                
            # Seleccionar locación
            print("\n🏠 Locaciones posibles:")
            for i, locacion in enumerate(LOCACIONES, 1):
                print(f"{i}. {locacion}")
                
            try:
                num_locacion = int(input("\nNúmero de la locación del crimen: ")) - 1
                locacion = LOCACIONES[num_locacion]
            except (ValueError, IndexError):
                print("Selección inválida. Intenta de nuevo.")
                continue
                
            # Verificar acusación
            if (personaje == historia['culpable'] and 
                arma == historia['arma'] and 
                locacion == historia['locacion']):
                
                print(f"\n{'='*50}")
                print("¡FELICIDADES! 🎉")
                print("Has resuelto el misterio correctamente.")
                print(f"\nEl culpable era {historia['culpable']}")
                print(f"Utilizó {historia['arma']} en {historia['locacion']}")
                print(f"\nMotivo: {historia['motivo']}")
                print(f"{'='*50}")
                break
            else:
                print("\n❌ Acusación incorrecta.")
                
                # Eliminar personaje incorrecto de sospechosos
                if personaje in personajes_disponibles:
                    personajes_disponibles.remove(personaje)
                    print(f"\n{personaje} ha sido eliminado de los sospechosos.")
                
                if not personajes_disponibles:
                    print("\n¡Te has quedado sin sospechosos!")
                    print(f"\nLa solución era: {historia['culpable']} con {historia['arma']} en {historia['locacion']}")
                    break
                
        elif opcion == "3":  # Ver personajes
            mostrar_personajes()
            input("\nPresiona Enter para continuar...")
            
        elif opcion == "4":  # Ver pistas descubiertas
            if pistas_descubiertas:
                print("\n🔍 Pistas descubiertas:")
                for i, pista in enumerate(pistas_descubiertas, 1):
                    print(f"{i}. {pista}")
            else:
                print("\nAún no has descubierto ninguna pista.")
            input("\nPresiona Enter para continuar...")
            
        else:
            print("Opción inválida. Por favor elige 1-4.")

def main():
    print("""
    ====================================
    🕵️♂️ BIENVENIDO AL SIMULADOR CLUE 🕵️♀️
    ====================================
    
    Un juego de misterio y deducción donde
    debes descubrir al culpable de un crimen
    basado en pistas y tu razonamiento.
    """)
    
    while True:
        jugar_partida()
        
        continuar = input("\n¿Quieres jugar otra partida? (s/n): ").lower()
        if continuar != 's':
            print("\n¡Gracias por jugar! Hasta la próxima investigación.")
            break

if __name__ == "__main__":
    main()
