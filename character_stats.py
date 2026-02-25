import random

def dice_rolls():
    str_stat = random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    dex_stat = random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    con_stat = random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    int_stat = random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    wiz_stat = random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    cha_stat = random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6)

    return str_stat, dex_stat, con_stat, int_stat, wiz_stat, cha_stat
