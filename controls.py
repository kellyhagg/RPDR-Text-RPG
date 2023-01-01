"""
Generate and operate the controls for the player.
"""


import challenges
import boards
import character


def show_score(player) -> None:
    """
    Display current character stats for player

    :param player: must be dictionary representing the player character with the keys 'Charisma',
    'Uniqueness', 'Nerve', and 'Talent'
    :precondition: character must be a dictionary
    :postcondition: create a string with the current stats of the player character inside
    :return: print statement displaying current stats of the player character
    """
    stats = player.get_stats()
    return print(f'Stats: [Charisma: {stats[0]}, Uniqueness: {stats[1]}, '
                 f'Nerve: {stats[2]}, Talent: {stats[3]}]')


def generate_directional_inputs(current_coordinates: tuple, board_name: str) -> list:
    """
    Generate possible directional inputs for player.

    :param current_coordinates: must be a tuple containing two positive integers representing
    the current coordinates of the player character on the game board
    :param board_name: must be a string representing the name of the current board
    :precondition: current_coordinates must be a tuple and board_name must be a string
    :postcondition: generate possible inputs for the player based on their current coordinates
    and the indices generated in index_board when applied to the opened board text file
    :return: a list of tuples representing the possible inputs and their english meaning
    """
    board_coordinates = boards.index_board(board_name)

    board_limits = [key for key in board_coordinates]
    board_limits.sort(reverse=True)
    limit_coordinate = board_limits.pop(0)

    row = current_coordinates[0]
    column = current_coordinates[1]

    pairs = []

    if board_coordinates[current_coordinates] == 'enter':
        pairs.append(('E', 'Enter'))
    elif board_coordinates[current_coordinates] == 'exit':
        pairs.append(('X', 'Exit'))

    challenge = False

    if row != 0 and board_coordinates[row - 1, column] is not False:
        if board_coordinates[row - 1, column] == 'queen':
            challenge = True
        else:
            pairs.append(('W', 'Up'))
    if row != limit_coordinate[0] and board_coordinates[row + 1, column] is not False:
        if board_coordinates[row + 1, column] == 'queen':
            challenge = True
        else:
            pairs.append(('S', 'Down'))
    if column != 0 and board_coordinates[row, column - 1] is not False:
        if board_coordinates[row, column - 1] == 'queen':
            challenge = True
        else:
            pairs.append(('A', 'Left'))
    if column != limit_coordinate[1] and board_coordinates[row, column + 1] is not False:
        if board_coordinates[row, column + 1] == 'queen':
            challenge = True
        else:
            pairs.append(('D', 'Right'))
    pairs.append(('0', 'Stats'))

    if challenge:
        pairs.insert(0, ('Q', 'Challenge her'))
    return pairs


def get_directional_input_from_user(game_input: list, player) -> str:
    """
    Process directional input from the player.

    :param game_input: must be a list representing valid potential inputs
    :param player: must be a dictionary representing the player character
    :precondition: game_input must be a list and character must be a dictionary
    :postcondition: accept input from player
    :postcondition: determines whether input is valid
    :postcondition: print to the user
    :return: self if user input is 'O' or not valid else string representing valid input from user
    """
    acceptable_answers = []

    print('Controls------------------------------------------------------------------------')

    for pair in game_input:
        acceptable_answers += pair[0]
        print(f'{pair[0]}: {pair[1]}')

    answer = input()

    if answer == '0':
        show_score(player)
        return get_directional_input_from_user(game_input, player)
    elif answer == 'quit':
        raise SystemExit("You quit the game.")
    elif answer not in acceptable_answers:
        print('That is not an acceptable answer! Please try again:')
        return get_directional_input_from_user(game_input, player)
    elif answer == 'X':
        print('Where the hell do you think you\'re going girl? Get your ass back in here!')
        return get_directional_input_from_user(game_input, player)
    elif answer == 'E' and player.get_location() != 'judges_panel':
        print('Not until you level up girl.')
        return get_directional_input_from_user(game_input, player)
    elif answer == 'Q' and player.get_location() == 'main_stage':
        print('What the hell are you doing girl? Get your ass to the other side of the stage!')
        return get_directional_input_from_user(game_input, player)

    answer_index = acceptable_answers.index(answer)
    answer_string = game_input[answer_index][1]

    return answer_string.lower()


def move_character(player):
    """
    Process player movement.

    :param player: must be a Character
    :precondition: player must be a Character
    :postcondition: process the movement of the player character depending on several conditions
    :return: character dictionary representing in-game movement events
    """
    current_coordinates = player.get_coordinates()
    board_name = player.get_location()

    game_input = generate_directional_inputs(current_coordinates, board_name)
    new_coordinates = get_directional_input_from_user(game_input, player)

    if new_coordinates == 'enter':
        if board_name == 'judges_panel':
            return player.change_location('dressing_room')
    elif new_coordinates == 'up':
        new_coordinates = (current_coordinates[0] - 1, current_coordinates[1])
    elif new_coordinates == 'down':
        new_coordinates = (current_coordinates[0] + 1, current_coordinates[1])
    elif new_coordinates == 'left':
        new_coordinates = (current_coordinates[0], current_coordinates[1] - 1)
    elif new_coordinates == 'right':
        new_coordinates = (current_coordinates[0], current_coordinates[1] + 1)
    elif new_coordinates == 'challenge her' and board_name == 'werk_room':
        return challenges.makeover_challenge(player)
    elif new_coordinates == 'challenge her' and board_name == 'dressing_room':
        challenges.final_battle(player)
        return player
    else:
        new_coordinates = current_coordinates

    player.move_to_coordinates(new_coordinates)
    return player


def main():
    """
    Drive the program
    """

    # print(f'Here is a demonstration of how user input is processed using move_character which uses '
    #       f'generate_directional_inputs and get_directional_input_from_user to move the player '
    #       f'character.')
    # move_character(player)
    # move_character(player)


if __name__ == '__main__':
    main()
