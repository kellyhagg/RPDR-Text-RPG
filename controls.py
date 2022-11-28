import itertools

def generate_directional_tools():

    pairs = []

    input_letters = ['W', 'S', 'A', 'D']
    directions = ['Up', 'Down', 'Left', 'Right']

    pairs = zip(input_letters, directions)

    return pairs

def generate_challenge_input(answers: list) -> list:
    """
    """
    pairs = []

    for number, answer in enumerate(answers, 1):
        pair = (str(number), answer)
        pairs.append(pair)
    return pairs

def get_input_from_user(game_input: list) -> str:
    """

    :param game_input:
    :return:
    """
    acceptable_answers = []

    for pair in game_input:
        acceptable_answers += pair[0]
        print(f'{pair[0]}: {pair[1]}')

    answer = input()
    if answer not in acceptable_answers:
        print("That is not an acceptable answer! Please try again:")
        return get_input_from_user(game_input)

    answer_index = acceptable_answers.index(answer)

    return game_input[answer_index][1]

def main():
    """
    Drive the program
    """
    # print(generate_directional_tools())
    print(get_input_from_user(generate_challenge_input(['answer 1', 'answer 2', 'answer 3', 'answer 4'])))
    # print(generate_challenge_input(['answer 1', 'answer 2', 'answer 3', 'answer 4']))

if __name__ == '__main__':
    main()
