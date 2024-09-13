class Router:
    def __init__(self):
        self.interfaces = {}

    def configure_interface(self, name, ip):
        self.interfaces[name] = ip
        print(f"Configured interface {name} with IP {ip}")

router = Router()
router.configure_interface('GigabitEthernet0/0', '192.168.1.1')
