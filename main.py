from client.llm_client import LLMClient
import asyncio

async def main() -> None:
    client = LLMClient()
    messages = [{
        'role': 'user',
        'content': "Hello"
    }]
    async for event in client.chat_completion(messages, True):
        print(event)
    print("done")


if __name__ == "__main__":
    asyncio.run(main())
