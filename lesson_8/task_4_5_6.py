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


def _amount_validation(obj, required_type, result=1):
    try:
        if not isinstance(obj, required_type):
            raise WrongDataPassed('')
        else:
            return obj
    except WrongDataPassed as W:
        print(f'{W}\n', f'\033[93mWrong data passed in amount variable expected int, got: {type(obj)}. '
                        f'Amount value set to default. \003')
        return result


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

    @property
    def accounting(self):
        return self._accounting

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
                self.accounting[sample.__class__.__name__] += 1
            else:
                self.storage[sample.__class__.__name__] = [sample]
                self.accounting[sample.__class__.__name__] = 1

        if isinstance(item, list):
            for i in item:
                take(i)
        else:
            take(item)

    def _clean_category(self):
        """Removing category from self.storage and self.accounting dicts if 0 items in accounted category"""
        while 0 in self.accounting.values():
            for k, v in self.accounting.items():
                if v == 0:
                    del self.accounting[k]
                    del self.storage[k]
                    break

    def _find_requested_items(self, product):
        count_suitable = 0
        for items_category in self.storage.values():
            count_suitable += sum(1 for position in items_category if product == f"{position.brand} {position.model}")
        print(f'\033[92mFound {count_suitable} matches of {product}\033[0m')

        return count_suitable

    def transfer(self, item, department, amount=1):
        """
        Items transferring protocol to some department from warehouse. If amount is not integer - set default
        :param item: item that we want to transfer
        :param department: department that will receive an item
        :param amount: amount of items passed to department
        :return: None
        """
        # Input data validation
        amount = _amount_validation(amount, int)

        # Search items started
        requested_items_found = self._find_requested_items(item)

        def __invoice(items: list):
            """
            Function to make an invoice (summarizing) items to transfer
            :param items: items picked to transfer
            :return:
            """
            for position in items:
                print(f"{position} passed to: {department} department")

        def packing(required_items: int):
            """
            Loading items to the truck
            :param required_items: amount of required items
            :return:
            """
            for category in self.storage.values():
                for prod in category:
                    if item == f'{prod.brand} {prod.model}':
                        packing_list.append(prod)
                        category.remove(prod)
                        self.accounting[prod.__class__.__name__] -= 1
                        required_items -= 1
                        break
            return required_items if required_items else 0

        if requested_items_found == 0:
            print(f'\033[91m-No {item} found in {self._wh_type}-\033[0m')
        elif requested_items_found >= amount:
            packing_list = []
            while amount:
                amount = packing(amount)
            __invoice(packing_list)
        elif requested_items_found < amount:
            print(f"\033[93m-Not Enough {item} on warehouse, {requested_items_found}/{amount} in stock- \033[0m")
            packing_list = []
            while requested_items_found:
                requested_items_found = packing(requested_items_found)
            __invoice(packing_list)

            # Optional: create an invoice as JSON file
            # with open(f'{some_invoice_name}_{some_invoice_counter}', 'w', encoding='utf-8') as F:
            #    json.dump(some bla-bla; to file bla-bla)
            #
            # Then unpack the JSON data into some WMS form and print Invoice based on packing list

        self._clean_category()

    def __iter__(self):
        return self.storage.__iter__()

    def __str__(self):
        _spacer = '-' * 10
        _type = f'Warehouse type: {self._wh_type}\n'
        _value = '\n'.join((f"{k:>8} ({self.accounting[k]}): "
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
    local.transfer('XiaoMi LiangYue', department='Kafedra magicheskih treugolnikov', amount='Ochen mnogo')
    print(local)
