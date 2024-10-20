from typing import Callable

class Lib:

    inst: Callable

    __path: str
    __class: str

    def __init__(self, path: str, class_name: str):

        self.__path = path
        self.__class = class_name

    def get(self) -> Callable:

        with open(f'lib/{self.__path}.py', 'r') as f:
            exec(f'def lib_wrapper_fns(lib_wrapper_inst):\n\t{'\n\t'.join(f.read().split('\n'))}'
                f'\n\tlib_wrapper_inst.inst = {self.__class}\nlib_wrapper_fns(self)')

        return self.inst