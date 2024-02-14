import asyncio
from aioquic.asyncio import QuicConnectionProtocol, serve


class SimpleServerProtocol(QuicConnectionProtocol):
    async def handle_stream(self, stream_id: int) -> None:
        # Handle incoming data on a stream
        data = await self._quic.receive_stream_data(stream_id)
        print(f"Received data on stream {stream_id}: {data.decode()}")


async def main() -> None:
    configuration = QuicConfiguration(
        alpn_protocols=[H3_ALPN, H0_ALPN],
        is_client=False,
    )
    async with serve(
        "localhost", 4433, configuration=configuration, create_protocol=SimpleServerProtocol
    ) as server:
        await asyncio.Future()  # Run forever


if __name__ == "__main__":
    asyncio.run(main())

