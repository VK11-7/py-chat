import bluetooth
nearby_devices = bluetooth.discover_devices()
print("Found %d devices" % len(nearby_devices))