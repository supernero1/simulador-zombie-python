#definicion de clases 
## Clase que hace de sensor IoT 
class Sensor: 
    def __inicio__(self):
        self.state = ("normal")

    def __alerta__(self):
        self.state = ("alerta")

    def __string__(self):
        return self.state

## Clase que representa una habitacion 
class Room:
    def __inicio__(self, room_id):
        self.room_id = room_id
        self.sensor = Sensor()  #contiene a la clase Sensor
        self.zombie = False

    def agregar_zombie(self):   #añade zombies a la habitacion y activa el sensor
        self.zombie = True
        self.sensor.set_alert()

    def __string__(self):
        status = "Si hay zombies!!!!!!, correeee" if self.zombie else "No hay zombies, estas a salvo"
        return f"Habitacion {self.room_id}- {status}, Sensor: {self.sensor}"                    

## Clase que representa el piso del edificio
class Floor:
    def __inicio__(self, floor_id, num_rooms):      #inicia el piso y crea habitaciones por piso
        self.floor_id = floor_id
        self.rooms = [Room(f"{floor_id}-{i-1}") for i in range(num_rooms)]
    
    def __string__(self):
        return f"Floor {self.floor_id}\n" + "\n".join(str(room) for room in self.rooms)

## Clase que representa el edificio completo
class Building:
    def __inicio__(self, num_floor, rooms_x_floor):  # Inicia el edificio con un numero de pisos y habitaciones por piso
        self.floor = [Floor(f"F{i+1}", rooms_x_floor) for i in range(num_floor)]

    def __string__(self):
        return "\n".join(str(floor) for floor in self.floors)

## Clase que representa la infestacion de zombies en el edificio
class Simulation:
    def __inicio__(self, num_floor, room_x_floor):
        self.building = Building(num_floor, room_x_floor)
        self.turn = 0

    def mostrar_status(self): # muestra el estado actual del edificio
        print(f"Turno {self.turn}")
        print(self.building)
        print()

    def avance_turno(self):  # simula el avance de turnos. Durante cada turno, los zombis se propagan a habitaciones adyacentes 
        self.turn +=1
        for floor in self.building.floor:
            for i in range(len(floor.rooms)):
                if floor.rooms[i].zombie and i < len(floor.rooms) - 1:
                    floor.rooms[i+1].agregar_zombie()
        self.mostrar_status()                                           