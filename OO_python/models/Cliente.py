
class Cliente: #CONTRUTOR DA CLASSE
  def __init__(self, nome, email, telefone, endereco):
    self._nome = nome
    self._email = email
    self._telefone = telefone
    self._endereco = endereco

  @property #GETTER NOME
  def nome(self) -> str:
    return self._nome

  @nome.setter #SETTER NOME
  def nome(self, value: str):
    self._nome = value

  @property #GETTER EMAIL
  def email(self) -> str:
    return self._email
  
  @email.setter #SETTER EMAIL
  def email(self, value: str):
    self._email = value

  @property #GETTER TELEFONE
  def telefone(self) -> str:
    return self._telefone
  
  @telefone.setter #SETTER TELEFONE
  def telefone(self, value: str):
    self._telefone = value

  @property #GETTER ENDEREÇO
  def endereco(self) -> str:
    return self._endereco
  
  @endereco.setter #SETTER ENDEREÇO
  def endereco(self, value: str):
    self._endereco = value

  def __str__(self) -> str:
    return f"{self.nome} - {self._telefone} - {self._endereco}"


  #print(file="Cliente criado com sucesso!")