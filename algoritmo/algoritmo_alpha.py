"""
Algoritmo do gerador de horários do Projeto Atena

Sumário Estendido
-----------------
Versão Alpha - Ainda nas implementações iniciais!

Inclui: Sistema básico de input dos dados e organização dos mesmos, ainda sem o algoritmo principal.
"""

# Ao fazer o ``git clone``, faça ``git pull`` antes de fazer qualquer coisa para obter as alterações da núvem!
# Depois, quando terminar, faça ``git add .`` na pasta onde se alterou algo (ou na pasta do repositório), ``git commit`` e depois ``git push``

# OBS: Lembrar de deletar __pycache__ antes de fazer ``git push``!
# OBS: Lembre de deixar o código legível, mas tabém formal!

# Notas extras:
# Pelo amor de Deus, comentar linhas para não gerar confusão mais que horários.
# Lembre-se de que certos comentários são piores do que o código
# Se tiver qualquer coisa que não é o que parece ou que não está funcionando ainda ou é só um teste ou conceito, sinaliza isso.
# Lembre-se de que este repositório é público e os surtos destes comentários também.
# Lembrar de usar o git direito e combinar com os colaboradores para não haver conflitos no meio dos pushs.

import numpy as np

class gerhor:
  """
  Classe do Gerador de Horários
  """

  def __init__(self) -> None:
    """
    Inicialização de variáveis essenciais
    """

    self.p : dict = dict()
    self.h : dict = dict()

  def get_input(self) -> None:
    """
    Gravar dados de entrada
    """

    # Input da quantidade de períodos diários
    p = int(input('Qual a quantidade de períodos por dia?\n').strip())

    # Input dos nomes das turmas
    n_ts : list[str] = input('Liste os nomes das turmas (Use espaços para separar as turmas, não vírgulas):\n').strip().split()

    # Inicialização da lista dos horários
    for n_t in n_ts: self.h[n_t] = [[list() for _ in range(p)] for _ in range(5)]

    # Input dos nomes dos professores
    n_ps : list[str] = input('Liste os nomes dos(as) professores(as) (Use espaços para separar os professores, não vírgulas):\n').strip().split()

    # Inicialização das listas dos professores + Input dos dados dos professores
    for n_p in n_ps:
        self.p[n_p] = { 'turmas & disc.' : list[tuple[str, str]](),
                        'horas semanais' : float }

        print(f'\nResponda sobre o(a) professor(a) {n_p}:')
        
        # Input dos nomes das turmas e disciplinas
        self.p[n_p]['turmas & disc.'] = list(map( lambda x : tuple(x.split('_')), input('Turmas & disciplinas (separadas por um _. Ex.: 1ºA_Química 3ºC_Física) que leciona (Use espaços para separar as turmas & disciplinas, não vírgulas):\n').strip().split() ))

        # Input da quantidade de períodos de trabalho        
        self.p[n_p]['horas semanais'] = float(input('Quantidade de períodos de trabalho por semana:\n').strip())

    ...
    # Dados de debug
    print(self.p)

  def allocate_h(self) -> None:
    """
    Alocar horários
    """

    def ch_p(pro : str) -> int:
      """
      Contar quantos períodos o professor leciona
      """

      c : int = 0

      # Para cada turma, para cada dia e para cada período
      for tur in self.t.values():
        for dia in tur:
          for per in dia:
            # Contar quantos são do professor
            if per and per.split('_')[0] == pro: c += 1

      return c

  def valloc(dia : int, pro : str, tur : str, per : int, h_s : int) -> bool:
      """
      Verificar se a alocação é possível
      """

      # Verificar se o horário foi alocado
      if self.h[tur][dia][per]: return False

      # Verificar se o professor já excedeu a quantidade de períodos semanais
      if ch_p(pro) >= h_s: return False
      
      # Verificar se o professor dá aula em outra turma
      for t, h_t in self.h.items():
        if h_t[dia][per] and h_t[dia][per].split('_')[0] == pro: return False

      # Caso esteja disponível
      return True
    
    def dalloc(dia: int, pro : str, dis : str, tur : str, per : int) -> None:
      """
      Fazer a alocação
      """
      
      # Alocar o período no dia e turma para o professor
      self.h[tur][dia][per] = pro+'_'+dis

    # ATENÇÃO ! OBS:
    #
    #  O algoritmo a seguir NÃO FUNCIONA para todos os casos e NÃO ESTÁ PRONTO
    #  Esta primeira versão irá somente testar se dá pra fazer uma verificação se um horário já foi alocado e alocar se sim
    #  Caso não dê para encaixar de primeira, o algoritmo teria que refazer algo e tentar outra possibilidade
    #  Existem inúmeras formas de fazer um algoritmo assim
    #  Isso é só uma ideia do que virá a ser o protótipo de uma parte do que poderia ser um BackTracking
    #  Olha o quão no início isso tá!

    # Para cada professor, fazer alocação
    for p, d in self.p.items():
      tnd : list[tuple[str, str]] = d['turmas & disc.']
      hs : float = d['horas semanais']

      # Para cada turma e disciplina
      for tur, dis in tnd:
        ...

        # Para cada dia
        for dia in range(5):

          # Para cada período
          for per in range(len(tur)):
          
            # Alocando se der
            if valloc(dia, p, tur, per, hs): dalloc(dia, p, dis, tur, per)

    ...
    # Dados de debug
    for t, h_t in self.h.items():
        print(f'\n{t}')
        print(h_t)

  def main(self) -> None:
    """
    Função principal
    """

    # Obtendo os dados da entrada padrão
    self.get_input()
    self.allocate_h()
    ...
    

if __name__ == '__main__':
  gerhor().main()
