import asyncio
import aiohttp

async def get_data(id: int, endpoint: str):
    print(f"Начал выполнение {id}")
    url = f"http://192.168.3.2:8001/{endpoint}/{id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            await resp.text()  # чтобы реально дождаться тела (не обязательно, но полезно)
            print(f"Закончил выполнение {id}, status={resp.status}")

async def main():
    await asyncio.gather(*[get_data(i, "async") for i in range(300)])

asyncio.run(main())
