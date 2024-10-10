# OBS: Lembrar de deletar __pycache__ antes de fazer ``git push``!

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

    # Input dos nomes das turmas
    n_ts : list[str] = input('Liste os nomes das turmas (Use underlines, não espaços):\n').strip().split()

    # Inicialização da lista dos horários
    for n_t in n_ts: self.h[n_p] = list[list[str]]

    # Input dos nomes dos professores
    n_ps : list[str] = input('Liste os nomes dos(as) professores(as) (Use underlines, não espaços):\n').strip().split()

    # Inicialização das listas dos professores + Input dos dados dos professores
    for n_p in n_ps:
        self.p[n_p] = { 'turmas & disc.' : list[tuple[str, str]](),
                        'horas semanais' : float }

        print(f'\nResponda sobre o(a) professor(a) {n_p}:')
        
        # Input dos nomes das turmas e disciplinas
        self.p[n_p]['turmas & disc.'] =
          list(map( lambda x : tuple(x.split('_')),
               input('Turmas & disciplinas (separado por um _. Ex.: 1ºA_Química) que leciona:\n').strip().split() ))

        # Input das horas de trabalho        
        self.p[n_p]['horas semanais'] = float(input('Horas de trabalho por semana:\n').strip())

    ...
    # Dados de debug
    print(self.p)

  def main(self) -> None:
    """
    Função principal
    """

    # Obtendo os dados da entrada padrão
    self.get_input()
    ...
    

if __name__ == '__main__':
  gerhor().main()
