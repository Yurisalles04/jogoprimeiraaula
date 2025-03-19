🚀 Cosmo Clash Shooter - Space Arcade Game
Cosmo Clash Shooter is a retro arcade game where the player controls a spaceship to face waves of enemies in an intergalactic battle. The game features different game modes, with progressively harder levels and a scoring system that automatically saves scores in an SQLite3 database.

🎮 Game Modes

Solo Mode
In Solo Mode, the player faces waves of enemies in three levels, with increasing difficulty as the player progresses:

Level 1:
Speed: 7
Damage: 7
Time limit: 30 seconds
Level 2:
Speed: 9
Damage: 8
Time limit: 25 seconds
Level 3:
Speed: 10
Damage: 15
Time limit: 60 seconds
Competitive Mode
In Competitive Mode, two players compete to get the highest score. Both face the same waves of enemies and can perform attack and defense actions to defeat them more quickly.

Cooperative Mode
In Cooperative Mode, two players collaborate to defeat enemies together, with a joint score. Cooperation between players is essential to maximize the score and survival.

🔧 Main Features

Score Recording: Scores are automatically saved in an SQLite3 database, allowing players to track their progress and improve performance over time.
Dynamic Gameplay: Quick and precise controls for a smooth and challenging arcade experience.
Retro Graphics: Classic arcade-style visuals with pixelated graphics that bring back the nostalgia of old-school games.
Sound Effects and Music: Immersive sound effects and a soundtrack that make the experience more exciting and engaging.
💻 Installation Instructions

System Requirements

Python 3.10 or higher
Library: pygame for graphics and sound
Installation Steps

Install Dependencies
To install the required dependencies, run the following command:

bash
Copiar
pip install pygame
Clone the Repository
Clone the game's repository to your local machine:

bash
Copiar
git clone https://github.com/Yurisalles04/jogoprimeiraaula  
cd arcade-space-shooter
Start the Game
After installing the dependencies and cloning the repository, run the following command to start the game:

bash
Copiar
python main.py
The game will start, and you can play it in your terminal or preferred IDE!

🎮 Game Controls

Player 1 (Player 1):
Movement: Use the arrow keys (↑, ↓, ←, →)
Shoot: Press the right Ctrl key
Player 2 (Player 2):
Movement: Use the W, A, S, D keys
Shoot: Press the left Ctrl key
🗃️ Database Structure
The SQLite3 database stores the following information for each score:

Field | Description
date | Date and time the score was recorded
score | Player’s score
The table is used to record scores and track player progress over time.

🚀 Future Improvements
We are constantly working to improve Cosmo Clash Shooter. Some planned improvements include:

Adding new ships and weapons to diversify gameplay.
A global ranking system so players can compare their scores with others worldwide.
An achievement system to reward players based on their performance and skills in the game.
📅 Versions

v1.0: Initial release with basic game modes and main features.
