import io
from controls import show_score
from unittest import TestCase
from unittest.mock import patch
import character


class TestShowScore(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_stats_all_negative_values(self, mock_output):
        player = character.Character('Name')
        player.set_stats([-5, -15, -400, -80])
        show_score(player)
        actual = mock_output.getvalue()
        expected = 'Stats: [Charisma: -5, Uniqueness: -15, Nerve: -400, Talent: -80]\n'
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_stats_all_zero_values(self, mock_output):
        player = character.Character('Name')
        player.set_stats([0, 0, 0, 0])
        show_score(player)
        actual = mock_output.getvalue()
        expected = 'Stats: [Charisma: 0, Uniqueness: 0, Nerve: 0, Talent: 0]\n'
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_stats_all_positive_values(self, mock_output):
        player = character.Character('Name')
        player.set_stats([50, 45, 9, 11])
        show_score(player)
        actual = mock_output.getvalue()
        expected = 'Stats: [Charisma: 50, Uniqueness: 45, Nerve: 9, Talent: 11]\n'
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_stats_mix_of_values(self, mock_output):
        player = character.Character('Name')
        player.set_stats([-16, 0, 4, 8])
        show_score(player)
        actual = mock_output.getvalue()
        expected = 'Stats: [Charisma: -16, Uniqueness: 0, Nerve: 4, Talent: 8]\n'
        self.assertEqual(expected, actual)