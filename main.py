import asyncio

from card import main




if __name__ == "__main__":
    query = "пальто из натуральной шерсти"
    queue = asyncio.Queue()
    asyncio.run(main(queue=queue, query=query))
