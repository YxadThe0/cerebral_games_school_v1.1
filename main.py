"""
Menu de l'app Cerebral games school
Ajout du typage
Simplification du code avec en cadeau de la documentation like Google yeah
Interface plus intuitive, notamment déplacement par les flèches directionnelles
Commit via commande git
Système de login avec pseudo et mot de passe
"""

import curses, sys
from curses import wrapper
import games.marathon
stdscr: curses.window = curses.initscr()

# Commencer par le menu de l'app
# Créer la selection des possibilités via les touches directionnelles
# Pour cela


def main(stdscr):
    curses.curs_set(False)
    selected_games: bool = False
    selected_classements: bool = False
    selected_exit: bool = False


    stdscr.clear()
    stdscr.addstr("Bienvenue dans la Cerebral Games School, que souhaitez-vous faire ?")
    win: curses.window = curses.newwin(10, 100, 2, 0)
    stdscr.refresh()
    active_index: int = 0
    win.clear()
    win.addstr("Jouer à un jeu\n", curses.A_REVERSE)
    win.addstr("Voir les classements\n")
    win.addstr("Quitter l'application")
    win.refresh()
    while True:
        select_user: int = stdscr.getch()
        if select_user == 10:   # code ASCII pour 'Entrée'
            win.clear()
            if active_index == 0:
                selected_games: bool = True
                selected_classements: bool = False
                selected_exit: bool = False
            elif active_index == 1:
                selected_games: bool = False
                selected_classements: bool = True
                selected_exit: bool = False   
            elif active_index == 2:
                selected_games: bool = False
                selected_classements: bool = False
                selected_exit: bool = True             
            break

        elif select_user == curses.KEY_UP: # code ASCII pour 'flèche haut' 38
            if active_index != 0:
                active_index -= 1

        elif select_user == curses.KEY_DOWN: # code ASCII pour 'flèche bas' 40
            if active_index != 2:
                active_index += 1 

        win.clear()
        if active_index == 0:
            win.addstr("Jouer à un jeu\n", curses.A_REVERSE)
        else:
            win.addstr("Jouer à un jeu\n")
        if active_index == 1:
            win.addstr("Voir les classements\n", curses.A_REVERSE)
        else:
            win.addstr("Voir les classements\n")
        if active_index == 2:
            win.addstr("Quitter l'application", curses.A_REVERSE)
        else:
            win.addstr("Quitter l'application")             
        win.refresh()
    stdscr.clear()
    win.clear()
    if selected_games:
        curses.endwin()
        stdscr.refresh()
        wrapper(selection_games_menu)
    if selected_classements:
        win.addstr('Choississez un classement :\n')
        win.getch()
    if selected_exit:
        sys.exit()
    stdscr.refresh()
    win.refresh()



def selection_games_menu(stdscr):    
    curses.curs_set(False)
    selected_marathon: bool = False
    selected_sprint: bool = False
    selected_return_main_menu: bool = False
    win: curses.window = curses.newwin(15, 150, 0, 0)
    win.addstr('Choississez un jeu :\n\n')
    win.addstr("Marathon des nombres\n", curses.A_REVERSE)
    win.addstr("Sprint des lettres\n")
    win.addstr("Retour au menu précédent\n\n")
    win.addstr("Répondez vite et bien aux opérations et engranger un maximum de point !")

    win.refresh()

    active_index: int = 0
    while True:
        select_game_user: int = stdscr.getch()
        win.clear()
        win.addstr('Choississez un jeu :\n\n')

        if select_game_user == curses.KEY_UP:
            if active_index != 0:
                active_index -= 1
        elif select_game_user == curses.KEY_DOWN:

            if active_index != 2:
                active_index += 1

        elif select_game_user == 10:
            if active_index == 0:
                selected_marathon: bool = True
                selected_sprint: bool = False
                selected_return_main_menu: bool = False

            elif active_index == 1:
                selected_marathon: bool = False
                selected_sprint: bool = True
                selected_return_main_menu: bool = False
    
            elif active_index == 2:
                selected_marathon: bool = False
                selected_sprint: bool = False      
                selected_return_main_menu: bool = True
                 
            break
        if active_index == 0:
            win.addstr("Marathon des nombres\n", curses.A_REVERSE)
        else:
            win.addstr("Marathon des nombres\n")
        if active_index == 1:
            win.addstr("Sprint des lettres\n", curses.A_REVERSE)
        else:
            win.addstr("Sprint des lettres\n")
        if active_index == 2:
            win.addstr("Retour au menu précédent\n\n", curses.A_REVERSE)
        else:
            win.addstr("Retour au menu précédent\n\n")

        match active_index:
            case 0:
                win.addstr("Répondez vite aux opérations et enchaîner les bonnes réponses\npour engranger un maximum de points !\n")
            case 1:
                win.addstr("Démontrer votre rapidité au clavier en écrivant\nle plus rapidement possible les différentes phrases affichées !\n")
            case 2:
                win.addstr("Retourner au précédent menu\n")

        win.refresh()
    stdscr.refresh()
    win.clear()
    stdscr.clear()
    if selected_marathon:
        wrapper(games.marathon.marathon_generation_operations)
    elif selected_sprint:
        stdscr.addstr("Démarrage du sprint dans 3, 2, 1...")
        stdscr.refresh()
        stdscr.getch()
    elif selected_return_main_menu:
        stdscr.refresh()
        wrapper(main)

def start_menu_app():
    wrapper(main)

if __name__ == '__main__':
    start_menu_app()