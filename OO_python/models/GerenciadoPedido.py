from typing import List
from .Cliente import Cliente
from .PedidoComida import PedidoComida
from .EntregaPedido import EntregaPedido
from .Pedido import Pedido
from .EntregaService import EntregaService
from .StatusPedido import StatusPedido  # Adicionado import necessário

class GerenciadorPedidos: #isso aqui tbm kkkkkkkkk
    def __init__(self):
        self._pedidos: List[Pedido] = []
        self._proximo_id = 1

    def obter_proximo_id(self) -> int: #isso aqui eu não vou mentir não sei praq serve
        "Retorna o próximo ID disponível e incrementa o contador."
        id_atual = self._proximo_id
        self._proximo_id += 1
        return id_atual

    def adicionar_pedido(self, pedido: Pedido) -> None: #funções extras
        "Adiciona um pedido à lista de pedidos."
        self._pedidos.append(pedido)

    def novo_pedido(self) -> None: #Funções extras
        print("NOVO PEDIDO DE COMIDA")
        try:
            nome = input("Nome do cliente: ")
            email = input("Email do cliente: ")
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")

            cliente = Cliente(nome, email, telefone, endereco)

            distancia = float(input("Distância para entrega (km): "))
            valor = float(input("Valor do pedido (R$): "))
            
            id_pedido = self.obter_proximo_id()
            pedido = PedidoComida(id_pedido, cliente, distancia, valor, StatusPedido.PREPARANDO)
            
            self.adicionar_pedido(pedido)
            
            # Demonstrar uso da interface
            entrega = EntregaPedido(pedido, distancia)
            print(f"{entrega.getTempoEstimado()}")
            print(f"Pedido urgente: {'Sim' if entrega.isPedidoUrgente() else 'Não'}")
            
        except ValueError:
            print("\n✗ Erro: Valor inválido! Tente novamente.")
        except Exception as e:
            print(f"\n✗ Erro ao criar pedido: {e}")