from abc import ABC, abstractmethod
from .Cliente import Cliente
from .StatusPedido import StatusPedido

class Pedido(ABC):

    # construtor da classe
    def __init__(self, id: int, cliente: Cliente, valor: float, status: StatusPedido): 
        self._id = id              # atributo protegido
        self._cliente = cliente    # objeto da classe Cliente
        self._valor = valor
        self._status = status


    # Métodos abstratos que as classes filhas devem implementar
    @abstractmethod
    def calcularTaxa(self) -> float: #tipo de retorno dos metodos
        pass

    @abstractmethod
    def getDetalhes(self) -> dict:
        pass


    # getters
    @property
    def id(self) -> int:
        return self._id

    @property
    def cliente(self) -> Cliente:
        return self._cliente

    @property
    def valor(self) -> float:
        return self._valor

    @property
    def status(self) -> StatusPedido:
        return self._status

    # settes

    @id.setter
    def id(self, id: int):
        self._id = id

    @cliente.setter
    def cliente(self, cliente: Cliente):
        self._cliente = cliente

    @valor.setter
    def valor(self, valor: float):
        self._valor = valor

    @status.setter
    def status(self, status: StatusPedido):
        self._status = status
