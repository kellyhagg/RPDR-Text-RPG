"""
Main game file.
"""


import boards
import controls
import challenges
import helpers
from character import Character


def game():
    """
    Run RuPaul's (Text-Based) Drag Race!

    :postcondition: a great time
    """
    player = Character(input("What is the name of your Drag Persona?\n"))
    helpers.deliver_introduction(player)

    while not player.get_achieved_goal():
        boards.display_board(player)
        controls.move_character(player)
        challenges.run_challenges(player)
    return print('The END.')


def main():
    """
    Drive the program.
    """
    game()


if __name__ == '__main__':
    main()
