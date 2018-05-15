# pp-code
24 points game injected into ICS Chat system (NYUSH)


Evan and Sherry’s NYU Shanghai ICS Presentation Project (Spring 2018)

Using a chat system already implemented, we injected a 24 Points game (https://en.wikipedia.org/wiki/24_Game) into it, which can be activated and played by typing the command “play 24” while in chat.
The main game is in 24_game.py, and the main injection occurs inside client_state_machine.py .
To run the chat system, in terminal, first you must open the server (chat_server.cpython-36.pyc for python 3.6 for example), then you must in other terminal windows open chat clients (chat_cmdl_client.py).
——————

Game details:
24 Points, or 24点 is a game where players try to get the number 24 by forming an expression from four cards or numbers, using the operators "+", "-", "*", "/". (e.g. given [2], [5], [7], [9]. One solution would be 5*7-2-9=24)

In our game, you can also use python’s built-in operators: ** (exponent) // (integer division) and % (modulus), and we even made factorial work if you did !(A) or !(A+b) etc..

Syntax should be a valid python expression.

If you press skip, the game will show a solution. And if you enter incorrectly and time has already passed 60 seconds for the round, the game will show a solution as well and then push you to the next round.

All rounds are solvable. Although some are more convoluted than others, with solutions requiring advanced operators like **, //, %, or !


For best experience, I used pyautogui to make sending scores between clients more compact, and also as a padding to fix some unexplainable bugs that probably stem from the chat backend.
If you wish, you can install it with instructions from here: https://pyautogui.readthedocs.io/en/latest/install.html. Though, even if you don’t, you can still play the game!

We also have a demo video here on vimeo: https://vimeo.com/269791932
