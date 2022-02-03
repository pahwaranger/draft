import pytest

from draft import linear_draft


class TestLinearDraft:
    @pytest.mark.parametrize("df", ["draft_zero.csv"], indirect=["df"])
    def test_draft_zero(self, df):
        fairness, assignment = linear_draft.get_fairest_attempt(linear_draft.permute_draft_order(df))
        assert fairness == 0

    @pytest.mark.parametrize("df", ["draft_one.csv"], indirect=["df"])
    def test_draft_one(self, df):
        fairness, assignment = linear_draft.get_fairest_attempt(linear_draft.permute_draft_order(df))
        assert fairness == 1.4142135623730951

    @pytest.mark.parametrize("df", ["draft_two.csv"], indirect=["df"])
    def test_draft_two(self, df):
        fairness, assignment = linear_draft.get_fairest_attempt(linear_draft.permute_draft_order(df))
        assert fairness == 2.0

    @pytest.mark.parametrize("df", ["draft_three.csv"], indirect=["df"])
    def test_draft_three(self, df):
        fairness, assignment = linear_draft.get_fairest_attempt(linear_draft.permute_draft_order(df))
        assert fairness == 1.4142135623730951