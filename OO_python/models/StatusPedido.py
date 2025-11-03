from enum import Enum

class StatusPedido(Enum):
    PREPARANDO = "Preparando"
    EM_TRANSITO = "Em trânsito"
    ENTREGUE = "Entregue"
    CANCELADO = "Cancelado"