import argparse

from core import gacha

parser = argparse.ArgumentParser(prog="ak", epilog="Have fun with RNJesus :))", description="Arknights gacha CLI client")
parser.add_argument("-c", "--count", type=int, default=10, help="Number of rolls")
parser.add_argument("-r", "--region", type=str, default="glb", help="Region to retrieve banner")
parser.add_argument("-i", "--id", type=str, default="standard", help="Banner to retrieve")

# TODO: Implement analytics
# parser.add_argument("-a", "--analyze", action="store_true", help="Use analytics post roll")

try:
    args = parser.parse_args()
    count = args.count
    region = args.region
    banner_id = args.id

    banner_data = gacha.load_banner(region, banner_id)
    result = gacha.roll(banner_data, count)

    for k in result:
        print(k, end="\n")
    print(gacha.analyze(result))
except Exception as e:
    print(e)
    exit(1)
