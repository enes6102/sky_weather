import python_weather

import asyncio
import os

async def getweather() -> None:
    #declaring the client
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        
        city = input("Enter a city: ")
        weather = await client.get(city)

        print(f"Pressure {weather.pressure}")
        print(f"{weather.temperature} Celcius")
        print(f"Wind speed {round(weather.wind_speed*1.852)} knots at {weather.wind_direction.degrees}")
        print(f"Visibility {weather.visibility*1000}m")
        print(f"{weather.kind}")


if __name__ == '__main__':
  if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
  
  asyncio.run(getweather())