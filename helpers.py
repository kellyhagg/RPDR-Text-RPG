"""
Helper functions to facilitate game events.
"""


import json
import random


def add_numbers(first, second):
    return first + second


def deliver_introduction(player) -> None:
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


def power_enemy_up_or_down(queen: dict, stat_changes: tuple) -> dict:
    """
    Update and print changes to stats for either the player or the enemy.

    :param queen: a dictionary representing a queen name and stats
    :param stat_changes: a list containing four integers
    :postcondition: adjusts values stored inside queen dictionary either up or down depending
    on whether the integers in values are positive or negative
    :return: dictionary representing the queen with their stats changed to reflect game events
    """
    stat_names = ['charisma', 'nerve']
    initial_stats = (queen['Charisma'], queen['Nerve'])
    index = 0

    queen['Charisma'] += stat_changes[0]
    queen['Nerve'] += stat_changes[1]

    for number in stat_changes:
        if number < 0:
            print(f'{queen["Name"]}\'s {stat_names[index]} has decreased by {abs(number)} to '
                  f'{initial_stats[index] + number}!')
        elif number > 0:
            print(f'{queen["Name"]}\'s {stat_names[index]} has increased by {number} to '
                  f'{initial_stats[index] + number}!')
        index += 1

    return queen


def you_win(player, enemy_name: str or None, challenge_name: str):
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
        return player.power_up_or_down((0, 0, 2, increase))
    if challenge_name == 'makeover_challenge':
        print(f"\n\"ConDRAGulations {player.get_name()} and {enemy_name},\nyou are the"
              f" winners of this mini challenge!\"\n")
        increase = random.randint(10, 15)
        return player.power_up_or_down((0, increase, 0, increase))
    if challenge_name == 'werk_room':
        print("\nYou are now level 2!")
        player.power_up_or_down((random.randint(30, 40), random.randint(30, 40),
                                 random.randint(30, 40), 15))
        print(f"\nRuPaul's voice echoes through the room: \n\n\"{player.get_name()}, "
              f"please make your way to the Main Stage. "
              f"\nYou have been chosen to take part in a Lip Sync for Your Legacy!\"\n"
              f"\nYou quickly make your way to the stage, \nthe potential lip sync songs spinning"
              f" through your head.")
        return player.change_location('main_stage')
    if challenge_name == 'lip_sync':
        print(f"RuPaul's voice echoes: 'ConDRAGulations {player.get_name()}, "
              f"you're a winner baby!'\nYou feel your inner saboteur melting away.")
        print("\nYou are now level 3!")
        player.power_up_or_down((random.randint(30, 40), random.randint(30, 40),
                                 random.randint(30, 40), 20))
        player.change_location('judges_panel')
        print(f"\nYou are ushered towards the Judge's Panel.")
        return player
    if challenge_name == 'rupaul':
        print(f"\nRuPaul's face breaks into a smile\n\"ConDRAGulations {player.get_name()}, "
              f"you're the winner baby!\"\nTriumphant music starts up as confetti begins to "
              f"fall from the ceiling.\n\nRuPaul says,\"You are now the Queen of the Mother Tucking"
              f" UNIVERSE!\"\n\nMother continues as she places a massive bejeweled crown upon your"
              f" head and a\nmatching scepter in your hand. You sob with happiness.\n\nYou"
              f" know that this... is the beginning of the rest of your life.\n")
        return player.achieved_goal()


def main():
    """
    Drive the program.
    """


if __name__ == '__main__':
    main()
