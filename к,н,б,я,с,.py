import random
player = 0
bot = 0
dog = ['к', 'н', 'б', 'я', 'с']
while True:
    choice = input("Играть(да, нет): ")
    if (choice == "нет"):
        break
    choice = input("Выбери (к, н, б, я, с): ")
    bot_choice = dog[random.randint(0, 4)]
    if (choice == 'к'):
        if (bot_choice == 'к'):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Ничья")
            print("Очки игрока", player)
            print("Очки бота", bot)
        elif (bot_choice == 'н'):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Выигрыш")
            player += 1
            print("Очки игрока", player)
            print("Очки бота", bot)
        elif (bot_choice == 'б'):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Проигрыш")
            bot += 1
            print("Очки игрока", player)
            print("Очки бота", bot)
        elif (bot_choice == 'я'):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Выйгрыш")
            player += 1
            print("Очки игрока", player)
            print("Очки бота", bot)
        elif (bot_choice == 'с'):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Проигрыш")
            bot += 1
            print("Очки игрока", player)
            print("Очки бота", bot)
    if (choice == 'н'):
        if (bot_choice == 'н'):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Ничья")
            print("Очки игрока", player)
            print("Очки бота", bot)
        elif (bot_choice == 'б'):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Выигрыш")
            player += 1
            print("Очки игрока", player)
            print("Очки бота", bot)
        elif (bot_choice == 'к'):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Проигрыш")
            bot += 1
            print("Очки игрока", player)
            print("Очки бота", bot)
        elif (bot_choice == "я"):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Выйгрыш")
            player += 1
            print("Очки игрока", player)
            print("Очки бота", bot)
        elif (bot_choice == "с"):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Проигрыш")
            bot += 1
            print("Очки игрока", player)
            print("Очки бота", bot)
    if (choice == 'б'):
        if (bot_choice == 'б'):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Ничья")
            print("Очки игрока", player)
            print("Очки бота", bot)
        elif (bot_choice == 'к'):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Выигрыш")
            player += 1
            print("Очки игрока", player)
            print("Очки бота", bot)
        elif (bot_choice == 'н'):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Проигрыш")
            bot += 1
            print("Очки игрока ", player)
            print("Очки бота", bot)
        elif (bot_choice == "я"):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Проигрыш")
            bot += 1
            print("Очки игрока", player)
            print("Очки бота", bot)
        elif (bot_choice == "с"):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Выйгрыш")
            player += 1
            print("Очки игрока", player)
            print("Очки бота", bot)
    if (choice == "я"):
        if (bot_choice == "я"):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("ничья")
            print("Очки игрока", player)
            print("Очки бота", bot)
        elif (bot_choice == "с"):
                print("Выбор бота: " + bot_choice)
                print("Выбор игрока: " + choice)
                print("Выйгрыш")
                player += 1
                print("Очки игрока", player)
                print("Очки бота", bot)
        elif (bot_choice == "б"):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Выйгрыш")
            player += 1
            print("Очки игрока", player)
            print("Очки бота", bot)
        elif (bot_choice == "к"):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Проигрыш")
            bot += 1
            print("Очки игрока", player)
            print("Очки бота", bot)
    if (choice == 'с'):
        if (bot_choice == 'с'):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("ничья")
            print("Очки игрока", player)
            print("Очки бота", bot)
        elif (bot_choice == 'н'):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Выйгрыш")
            player += 1
            print("Очки игрока", player)
            print("Очки бота", bot)
        elif (bot_choice == 'б'):
            print('Выбор бота: ' + bot_choice)
            print("Выбор игрока: " + choice)
            print("Проигрыш")
            bot += 1
            print("Очки игрока", player)
            print("Очки бота", bot)
        elif (bot_choice == 'к'):
            print("Выбор бота: " + bot_choice)
            print("Выбор игрока: " + choice)
            print("Выйгрыш")
            player += 1
        print("Очки игрока", player)
        print("Очки бота", bot)
