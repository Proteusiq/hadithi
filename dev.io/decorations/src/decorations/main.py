import random
import time
from typing import Final

import httpx
import jmespath

# from klass import cacher
from function import cacher
from context import timers

POKENMON_URI: Final = "https://pokeapi.co/api"


@timers("catcher")
@cacher(timeout=4)
def get_pokemons(offset: int = 151, limit: int = 151) -> list[str]:
    with httpx.Client(base_url=POKENMON_URI) as client:
        response = client.get(
            url="v2/pokemon", params={"offset": offset, "limit": limit}
        )

    # pretend time taken process
    time.sleep(1)
    pokemons = random.choices(jmespath.search("results[].name", response.json()), k=5)

    return pokemons


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()

    def caller(name: str = "trainer") -> None:
        print(f"Trainer: {name}", end=" - ")
        _ = get_pokemons()

        loop.call_later(1, caller, "Ash")

    loop.call_soon(caller, "Akari")
    loop.call_soon(caller, "Amethio")
    loop.call_later(8, loop.stop)

    loop.run_forever()
