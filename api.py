import json
from typing import Optional, Any

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
    return [0.02, 0.08, 0.5, 0.4]


@app.get("/operators", response_class=PrettyJSONResponse)
def get_gacha_pool():
    return {
        "six_stars": six_stars_pool,
        "five_stars": five_stars_pool,
        "four_stars": four_stars_pool,
        "three_stars": three_stars_pool
    }


@app.get("/roll", response_class=PrettyJSONResponse)
def roll(roll_count: int, sr_pity_hit: Optional[bool] = False, pity_count: Optional[int] = 0):
    return arknights_gacha(roll_count, sr_pity_hit, pity_count)


# Rate-up zone
# /rate-up/operators
# /rate-up/rates
@app.get("/rate-up/operators", response_class=PrettyJSONResponse)
def get_rate_up_operators():
    return {
        "six_stars": six_rate_up_pool,
        "five_stars": five_rate_up_pool,
        "four_stars": four_rate_up_pool
    }


@app.get("/rate-up/rates", response_class=PrettyJSONResponse)
def get_rate_up_rates():
    return {
        "six_stars": six_stars_up,
        "five_stars": five_stars_up,
        "four_stars": four_stars_up
    }


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000)
