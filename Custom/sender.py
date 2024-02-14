from aioquic.asyncio.client import connect
import aioquic
async def main():
    async with connect("localhost:4453", 4453) as conn:
        data = b"Hello, world!"
        await conn.send(data)
        print(f"Sent data: {data}")

if __name__ == "__main__":
    aioquic.asyncio.run(main())

