"""4-5-6. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники."""


class WrongAttr(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f'WrongDataPassed error - {self.text}'


class WrongDataPassed(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f'WrongDataPassed error - {self.text}'


class NotEnoughItems(TypeError):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f'Missing items - {self.text}'


class Warehouse:
    """
    Ochen nehoroshaya realisatsiya sklada cherez slovar'. Mojno bilo sdelat cherez list,
    no cherez luche slojno, no interestno, chem prosto i skuchno
    """
    def __init__(self, warehouse_type: str):
        """
        :param warehouse_type: Describes the location of the warehouse or its size based on type
        Global > local > temporary_hub
        :param __storage: dict of items stored in the warehouse
        :param _accounting: dict of calculated items stored on warehouse
        """
        self._wh_type = warehouse_type
        self.__storage = {}
        self._accounting = {}

    @property
    def storage(self):
        return self.__storage

    def store(self, item):
        """
        Function to accept items to the storage
        :param item: item(or list of items) to the warehouse
        :return: None
        """
        def take(sample):
            """
            Passes item to warehouse one by one
            :param sample: 1 pcs of item(s)
            :return: None
            """
            if sample.__class__.__name__ in self.storage.keys():
                self.storage[sample.__class__.__name__].append(sample)
                self._accounting[sample.__class__.__name__] += 1
            else:
                self.storage[sample.__class__.__name__] = [sample]
                self._accounting[sample.__class__.__name__] = 1

        if isinstance(item, list):
            for i in item:
                take(i)
        else:
            take(item)

    def transfer(self, item, department, amount=1):
        """
        Function of transferring items to some department from warehouse
        :param item: item that we want to transfer
        :param department: department that will receive an item
        :param amount: amount of items passed to department
        :return: None
        """
        count_suitable = 0
        for items_category in self.storage.values():
            count_suitable += sum(1 for position in items_category if item == f"{position.brand} {position.model}")
        print(f'\033[92mFound {count_suitable} matches of {item}\033[0m')

        def invoice(items: list):
            """
            Function to make an invoice (summarizing) items to transfer
            :param items: items picked to transfer
            :return:
            """
            for position in items:
                print(f"{position} passed to {department} department")

        def packing(required_items: int):
            """
            Loading items to the truck
            :param required_items: amount of required items
            :return:
            """
            for i in self.storage.values():
                for j in i:
                    if item == f'{j.brand} {j.model}':
                        packing_list.append(j)
                        i.remove(j)
                        self._accounting[j.__class__.__name__] -= 1
                        required_items -= 1
                        break
            return required_items if required_items else 0

        if count_suitable == 0:
            print(f'\033[91m-No {item} found in {self._wh_type}-\033[0m')
        elif count_suitable >= amount:
            packing_list = []
            while amount:
                amount = packing(amount)
            invoice(packing_list)
        elif count_suitable < amount:
            print(f"\033[93m-Not Enough {item} on warehouse, {count_suitable}/{amount} in stock- \033[0m")
            packing_list = []
            while count_suitable:
                count_suitable = packing(count_suitable)
            invoice(packing_list)

            # Optional: create an invoice as JSON file
            # with open(f'{some_invoice_name}_{some_invoice_counter}', 'w', encoding='utf-8') as F:
            #    json.dump(some bla-bla; to file bla-bla)
            #
            # Then unpack the JSON data into some WMS form and print Invoice based on packing list

        """Removing category from warehouse dict if 0 items in accounted category"""
        while 0 in self._accounting.values():
            for k, v in self._accounting.items():
                if v == 0:
                    del self._accounting[k]
                    del self.storage[k]
                    break

    def __iter__(self):
        return self.storage.__iter__()

    def __str__(self):
        _spacer = '-' * 10
        _type = f'Warehouse type: {self._wh_type}\n'
        _value = '\n'.join((f"{k:>8} ({self._accounting[k]}): "
                            f"{', '.join(map(lambda i: f'{i.brand} {i.model}', self.storage[k]))}"
                           for k, v in self.storage.items()))
        return f'{_spacer}\n{_type}{_value}\n{_spacer}'


class Equipment:
    """Eshe odin ochen ploho napisanniy class no uje dlya tehniki"""
    whole_discount = 0.9

    def __init__(self, brand: str, model: str, price: int, whole_sale=False, dpt=None):
        """
        :param brand: item brand
        :param model: item model
        :param price: item price
        :param whole_sale: if item purchased as wholesale or single purchase, if items >= 10 - wholesale = True
        :param dpt: if item was purchased to some department else None
        """
        self.brand = brand
        self.model = model
        self.tp = f'{self.__class__.__name__.lower()}'
        self.cost = int(price * self.whole_discount) if whole_sale else price
        self.dpt = dpt

    @classmethod
    def batch(cls, count, **properties):
        """
        Batch purchase
        :param count: Amount of items purchased
        :param properties: Item attributes unpacked as kwargs
        :return: None
        """
        try:
            if isinstance(count, int):
                return [cls(**properties, whole_sale=True if count >= 10 else False, ) for _ in range(count)]
            else:
                raise WrongDataPassed('Item amount must be integer')
        except WrongDataPassed:
            print('Item amount must be integer')

    def __str__(self):
        return f"{' '.join([self.brand, self.model])} {self.tp}"


class Printer(Equipment):
    """Class describing printer"""
    def __init__(self, ink_jet='full', **kwargs):
        """
        :param ink_jet: if has ink in cartridge or not
        :param kwargs: Equipment attributes
        """
        super(Printer, self).__init__(**kwargs)
        self.ink = ink_jet

    def to_print(self, document="*empty*"):
        """Function that prints some data, if empty - prints filler *empty*"""
        return f"{self.dpt if self.dpt else ''}{'(s) dpt ' if self.dpt else ''}{self.brand} {self.model} prints: {document}"


class Scanner(Equipment):
    """Class describing scanner"""
    def __init__(self, two_side_scan=False, **kwargs):
        """
        :param two_side_scan: if scanner can scan both sides
        :param kwargs: Equipment attributes
        """
        super(Scanner, self).__init__(**kwargs)
        self.two_side_scan = two_side_scan

    def to_scan(self, document=None):
        """Printer scans some document, if no document - scans Nothing"""
        department_allocation: str = f"{self.dpt}s {self.__class__.__name__} " if self.dpt else ''
        return f"{department_allocation}{self.brand} {self.model} scans: {'Nothing' if not document else document}"


class Xerox(Scanner, Printer):
    """Class describing Xerox
    has both methods: scan/print"""
    def __init__(self, **kwargs):
        super(Xerox, self).__init__(**kwargs)
        # self.magic = magic

    def __str__(self):
        return f'{self.brand} {self.model}'


if __name__ == '__main__':
    local = Warehouse('Local')
    pr1 = Printer(brand='HP', model='Super printer', price=7500)
    print(pr1.to_print('HORSE'))
    sc1 = Scanner(brand='Kyocera', model='vv-12', price=8000)
    print(sc1.to_scan('Super secret documents'))
    xr1 = Xerox(brand='HP', model='EOS-2', price=6900)
    print(xr1.to_scan("Someone's face"))
    print(xr1.to_print("Someone's face"))
    try:
        pr2 = Printer(brand='HP', price=7500)
    except TypeError as E:
        print('Error: ', E)

    local.store(pr1)
    local.store(sc1)
    local.store(xr1)
    local.store(Scanner.batch(10, brand='HP', model='X-35', price=6500, two_side_scan=True))
    local.store(Xerox.batch(10, brand='XiaoMi', model='LiangYue', price=6500, two_side_scan=True, ink_jet='Empty'))
    print(local)

    local.transfer('HP EOS-2', department='Bubbles blowing', amount=3)
    local.transfer('HP X-35', department='Not your business', amount=4)
    local.transfer('HP X-35', department='Not your business', amount=15)
    local.transfer('XiaoMi LiangYue', department='Somewhere inside China mainland', amount=3)
    local.transfer('Give me something', department='Greedy douche dpt', amount=99)
    print(local)
