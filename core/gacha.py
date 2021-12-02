import json
import random

from pathlib import Path

from core.pool import *

# Hardcoded rarity names for now
six_stars_name = '6*'
five_stars_name = '5*'
four_stars_name = '4*'
three_stars_name = '3*'


def load_banner(region: str, banner_id: str) -> tuple[str, int, dict]:
    try:
        script_location = Path(__file__).absolute().parent
        file_location = script_location / f"banners-{region}.json"
        file = file_location.open()
        j = json.loads(file.read())
        file.close()

        try:
            banner_data = j[banner_id]
            return banner_data["name"], banner_data["type"], banner_data["rate_up"]
        except KeyError:
            raise Exception(f"Banner ID '{banner_id}' for region {region} not exist")

    except FileNotFoundError:
        raise FileNotFoundError(f"Can not found banner data for region '{region}'")


def roll(banner_data: tuple[str, int, dict], roll_count: int) -> list[dict]:
    rates = [0.02, 0.08, 0.5, 0.4]
    rarities = [six_stars_name, five_stars_name, four_stars_name, three_stars_name]
    operators_pool = [six_stars_pool, five_stars_pool, four_stars_pool, three_stars_pool]

    banner_type = banner_data[1]
    rate_up = list(banner_data)[2]

    pity_count = 0
    sr_pity_hit = False

    choices = list(random.choices(rarities, rates, k=roll_count))

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
                # If previous 9 rolls don't give you 6* or higher
                # then 10th roll will give it to you.
                choice = random.choices([six_stars_name, five_stars_name], weights=[0.02, 0.98], k=1)[0]
                sr_pity_hit = True
                is_pity = True
                pity_type = "First Ten Guarantee"
        else:
            # If previous 50 rolls doesn't give you 6* or higher
            # then from 51st roll, 6* rate will increase by 2% per roll
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
                choice = random.choices(rarities, weights=rates, k=1)[0]

        if choice == six_stars_name:
            if pity_count >= 50:
                is_pity = True
                pity_type = "50-th Roll Pity"
            pity_count = 0
        else:
            pity_count += 1

        # Store post-processed choice
        # Since choice will be used to determine the name
        rarity = choice

        is_rate_up = False
        is_limited_rate_up = False
        is_limited_comeback_rate_up = False

        for index, name in enumerate(rarities):
            if choice == name:
                # If the banner is Limited Banner (either with Comeback Limited Operators or not)
                if choice == six_stars_name and (banner_type == 2 or banner_type == 3):
                    up_names = [rate_up["operators"][0], rate_up["limited_comebacks"], six_stars_pool]
                    prob = [0.64, 0.3, 0.06]

                    res = random.choices(up_names, prob, k=1)[0]
                    choice = random.choice(res)

                    if (choice in up_names[0]) or (choice in up_names[1]):
                        is_rate_up = True

                        if choice[0] == "*":
                            is_limited_rate_up = True
                        if choice in up_names[1]:
                            is_limited_comeback_rate_up = True

                        choice = choice.replace("*", "")
                else:
                    up_rate = rate_up["rates"][index]
                    pool = rate_up["operators"][index]

                    up_names = [pool, list(set(operators_pool[index]) - set(pool))]
                    prob = [up_rate, 1 - int(up_rate)]
                    res = random.choices(up_names, prob, k=1)[0]
                    choice = random.choice(res)

                    if choice in up_names[0]:
                        is_rate_up = True

        choices[idx] = {
            "order": idx + 1,
            "name": choice,
            "rarity": rarity,
            "pity": {
                "is_pity": is_pity,
                "pity_type": pity_type,
                "pity_count": pity_count,
            },
            "rate_up": {
                "is_rate_up": is_rate_up,
                "is_limited_rate_up": is_limited_rate_up,
                "is_limited_comeback_rate_up": is_limited_comeback_rate_up
            }
        }

        rates = temp_rates.copy()

    return choices


def analyze(results: list[dict]) -> dict:
    # TODO: implement
    pass
