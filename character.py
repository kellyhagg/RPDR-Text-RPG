import challenges


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

        self.charisma = 10
        self.uniqueness = 10
        self.nerve = 10
        self.talent = 10
        self.location = 'werk_room'
        self.coordinates = (0, 4)

        self.id = Character.id_counter
        Character.id_counter += 1

    def get_name(self):
        return self.name

    def get_charisma(self):
        return self.charisma

    def get_uniqueness(self):
        return self.uniqueness

    def get_nerve(self):
        return self.nerve

    def get_talent(self):
        return self.nerve

    def get_location(self):
        return self.location

    def get_coordinates(self):
        return self.coordinates

    def setup_character(self):
        """
        Add base stats per base character type selection by user.
        """
        queen_types = ['Look Queen', 'Comedy Queen', 'Performance Queen', 'Alternative Queen']

        queen_add_ons = ((4, 5, 0, 0), (5, 4, 0, 0), (7, 2, 0, 0), (2, 7, 0, 0))

        print("What type of queen are you?")
        answer = challenges.get_challenge_input_from_user(queen_types)
        if answer == 'look_queen':
            selected_add_ons = queen_add_ons[0]
        elif answer == 'comedy_queen':
            selected_add_ons = queen_add_ons[1]
        elif answer == 'performance_queen':
            selected_add_ons = queen_add_ons[2]
        else:
            selected_add_ons = queen_add_ons[3]

        self.charisma += selected_add_ons[0]
        self.uniqueness += selected_add_ons[1]
        self.nerve += selected_add_ons[2]
        self.talent += selected_add_ons[3]

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
        initial_stats = [self.charisma, self.uniqueness, self.nerve, self.talent]
        index = 0

        self.charisma += stat_changes[0]
        self.uniqueness += stat_changes[1]
        self.nerve += stat_changes[2]
        self.talent += stat_changes[3]

        for number in stat_changes:
            if number < 0:
                print(f'Your {stat_names[index]} has decreased by {abs(number)} to '
                      f'{initial_stats[index] + number}!')
            elif number > 0:
                print(f'Your {stat_names[index]} has increased by {abs(number)} to '
                      f'{initial_stats[index] + number}!')
            index += 1


def main():
    my_character = Character('Kelly')
    print(my_character.get_name())
    print(my_character.get_uniqueness())
    print(my_character.get_location())
    print(my_character.get_coordinates())
    my_character.setup_character()
    my_character.power_up_or_down((1, 2, 0, 4))


if __name__ == '__main__':
    main()
