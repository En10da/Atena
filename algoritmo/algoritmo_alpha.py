"""
Algoritmo do gerador de horários do Projeto Atena

Sumário Estendido
-----------------
Versão Alpha - Ainda nas implementações iniciais!

Inclui: Classe para o input dos dados e geração de horários
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
        self.p[n_p] = { 'turmas & disc.' : [],
                        'horas semanais' : 0.0 }

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

    def ch_p(pro : str, t : dict) -> int:
      """
      Contar quantos períodos o professor leciona
      """

      c : int = 0

      # Para cada turma, para cada dia e para cada período
      for tur in t.values():
        for dia in tur:
          for per in dia:
            # Contar quantos são do professor
            if per and per.split('_')[0] == pro: c += 1

      return c

    def valloc(dia : int, pro : str, tur : str, per : int, h_s : int, h : dict) -> bool:
      """
      Verificar se a alocação é possível
      """

      # Verificar se o horário foi alocado
      if h[tur][dia][per]: return False

      # Verificar se o professor já excedeu a quantidade de períodos semanais
      if ch_p(pro, h) >= h_s: return False
      
      # Verificar se o professor dá aula em outra turma
      for t, h_t in h.items():
        if h_t[dia][per] and h_t[dia][per].split('_')[0] == pro: return False

      # Caso esteja disponível
      return True

    def vvag(t : dict) -> bool:
      """
      Verificar aulas vagas
      """

      for t_i in t.values():
        for d in t_i:
          for dp in d:
            if not dp: return True

      return False

    def verrors(t : dict) -> int:
      """
      Verificar quantos erros há
      """

      c : int = 0

      # Para cada professor
      for p_i in self.p:

        # Verificar quantos professores tem mais ou menos trabalho que o necessário
        if ch_p(p_i, self.p, t) != self.p[p_i]['horas semanais']: c += 1

        for tur, dis in self.p[p_i]['turmas & disc.']:

          tmp = False

          # Para cada turma
          for t_i_n, t_i in t.items():
            # Para cada dia e período
            for d in t_i:
              for dp in d:

                # Verificar quantas turmas tem aulas vagas
                if not dp: c += 2

                # Verificar se todas as matérias estão sendo dadas
                if dp and not tmp and dp.split('_')[1] == dis and dp.split('_')[0] == p_i and t_i_n == tur: tmp = True

          if not tmp: c += 2

      return c

    def backtrack(t : dict, dia : int, per : int, pro : str, dis : str, tur : str) -> tuple[int, dict[str,
    list[list[str]]]]:
      """
      Backtracking para o algoritmo funcionar
      """

      # Se todos os horários estiverem alocados, retornar contagem de erros e os horários
      if not vvag(t) or not (0 <= dia < 5) or not (0 <= per < len(list(t.values())[0][0])): return verrors(t), t

      r : tuple[int, dict[str, list[list[str]]]]

      # Se não der pra alocar, retornar contagem de erros e os horários
      if not valloc(dia, pro, tur, per, self.p[pro]['horas semanais'], t): return verrors(t), t
      # Se der pra alocar, alocar
      t[tur][dia][per] = pro+'_'+dis

      r = verrors(t), t

      # Para cada professor e disciplina
      for npro, npro_d in self.p.items():
        for ndis in npro_d['turmas & disc.']:

          # Testar outras opções
          tmp = backtrack(t, dia+1, per, npro, ndis[1], ndis[0])
          tmp2 = backtrack(t, dia, per+1, npro, ndis[1], ndis[0])

          # Obter a ótima
          if tmp[0] > tmp2[0]: tmp = tmp2
          if r[0] > tmp[0]: r = tmp

      return r

    r = None

    # Para cada professor e disciplina
    for npro, npro_d in self.p.items():
      for ndis in npro_d['turmas & disc.']:

        # Testar opções
        tmp = backtrack(self.h, 0, 0, npro, ndis[1], ndis[0])

        # Obter a ótima
        if not r or r[0] > tmp[0]: r = tmp

    self.h = r[1]

    # Dados de debug
    print(r[0], '\n')
    for t, h_t in self.h.items():
      print(f'\n{t}')
      print(h_t)

  def main(self) -> None:
    """
    Função principal
    """

    # Obtendo os dados da entrada padrão
    self.get_input()
    # Alocando os dados
    self.allocate_h()
    ...
    

if __name__ == '__main__':
  gerhor().main()
