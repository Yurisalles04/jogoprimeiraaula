Cosmo Clash Shooter - README

Sobre o Jogo

Cosmo Clash Shooter é um jogo de arcade onde o jogador controla uma nave espacial para destruir naves inimigas. O jogo possui três modos e salva scores automaticamente em um banco de dados SQLite3.

Modos de Jogo

1. Modo Sozinho

Neste modo, você enfrenta ondas de inimigos em três níveis, onde a diferença está na rapidez e dano dos inimigos:

Nível 1: Velocidade 7, Dano 7, Tempo limite 30 segundos.

Nível 2: Velocidade 9, Dano 8, Tempo limite 25 segundos.

Nível 3: Velocidade 10, Dano 15, Tempo limite 60 segundos.

2. Modo Competitivo

Dois jogadores competem para obter o maior score enfrentando naves inimigas.

3. Modo Cooperativo

Dois jogadores colaboram para derrotar inimigos e somar pontos em um score conjunto.

Funcionalidades Principais

Gravação de Scores: Scores são salvos no SQLite3.

Jogabilidade Dinâmica: Controles ágeis e precisos.

Gráficos Retro: Visual clássico de arcade.

Sons e Trilha Sonora: Efeitos imersivos.

Instruções de Instalação

Requisitos do Sistema:

Python 3.10 ou superior.

Bibliotecas: pygame.

Instale as Dependências:

pip install pygame

Clone o Repositório:

git clone https://github.com/Yurisalles04/jogoprimeiraaula
cd arcade-space-shooter

Inicie o Jogo:

python main.py

Controles do Jogo

Movimento: Teclas de setas ou W, A, S, D

Atirar: Barra de espaço

Pausar: Tecla P

Estrutura do Banco de Dados

O banco de dados SQLite3 salva os seguintes dados:

mode (TEXT: "Sozinho", "Competitivo", "Cooperativo")

date (TEXT, data e hora do score)

Melhorias Futuras

Adição de novas naves e armas.

Classificações globais e sistema de conquistas.