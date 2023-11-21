print("Так познакомились гостем теперь начнем игру") 
import random
words = ["bmw", "mersedes","hyondai", "toyota","audi","chevrolet"]
word = random.choice(words)
def game_start(): 

    word_letters = []
    attempts = 5 
    
    print("Сегодня наш гость, будет угадывать лучшие машины во всем мире!")
    print("На все про все у него 5 попыток!")
    print("Пожелаем удачи!")
    
    while attempts > 0: 
        Invisible_letters = ""
        for letter in word: 
            if letter in word_letters:
                Invisible_letters += letter
            else: 
                Invisible_letters +="_"
                  
                    
        print(f'наше загадоное слова {Invisible_letters}')
        print(f"осталось {attempts} попыток")
        user = input("Ввeдите букву: ").lower() 
    
        if user in word_letters: 
            print(f"Откроту букву {user}")
            continue 
        word_letters.append(user)
        if user not in word: 
            attempts -= 1
            print("ты не угодал :(") 
            
        if "_" not in Invisible_letters: 
            print("поздравляю вы выйграли")
            print(f"ваш приз машина которую вы отгадали! {word}")
            break
        if attempts == 0: 
            print("вы проиграли ") 
            break
game_start()            
            
 