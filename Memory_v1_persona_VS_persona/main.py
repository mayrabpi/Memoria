from juegoMemoria import JuegoMemoria
from start import Start
while True:
        Start.limpiar_pantalla()
        opcion = Start.mostrar_menu_principal()
        
        if opcion == 3:
            print("\n¡Gracias por jugar!")
            break
        
        juego = JuegoMemoria(opcion)
        juego.jugar()
        
        input("\nPresione Enter para volver al menú principal...")
    