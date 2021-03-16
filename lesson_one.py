from random import*
class HERO():
    def __init__(self, health, damage, name): #ХАРАКТЕРИСТИКИ ПЕРСОНАЖА
        self.health = health
        self.damage = damage
        self.name = name

def hero(checklist):
    answer = input("Введите бойца для схватки:") #ВЫБОР ПЕРОСНАЖА
    ind = 0
    for i in checklist:
        if i.name == answer:
            print("------ БОЕЦ ВЫБРАН ------")
            ind = i
    return ind

def create(objective):
    name = input("Введите имя для бойца:")
    health = int(input("Введите уровень здоровья для бойца")) #ВВОД ДАННЫХ БОЙЦА
    damage = int(input("Введите урон для бойца:"))
    objective = HERO(health, damage, name)
    return objective

print('Суть мини игры: рандомно выбирать кто из 2-х персонажей будет бить и кто в итоге останется жив, тот победит. Только в этой версии будет дан список ранее введенных бойцов.')
count = int(input("Введите колличество бойцов:"))
checklist = []
for i in range(count):
    checklist.append(create(i)) #ЗАПОЛЕНИЕ СПИСКА БОЙЦАМИ

ans = ""
while ans == "" or ans == "ДА" or ans == "да" or ans =="Да":
    print("--------- СПИСОК БОЙЦОВ ---------")
    for i in checklist:
        print("--------- " + i.name + " --------- " + "урон " + str(i.damage) + " --------- здоровье " + str(i.health)) #ВЫВОД СПСИКА БОЙЦОВ И ИХ ХАРАКТЕРИСТИКИ
    first = 0
    second = 0
    print("------- ПЕРВЫЙ БОЕЦ -------")
    while first == 0:
        first = hero(checklist)
    print("------- ВТОРОЙ БОЕЦ -------")
    while second == 0:
        second = hero(checklist)
    heal_1 = first.health
    heal_2 = second.health #ДЛЯ ВОССТАНОВЛЕНИЯ ЗДОРОВЬЯ ПРИ НОВОЙ ИГРЕ

    while second.health > 0 and first.health > 0:
        punch = randint(1, 2)
        if punch == 1:
            second.health -= first.damage
            print(first.name + " наносит удар!!!")
        if punch == 2:
            first.health -= second.damage
            print(second.name + " наносит удар!!!")
    if second.health <= 0:
        print(first.name + " ПОБЕДИЛ/А В ЭТОЙ ЦИФРОВОЙ СХВАТКЕ!!!")
    else:
        print(second.name + " ПОБЕДИЛ/А В ЭТОЙ ЦИФРОВОЙ СХВАТКЕ!!!")
    first.health = heal_1
    second.health = heal_2
    ans = input("Если вы хотите выбрать других бойцов для поединка из уже существующего списка нажмите ENTER ИЛИ НАПИШИТЕ 'Да'. Иначе сеанс завершится!!!")
