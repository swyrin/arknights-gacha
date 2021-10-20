import random
import sys
from pool import *


"""
How this works:
1. 5* or higher is guaranteed in the first ten rolls
2. If the first 50 rolls doesn't give you a 6*, then starting from 51th roll, the 6* rate will go up by 2%
"""

def arknights_gacha(roll_count):
    rates = [0.02, 0.08, 0.5, 0.4]

    # Name
    six_stars_name = '6*'
    five_stars_name = '5*'
    four_stars_name = '4*'
    three_stars_name = '3*'

    # Rate-up
    six_stars_up = 0.5
    five_stars_up = 0.5

    # TODO: Implement debut banner type
    # four_stars_up = 0.4

    names = [six_stars_name, five_stars_name, four_stars_name, three_stars_name]

    sr_pity_hit = False
    pity_count = 0
    choices = random.choices(names, weights=rates, k=roll_count)

    for idx, choice in enumerate(choices):
        temp_rates = rates.copy()
        # guarantee 6*/5* in first ten rolls
        if idx + 1 <= 10:
            if (choice == six_stars_name or choice == five_stars_name) and not sr_pity_hit:
                sr_pity_hit = True
            if idx + 1 == 10 and not sr_pity_hit:
                sr_pity_hit = True
        else:
            if pity_count >= 50:
                rates[0] += (pity_count - 50) * 0.02
                max_index = 0

                if rates[1] > rates[2] > rates[3]:
                    max_index = 1
                elif rates[1] < rates[2] and rates[2] > rates[3]:
                    max_index = 2
                elif rates[1] < rates[2] < rates[3]:
                    max_index = 3

                rates[max_index] -= 0.02
                choice = random.choices(names, weights=rates, k=1)[0]


        if choice == six_stars_name:
            pity_count = 0
        else:
            pity_count += 1

        isRateUp = False
        # Rate-up processing
        if choice == six_stars_name:
                up_rate = [six_stars_up, 1 - six_stars_up]
                up_name = [six_rate_up_pool, list(set(six_stars_pool) - set(six_rate_up_pool))]
                pick = random.choices(up_name, up_rate, k=1)[0]
                if pick == six_rate_up_pool:
                        isRateUp = True
                choice = random.choice(pick)
        elif choice == five_stars_name:
                up_rate = [five_stars_up, 1 - five_stars_up]
                up_name = [five_rate_up_pool, list(set(five_stars_pool) - set(five_rate_up_pool))]
                pick = random.choices(up_name, up_rate, k=1)[0]
                if pick == five_rate_up_pool:
                        isRateUp = True
                choice = random.choice(pick)
        elif choice == four_stars_name:
                # To-do: Rate-up
                choice = random.choice(four_stars_pool)
        elif choice == three_stars_name:
                choice = random.choice(three_stars_pool)

        if isRateUp:
                choice += " (RATE UP)"
            
        print(f'Roll number {idx + 1}: {choice} \t\t\t\t - Pity count: {pity_count} \t')
        rates = temp_rates.copy()

if __name__ == "__main__":
        # rolls = int(sys.argv[0])
        arknights_gacha(300)
