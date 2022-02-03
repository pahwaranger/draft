# Draft

Brute-force drafting tools.

Currently only contains `snake_draft.py` which computes the most fair assignments using a simple snake draft approach. The basic logic is to start from one side of the list of people and assign their top ranked non-taken item. The last person in the order is the first to pick the second time around. The script will test all possible solutions, compute a fairness score (the STDDEV) and returns the best result. The lower the fairness score, the better.

## Setup

```sh
> curl -sSL https://install.python-poetry.org | python3 -
> poetry config virtualenvs.in-project true
> poetry install
```

## Usage

```sh
$ poetry run python draft/snake_draft.py          
Path to CVS file [test/data/draft_zero.csv]: 
fairness score: 0.0
john: item 1, item 2
drew: item 3, item 4
casey: item 5, item 6
lynn: item 7, item 8
```

```sh
$ poetry run python draft/snake_draft.py
Path to CVS file [test/data/draft_zero.csv]: test/data/draft_two.csv 
fairness score: 4.242640687119285
john: item 1
drew: item 2
casey: item 3, item 6
lynn: item 4, item 5
```

```sh
$ poetry run python draft/snake_draft.py --verbose
Path to CVS file [test/data/draft_zero.csv]: test/data/draft_three.csv
INFO: Set debug level to DEBUG
DEBUG: Attempt: ('john', 'drew', 'casey', 'lynn')
DEBUG: Assignments: {'john': [('item 1', 1)], 'drew': [('item 2', 2), ('item 5', 3)], 'casey': [('item 3', 2)], 'lynn': [('item 4', 1), ('item 6', 4)]}
DEBUG: {'john': 1, 'drew': 5, 'casey': 2, 'lynn': 5}
DEBUG: Fairness: 2.0
DEBUG: Attempt: ('john', 'drew', 'lynn', 'casey')
DEBUG: Assignments: {'john': [('item 1', 1)], 'drew': [('item 2', 2), ('item 5', 3)], 'lynn': [('item 4', 1)], 'casey': [('item 3', 2), ('item 6', 5)]}
DEBUG: {'john': 1, 'drew': 5, 'lynn': 1, 'casey': 7}
DEBUG: Fairness: 3.0
DEBUG: Attempt: ('john', 'casey', 'drew', 'lynn')
DEBUG: Assignments: {'john': [('item 1', 1)], 'casey': [('item 2', 1), ('item 6', 5)], 'drew': [('item 5', 3)], 'lynn': [('item 4', 1), ('item 3', 2)]}
DEBUG: {'john': 1, 'casey': 6, 'drew': 3, 'lynn': 3}
DEBUG: Fairness: 2.0
DEBUG: Attempt: ('john', 'casey', 'lynn', 'drew')
DEBUG: Assignments: {'john': [('item 1', 1)], 'casey': [('item 2', 1)], 'lynn': [('item 4', 1), ('item 6', 4)], 'drew': [('item 5', 3), ('item 3', 4)]}
DEBUG: {'john': 1, 'casey': 1, 'lynn': 5, 'drew': 7}
DEBUG: Fairness: 3.0
DEBUG: Attempt: ('john', 'lynn', 'drew', 'casey')
DEBUG: Assignments: {'john': [('item 1', 1)], 'lynn': [('item 4', 1)], 'drew': [('item 2', 2), ('item 5', 3)], 'casey': [('item 3', 2), ('item 6', 5)]}
DEBUG: {'john': 1, 'lynn': 1, 'drew': 5, 'casey': 7}
DEBUG: Fairness: 3.0
DEBUG: Attempt: ('john', 'lynn', 'casey', 'drew')
DEBUG: Assignments: {'john': [('item 1', 1)], 'lynn': [('item 4', 1)], 'casey': [('item 2', 1), ('item 6', 5)], 'drew': [('item 5', 3), ('item 3', 4)]}
DEBUG: {'john': 1, 'lynn': 1, 'casey': 6, 'drew': 7}
DEBUG: Fairness: 3.1622776601683795
DEBUG: Attempt: ('drew', 'john', 'casey', 'lynn')
DEBUG: Assignments: {'drew': [('item 1', 1), ('item 5', 3)], 'john': [('item 2', 2)], 'casey': [('item 3', 2)], 'lynn': [('item 4', 1), ('item 6', 4)]}
DEBUG: {'drew': 4, 'john': 2, 'casey': 2, 'lynn': 5}
DEBUG: Fairness: 1.4142135623730951
DEBUG: Attempt: ('drew', 'john', 'lynn', 'casey')
DEBUG: Assignments: {'drew': [('item 1', 1), ('item 5', 3)], 'john': [('item 2', 2)], 'lynn': [('item 4', 1)], 'casey': [('item 3', 2), ('item 6', 5)]}
DEBUG: {'drew': 4, 'john': 2, 'lynn': 1, 'casey': 7}
DEBUG: Fairness: 2.6457513110645907
DEBUG: Attempt: ('drew', 'casey', 'john', 'lynn')
DEBUG: Assignments: {'drew': [('item 1', 1), ('item 5', 3)], 'casey': [('item 2', 1)], 'john': [('item 3', 3)], 'lynn': [('item 4', 1), ('item 6', 4)]}
DEBUG: {'drew': 4, 'casey': 1, 'john': 3, 'lynn': 5}
DEBUG: Fairness: 1.4142135623730951
DEBUG: Attempt: ('drew', 'casey', 'lynn', 'john')
DEBUG: Assignments: {'drew': [('item 1', 1), ('item 5', 3)], 'casey': [('item 2', 1)], 'lynn': [('item 4', 1)], 'john': [('item 3', 3), ('item 6', 5)]}
DEBUG: {'drew': 4, 'casey': 1, 'lynn': 1, 'john': 8}
DEBUG: Fairness: 3.3166247903554
DEBUG: Attempt: ('drew', 'lynn', 'john', 'casey')
DEBUG: Assignments: {'drew': [('item 1', 1), ('item 5', 3)], 'lynn': [('item 4', 1)], 'john': [('item 2', 2)], 'casey': [('item 3', 2), ('item 6', 5)]}
DEBUG: {'drew': 4, 'lynn': 1, 'john': 2, 'casey': 7}
DEBUG: Fairness: 2.6457513110645907
DEBUG: Attempt: ('drew', 'lynn', 'casey', 'john')
DEBUG: Assignments: {'drew': [('item 1', 1), ('item 5', 3)], 'lynn': [('item 4', 1)], 'casey': [('item 2', 1)], 'john': [('item 3', 3), ('item 6', 5)]}
DEBUG: {'drew': 4, 'lynn': 1, 'casey': 1, 'john': 8}
DEBUG: Fairness: 3.3166247903554
DEBUG: Attempt: ('casey', 'john', 'drew', 'lynn')
DEBUG: Assignments: {'casey': [('item 2', 1)], 'john': [('item 1', 1), ('item 6', 5)], 'drew': [('item 5', 3)], 'lynn': [('item 4', 1), ('item 3', 2)]}
DEBUG: {'casey': 1, 'john': 6, 'drew': 3, 'lynn': 3}
DEBUG: Fairness: 2.0
DEBUG: Attempt: ('casey', 'john', 'lynn', 'drew')
DEBUG: Assignments: {'casey': [('item 2', 1)], 'john': [('item 1', 1)], 'lynn': [('item 4', 1), ('item 6', 4)], 'drew': [('item 5', 3), ('item 3', 4)]}
DEBUG: {'casey': 1, 'john': 1, 'lynn': 5, 'drew': 7}
DEBUG: Fairness: 3.0
DEBUG: Attempt: ('casey', 'drew', 'john', 'lynn')
DEBUG: Assignments: {'casey': [('item 2', 1)], 'drew': [('item 1', 1), ('item 5', 3)], 'john': [('item 3', 3)], 'lynn': [('item 4', 1), ('item 6', 4)]}
DEBUG: {'casey': 1, 'drew': 4, 'john': 3, 'lynn': 5}
DEBUG: Fairness: 1.4142135623730951
DEBUG: Attempt: ('casey', 'drew', 'lynn', 'john')
DEBUG: Assignments: {'casey': [('item 2', 1)], 'drew': [('item 1', 1), ('item 5', 3)], 'lynn': [('item 4', 1)], 'john': [('item 3', 3), ('item 6', 5)]}
DEBUG: {'casey': 1, 'drew': 4, 'lynn': 1, 'john': 8}
DEBUG: Fairness: 3.3166247903554
DEBUG: Attempt: ('casey', 'lynn', 'john', 'drew')
DEBUG: Assignments: {'casey': [('item 2', 1)], 'lynn': [('item 4', 1)], 'john': [('item 1', 1), ('item 6', 5)], 'drew': [('item 5', 3), ('item 3', 4)]}
DEBUG: {'casey': 1, 'lynn': 1, 'john': 6, 'drew': 7}
DEBUG: Fairness: 3.1622776601683795
DEBUG: Attempt: ('casey', 'lynn', 'drew', 'john')
DEBUG: Assignments: {'casey': [('item 2', 1)], 'lynn': [('item 4', 1)], 'drew': [('item 1', 1), ('item 5', 3)], 'john': [('item 3', 3), ('item 6', 5)]}
DEBUG: {'casey': 1, 'lynn': 1, 'drew': 4, 'john': 8}
DEBUG: Fairness: 3.3166247903554
DEBUG: Attempt: ('lynn', 'john', 'drew', 'casey')
DEBUG: Assignments: {'lynn': [('item 4', 1)], 'john': [('item 1', 1)], 'drew': [('item 2', 2), ('item 5', 3)], 'casey': [('item 3', 2), ('item 6', 5)]}
DEBUG: {'lynn': 1, 'john': 1, 'drew': 5, 'casey': 7}
DEBUG: Fairness: 3.0
DEBUG: Attempt: ('lynn', 'john', 'casey', 'drew')
DEBUG: Assignments: {'lynn': [('item 4', 1)], 'john': [('item 1', 1)], 'casey': [('item 2', 1), ('item 6', 5)], 'drew': [('item 5', 3), ('item 3', 4)]}
DEBUG: {'lynn': 1, 'john': 1, 'casey': 6, 'drew': 7}
DEBUG: Fairness: 3.1622776601683795
DEBUG: Attempt: ('lynn', 'drew', 'john', 'casey')
DEBUG: Assignments: {'lynn': [('item 4', 1)], 'drew': [('item 1', 1), ('item 5', 3)], 'john': [('item 2', 2)], 'casey': [('item 3', 2), ('item 6', 5)]}
DEBUG: {'lynn': 1, 'drew': 4, 'john': 2, 'casey': 7}
DEBUG: Fairness: 2.6457513110645907
DEBUG: Attempt: ('lynn', 'drew', 'casey', 'john')
DEBUG: Assignments: {'lynn': [('item 4', 1)], 'drew': [('item 1', 1), ('item 5', 3)], 'casey': [('item 2', 1)], 'john': [('item 3', 3), ('item 6', 5)]}
DEBUG: {'lynn': 1, 'drew': 4, 'casey': 1, 'john': 8}
DEBUG: Fairness: 3.3166247903554
DEBUG: Attempt: ('lynn', 'casey', 'john', 'drew')
DEBUG: Assignments: {'lynn': [('item 4', 1)], 'casey': [('item 2', 1)], 'john': [('item 1', 1), ('item 6', 5)], 'drew': [('item 5', 3), ('item 3', 4)]}
DEBUG: {'lynn': 1, 'casey': 1, 'john': 6, 'drew': 7}
DEBUG: Fairness: 3.1622776601683795
DEBUG: Attempt: ('lynn', 'casey', 'drew', 'john')
DEBUG: Assignments: {'lynn': [('item 4', 1)], 'casey': [('item 2', 1)], 'drew': [('item 1', 1), ('item 5', 3)], 'john': [('item 3', 3), ('item 6', 5)]}
DEBUG: {'lynn': 1, 'casey': 1, 'drew': 4, 'john': 8}
DEBUG: Fairness: 3.3166247903554
fairness score: 1.4142135623730951
drew: item 1, item 5
john: item 2
casey: item 3
lynn: item 4, item 6
```