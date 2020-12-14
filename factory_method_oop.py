from abc import ABC, abstractmethod


class Guitar(ABC):
	def __init__(self, name):  # конструктор объектов
		self._name = name  # инкапсуляция - _name является доступным для классов и подклассов

	def get_name(self):
		return self._name

	@abstractmethod
	def adjust(self):
		...

	@staticmethod
	def tune_in():
		print('Tuning guitar! Sounds marvelous!')


class Acoustic(Guitar):  # наследование от абстрактного класса
	def adjust(self):  # полиморфизм - метод adjust находится и в классе Electric
		print('Adjusting neck!')


class Electric(Guitar):
	def adjust(self):
		print('Replacing strings! Adjusting guitar pickups! Also put a bit of lemon oil on top!')




class GuitarFactory(ABC):  # абстрактный класс фабрики

	@abstractmethod
	def create_guitar(self, model):
		...

	def order_guitar(self, model):
		guitar = self.create_guitar(model)
		if guitar:
			print(f'Making your {guitar.get_name()} all nice and good looking!')
			guitar.adjust()
			guitar.tune_in()
			print('Its all done! Look at this beauty!')
		else:
			print('Sorry, we do not make these guitars')
			return
		return guitar


class GuitarShop(GuitarFactory):  # имплементация фабрики
	def create_guitar(self, model):
		if model == 'acoustic':
			return Acoustic('Acoustic guitar')
		elif model == 'electric':
			return Electric('Electric guitar')
		else:
			return


if __name__ == "__main__":
	gt = GuitarShop()
	gt.order_guitar(input('Order guitar here. Please tell us, which would you prefer?\n'))
