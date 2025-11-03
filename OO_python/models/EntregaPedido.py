from .EntregaService import EntregaService

class EntregaPedido(EntregaService):
  def getTempoEstimado(self):
    if self.isPedidoUrgente(): #"def" getTempoEstimado(self): tava assim antes
      return "Tempo medio estimado de 30 minutos" #aqui tava retornando "return + print" sendo que só o return mas a msg já ia
    else:
      return "Tempo medio estimado de 50 minutos" #mesmo esquema aqui

  def isPedidoUrgente(self):
    # Implementação do método abstrato
    return False
