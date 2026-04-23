from room_sensor import RoomSensor
from room_sensor import TemperatureSensor, LightSensor, HumiditySensor  # assuming this exists

temp_sensor = TemperatureSensor("Temp1")
humidity_sensor = HumiditySensor("Hum1")
light_sensor = LightSensor("Light1")

kitchen = RoomSensor(
    "Kitchen",
    temp_sensor.read(),
    humidity_sensor.read(),
    light_sensor.read()
)

bedroom = RoomSensor(
    "Bedroom",
    temp_sensor.read(),
    humidity_sensor.read(),
    light_sensor.read()
)

balcony = RoomSensor(
    "Balcony",
    temp_sensor.read(),
    humidity_sensor.read(),
    light_sensor.read()
)

rooms = [kitchen, bedroom, balcony]

comfortable = 0
normal = 0
warning = 0

for room in rooms:
    room.show_info()

    c = room.comfort_level()
    l = room.light_status()

    print(f"Comfort Level: {c}")
    print(f"Light Status: {l}")
    print()

    if c == "Comfortable":
        comfortable += 1
    elif c == "Normal":
        normal += 1
    else:
        warning += 1
print("Summary:")
print(f"Comfortable: {comfortable}")
print(f"Normal: {normal}")
print(f"Warning: {warning}")
#took help from a "FRIEND"
