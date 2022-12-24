"""
Create the player player and give them the introduction
"""


import json
import random
import boards
import character
from character import Character
import challenges
from game import game


def add_numbers(first, second):
    return first + second


def deliver_introduction(player: Character) -> None:
    """
    Deliver introduction to player.

    :param player: the player
    :precondition: player must be a Character
    :postcondition: print the game introduction
    """
    filename = './json_files/introduction.json'
    with open(filename) as file_object:
        introduction = json.load(file_object)

    print(f"{introduction[0]}ConDRAGulations {player.get_name()},{introduction[1]}")


def apply_power_up(stat: tuple, value: int) -> dict:
    """
    Calculate new value to be assigned to a stat.

    :param stat: a tuple containing a string representing the name of a stat and an integer
    representing the value assigned to that stat
    :param value: an integer
    :precondition: stat must be a tuple and value must be an integer
    :postcondition: calculate the new value of the second element in the stat tuple after the
    addition of value
    :return: a dictionary with a key which is equal to the first element of the stat tuple with a
    value of 0 if adding the value parameter to it would have made it negative, else a dictionary
    with a key which is equal to the first element of the stat tuple with a value that is equal to
    the second element of the stat tuple with the value parameter added to it
    >>> apply_power_up(('Charisma', 15), 34)
    {'Charisma': 49}
    >>> apply_power_up(('Nerve', 4), -4)
    {'Nerve': 0}
    >>> apply_power_up(('Uniqueness', 12), -20)
    {'Uniqueness': 0}
    """
    if stat[1] + value < 0:
        return {stat[0]: 0}
    return {stat[0]: stat[1] + value}


def power_enemy_up_or_down(queen: dict, stat_changes: tuple) -> dict:
    """
    Update and print changes to stats for either the player or the enemy.

    :param queen: a dictionary representing a queen name and stats
    :param stat_changes: a list containing four integers
    :postcondition: adjusts values stored inside queen dictionary either up or down depending
    on whether the integers in values are positive or negative
    :return: dictionary representing the queen with their stats changed to reflect game events
    """
    stat_names = ['charisma', 'uniqueness', 'nerve', 'talent']
    initial_stats = queen.get('stats')
    index = 0

    stats = tuple(map(add_numbers, queen.get('stats'), stat_changes))

    for number in stat_changes:
        if number < 0:
            print(f'Your {stat_names[index]} has decreased by {abs(number)} to '
                  f'{initial_stats[index] + number}!')
        elif number > 0:
            print(f'Your {stat_names[index]} has increased by {abs(number)} to '
                  f'{initial_stats[index] + number}!')
        index += 1

    return queen


def you_win(player: Character, enemy_name: str or None, challenge_name: str) -> dict:
    """
    Perform win events for player.

    :param player: a dictionary representing the player character with the keys 'Name'
    and 'completed_lip_sync' present, with the value assigned to 'Name' being a string and the
    value assigned to 'completed_lip_sync' being a Boolean
    :param enemy_name: a non-empty string representing an NPC name or None if there is
    no NPC
    :param challenge_name: a non-empty string
    :precondition: player must be a Character, enemy_name must be either a string or None,
    and challenge_name must be a string
    :postcondition: print specified win statements depending on the string passed as challenge_name
    :postcondition: change achieved_goal value to True if challenge_name is equal to 'rupaul'
    :return: player with their stats changed to reflect game events
    """
    if challenge_name == 'read_battle':
        print('You win!')
        print(f"{enemy_name} slinks away, clearly feeling the shade of it all.")
        print('You regain composure after all the reads.')
        increase = random.randint(8, 12)
        return power_enemy_up_or_down(player, [0, 0, 2, increase], False)
    if challenge_name == 'makeover_challenge':
        print(f"\n\"ConDRAGulations {player['Name']} and {enemy_name},\nyou are the"
              f" winners of this mini challenge!\"\n")
        increase = random.randint(10, 15)
        return power_enemy_up_or_down(player, [0, increase, 0, increase], False)
    if challenge_name == 'werk_room':
        print("\nYou are now level 2!")
        # power_enemy_up_or_down(player, [random.randint(30, 40), random.randint(30, 40),
                                     random.randint(30, 40), 15], False)
        print(f"\nRuPaul's voice echoes through the room: \n\n\"{player['Name']}, "
              f"please make your way to the Main Stage. "
              f"\nYou have been chosen to take part in a Lip Sync for Your Legacy!\"\n"
              f"\nYou quickly make your way to the stage, \nthe potential lip sync songs spinning"
              f" through your head.")
        return boards.set_board(player)
    if challenge_name == 'lip_sync':
        print(f"RuPaul's voice echoes: 'ConDRAGulations {character['Name']}, "
              f"you're a winner baby!'\nYou feel your inner saboteur melting away.")
        print("\nYou are now level 3!")
        character['completed_lip_sync'] = True
        power_enemy_up_or_down(character, [random.randint(30, 40), random.randint(30, 40),
                                           random.randint(30, 40), 20], False)
        boards.set_board(character)
        print(f"\nYou are ushered towards the Judge's Panel.")
        return character
    if challenge_name == 'rupaul':
        print(f"\nRuPaul's face breaks into a smile\n\"ConDRAGulations {character['Name']}, "
              f"you're the winner baby!\"\nTriumphant music starts up as confetti begins to "
              f"fall from the ceiling.\n\nRuPaul says,\"You are now the Queen of the Mother Tucking"
              f" UNIVERSE!\"\n\nMother continues as she places a massive bejeweled crown upon your"
              f" head and a\nmatching scepter in your hand. You sob with happiness.\n\nYou"
              f" know that this... is the beginning of the rest of your life.\n")
        character['achieved_goal'] = True
        return character


def check_for_level_up(character: dict) -> dict:
    """
    Determine whether the player player has leveled up.

    :param character: a dictionary representing the player player with the keys
    'location', 'Talent', and 'level' present, with the value assigned to 'location' being a string
    and the values assigned to 'Talent' and 'level' being positive integers
    :precondition: player must be a dictionary
    :postcondition: determine whether the player player has leveled up based on the values
    currently assigned to the 'location' and 'Talent' keys
    :postcondition: pass player dictionary to function which levels up the player if the
    conditions are met
    :return: dictionary representing the player player
    """
    if character['location'] == 'werk_room' and character['Talent'] >= 40:
        character['level'] += 1
        you_win(character, None, 'werk_room')
    return character


def check_if_dead(character: dict) -> dict:
    """
    Determine whether player player has lost all of their health ('Nerve')

    :param character: a dictionary with the keys 'Nerve' and 'Name' present, with the value
    assigned to 'Nerve' being an integer and the value assigned to 'Name' being a string
    :precondition: player must be a dictionary
    :postcondition: determine whether the value assigned to 'Nerve' is 0 or less
    :postcondition: print loss statement, clears player dictionary, and restarts game if 'Nerve'
    is 0 or less
    :return: dictionary representing the player
    """
    if character['Nerve'] <= 0:
        print(f"\nYou hear RuPaul's voice:\n\n\"{character['Name']},\nThank you for bringing your "
              f"Charisma, Uniqueness, Nerve, and Talent to the\ncompetition. "
              f"But this is not your time.\nNow.... Sashay Away.\"\n"
              f"--------------------------------------------------------------------------------")
        character.clear()
        game()
    return character


def main():
    """Drive the program."""
    new_character = make_character(input('What is the name of your Drag Persona?\n'))
    print(f"Your new player {new_character['Name']} has been created.")
    deliver_introduction(new_character)
    print(new_character)
    character = {'Charisma': 15, 'Uniqueness': 14, 'Nerve': 10, 'Talent': 10, 'met_rupaul': False,
                 'completed_lip_sync': False, 'level': 2, 'Name': 'Ginger Snaps',
                 'coordinates': (6, 8), 'location': 'main_stage'}
    you_win(character, {'Name': 'test'}, 'read_battle')
    print(character)
    print(power_enemy_up_or_down(character, [0, 0, 0, 8], True))


if __name__ == '__main__':
    main()
