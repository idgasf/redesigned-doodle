
class Owner:

	__instance = None

	def __new__(cls, name):
		if cls.__instance is None:
			cls.__instance = object.__new__(cls)
		cls.__instance.name = name
		return cls.__instance

	def __call__(cls, *args, **kwargs):
		print(f'Owner is {cls.__instance.name}')


if __name__ == "__main__":
	own_1 = Owner('First')
	own_1()
	own_2 = Owner('Second')
	own_2()
	own_1()
