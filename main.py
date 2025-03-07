import random


# Definición de clases

## Clase que hace de sensor IoT
class Sensor:
    def __init__(self):
        self.state = "normal"

    def set_alert(self):
        self.state = "alerta"

    def __str__(self):
        return self.state


## Clase que representa una habitación
class Room:
    def __init__(self, room_id):
        self.room_id = room_id
        self.sensor = Sensor()  # Contiene a la clase Sensor
        self.zombie = False

    def agregar_zombie(self):  # Añade zombies a la habitación y activa el sensor
        if not self.zombie:  # Solo agregar zombis si no los hay ya
            self.zombie = True
            self.sensor.set_alert()

    def __str__(self):
        status = "Si hay zombies!!!!!!, correeee" if self.zombie else "No hay zombies, estás a salvo"
        return f"Habitación {self.room_id} - {status}, Sensor: {self.sensor}"


## Clase que representa el piso del edificio
class Floor:
    def __init__(self, floor_id, num_rooms):
        self.floor_id = floor_id
        self.rooms = [Room(f"{floor_id}-{i+1}") for i in range(num_rooms)]

    def __str__(self):
        return f"Piso {self.floor_id}\n" + "\n".join(str(room) for room in self.rooms)


## Clase que representa el edificio completo
class Building:
    def __init__(self, num_floors, rooms_x_floor):
        self.floors = [Floor(f"P{i+1}", rooms_x_floor) for i in range(num_floors)]
        # Infectar una habitación aleatoria con zombies
        self.infectar_habitacion_aleatoria()

    def infectar_habitacion_aleatoria(self):
        # Seleccionar un piso y una habitación al azar
        piso_aleatorio = random.choice(self.floors)
        habitacion_aleatoria = random.choice(piso_aleatorio.rooms)
        habitacion_aleatoria.agregar_zombie()

    def __str__(self):
        return "\n".join(str(floor) for floor in self.floors)

## Clase que representa la infestación de zombies en el edificio
class Simulation:
    def __init__(self, num_floors, rooms_x_floor):
        self.building = Building(num_floors, rooms_x_floor)
        self.turn = 0

    def mostrar_status(self):  # Muestra el estado actual del edificio
        print(f"\nTurno {self.turn}\n")
        print(self.building)
        print()

    def avance_turno(self):  # Simula el avance de turnos. Durante cada turno, los zombies se propagan a habitaciones adyacentes
        self.turn += 1
        for floor in self.building.floors:
            for i, room in enumerate(floor.rooms):
                if room.zombie:
                    # Elegir una dirección aleatoria para propagar (izquierda, derecha, arriba, abajo)
                    direccion = random.choice(["izquierda", "derecha", "arriba", "abajo"])
                    if direccion == "izquierda" and i > 0:
                        floor.rooms[i - 1].agregar_zombie()
                    elif direccion == "derecha" and i < len(floor.rooms) - 1:
                        floor.rooms[i + 1].agregar_zombie()
                    elif direccion == "arriba" and floor.floor_id != "F1":  # No propagar arriba en el primer piso
                        piso_anterior = self.building.floors[self.building.floors.index(floor) - 1]
                        piso_anterior.rooms[i].agregar_zombie()
                    elif direccion == "abajo" and floor.floor_id != f"F{len(self.building.floors)}":  # No propagar abajo en el último piso
                        piso_siguiente = self.building.floors[self.building.floors.index(floor) + 1]
                        piso_siguiente.rooms[i].agregar_zombie()
        self.mostrar_status()


def main():
    num_floors = int(input("Ingresa el número de pisos: "))
    hab_x_pisos = int(input("Ingresa el número de habitaciones por piso: "))
    simulation = Simulation(num_floors, hab_x_pisos)

    while True:
        print("\n **********************************")
        print("1. Mostrar status                 *")
        print("2. Avanzar turno                  *")
        print("3. Salir                          *")
        print(" **********************************")
        choice = input("Elige una opción: ")

        if choice == "1":
            simulation.mostrar_status()
        elif choice == "2":
            simulation.avance_turno()
        elif choice == "3":
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()