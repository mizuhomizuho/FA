from src.lib import Lib

class Tools:

    async def lifespan(self) -> None:
        pass
        # inst = Lib('items/tools', 'Tools').get()()
        # print('Create db')
        # await inst.create_db()
        # print('Drop db')
        # await inst.drop_db()

    async def lifespan_end(self) -> None:
        print('End')