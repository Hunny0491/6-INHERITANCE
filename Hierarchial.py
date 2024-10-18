class Developer:

    def code(self):
        print('INDIA')

class BackDeveloper(Developer):

    def back_code(self):
        print('BACK SIDE')

class FrontDeveloper(Developer):

    def front_code(self):
        print('FRONT SIDE')

back_dev = BackDeveloper()
back_dev.code()
back_dev.back_code()

front_dev = FrontDeveloper()
front_dev.code()
front_dev.front_code()