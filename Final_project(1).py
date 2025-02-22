class Device:
    def __init__(self,topic,pin=None):
        self.topic=topic
        self.topic_list=self.topic.split('/')
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.name=self.topic_list[3]
        self.status='off'
        self.pin=pin
    def turn_on(self):
        self.status='on'
        print('turned on successfully ')
    def turn_off(self):
        self.status='off'
        print('turned off successfully ')
    def get_status(self):
        return self.status
import numpy as np
class Sensor:
    def __init__(self,name,group,unit,pin):
        self.name=name
        self.group=group
        self.pin=pin
        self.unit=unit
        self.current_value=None
    def read_sensor(self):
        return np.random.uniform(20,25)

class admin_panel():
    def __init__(self):
        self.groups={}
    def create_group(self,group_name):
        if group_name not in self.groups:
            self.groups[group_name]=[]
            print(f'Group "{group_name}" is created successfully ')
        else:
            print('your name is dublicated')
    def add_device_to_group(self,group_name,device):
        if group_name in self.groups:
            self.groups[group_name].append(device)
            print(f'device {device.name} added in group {group_name} successfully ')
        else:
            print(f' group {group_name} not found')
    def create_device(self,group_name,device_type,name):
        if group_name in self.groups:
            topic=f'home/{group_name}/{device_type}/{name}'
            new_device=Device(topic)
            self.add_device_to_group(group_name, new_device)
            print(f'device {name} ({device_type}) is created in group {group_name} successfully')
        else:
            print(f'your group {group_name} is dublicated')
    def create_multiple_devices(self,group_name,device_type,number_of_devcies):
        if group_name in self.groups:
            for i in range(1,number_of_devcies+1):
                device_name=f'{device_type}{i}'
                topic=f'home/{group_name}/{device_type}/{device_name}'
                new_device=Device(topic)
                self.add_device_to_group(group_name, new_device)
                print(f'device {device_name} {device_type} added to group {group_name} successfully')
        else:
            print(f'group {group_name} does not exist')
    def get_devices_in_groups(self,group_name):
        if group_name in self.groups:
            return self.groups[group_name]
        else:
            print(f'group {group_name} does not exist')
    def turn_on_all_in_groups(self,group_name):
        devices=self.get_devices_in_groups(group_name) 
        for device in devices:
            device.turn_on()
            print(f'all devices in group {group_name} are turned on successfully')
    def turn_off_all_in_groups(self,group_name):
        devises=self.get_devices_in_groups(group_name)
        for devise in devises:
            devise.turn_off()
            print(f'all devices in group {group_name} are turned off successfully')
    def turn_on_all_devices(self):
        for devices in self.groups.values():
            all_devices=[]
            all_devices.extend(devices)
        for i in all_devices:
            i.turn_on()
        print('all devices turned on successfully') 
    def turn_off_all_devices(self):
        for devices in self.groups.values():
            all_devices=[]
            all_devices.extend(devices)
        for i in all_devices:
            i.turn_off()
        print('all devices turned off successfully')
    def get_status_in_group(self,group_name):
        if group_name in self.groups:
         devices = self.groups[group_name]
         for i in devices:
            print('status of device is:',i.status)
        else:
         print('sorry group not found')
    def get_status_in_device_type(self,device_type):
        devices=[]
        for i in self.groups.values():
            devices.extend(i)
            for i in devices:
                if isinstance(i,Device) and i.device_type == device_type:
                    print(f'{i.name} in {i.group} is : {i.status}')
                else:
                    print(f'{device_type} not found')
    def create_sensor(self,name,group_name,unit,pin=None):
        if group_name in self.groups:
            new_sensor=Sensor(group_name,name,unit,pin)
            self.add_sensor_in_group(group_name, new_sensor)
            print(f'sensor {name} is created in group {group_name} successfully')
        else:
            print(f' group {group_name} not found')
    def add_sensor_in_group(self,group_name,sensor):
        if group_name in self.groups:
            self.groups[group_name].append(sensor)
            print(f'sensor {sensor} added in group {group_name} successfully ')
        else:
            print(f' group {group_name} not found')
    def get_data_from_sensor_in_group(self,group_name):
        if group_name in self.groups:
            sensors=[]
            for i in self.groups[group_name]:
                if isinstance(i,Sensor):
                    sensors.append(i)
                    if sensors:
                        for sensor in sensors:
                            sensor.read_sensor()
                    else:
                        print(f'sensors not found in group {group_name}')
                else:
                    print(f'group {group_name} not exist')
    def update_device(self, group_name, device_name, new_name=None, new_device_type=None, new_status=None):
        if group_name in self.groups:
            for device in self.groups[group_name]:
                if isinstance(device, Device) and device.name == device_name:
                    if new_name is not None:
                        device.name = new_name
                        device.topic = f'home/{group_name}/{device.device_type}/{new_name}'
                        device.topic_list = device.topic.split('/')
                    if new_device_type is not None:
                        device.device_type = new_device_type
                        device.topic = f'home/{group_name}/{new_device_type}/{device.name}'
                        device.topic_list = device.topic.split('/')
                    if new_status is not None:
                        if new_status.lower() in ['on', 'off']:
                            device.status = new_status
                        else:
                            print("Status must be 'on' or 'off'.")

                    print(f'Device {device_name} updated successfully.')
                    return
            print(f'Device {device_name} not found in group {group_name}.')
        else:
            print(f'Group {group_name} does not exist.')
    def update_sensor(self, group_name, sensor_name, new_name=None, new_unit=None):
        if group_name in self.groups:
            for item in self.groups[group_name]:
                if isinstance(item, Sensor) and item.name == sensor_name:
                    if new_name is not None:
                        item.name = new_name
                    if new_unit is not None:
                        item.unit = new_unit
                    print(f'Sensor {sensor_name} updated successfully.')
                    return
            print(f'Sensor {sensor_name} not found in group {group_name}.')
        else:
            print(f'Group {group_name} does not exist.')
    def send_alerts(self, group_name):
        if group_name in self.groups:
            for i in self.groups[group_name]:
                if isinstance(i, Sensor):
                    if i.name == "temperature_sensor" and i.unit == "Celsius":
                        temperature_sensor = 35  
                        if temperature_sensor > 30:
                            print(f"Alert: The temperature is too high ({temperature_sensor}°C)!")
                elif isinstance(i, Device):
                    if i.name == "lamp" and i.status == "off":
                        print(f"Alert: The device '{i.name}' is turned off.")
if __name__ == "__main__":
    panel = admin_panel()

    panel.create_group("living_room")
    panel.create_device("living_room", "light", "lamp")

    panel.create_multiple_devices("living_room", "fan", 3)
    devices = panel.get_devices_in_groups('living_room')
    panel.turn_on_all_in_groups("living_room")

    panel.turn_off_all_in_groups("living_room")
    panel.turn_on_all_devices()


    panel.turn_off_all_devices()


    panel.get_status_in_group('living_room')


    panel.get_status_in_device_type("light")

 
    panel.create_sensor("temperature_sensor", "living_room", "Celsius" , pin=5)

    sensor2 = Sensor("humidity_sensor", "living_room", "%", pin=8)
    panel.add_sensor_in_group("living_room", sensor2)

    panel.get_data_from_sensor_in_group("living_room")
    panel.create_device("living_room", "light", 'lamp')
    panel.create_sensor("living_room", "temperature_sensor", "Celsius")

    panel.update_device("living_room", "lamp", new_name="living_room_lamp", new_status="on")
    panel.update_sensor("living_room", "temperature_sensor", new_unit="Fahrenheit")
    panel.send_alerts('living_room')