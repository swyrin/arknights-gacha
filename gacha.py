import random
import sys

"""
How this works:
1. 5* or higher is guaranteed in the first ten rolls
2. If the first 50 rolls doesn't give you a 6*, then starting from 51th roll, the 6* rate will go up by 2%
"""

def arknights_gacha(roll_count):
	rates = [0.02, 0.08, 0.5, 0.4]
	six_stars_name = '6*'
	five_stars_name = '5*'
	four_stars_name = '4*'
	three_stars_name = '3*'

	names = [six_stars_name, five_stars_name, four_stars_name, three_stars_name]

	sr_pity_hit = False
	pity_count = 0
	choices = random.choices(names, weights=rates, k=roll_count)

	for idx, choice in enumerate(choices):
		# guarantee 6*/5* in first ten rolls
		if idx + 1 <= 10:
			if (choice == six_stars_name or choice == five_stars_name) and not sr_pity_hit:
				sr_pity_hit = True
			if idx + 1 == 10 and not sr_pity_hit:
				sr_pity_hit = True
		else:
			if pity_count >= 50:
				temp_rates = rates.copy()
				temp_rates[0] += (pity_count - 50) * 0.02
				max_index = 0

				if temp_rates[1] > temp_rates[2] > temp_rates[3]:
					max_index = 1
				elif temp_rates[1] < temp_rates[2] and temp_rates[2] > temp_rates[3]:
					max_index = 2
				elif temp_rates[1] < temp_rates[2] < temp_rates[3]:
					max_index = 3

				temp_rates[max_index] -= 0.02
				choice = random.choices(names, weights=temp_rates, k=1)[0]

		if choice == six_stars_name:
			pity_count = 0
		else:
			pity_count += 1

		print(f'Roll number {idx + 1}: {choice} \t - Pity count: {pity_count}')

if __name__ == "__main__":
        rolls = int(sys.argv[0])
        arknights_gacha(rolls)
