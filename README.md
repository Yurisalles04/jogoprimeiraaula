🚀 Cosmo Clash Shooter - Jogo de Arcade Espacial
Cosmo Clash Shooter é um jogo de arcade retro onde o jogador assume o controle de uma nave espacial para enfrentar ondas de inimigos em uma batalha intergaláctica. O jogo apresenta diferentes modos de jogo, com níveis progressivos de dificuldade e um sistema de pontuação que grava automaticamente as pontuações em um banco de dados SQLite3.

🎮 Modos de Jogo
1. Modo Sozinho
No Modo Sozinho, o jogador enfrenta ondas de inimigos em três níveis, com aumento de dificuldade conforme o progresso:

Nível 1:

Velocidade: 7
Dano: 7
Tempo limite: 30 segundos
Nível 2:

Velocidade: 9
Dano: 8
Tempo limite: 25 segundos
Nível 3:

Velocidade: 10
Dano: 15
Tempo limite: 60 segundos
2. Modo Competitivo
Aqui, dois jogadores competem para obter o maior score. Ambos enfrentam as mesmas ondas de inimigos e podem realizar ações de ataque e defesa para derrotá-los mais rapidamente.

3. Modo Cooperativo
No Modo Cooperativo, dois jogadores colaboram para derrotar inimigos juntos, com um score conjunto. A colaboração entre os jogadores é essencial para maximizar a pontuação e a sobrevivência.

🔧 Funcionalidades Principais
Gravação de Scores: As pontuações são salvas automaticamente em um banco de dados SQLite3, permitindo acompanhar seu progresso e melhorar seu desempenho ao longo do tempo.
Jogabilidade Dinâmica: Controles rápidos e precisos para uma experiência arcade fluida e desafiadora.
Gráficos Retro: Visual estilo arcade clássico, com gráficos pixelados que resgatam a nostalgia dos jogos antigos.
Sons e Trilha Sonora: Efeitos sonoros imersivos e trilha sonora que tornam a experiência mais emocionante e envolvente.
💻 Instruções de Instalação
Requisitos do Sistema
Python 3.10 ou superior
Biblioteca: pygame para gráficos e sons
Passos para Instalar e Rodar
Instalar as Dependências

Para instalar as dependências necessárias, execute o seguinte comando:

bash
Copiar
pip install pygame
Clonar o Repositório

Clone o repositório do jogo para sua máquina local:

bash
Copiar
git clone https://github.com/Yurisalles04/jogoprimeiraaula
cd arcade-space-shooter
Iniciar o Jogo

Após instalar as dependências e clonar o repositório, basta rodar o seguinte comando para iniciar o jogo:

bash
Copiar
python main.py
O jogo será iniciado e você poderá jogar no seu terminal ou IDE preferida!

🎮 Controles do Jogo
Player 1 (Jogador 1):

Movimento: Use as setas do teclado (↑, ↓, ←, →)
Atirar: Pressione Ctrl da direita
Player 2 (Jogador 2):

Movimento: Use as teclas W, A, S, D
Atirar: Pressione Ctrl da esquerda
🗃️ Estrutura do Banco de Dados
O banco de dados SQLite3 armazena as seguintes informações para cada score:

Campo	Descrição
date	Data e hora do score registrado
score	Pontuação do jogador
A tabela é usada para registrar as pontuações e acompanhar o progresso dos jogadores ao longo do tempo.

🚀 Melhorias Futuras
Estamos constantemente trabalhando para melhorar Cosmo Clash Shooter. Algumas das melhorias planejadas incluem:

Adição de novas naves e armas para diversificar a jogabilidade.
Sistema de classificações globais para que os jogadores possam comparar seus scores com outros ao redor do mundo.
Sistema de conquistas para recompensar os jogadores com base em suas performances e habilidades no jogo.
📅 Versões
v1.0: Lançamento inicial com modos de jogo básicos e funcionalidades principais.
