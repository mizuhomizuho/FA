from lib.lib import Lib

class Tools:

    async def lifespan(self) -> None:
        pass
        # inst = Lib('tools/db', 'DbTools').get()()
        # print('Create db')
        # await inst.create_db()
        # print('Drop db')
        # await inst.drop_db()

    async def lifespan_end(self) -> None:
        print('End')