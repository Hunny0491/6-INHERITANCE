class Developer:

    def __init__(self,name):
        self.name = name

    def code(self):
        print(f'{self.name} Growing Nation')


class BackDeveloper(Developer):

    def __init__(self,name,backend_skill):
        super().__init__(name)
        self.backend_skill = backend_skill

    def deploy(self):
        print(f'{self.name} is Third {self.backend_skill} economy ')


dev = BackDeveloper('INDIA', 'largest')
dev.code()
dev.deploy()