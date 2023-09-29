from abc import ABC, abstractmethod


class RequiredForAirborn(ABC):
    @abstractmethod
    def fly(self):
        pass

    def scream(self):
        print('Yo-ho')


class RequiredFuel(ABC):
    @abstractmethod
    def refuling(self):
        pass

    def scream(self):
        print('Yo-ho11111111111')


class AvatarCreatureAlive(RequiredForAirborn):
    def fly(self):
        # raise NotImplemented
        print('Creature flying')


class AvatarDrones(RequiredFuel, RequiredForAirborn):
    def fly(self):
        print('Fly')

    def refuling(self):
        print('Refuling')

    def scream(self):
        super(AvatarDrones, self).scream()
        print('Yo-ho ***********************')


creature = AvatarCreatureAlive()
creature.scream()
drone = AvatarDrones()
drone.scream()


class AbcDB(ABC):
    @abstractmethod
    def get_data(self, data: dict):
        pass

    @abstractmethod
    def save_data(self, data: dict):
        pass


class Mongo(AbcDB):
    TOKEN = 'dkjhgkjdfhdjkgb'


class Postgresql(AbcDB):
    TOKEN = 'dkjhgkjdfhdjkgb'
    URL = 'kjdfhgjkdfhgkf'


entrypoint = Mongo()

entrypoint.get_data({'name': 555})