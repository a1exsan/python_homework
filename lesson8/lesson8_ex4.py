
class Storage:
    def __init__(self):
        self.storage_input_tab = None
        self.storage_output_tab = None

    def get_count(self, equipment):
        if self.storage_input_tab != None:
            count = 0
            for e in self.storage_input_tab:
                if e == equipment:
                    count += 1
            return count
        else:
            return 0

    def load_input_equipment(self, equipment, count):

        if self.storage_input_tab == None:
            self.storage_input_tab = []

        for i in range(count):
            self.storage_input_tab.append(equipment)

    def send_equipment(self, equipment, count, destination):
        if self.storage_output_tab == None:
            self.storage_output_tab = []

        if self.get_count(equipment) >= count:
            self.storage_output_tab.append({'equipment': equipment, 'count': count, 'destination': destination})

            for i in range(count):
                self.storage_input_tab.remove(equipment)
        else:
            print(f"Storage can't get {count} of {equipment.model_name}")



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

    def __eq__(self, other):
        return self.model_name == other.model_name and self.color == other.color

class Printer(officeEquipment):
    def __init__(self, model_name, color):
        super().__init__()
        self.model_name = model_name
        self.color = color
        self.color_type = 'b&w'
        self.print_velocity = 0
        self.print_type = 'laser'

class Copier(officeEquipment):
    def __init__(self, model_name, color):
        super().__init__()
        self.model_name = model_name
        self.color = color
        self.max_copies_count = 0
        self.changing_scale = 0
        self.copying_speed = 0

class Scaner(officeEquipment):
    def __init__(self, model_name, color):
        super().__init__()
        self.model_name = model_name
        self.color = color
        self.scaning_file_format = 'pdf'
        self.scaning_speed = 0
        self.type_light_source = 'LED'


storage = Storage()

p1, p2, p3 = Printer('P01 Epson', 'white'), Printer('P02 HP', 'black'), Printer('P01 Xerox', 'red')

s1, s2 = Scaner('S1 Epson', 'black'), Scaner('S1 Epson', 'white')

c1, c2 = Copier('C1 Xerox', 'red'), Copier('C2 Epson', 'white')

print(p1.model_name, p1.color, p1.width, p1.max_dpi)

storage.load_input_equipment(p1, 5)
print(storage.get_count(p1))

storage.load_input_equipment(s1, 2)
storage.load_input_equipment(s2, 3)
storage.load_input_equipment(c1, 2)

print(storage.storage_input_tab)

storage.send_equipment(p1, 6, 'marketing department')

print(storage.storage_output_tab, '\n')

storage.send_equipment(p1, 5, 'marketing department')

print(storage.storage_output_tab, '\n')

print(storage.storage_input_tab)





