"""
Fichier contenant les principales fonctions gérant la création
et le lancement du jeu Marathon des nombres
Pour la fonction generation operations:
2 niveaux de difficultés, facile et... moins facile (easy and... less easier) ou plutôt moins facile = normal ?
Le niveau normal se lance dès l'enchaînement de 3 bonnes réponses d'affilées au niveau facile
Si 1 mauvaise réponse au niveau normal, retour au niveau facile
Les bonnes réponses au niveau normal rapportent plus de points
En facile probabilité de tomber sur une multiplication: 20%
En normal elle sera de 50%
En normal facile seulement des opérations avec 3 chiffres

Avant ajout du chronomètre, implementation de curses
"""

import curses
from curses import wrapper
from curses.ascii import isdigit
from curses.textpad import Textbox, rectangle
import random
import time

from main import start_menu_app

def marathon_start(stdscr, list_easy, list_normal):
    curses.curs_set(False)
    diff: str = 'easy'  # le jeu démarre de base en facile
    # Système de scoring
    stdscr.clear()
    score_points: int = 0
    score_combo: int = 0
    window_score: curses.window = curses.newwin(2, 70, 0, 33)
    window_score.clear()
    window_score.addstr(f"Score: {score_points}   Combo: {score_combo}")
    window_score.refresh()
    # Bonne réponse en facile = 100 points
    # Bonne réponse en normal = 200 points
    """
    Bonus combo:
    2 = 50 points bonus
    3 = 70
    4 = 100
    5+ = 130
    """
    time_start: float = time.time()
    timer: float = 20.0
    while True:
        if diff == 'easy':
            for ope in list_easy:   
                if ope[2] >= 0 and ope[2] < 4:
                    complete_ope: str = f"Opération: {ope[0]} + {ope[1]} = "
                    result_ope = ope[0] + ope[1]
                elif ope[2] >= 4 and ope[2] < 8:
                    complete_ope: str = f"Opération: {ope[0]} - {ope[1]} = "
                    result_ope = ope[0] - ope[1]
                else:
                    complete_ope: str = f"Opération: {ope[0]} * {ope[1]} = "
                    result_ope = ope[0] * ope[1]
                list_easy.remove(ope)
        elif diff == 'normal':
            for ope in list_normal:
                match ope[3]:
                    case 0:
                        complete_ope: str = f"Opération: {ope[0]} + {ope[1]} + {ope[2]} = "
                        result_ope: int =  ope[0] + ope[1] + ope[2]
                    case 1:
                        complete_ope: str = f"Opération: {ope[0]} + {ope[1]} - {ope[2]} = "
                        result_ope: int =  ope[0] + ope[1] - ope[2]

                    case 2:
                        complete_ope: str = f"Opération: {ope[0]} - {ope[1]} + {ope[2]} = "
                        result_ope: int =  ope[0] - ope[1] + ope[2]

                    case 3:
                        complete_ope: str = f"Opération: {ope[0]} - {ope[1]} - {ope[2]} = "
                        result_ope: int =  ope[0] - ope[1] + ope[2]

                    case 4:
                        complete_ope: str = f"Opération: {ope[0]} * {ope[1]} + {ope[2]} = "
                        result_ope: int =  ope[0] * ope[1] + ope[2]

                    case 5:
                        complete_ope: str = f"Opération: {ope[0]} * {ope[1]} - {ope[2]} = "
                        result_ope: int =  ope[0] * ope[1] - ope[2]

                    case 6:
                        complete_ope: str = f"Opération: {ope[0]} + {ope[1]} * {ope[2]} = "
                        result_ope: int =  ope[0] + ope[1] * ope[2]

                    case 7:
                        complete_ope: str = f"Opération: {ope[0]} - {ope[1]} * {ope[2]} = "
                        result_ope: int =  ope[0] - ope[1] * ope[2]

                    case 8:
                        complete_ope: str = f"Opération: {ope[0]} * {ope[1]} * {ope[2]} = "
                        result_ope: int =  ope[0] * ope[1] * ope[2]
                list_normal.remove(ope)


        if diff == 'easy':
            window_anwser: curses.window = curses.newwin(1, 9, 0, 19)
            window_ope: curses.window = curses.newwin(12, 18, 0, 0)
        else:
            window_anwser: curses.window = curses.newwin(1, 5, 0, 23)
            window_ope: curses.window = curses.newwin(12, 22, 0, 0)
        window_ope.clear()
        window_anwser.clear()
        window_ope.addstr(f"{complete_ope}")
        window_ope.refresh()
        box_answer = Textbox(window_anwser)
        box_answer.edit()
        user_answer: str = box_answer.gather()
        window_anwser.refresh()
        time_end: float = time.time()
        time_passed: float = time_end - time_start
        if not time_passed >= timer:
            try:
                user_answer_int: int = int(user_answer)
                if user_answer_int == result_ope:
                    if diff == 'easy':
                        score_points += 100
                    elif diff == 'normal':
                        score_points += 200
                    score_combo += 1
                else:
                    score_combo = 0
                if score_combo == 2:
                    score_points += 50
                elif score_combo == 3:
                    score_points += 70
                elif score_combo == 4:
                    score_points += 100
                elif score_combo >= 5:
                    score_points += 130

                if score_combo >= 4:
                    diff = 'normal'
                else:
                    diff = 'easy'
                window_score.clear()
                window_score.addstr(f"Score: {score_points}   Combo: {score_combo}")
                window_score.refresh()
            except ValueError:
                diff = 'easy'
                window_score.clear()
                window_score.addstr(f"Score: {score_points}   Combo: {score_combo}")
                window_score.refresh()
        else:
            window_score.clear()
            window_ope.clear()
            window_anwser.clear()
            window_score.addstr(f"Score: {score_points}   Combo: {score_combo}")
            window_ope.addstr(0, 0, "Fin de la partie !")
            window_ope.addstr(2, 0, "Enregistrer score", curses.A_REVERSE)
            window_ope.addstr(3, 0, "Rejouer")
            window_ope.addstr(4, 0, "Menu principal")
            window_score.refresh()
            window_ope.refresh()
            end_game_index: int = 0
            while True:
                window_anwser.clear()
                select_option: int = window_anwser.getch()
                window_anwser.refresh()
                # Système de selection d'options
                window_ope.clear()
                if select_option == curses.KEY_UP:
                    if end_game_index != 0:
                        end_game_index -= 1
                elif select_option == curses.KEY_DOWN:
                    if end_game_index != 2:
                        end_game_index += 1
                elif select_option == 10:
                    match end_game_index:
                        case 0:
                            window_ope.clear()
                            window_score.clear()
                        case 1:
                            window_ope.clear()
                            window_score.clear()
                            curses.endwin()
                            wrapper(marathon_generation_operations)
                        case 2:
                            window_ope.clear()
                            window_score.clear()
                            curses.endwin()
                            start_menu_app()

                window_ope.addstr(0, 0, "Fin de la partie !")
                if end_game_index == 0:
                    window_ope.addstr(2, 0, "Enregistrer score", curses.A_REVERSE)
                else:
                    window_ope.addstr(2, 0, "Enregistrer score")

                if end_game_index == 1:
                    window_ope.addstr(3, 0, "Rejouer", curses.A_REVERSE)
                else:
                    window_ope.addstr(3, 0, "Rejouer")

                if end_game_index == 2:
                    window_ope.addstr(4, 0, "Menu principal", curses.A_REVERSE)
                else:
                    window_ope.addstr(4, 0, "Menu principal")
                window_score.clear()
                window_score.addstr(f"Score: {score_points}   Combo: {score_combo}")
                window_score.refresh()
                window_ope.refresh()

# Il reste le menu de fin de partie, avec possibilité d'enregistrer son score
# Puis après avoir accepté ou refusé, soit rejouer soit retour menu principal


def marathon_generation_operations(stdscr) -> None:
    curses.curs_set(False)
    ope_list_easy: list[list] = []
    ope_list_normal: list[list] = []
    stdscr.clear()

    for _ in range(100):
        first_number: int = random.randint(0, 9)
        second_number: int = random.randint(0, 9)
        ope_sign: int = random.randint(0, 9)
        ope_complete_easy: list[int] = [first_number, second_number, ope_sign]
        ope_list_easy.append(ope_complete_easy)
    
    for _ in range(100):
        first_number: int = random.randint(0, 9)
        second_number: int = random.randint(0, 9)
        third_number: int = random.randint(0, 9)
        ope_sign: int = random.randint(0, 8)
        ope_complete_normal: list[int] = [first_number, second_number, third_number, ope_sign]
        ope_list_normal.append(ope_complete_normal)
    marathon_start(stdscr=stdscr, list_easy=ope_list_easy, list_normal=ope_list_normal )

    




