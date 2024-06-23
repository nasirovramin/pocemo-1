from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = randint(50,100)
        self.power = randint(10,20)
        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        pass
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"""Имя твоего покеомона: {self.name}
Здоровье покемона: {self.hp}
Сила покемона: {self.power}"""

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    


def attack(self, enemy):
    if enemy.hp > self.power:
        enemy.hp -= self.power
        return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
    else:
        enemy.hp = 0
        return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "



class Wizard(Pokemon):
    def info(self):
        return "У тебя покемон волшебник" + super().info()


class Figter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5, 15)
        self_power = self_power
        result = super().attack(enemy)
        self.power = super_power
        return result + f"Бэст пременил суператаку с силой {super_power}"
    

    def info(self):
        return "У тебя покемон боец" + super().info()
    