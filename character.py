import challenges
import helpers


class Character:
    """
    A class representing the character.
    """
    id_counter = 0

    def __init__(self, name):
        if name == '':
            raise ValueError("Character name cannot be empty.")
        else:
            self.name = name

        self.stats = (10, 10, 10, 10)
        self.location = 'werk_room'
        self.coordinates = (0, 4)
        self.achieved_goal = False

        self.id = Character.id_counter
        Character.id_counter += 1

    def get_name(self):
        return self.name

    def get_stats(self):
        return self.stats

    def get_location(self):
        return self.location

    def get_coordinates(self):
        return self.coordinates

    def get_achieved_goal(self):
        return self.achieved_goal

    def setup_character(self):
        """
        Add base stats per base character type selection by user.
        """
        queen_types = ['Look Queen', 'Comedy Queen', 'Performance Queen', 'Alternative Queen']
        stat_add_ons = ((4, 5, 0, 0), (5, 4, 0, 0), (7, 2, 0, 0), (2, 7, 0, 0))

        print("What type of queen are you?")
        answer = challenges.get_challenge_input_from_user(queen_types)
        index = queen_types.index(answer)

        self.stats = tuple(map(helpers.add_numbers, self.stats, stat_add_ons[index]))

    def change_location(self, new_location):
        """
        Update character location.
        """
        self.location = new_location

    def power_up_or_down(self, stat_changes):
        """
        Update and print changes to stats for either the character.
        """
        stat_names = ['charisma', 'uniqueness', 'nerve', 'talent']
        initial_stats = self.stats
        index = 0

        self.stats = tuple(map(helpers.add_numbers, self.stats, stat_changes))

        for number in stat_changes:
            if number < 0:
                print(f'Your {stat_names[index]} has decreased by {abs(number)} to '
                      f'{initial_stats[index] + number}!')
            elif number > 0:
                print(f'Your {stat_names[index]} has increased by {abs(number)} to '
                      f'{initial_stats[index] + number}!')
            index += 1

    def achieved_goal(self):
        self.achieved_goal = True
        return self.achieved_goal


def main():
    my_character = Character('Kelly')
    print(my_character.get_name())
    print(my_character.get_stats())
    print(my_character.get_location())
    print(my_character.get_coordinates())
    my_character.setup_character()
    print(my_character.get_stats())
    my_character.power_up_or_down((1, 2, 0, 4))


if __name__ == '__main__':
    main()
