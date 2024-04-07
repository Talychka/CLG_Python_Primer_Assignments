class SmartDevice:
    def __init__(self, model_name, model_version, brand, screen_size, app_list = {}):
        self.model_name = model_name
        self.model_version = str(model_version)
        self.brand = brand
        self.screen_size = str(screen_size)
        self.app_list = set(app_list)

    def report(self):
        print(f'This is ' + self.model_name + ' Version ' + self.model_version + ' from ' + self.brand + '. Its screen size is ' + self.screen_size + 'cm.')

    def install_app(self, app_name = ""):
        print(f"Installing {app_name}...")
        self.app_list.update(app_name)
        return self.app_list
    
    def delete_app(self, app_name = ""):
        print(f"Deleting {app_name}...")
        self.app_list.remove(app_name)
        return self.app_list

    
TM_phone = SmartDevice("TM Phone", 2, "Talya Mathews Enterprises", 5.7)
TM_phone.report()
TM_phone.install_app()
print(TM_phone.app_list)
TM_phone.install_app({"TM Notes"})
TM_phone.install_app({"TM Time"}) 
TM_phone.install_app({"TM Maps"}) 
TM_phone.install_app({"TM Contacts"})
TM_phone.install_app({"TM Contacts"})
print(TM_phone.app_list)
TM_phone.delete_app("TM Notes")
print(TM_phone.app_list)