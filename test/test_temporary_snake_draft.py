import pytest

from draft import temporary_snake_draft


class TestTemporarySnakeDraft:
    @pytest.mark.parametrize("df", ["draft_zero.csv"], indirect=["df"])
    def test_draft_zero(self, df):
        fairness, assignment = temporary_snake_draft.get_fairest_attempt(temporary_snake_draft.permute_draft_order(df))
        assert fairness == 0

    @pytest.mark.parametrize("df", ["draft_one.csv"], indirect=["df"])
    def test_draft_one(self, df):
        fairness, assignment = temporary_snake_draft.get_fairest_attempt(temporary_snake_draft.permute_draft_order(df))
        assert fairness == 0

    @pytest.mark.parametrize("df", ["draft_two.csv"], indirect=["df"])
    def test_draft_two(self, df):
        fairness, assignment = temporary_snake_draft.get_fairest_attempt(temporary_snake_draft.permute_draft_order(df))
        assert fairness == 4.242640687119285

    @pytest.mark.parametrize("df", ["draft_three.csv"], indirect=["df"])
    def test_draft_three(self, df):
        fairness, assignment = temporary_snake_draft.get_fairest_attempt(temporary_snake_draft.permute_draft_order(df))
        assert fairness == 3.0

    @pytest.mark.parametrize("df", ["draft_four.csv"], indirect=["df"])
    def test_draft_four(self, df):
        fairness, assignment = temporary_snake_draft.get_fairest_attempt(temporary_snake_draft.permute_draft_order(df))
        assert fairness == 2.0
