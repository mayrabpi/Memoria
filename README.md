# 🎮 Juego de Memoria en Python

Un juego de memoria interactivo implementado en Python, donde los jugadores deben encontrar pares de cartas coincidentes. El juego soporta múltiples modos de juego y utiliza emojis como símbolos para las cartas.

## 📝 Descripción

Este juego de memoria es una implementación en consola que permite a los jugadores encontrar pares de cartas coincidentes en un tablero personalizable. El juego incluye tres modos diferentes de juego y utiliza emojis para hacer la experiencia más visual y entretenida.

## 🎯 Características

- **Múltiples Modos de Juego:**
  - 👥 Jugador vs Jugador
  - 🤖 Jugador vs Máquina
  - 🤖 Máquina vs Máquina

- **Tablero Personalizable:**
  - Tamaño mínimo: 2x2
  - Tamaño máximo: 6x5
  - Validación automática para asegurar un número par de casillas

- **Características del Juego:**
  - Sistema de puntuación
  - Seguimiento de parejas encontradas
  - Interfaz visual con emojis
  - Sistema de turnos
  - Validación de movimientos



## 🚀 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/[mayrabpi]/juego-memoria-python.git
```

2. Navega al directorio del proyecto:
```bash
cd juego-memoria-python
```

3. Ejecuta el juego:
```bash
python main.py
```

## 🎮 Cómo Jugar

1. Al iniciar el juego, selecciona uno de los tres modos de juego disponibles.
2. Configura el tamaño del tablero (entre 2x2 y 6x5).
3. En tu turno:
   - Selecciona la primera carta ingresando sus coordenadas (fila y columna)
   - Selecciona la segunda carta de la misma manera
   - Si las cartas coinciden, ¡obtienes un punto!
   - Si no coinciden, las cartas se voltean y pasa el turno
4. El juego continúa hasta que se encuentran todos los pares.

## 🏗️ Estructura del Proyecto

```
juego-memoria/
│
├── main.py                 # Archivo principal del juego
├── README.md              # Documentación del proyecto
│
└── classes/               # Módulos del juego
    ├── jugador.py        # Clase base para los jugadores
    ├── jugador_maquina.py # Implementación de la IA
    ├── tablero.py        # Lógica del tablero de juego
    └── juego_memoria.py  # Controlador principal del juego
```

## 🤖 Implementación de la IA

Modo juega la máquina:

 1. **Modo Simple:**
   - Selección aleatoria de cartas
   - No mantiene memoria de jugadas anteriores
   - Ideal para jugadores principiantes

## 🛠️ Requisitos Técnicos

- Python 3.6 o superior
- Sistema operativo compatible (Windows/Linux/MacOS)
- Terminal que soporte emojis UTF-8

## 📈 Futuras Mejoras
- [ ] Jugo Modo con memoria de la máquina
- [ ] Más modos de juego
- [ ] Sistema de niveles de dificultad
- [ ] Guardar puntuaciones máximas
- [ ] Modo multijugador en red
- [ ] Temas personalizables


## 👥 Autor

[Mayra]
- GitHub: [https://github.com/mayrabpi](https://github.com/tu-usuario)
- LinkedIn: [https://www.linkedin.com/in/mayrabpi/](https://linkedin.com/in/tu-perfil)

## 🙏 Agradecimientos

- A la comunidad de Python por las herramientas y recursos
- A todos los que han contribuido con sugerencias y mejoras
- A los testers que han ayudado a mejorar el juego

