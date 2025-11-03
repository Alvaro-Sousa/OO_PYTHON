from abc import ABC, abstractmethod

# define interface usando ABC
class EntregaService(ABC):
  @abstractmethod
  def getTempoEstimado(self): #tava faltando o self pra dar retorno
    pass

  @abstractmethod
  def isPedidoUrgente(self): #aqui tbm tava faltando o self
    pass
