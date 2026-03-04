import random

str_stat = 0
dex_stat = 0
con_stat = 0
int_stat = 0
wiz_stat = 0
cha_stat = 0

def dice_rolls():
    stat_1 = random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    stat_2 = random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    stat_3 = random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    stat_4 = random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    stat_5 = random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    stat_6 = random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6)

    for stat in [stat_1, stat_2, stat_3, stat_4, stat_5, stat_6]:
        choice_stat = input(f'Where do you want to assign {stat_1}?  Choices are Str, Dex, Con, Int, Wiz, Cha')
        if choice_stat == 'Str':
            stat = str_stat
        elif choice_stat == 'Dex':
            stat = dex_stat
        elif choice_stat == 'Con':
            stat = con_stat
        elif choice_stat == 'Int':
            stat = int_stat
        elif choice_stat == 'Wiz':
            stat = wiz_stat
        elif choice_stat == 'Cha':
            stat = cha_stat    

    return str_stat, dex_stat, con_stat, int_stat, wiz_stat, cha_stat

if __name__ == '__main__':
    dice_rolls()