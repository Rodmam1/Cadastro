class pessoa:
  def __init__(self,nome,ano,idade):
     self.nome=nome
     self.ano=ano
     self.idade=idade
  def trocar_nome(self,nome):
     self.nome=nome
     print(f"nome trocado com sucesso {nome}")


joao=pessoa("Andre",200,25)
joao.trocar_nome("ana")



