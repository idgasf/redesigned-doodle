from abc import ABC, abstractmethod

class Guitar(ABC):
	def __init__(self, name):
		self._name = name

	def get_name(self):
		return self._name

	@abstractmethod
	def adjust(self):
		...

	@staticmethod
	def tune_in():
		print('Tuning guitar! Sounds marvelous!')

class Acoustic(Guitar):
	def adjust(self):
		print('Adjusting neck!')


class Electric(Guitar):
	def adjust(self):
		print('Replacing strings! Adjusting guitar pickups! Also put a bit of lemon oil on top!')

class GuitarFactory(ABC):

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
			print('Sorry, we dont make these guitars')
			return
		return guitar

class GuitarShop(GuitarFactory):
	def create_guitar(self, model):
		if model == 'acoustic':
			return Acoustic('Acoustic guitar')
		elif model == 'electric':
			return Electric('Electric guitar')
		else:
			return


gt = GuitarShop()
gt.order_guitar(input('Order guitar here. Please tell us, which would you prefer?\n'))
