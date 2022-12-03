"""
Colin Doig A01334230
Kelly Hagg A01324804
"""
import boards
import challenges
from boards import index_board


def show_score(character: dict) -> None:
    """
    Display current character stats for player

    :param character: must be dictionary representing the player character with the keys 'Charisma', 'Uniqueness',
    'Nerve', and 'Talent' whose values must all be positive integers
    :precondition: character must be a dictionary
    :postcondition: creates a string with the current stats of the player character inside
    :return: print statement displaying current stats of the player character
    """
    charisma = character['Charisma']
    uniqueness = character['Uniqueness']
    nerve = character['Nerve']
    talent = character['Talent']
    return print(f'Stats: [Charisma: {charisma}, Uniqueness: {uniqueness}, '
                 f'Nerve: {nerve}, Talent: {talent}]')


def generate_directional_inputs(current_coordinates, board_name):
    """
    Generate possible directional inputs for player.

    :param current_coordinates: must be a tuple containing two positive integers representing the current coordinates
    of the player character on the game board
    :param board_name: must be a string representing the name of the current board
    :precondition: current_coordinates must be a tuple and board_name must be a string
    :postcondition: generates possible inputs for the player based on their current coordinates on the board
    :return: a list of strings representing the possible inputs for the player
    """
    board_coordinates = index_board(board_name)

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


def get_directional_input_from_user(game_input: list, character: dict) -> str:
    """

    :param game_input:
    :return:
    """
    acceptable_answers = []

    print('Controls------------------------------------------------------------------------')

    for pair in game_input:
        acceptable_answers += pair[0]
        print(f'{pair[0]}: {pair[1]}')

    answer = input()

    if answer == '0':
        show_score(character)
        return get_directional_input_from_user(game_input, character)
    if answer not in acceptable_answers:
        print('That is not an acceptable answer! Please try again:')
        return get_directional_input_from_user(game_input, character)

    answer_index = acceptable_answers.index(answer)
    answer_string = game_input[answer_index][1]

    return answer_string.lower()


def move_character(character):
    """

    :param character:
    :return:
    """
    current_coordinates = character['coordinates']
    board_name = character['location']

    game_input = generate_directional_inputs(current_coordinates, board_name)
    move_to_coordinates = get_directional_input_from_user(game_input, character)

    if move_to_coordinates == 'enter':
        if character['location'] == 'judges_panel':
            character['met_rupaul'] = True
            return boards.set_board(character)
        print('Not until you level up girl.')
        move_to_coordinates = current_coordinates
    elif move_to_coordinates == 'exit' and character['location']:
        print('Where the hell do you think you\'re going girl? Get your ass back in here!')
        return get_directional_input_from_user(game_input, character)
    elif move_to_coordinates == 'up':
        move_to_coordinates = (current_coordinates[0] - 1, current_coordinates[1])
    elif move_to_coordinates == 'down':
        move_to_coordinates = (current_coordinates[0] + 1, current_coordinates[1])
    elif move_to_coordinates == 'left':
        move_to_coordinates = (current_coordinates[0], current_coordinates[1] - 1)
    elif move_to_coordinates == 'right':
        move_to_coordinates = (current_coordinates[0], current_coordinates[1] + 1)
    elif move_to_coordinates == 'challenge her' and character['location'] == 'werk_room':
        return challenges.makeover_challenge(character)
    elif move_to_coordinates == 'challenge her' and character['location'] == 'dressing_room':
        return challenges.final_battle(character)
    else:
        move_to_coordinates = current_coordinates

    return character.update({'coordinates': move_to_coordinates})


def main():
    """
    Drive the program
    """
    character = {'Charisma': 15, 'Uniqueness': 14, 'Nerve': 10, 'Talent': 10, 'met_rupaul': False,
                 'completed_lipsync': False, 'level': 1, 'Name': 'Ginger Snaps',
                 'coordinates': (6, 3), 'location': 'main_stage'}
    # print(read_board('dressing_room'))
    # print(generate_directional_tools((0, 5), 'main_stage'))
    # print(get_input_from_user(generate_challenge_input(['answer 1', 'answer 2', 'answer 3', 'answer 4'])))
    # print(generate_challenge_input(['answer 1', 'answer 2', 'answer 3', 'answer 4']))
    move_character(character)
    move_character(character)


if __name__ == '__main__':
    main()
