import random
import sys
from pool import *

rates = [0.02, 0.08, 0.5, 0.4]

# Rate-up
six_stars_up = 0.5
five_stars_up = 0.5
# TODO: Implement debut banner type
four_stars_up = 0.0


def arknights_gacha(roll_count, sr_pity_hit, pity_count):
    global rates

    results = []

    # Name
    six_stars_name = '6*'
    five_stars_name = '5*'
    four_stars_name = '4*'
    three_stars_name = '3*'

    names = [six_stars_name, five_stars_name, four_stars_name, three_stars_name]

    choices = random.choices(names, weights=rates, k=roll_count)

    for idx, choice in enumerate(choices):
        temp_rates = rates.copy()

        is_pity = False
        pity_type = "None"

        # guarantee 6*/5* in first ten rolls
        if idx + 1 <= 10:
            if (choice == six_stars_name or choice == five_stars_name) and not sr_pity_hit:
                sr_pity_hit = True
                is_pity = True
                pity_type = "First Ten Guarantee"
            if idx + 1 == 10 and not sr_pity_hit:
                # If nine previous rolls don't give you SSR or higher
                # then 10th roll will give it forcefully
                choice = random.choices([six_stars_name, five_stars_name], weights=[0.02, 0.98], k=1)[0]
                sr_pity_hit = True
                is_pity = True
                pity_type = "First Ten Guarantee"
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
            if pity_count >= 50:
                is_pity = True
                pity_type = "50-th Roll Pity"
            pity_count = 0
        else:
            pity_count += 1

        is_rate_up = False
        # Rate-up processing
        if choice == six_stars_name:
            up_rate = [six_stars_up, 1 - six_stars_up]
            up_name = [six_rate_up_pool, list(set(six_stars_pool) - set(six_rate_up_pool))]
            pick = random.choices(up_name, up_rate, k=1)[0]
            if pick == six_rate_up_pool:
                is_rate_up = True
            choice = random.choice(pick)
        elif choice == five_stars_name:
            up_rate = [five_stars_up, 1 - five_stars_up]
            up_name = [five_rate_up_pool, list(set(five_stars_pool) - set(five_rate_up_pool))]
            pick = random.choices(up_name, up_rate, k=1)[0]
            if pick == five_rate_up_pool:
                is_rate_up = True
            choice = random.choice(pick)
        elif choice == four_stars_name:
            # TODO: Rate-up
            choice = random.choice(four_stars_pool)
        elif choice == three_stars_name:
            choice = random.choice(three_stars_pool)

        if is_rate_up:
            choice += " (RATE UP)"

        if __name__ == "__main__":
            print(f'Roll number {idx + 1}: {choice} \t\t\t\t - Pity count: {pity_count} \t')
        else:
            results.append(
                {
                    "roll_number": idx + 1,
                    "result": choice.replace(" (RATE UP)", ""),
                    "is_rate_up": is_rate_up,
                    "pity": {
                        "pity_count": pity_count,
                        "is_pity": is_pity,
                        "pity_type": pity_type
                    }
                }
            )

        rates = temp_rates.copy()

    return results


if __name__ == "__main__":
    rolls = int(sys.argv[1])
    arknights_gacha(rolls, False, 0)
