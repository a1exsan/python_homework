from abc import ABC, abstractmethod


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



class officeEquipment(ABC):

    TOTAL_EQUIPMENTS_obj = 0

    def __init__(self):
        officeEquipment.TOTAL_EQUIPMENTS_obj += 1

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

    @classmethod
    def get_total_obj(cls):
        return cls.TOTAL_EQUIPMENTS_obj

    @abstractmethod
    def get_param_list(self):
        pass

    def __eq__(self, other):
        return self.model_name == other.model_name and self.color == other.color

    @property
    def max_dpi(self):
        return self.__max_dpi

    @max_dpi.setter
    def max_dpi(self, value):
        if type(value) == str:
            self.__max_dpi = value
        else:
            print(' max_dpi must be str type! ')

    @property
    def model_name(self):
        return self.__model_name

    @model_name.setter
    def model_name(self, value):
        if type(value) == str:
            self.__model_name = value
        else:
            print(' model_name must be str type! ')

    @property
    def power_consumption(self):
        return self.__power_consumption

    @model_name.setter
    def power_consumption(self, value):
        if type(value) in [int, float]:
            self.__power_consumption = value
        else:
            print(' power_consumption must be numeric type! ')

class Printer(officeEquipment):
    def __init__(self, model_name, color):
        super().__init__()
        self.model_name = model_name
        self.color = color
        self.color_type = 'b&w'
        self.print_velocity = 0
        self.print_type = 'laser'

    def get_param_list(self):
        return [self.color_type, self.print_velocity, self.print_type]

class Copier(officeEquipment):
    def __init__(self, model_name, color):
        super().__init__()
        self.model_name = model_name
        self.color = color
        self.max_copies_count = 0
        self.changing_scale = 0
        self.copying_speed = 0

    def get_param_list(self):
        return [self.max_copies_count, self.changing_scale, self.copying_speed]

class Scaner(officeEquipment):
    def __init__(self, model_name, color):
        super().__init__()
        self.model_name = model_name
        self.color = color
        self.scaning_file_format = 'pdf'
        self.scaning_speed = 0
        self.type_light_source = 'LED'

    def get_param_list(self):
        return [self.scaning_speed, self.scaning_file_format, self.type_light_source]


storage = Storage()

p1, p2, p3 = Printer('P01 Epson', 'white'), Printer('P02 HP', 'black'), Printer('P01 Xerox', 'red')

print(p1.get_param_list())

s1, s2 = Scaner('S1 Epson', 'black'), Scaner('S1 Epson', 'white')

print(s1.get_param_list())

c1, c2 = Copier('C1 Xerox', 'red'), Copier('C2 Epson', 'white')

print(c1.get_param_list())

storage.load_input_equipment(p1, 5)
storage.load_input_equipment(p2, 2)
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

p3.max_dpi = 'HP 71021'
print(p3.max_dpi)

p3.power_consumption = {}

print(officeEquipment.TOTAL_EQUIPMENTS_obj)

print(p1.get_total_obj())





