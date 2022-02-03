import pytest
import pandas

from draft.utils import utils


class TestUtils:
    def test_draft_order(self):
        people = ['A', 'B', 'C']
        rounds = 1
        result1 = utils.draft_order(people, rounds)
        expected1 = ['A', 'B', 'C']
        assert result1 == expected1

        rounds = 2
        result2 = utils.draft_order(people, rounds)
        expected2 = ['A', 'B', 'C', 'C', 'B', 'A']
        assert result2 == expected2

    def test_get_first_preference(self):
        df = pandas.DataFrame([[1, 2, 1], [1, 3, 2], [4, 6, 3], [4, 3, 4], [5, 4, 5]], columns=['A', 'B', 'C'])
        result1 = utils.get_first_preference(person=df['A'], reserved_items=[])
        expected1 = 1
        assert result1 == expected1

        result2 = utils.get_first_preference(person=df['A'], reserved_items=[1])
        expected2 = 4
        assert result2 == expected2

        result2 = utils.get_first_preference(person=df['A'], reserved_items=[1,4,5])
        assert result2 is None

    def test_get_all_possible_items(self):
        df = pandas.DataFrame([[1]], columns=['A'])
        result1 = list(utils.get_all_possible_items(df))
        expected1 = [1]
        assert result1 == expected1

        df = pandas.DataFrame([[1, 2]], columns=['A', 'B'])
        result2 = list(utils.get_all_possible_items(df))
        expected2 = [1, 2]
        assert result2 == expected2

        df = pandas.DataFrame([[1, 2], [1, 2]], columns=['A', 'B'])
        result3 = list(utils.get_all_possible_items(df))
        expected3 = [1, 2]
        assert result3 == expected3

        df = pandas.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
        result4 = list(utils.get_all_possible_items(df))
        expected4 = [1, 2, 3, 4]
        assert result4 == expected4
    
    def test_get_priority(self):
        df = pandas.DataFrame([[1]], columns=['A'])
        result1 = utils.get_priority(df, 'A', 1)
        expected1 = 1
        assert result1 == expected1

        df = pandas.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
        result2 = utils.get_priority(df, 'A', 3)
        expected2 = 2
        assert result2 == expected2

        df = pandas.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
        with pytest.raises(IndexError):
            utils.get_priority(df, 'A', 2)
