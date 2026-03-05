import random
import dice

str_stat = 0
dex_stat = 0
con_stat = 0
int_stat = 0
wiz_stat = 0
cha_stat = 0

def dice_rolls():
    num_dice = 6
    stat_1 = dice.roll_dice(num_dice)
    print(f"\n{dice.dice_face_diagram}")
    stat1_total = stat_1[0] + stat_1[1] + stat_1[2] + stat_1[3] + stat_1[4] + stat_1[5]
    stat_2 = dice.roll_dice(num_dice)
    stat2_total = stat_2[0] + stat_2[1] + stat_2[2] + stat_2[3] + stat_2[4] + stat_2[5]
    stat_3 = dice.roll_dice(num_dice)
    stat3_total = stat_3[0] + stat_3[1] + stat_3[2] + stat_3[3] + stat_3[4] + stat_3[5]
    stat_4 = dice.roll_dice(num_dice)
    stat4_total = stat_4[0] + stat_4[1] + stat_4[2] + stat_4[3] + stat_4[4] + stat_4[5]
    stat_5 = dice.roll_dice(num_dice)
    stat5_total = stat_5[0] + stat_5[1] + stat_5[2] + stat_5[3] + stat_5[4] + stat_5[5]
    stat_6 = dice.roll_dice(num_dice)
    stat6_total = stat_6[0] + stat_6[1] + stat_6[2] + stat_6[3] + stat_6[4] + stat_6[5]

    for stat in [stat1_total, stat2_total, stat3_total, stat4_total, stat5_total, stat6_total]:
        choice_stat = input(f'Where do you want to assign {stat}?  Choices are Str, Dex, Con, Int, Wiz, Cha: ')
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

    print(f"You've set the following stats: Str = {str_stat}, Dex = {dex_stat}, Con = {con_stat}, Int = {int_stat}, Wiz = {wiz_stat}, Cha = {cha_stat}")

    stats_file = open('stats.txt', 'w')
    stats_file.write(f'{str_stat}\n')
    stats_file.write(f'{dex_stat}\n')
    stats_file.write(f'{int_stat}\n')
    stats_file.write(f'{con_stat}\n')
    stats_file.write(f'{wiz_stat}\n')
    stats_file.write(f'{cha_stat}\n')
    stats_file.close()


if __name__ == '__main__':
    dice_rolls()