#definicion de clases 

class Sensor:
    def __inicio__(self):
        self.state = ("normal")

    def __alerta__(self):
        self.state = ("alerta")

    def __string__(self):
        return self.state

class Room:
    def __inicio__(self, room_id):
        self.room_id = room_id
        self.sensor = Sensor()
        self.zombie = False

    def agregar_zombie(self):
        self.zombie = True
        self.sensor.set_alert()

    def __string__(self):
        status = "Si hay zombies!!!!!!, correeee" if self.zombie else "No hay zombies, estas a salvo"
        return f"Habitacion {self.room_id}- {status}, Sensor: {self.sensor}"                    
