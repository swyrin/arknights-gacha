import json
import random
import sys

from pool import *

rates = [0.02, 0.08, 0.5, 0.4]


def load_banner(banner_id: str):
    j = {}

    with open("banner.json", "r") as f:
        j = json.loads(f.read())

    banner_data = j[banner_id]
    # name, type, rate-up pool, rate-up rates
    return banner_data['name'], banner_data['type'], banner_data['rate_up']['rates'], banner_data['rate_up']['pool']


def arknights_gacha(banner_id, roll_count):
    global rates

    results = []

    sr_pity_hit = False
    pity_count = 0

    _, _, rate_up_rates, rate_up_pool = load_banner(banner_id)

    # Name
    six_stars_name = '6*'
    five_stars_name = '5*'
    four_stars_name = '4*'
    three_stars_name = '3*'

    names = [six_stars_name, five_stars_name, four_stars_name, three_stars_name]
    overall_pool = [six_stars_pool, five_stars_pool, four_stars_pool, three_stars_pool]

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

        for index, name in enumerate(names):
            if choice == three_stars_name:
                choice = random.choice(overall_pool[2])
                break
            elif choice == name:
                up_rates = rate_up_rates[index]
                prob = [up_rates, 1 - up_rates]

                pool = rate_up_pool[index]

                up_names = [pool, list(set(overall_pool[index]) - set(pool))]
                res = random.choices(up_names, prob, k=1)[0]
                choice = random.choice(res)

                if choice in up_names[0]:
                    is_rate_up = True

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
    arknights_gacha("surtr-debut", rolls)
