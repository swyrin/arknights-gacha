from typing import Any

import uvicorn
from fastapi import FastAPI
from starlette.responses import Response

from gacha import *

app = FastAPI()


# https://gitter.im/tiangolo/fastapi?at=5d381c558fe53b671dc9aa80
class PrettyJSONResponse(Response):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=4,
            separators=(", ", ": "),
        ).encode("utf-8")


@app.get("/")
def index_page():
    return "Hi"


# General zone
# /rates
# /operator
# /roll
@app.get("/rates")
def get_gacha_rates():
    return rates


@app.get("/operators", response_class=PrettyJSONResponse)
def get_gacha_pool():
    return {
        "six_stars": six_stars_pool,
        "five_stars": five_stars_pool,
        "four_stars": four_stars_pool,
        "three_stars": three_stars_pool
    }


@app.get("/{banner_id}/roll", response_class=PrettyJSONResponse)
def roll(banner_id, roll_count: int):
    return arknights_gacha(banner_id, roll_count)


@app.get("/{banner_id}", response_class=PrettyJSONResponse)
def banner_info(banner_id):
    name, _, rates, pool = load_banner(banner_id)
    return {
        "name": name,
        "rate_up": {
            "rates": rates,
            "pool": pool
        }
    }


# Banner-specific zone
# /rate-up/operators
# /rate-up/rates
@app.get("/{banner_id}/operators", response_class=PrettyJSONResponse)
def get_rate_up_operators(banner_id):
    _, _, _, pool = load_banner(banner_id)

    return {
        "six_stars": pool[0],
        "five_stars": pool[1],
        "four_stars": pool[2]
    }


@app.get("/{banner_id}/rates", response_class=PrettyJSONResponse)
def get_rate_up_rates(banner_id):
    _, _, rates, _ = load_banner(banner_id)
    return {
        "six_stars": rates[0],
        "five_stars": rates[1],
        "four_stars": rates[2]
    }


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000)
