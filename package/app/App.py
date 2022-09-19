from typing import Type
from package.Process import Process
from package.app.modules.moduloexemplo.ExemploModule import ExemploModule
from package.app.template.IAppModule import IAppModule

INITIAL_MODULE: Type[IAppModule] = ExemploModule

class App(Process):

    @staticmethod
    def start():
        INITIAL_MODULE().start()
