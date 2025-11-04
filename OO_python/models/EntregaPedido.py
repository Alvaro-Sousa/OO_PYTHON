from .EntregaService import EntregaService
from .Pedido import Pedido

class EntregaPedido(EntregaService):
  def __init__ (self, pedido: Pedido, distancia: float):
    self._pedido = pedido
    self._distancia = distancia
  
  def getTempoEstimado(self) -> str:
    temp_base = 10 #tempo em minutos
    temp_km = 5 #km médio por minuto
    temp_total = temp_base + (self._distancia * temp_km)
    return f"{temp_total:.0f} minutos"

  def isPedidoUrgente(self) -> bool:
    # Implementação do método abstrato
    return self._distancia < 5 and self._pedido.valor > 100.0
