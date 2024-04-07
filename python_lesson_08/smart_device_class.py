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

# Homework Practice
# Attempt 1

# class SmartDevice:
#     def __init__(self, model_name, model_version, brand, screen_size, app_set = {}):
#         self.model_name = model_name
#         self.model_version = model_version
#         self.brand = brand
#         self.screen_size = screen_size
#         self.app_set = app_set

#     def report(self):
#         print(f'This is {self.model_name}, version {self.model_version} from {self.brand}. Its screen size is {self.screen_size}cm.')

#     def install_app(self, app_name = ""):
#         print(f"Installing {app_name}...")
#         self.app_set.update(app_name)
#         return self.app_set
    
#     def delete_app(self, app_name):
#         print(f"Deleting {app_name}...")
#         self.app_set.remove(app_name)
#         return self.app_set

    
# TM_phone = SmartDevice("TM Phone", 2, "Talya Mathews Enterprises", 5.7)
# TM_phone.report()
# TM_phone.install_app()
# print(TM_phone.app_set)
# TM_phone.install_app("TM Notes")
# # TM_phone.install_app("TM Time") 
# # TM_phone.install_app("TM Maps") 
# # TM_phone.install_app("TM Contacts")
# # print(TM_phone.app_set)
# # TM_phone.delete_app("TM Notes")
# # print(TM_phone.app_set)

# Attempt 2
# class SmartDevice:
#     def __init__(self, model_name, model_version, brand, screen_size):
#         self.model_name = model_name
#         self.model_version = model_version
#         self.brand = brand
#         self.screen_size = screen_size
#         self.app_list = set()

#     def report(self):
#         print(f'This is {self.model_name}, version {self.model_version} from {self.brand}. Its screen size is {self.screen_size}cm.')

#     def install_app(self, app_name = ""):
#         print(f"Installing {app_name}...")
#         self.app_list.update(app_name)
#         return self.app_list
    
#     def delete_app(self, app_name):
#         print(f"Deleting {app_name}...")
#         self.app_list.remove(app_name)
#         return self.app_list

    
# TM_phone = SmartDevice("TM Phone", 2, "Talya Mathews Enterprises", 5.7)
# TM_phone.report()
# TM_phone.install_app()
# print(TM_phone.app_list)
# TM_phone.install_app("TM Notes")
# TM_phone.install_app("TM Time") 
# TM_phone.install_app("TM Maps") 
# TM_phone.install_app("TM Contacts")
# print(TM_phone.app_list)
# TM_phone.delete_app("TM Notes")
# print(TM_phone.app_list)