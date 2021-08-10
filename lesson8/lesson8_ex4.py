
class Storage:
    def __init__(self):
        pass

class officeEquipment:
    def __init__(self):
        self.model_name = 'None'
        self.product_country = 'None'
        self.color = 'black'
        self.width = 0
        self.height = 0
        self.length = 0
        self.weight = 0
        self.paper_format = 'A4'
        self.max_dpi = 'None'
        self.power_consumption = 0

class Printer(officeEquipment):
    def __init__(self):
        super().__init__()
        self.color_type = 'b&w'
        self.print_velocity = 0
        self.print_type = 'laser'

class Xerox(officeEquipment):
    def __init__(self):
        super().__init__()
        self.max_copies_count = 0
        self.changing_scale = 0
        self.copying_speed = 0

class Scaner(officeEquipment):
    def __init__(self):
        super().__init__()
        self.scaning_file_format = 'pdf'
        self.scaning_speed = 0
        self.type_light_source = 'LED'








