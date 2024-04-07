# Add a default argument for install_app method. DONE

# Modify install_app method to avoid duplicates inapp_list. DONE BY CHANGING TO Aapp_list INSTEAD OF A LIST

# Add a delete_app method which takes in one parameter: the name of the app you would like to delete. DONE

# Create a SmartDevice object and use it to call the functions. DONE

# Use print statements to check if both methods work as you expect them to. DONE

class SmartDevice:
    def __init__(self, model_name, model_version, brand, screen_size):
        self.model_name = model_name
        self.model_version = model_version
        self.brand = brand
        self.screen_size = screen_size
        self.app_list = set()

    def report(self):
        print(f'This is {self.model_name}, version {self.model_version} from {self.brand}. Its screen size is {self.screen_size}cm.')

    def install_app(self, app_name = ""):
        print(f"Installing {app_name}...")
        self.app_list.update(app_name)
        return self.app_list
    
    def delete_app(self, app_name):
        print(f"Deleting {app_name}...")
        self.app_list.remove(app_name)
        return self.app_list

    
TM_phone = SmartDevice("TM Phone", 2, "Talya Mathews Enterprises", 5.7)
TM_phone.report()
TM_phone.install_app()
print(TM_phone.app_list)
TM_phone.install_app("TM Notes")
TM_phone.install_app("TM Time") 
TM_phone.install_app("TM Maps") 
TM_phone.install_app("TM Contacts")
print(TM_phone.app_list)
TM_phone.delete_app("TM Notes")
print(TM_phone.app_list)