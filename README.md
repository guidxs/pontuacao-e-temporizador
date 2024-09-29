# Sistema de Treinamento para Médicos Residentes

## Faculdade de Informática e Administração  
**Curso:** Engenharia de Software  
**Sala:** 2ESPF  

### Projeto: Dynamic Programming - SPRINT 3

### Integrantes:
- **Guilherme Doretto Sobreiro** – RM: 99674
- **Henrique Lima** – RM: 551528
- **Ricardo Akira** – RM: 551447
- **Guilherme Fazito** – RM: 550539
- **Augusto Milreu** – RM: 98245 

## Descrição do Projeto

O projeto consiste em desenvolver um **Sistema de Treinamento para Médicos Residentes**, com funcionalidades que incluem um sistema de pontuação com histórico e um temporizador para monitorar a eficiência do treinamento. As funcionalidades são desenvolvidas e analisadas em termos de eficiência computacional, com a utilização de diferentes abordagens para comparação.

## Diagrama de Casos de Uso

![Diagrama](https://github.com/user-attachments/assets/ca7db570-f003-4827-a010-4d79bbb9d075)

O diagrama de casos de uso ilustra as interações entre os usuários e o sistema de treinamento, abrangendo:

### Portal da Plataforma:

**Treinador:**  
- **Cadastro:** Registro de novos residentes.
- **Login:** Acesso seguro ao sistema.
- **Consulta de Estatísticas:** Visualização do tempo de treinamento e pontuação acumulada dos residentes.

### Plataforma VR (Treinamento):

**Médico Residente:**  
- **Jogo:** Simulações práticas de treinamento.
- **Objetivos e Temporizador:** Metas a serem alcançadas com monitoramento do tempo.
- **Tutoriais:** Orientações para facilitar o uso da plataforma.
- **Configuração:** Personalização da experiência de treinamento.

O sistema se conecta ao Banco de Dados para armazenar todas as informações relevantes, permitindo o acompanhamento detalhado do desempenho dos residentes.

## Documentação

### 1. Introdução

Este artigo aborda a implementação de um sistema de pontuação com histórico e a medição de tempo utilizando a biblioteca `time` do Python. O sistema de pontuação gerencia as ações realizadas pelos usuários, fornecendo feedback imediato. O temporizador mede o tempo necessário para a execução das operações, importante para monitorar a eficiência e o progresso dos exercícios. Ambas as funções são implementadas e analisadas em termos de eficiência computacional, discutindo os benefícios e desvantagens de diferentes abordagens.

### 2. Metodologia

1. **Sistema de Pontuação com Histórico:**  
   Implementamos uma classe que armazena a pontuação de um aluno e mantém um histórico das ações realizadas. A complexidade das operações de adição e remoção de pontos é `O(1)`, enquanto a exibição da pontuação tem complexidade `O(n)`, onde n é o número de ações no histórico.
   
![Captura de tela 2024-09-28 225031](https://github.com/user-attachments/assets/c180e455-bf4f-4663-b5f1-a37363989b01)

2. **Temporizador:**  
   Implementamos uma função que mede o tempo de execução de uma operação simulada utilizando `time.time()`. A operação simulada consiste no cálculo da soma dos primeiros `n` números, com complexidade `O(n)`. Também apresentamos uma implementação otimizada que utiliza uma fórmula aritmética para calcular a soma, reduzindo a complexidade para `O(1)`.

O(n)

![Captura de tela 2024-09-28 223654](https://github.com/user-attachments/assets/99cf05c2-c6e9-43c8-b1f2-67d640bbefab)

O(1)

![Captura de tela 2024-09-28 224113](https://github.com/user-attachments/assets/0d6883da-0455-4739-839a-f84034c9f949)

3. **Comparação de Implementações:**  
   Comparamos as implementações do temporizador, observando um desempenho linear em uma forma de implementação e constante em outra, analisando possíveis resultados e limitações em termos de consumo de memória e precisão na medição de tempo.

### 3. Resultados

#### 3.1 Sistema de Pontuação com Histórico

- **Adicionar Ponto:** `O(1)`
- **Remover Ponto:** `O(1)`
- **Exibir Pontuação:** `O(n)`
- **Eficiência:** A implementação é eficiente para manter tanto as pontuações quanto o histórico. No entanto, à medida que o histórico cresce, a operação de exibição pode se tornar mais lenta e consumir mais memória.
- **Possíveis Problemas:** O histórico pode crescer indefinidamente, aumentando o uso de memória. Não há validação de entrada para a pontuação, o que pode causar erros se valores não numéricos forem inseridos.

#### 3.2 Temporizador com `time.time()`

- **Operação Simulada:** `sum(range(n))`
- **Complexidade O(n):** Cresce proporcionalmente ao valor de `n`.
- **Tempo de execução medido para `n = 100.000.000`:** Aproximadamente 2 segundos.
- **Implementação Otimizada:** Utilizando a fórmula aritmética `n*(n-1)//2` com complexidade `O(1)`.
- **Tempo de execução para `n = 100.000.000`:** Aproximadamente 0 segundos (tempo praticamente imperceptível).

- **Possíveis Problemas:** Para operações muito rápidas, `time.time()` pode não ter precisão suficiente. A implementação otimizada só é válida para operações específicas, como somas aritméticas. Para outras operações, a complexidade continua sendo `O(n)`.

### 4. Conclusão

As implementações apresentadas destacam a importância de escolher corretamente as estruturas de dados e algoritmos para cada funcionalidade:

1. **Sistema de Pontuação com Histórico:**  
   A implementação otimizada para adição e remoção de pontos tem complexidade `O(1)`, mas a exibição do histórico com complexidade `O(n)` pode se tornar problemática com o aumento das ações. Limitar o tamanho do histórico ou adicionar uma função para limpá-lo periodicamente pode mitigar esse problema.

2. **Temporizador com `time.time()`:**  
   A implementação original com `sum(range(n))` tem complexidade linear (`O(n)`), enquanto a versão otimizada, que usa uma fórmula aritmética, reduz a complexidade para `O(1)`. Esta otimização, porém, é válida apenas para somas de sequências aritméticas.

3. **Comparação:**  
   A diferença entre `O(n)` e `O(1)` é significativa, especialmente com grandes valores de `n`. Contudo, é crucial entender o contexto para aplicar a otimização correta. Avaliar constantemente a complexidade computacional é essencial para desenvolver sistemas eficientes e escaláveis.

Por fim, a análise reforça a importância de explorar diferentes abordagens para resolver problemas e otimizar o desempenho do sistema.
