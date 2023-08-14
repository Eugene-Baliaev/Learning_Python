#№ 1
from random import *
class CRM:
    def __init__(self):
        self.__abiturients = {}
    def add(self, abiturient):
        # получение СНИЛСа
        number = abiturient.get_number()
        # добавление абитуриента в словарь,
        # где информация хранится под СНИЛСами
        self.__abiturients[number] = abiturient
    def get_status(self,number):
        #Проверяем проходит ли абитуриент по БВИ
        if self.__abiturients[number].bvi:
            return "Проходишь"
        #Если нет БВИ, то гадаем из трёх вариантов
        else:
            options = ["Проходишь", "Не проходишь", "А фиг его знает"]
            return choice(options)
class Abiturient:
    def __init__(self, name, surname, patronymic, age, number, bvi=False):
        self.__name = name
        self.__surname = surname
        self.__patronymic = patronymic
        self.__age = age
        # СНИЛС
        self.__number = number
        # Russian National Exam (ЕГЭ), баллы
        self.__RNE = self.__fetch_RNE()
        # есть ли БВИ
        self.__bvi = bvi
    # функция получения результатов ЕГЭ
    def __fetch_RNE(self):
        return tuple(randint(0, 100) for _ in range(3))
    # функция ответа на вопрос, проходит ли абитуриент
    def __check(self):
        if self.__bvi:
            return "Да"
        if random() > 0.95:
            return "Да"
        return "Нет"
    #Геттер и сеттер для фамилии
    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self,surname):
        self.__surname = surname
    #Геттер и сеттер для имени
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    #Геттер и сеттер для псевдонима
    @property
    def patronymic(self):
        return self.__patronymic
    @patronymic.setter
    def patronymic(self, patronymic):
        self.__patronymic = patronymic
    #Геттер и сеттер для имени
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        self.__age = age
    #Геттер и сеттер для результатов ЕГЭ
    @property
    def RNE(self):
        return self.__RNE
    @RNE.setter
    def RNE(self,RNE):
        self.__RNE = RNE
    #Геттер и сеттер для БВИ
    @property
    def bvi(self):
        return self.__bvi
    @bvi.setter
    def bvi(self,bvi):
        self.__bvi = bvi
    #Геттер для получения СНИЛСа
    def get_number(self):
        return self.__number


module = CRM()
# добавление АР-а в список абитуриентов
module.add(Abiturient("Александр", "Вотяков", "Романович", 18, "111-222-333 00", True))
# добавление РА в список абитуриентов
module.add(Abiturient("Роман", "Вотяков", "Александрович", 18, "333-222-111 00"))
# проверка, проходят ли абитуриенты
print(module.get_status("111-222-333 00"))
print(module.get_status("333-222-111 00"))

#№ 2
from random import *
class RIP(Exception):
    pass

#работаем с изумрудом
class Emerald:
    statuses = ['Не учтён','учтён','отправлен под спуд']
    def __init__(self):
        # статус изумруда:
        # 0 - не учтён
        # 1 - учтён
        # 2 - отправлен под спуд
        self.__status = 0
        # цена изумруда
        self.__price = randint(10,100)
    def account(self):
        if self.__status == 0:
            self.__status = 1
        else:
            return RIP('Так делать нельзя')
    def store(self):
        if self.__status == 1:
            self.__status = 2
        else:
            return RIP('Так делать нельзя')

    @property
    def status(self):
        return Emerald.statuses[self.__status]
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,price):
        if isinstance(price, int) and price >= 0:
            self.__price = price
        else:
            RIP('Так делать нельзя')

class Shell:
    statuses = ['Не учтена','Учтена','Отправлена в монетолитейное отделение','Переплавлена в монету']
    def __init__(self):
        # статус скорлупки:
        # 0 - не учтена
        # 1 - учтена
        # 2 - отправлена в монетолитейное отделение
        # 3 - переплавлена в монету
        self.__status = 0

        # цена скорлупки
        self.__price = randint(100,1000)
    @property
    def status(self):
        return Shell.statuses[self.__status]
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,price):
        self.__price = price
    def account(self):
        if self.__status == 0:
            self.__status = 1
        else:
            RIP('Так делать нельзя')
    def process(self):
        if self.__status == 1:
            self.__status = 2
        else:
            RIP('Так делать нельзя')
    def smelt(self,archive):
        if self.__status == 2:
            year = 2023
            if self.__price != 0:
                value = self.__price
            else:
                value = randint(10,10**5)
            new_coin = Coin(Coin.Serial_Number,year,value)
            archive.add(Entry(new_coin))

class Coin:
    Serial_Number = 0
    def __init__(self, serial_number, year, value):
        # серийный номер монеты
        self.__serial_number = serial_number

        # год выпуска монеты
        self.__year = year

        # номинал монеты
        self.__value = value
        Coin.Serial_Number += 1

    @property
    def serial_number(self):
        return f'Серийный номер: {self.__serial_number:06}'
    @property
    def year(self):
        return f'Год выпуска: {self.__year}'
    @property
    def value(self):
        return f'Номинал моменты: {self.__value:06}'
#Храним...
class Archive:
    def __init__(self):
        # список учтённых объектов
        self.__storage = []
    #Добавляем запись в архив
    def add(self,entry):
        if isinstance(entry,Entry):
            self.__storage.append(entry)
        else:
            raise RIP('Так делать нельзя')
    def get(self,index):
        entry = self.__storage[index]
        if entry == None or entry.secret:
            return f'[Запись {index}] Информация удалена'
        item = entry.item
        result = f'[Запись {index}-{entry.ID}]'
        result += f'[{str(item)}] {entry.date} "{entry.info}" '
        if isinstance(item,Emerald) or isinstance(item,Shell):
            result += f"Статус: {item.status} Цена: {item.price} "
        elif isinstance(item,Coin):
            result += f"{str(item.serial_number):06} "
            result += f"{item.year} "
            result += f"{item.value}"
        return result
    def edit(self,index,info):
        self.__storage[index].info = info
    def classify(self,index):
        self.__storage[index].secret = True
    def declassify(self,index):
        self.__storage[index].secret = False
    def delete(self,index):
        self.__storage[index] = None
    def info(self):
        for _ in range(len(self.__storage)):
            print(self.get(_))
    def item(self,index):
        return self.__storage[index].item
#Создаём запись объекта
class Entry:
    def __init__(self, item, date='01.01.2023', info='', secret=False):
        # идентификационный номер, создаётся автоматически
        self.__ID = self.__get_next_ID()
        # указатель на объект
        self.__item = item
        # дата создания записи
        self.__date = date
        # дополнительная информация об объекте
        self.__info = info
        # информация засекречена?
        self.__secret = secret

    @property
    def ID(self):
        return self.__ID
    @property
    def item(self):
        return self.__item
    @property
    def date(self):
        return self.__date
    @property
    def info(self):
        return self.__info
    @info.setter
    def info(self,information):
        if isinstance(information,str) or isinstance(information,int):
            self.__info = information
        else:
            RIP('Так делать нельзя')

    @property
    def secret(self):
        return self.__secret
    @secret.setter
    def secret(self,Secret):
        if isinstance(Secret,bool):
            self.__secret = Secret
        else:
            raise RIP('Так делать нельзя')
    def __get_next_ID(self):
        return hash(self)


archive = Archive()
for _ in range(20):
    shell = Shell()
    shell.account()

    archive.add(Entry(shell))

archive.info()

for _ in range(10):
    emerald = Emerald()
    emerald.account()

    archive.add(Entry(emerald))

archive.info()

for i in range(20, 30):
    archive.item(i).store()

archive.info()

for i in range(20):
    archive.item(i).process()

archive.info()

for i in range(20):
    archive.item(i).smelt(archive)

archive.info()

for i in range(20, 30):
    archive.classify(i)

archive.info()

for i in range(20):
    archive.delete(i)

archive.info()

for i in range(25, 30):
    archive.declassify(i)

archive.info()

for i in range(25, 30):
    archive.edit(i, "Информация обновлена")

archive.info()

i = 30
try:
    while True:
        print(archive.get(i))
        i += 1
except IndexError:
    pass