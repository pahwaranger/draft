import os
import pytest
import pandas


@pytest.fixture
def root_dir():
    return os.path.dirname(os.path.realpath(__file__))


@pytest.fixture
def data_dir(root_dir):
    return os.path.join(root_dir, "data")


@pytest.fixture
def df(request, data_dir):
    path = getattr(request, "param", "draft_one.csv")
    file = os.path.join(data_dir, path)
    return pandas.read_csv(file)
