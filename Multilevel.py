class Developer:

    def code(self):
        print('INDIA')

class BackDeveloper(Developer):

    def back_code(self):
        print('BACK SIDE')

class SeniorBackDeveloper(BackDeveloper):

    def lead_project(self):
        print('Leading a back project')

dev = SeniorBackDeveloper()
dev.code()
dev.back_code()
dev.lead_project()