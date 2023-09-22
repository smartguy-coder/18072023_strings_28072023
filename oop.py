from datetime import datetime


class Human:
    __population = 0
    DNA = 'XXX YYY'

    @classmethod
    def __increase_population(cls):
        cls.__population += 1

    @classmethod
    def __decrease_population(cls):
        cls.__population -= 1

    def __init__(self, name: str):
        self.name = name.title()
        self.__money = 0
        # self.__class__.__increase_population()
        Human.__increase_population()

    def __str__(self):
        return f'I am {self.name}'

    # def __repr__(self):
    #     return f'Human {self.name}'
    __repr__ = __str__

    def take_some_money(self, amount: int):
        card = input('Give card number')
        if card == '1234':
            self.__money += amount

    def __del__(self):
        print('Died', self)
        Human.__decrease_population()
        print(Human.__population, 555555555555)



class Player(Human):
    def __init__(self, name: str, skills: list[str]):
        super().__init__(name=name)
        self.skills = skills


class Teacher(Human):
    def __init__(self, name: str, subjects: list[str]):
        super().__init__(name=name)
        self.subjects = subjects


class SportTeam:
    def __init__(self, name: str, month_salary_one_person: int = 1000):
        self.name = name
        self.date = datetime.now()
        self.players: list[Player] = []
        self.__money = 0
        self.month_salary_one_person = month_salary_one_person

    def __str__(self):
        return f'Team {self.name}'

    __repr__ = __str__

    def pay_salary(self) -> None:
        if len(self.players) * self.month_salary_one_person <= self.__money:
            print('paying......')
            for player in self.players:
                player.take_some_money(self.month_salary_one_person)
                self.__money -= self.month_salary_one_person
        else:
            print('Not enough money')

    def fire(self, player: Player):
        self.players.remove(player)
        return self


team = SportTeam('Desna')
# team2 = SportTeam('Desna')

# print(team == team)

max_p = Player(name='Max2', skills=['soccer'])
max2 = Teacher(name='Max', subjects=['biology'])

del max_p
# print(max_p)

print(max_p.DNA)
print(max2.DNA)


# print(max2.__money)
print('*'*20)
# max2.__money = 50000
# max2.__money += 10
# print(max2.__money)

# max2._Human__money = 200
# print(max2.__money)
# team.players.append(max)

team.pay_salary()
# team2.pay_salary()
# team.__money += 5000
# team.pay_salary()

# john = Human('John')
# team.players.append(john)
# team.pay_salary()

# print(max)
# print(john)
# print(max)
# print(team)
# print(team.money)
# print(team.players)

# print(team.money)
# print(max.money)
# print(john.money)
#
# print(team.fire(max).fire(john))
# # team.fire(john)
# print(team.players)
