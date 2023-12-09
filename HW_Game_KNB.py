import random

list_choise = ["К", "Н", "Б"]


def КНБ_Сhoise(C):
    if C == "К":
        print("Камень")
    elif C == "Н":
        print("Ножницы")
    elif C == "Б":
        print("Бумага")


print("Приветствую тебя в игре Камень-Ножницы-Бумага")


def main():
    print()


choise = input("Введи на выбор 'К','Н','Б'. Где К - Камень, Н - Ножницы, Б - Бумага :")

if choise not in list_choise:
    print("Не правильное значенние")
    exit()
else:
    КНБ_Сhoise(choise)
c_choise = random.choice(list_choise)
КНБ_Сhoise(c_choise)
if (
    (choise == "К" and c_choise == "Н")
    or (choise == "Н" and c_choise == "Б")
    or (choise == "Б" and c_choise == "К")
):
    print("Ты выиграл!")
if (
    (choise == "К" and c_choise == "Б")
    or (choise == "Н" and c_choise == "К")
    or (choise == "Б" and c_choise == "Н")
):
    print("Ты проиграл!")
if (
    (choise == "К" and c_choise == "К")
    or (choise == "Н" and c_choise == "Н")
    or (choise == "Б" and c_choise == "Б")
):
    print("У нас ничья!")

if __name__ == "__main__":
    main()
