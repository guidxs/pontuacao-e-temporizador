import time

#Sistema de Pontuação com Histórico
class SistemaPontuacaoHistorico:
    def __init__(self):
        #Inicializa a pontuação e o histórico de ações.
        self.pontuacao = 0
        self.historico = []

    def adicionar_pontos(self, pontos, descricao=""):
        #Adiciona pontos e registra a ação no histórico.
        self.pontuacao += pontos
        self.historico.append(f"+{pontos} pontos: {descricao}")

    def remover_pontos(self, pontos, descricao=""):
        #Remove pontos e registra a ação no histórico.
        self.pontuacao = max(0, self.pontuacao - pontos)
        self.historico.append(f"-{pontos} pontos: {descricao}")

    def exibir_pontuacao(self):
        #Retorna a pontuação atual e o histórico de ações.
        return f"Pontuação Atual: {self.pontuacao}\nHistórico:\n" + "\n".join(self.historico)

#Exemplo de uso do Sistema de Pontuação com Histórico
sistema = SistemaPontuacaoHistorico()
sistema.adicionar_pontos(50, "Completou o módulo 1")  #Adiciona 50 pontos
sistema.remover_pontos(10, "Erro no teste")           #Remove 10 pontos
print(sistema.exibir_pontuacao())                     #Saída: Pontuação Atual: 40, Histórico: [...]

#Temporizador utilizando time.time()
def temporizador_tempo(n):
    
    #Temporizador usando time.time().
    #Retorna o tempo de execução para o cálculo da soma dos primeiros 'n' números.
    
    tempo_inicial = time.time()
    total = sum(range(n))  #Operação simulada
    tempo_final = time.time()
    tempo_decorrido = tempo_final - tempo_inicial
    return tempo_decorrido

""" 
def temporizador_tempo_otimizado(n):
    tempo_inicial = time.time()
    total = n * (n - 1) // 2  #Operação O(1) usando fórmula direta
    tempo_final = time.time()
    tempo_decorrido = tempo_final - tempo_inicial
    return tempo_decorrido
"""


#Exemplo de uso do Temporizador
n = 100000000  # Se adicionarmos mais um zero, o tempo vai para 20 segundos
print(f"Tempo de execução usando time.time(): {temporizador_tempo(n)} segundos")