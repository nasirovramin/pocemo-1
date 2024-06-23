import telebot 
from config import token


from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")


bot.infinity_polling(none_stop=True)


# Метод для получения имени покемона через API
def get_name(self):
    url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
    response = response.get(url)
    if response.status_code == 200:
        data = response.json()
        return (data['forms'][0]['name'])
    else:
        return "Pikachu"
    
@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pok.info())
    else:
        bot.send_message("У одного из игроков нет покемона")


















