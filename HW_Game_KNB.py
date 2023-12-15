import random

list_choise = ["К", "Н", "Б"]


def KNB_Сhoise(С):
    if С == "К":
        print("Камень")
    elif С == "Н":
        print("Ножницы")
    elif С == "Б":
        print("Бумага")


print("Приветствую тебя в игре Камень-Ножницы-Бумага")


def main():
    print()


if __name__ == "__main__":
    choise = input(
        "Введи на выбор 'К','Н','Б'. Где К - Камень, Н - Ножницы, Б - Бумага :"
    )

if choise not in list_choise:
    print("Не правильное значенние")
    exit()
else:
    KNB_Сhoise(choise)
c_choise = random.choice(list_choise)
KNB_Сhoise(c_choise)

if choise == c_choise:
    print("У нас ничья!")


elif (
    choise == "К"
    and c_choise == "Н"
    or choise == "Н"
    and c_choise == "Б"
    or choise == "Б"
    and c_choise == "К"
):
    print("Ты выиграл!")


elif (
    (choise == "К" and c_choise == "Б")
    or (choise == "Н" and c_choise == "К")
    or (choise == "Б" and c_choise == "Н")
):
    print("Ты проиграл!")

main()
