class SmartDevice:
    def __init__(self, model_number, brand, screen_size, app_list = []):
        self.model_number = model_number
        self.brand = brand
        self.screen_size = screen_size
        self.app_list = app_list

    def report(self):
        print(f"This is " + str(self.model_number) + " from " + self.brand)

    def install_app(self, app_name = "Demo app"):
        print(f"Installing {app_name}...")
        self.app_list.append(app_name)
        return self.app_list
    
device_a = SmartDevice(12345, 'CLG', 5.7)
device_a.report()
print(device_a.app_list)
device_a.install_app()
device_a.install_app('Python Dojo')
print(device_a.app_list)