# Draft

[![MIT license](https://badgen.net/pypi/license/pip/)](https://github.com/pahwaranger/draft/blob/master/LICENSE)
[![Tests Status](https://github.com/pahwaranger/draft/workflows/Tests/badge.svg?branch=master&event=push)](https://github.com/pahwaranger/draft/actions/workflows/tests.yml?query=event%3Apush+branch%3Amaster)
[![Lint Status](https://github.com/pahwaranger/draft/workflows/Lint/badge.svg?branch=master&event=push)](https://github.com/pahwaranger/draft/actions/workflows/lint.yml?query=event%3Apush+branch%3Amaster)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
Brute-force drafting tools.

## Draft types

The scripts will test all possible solutions for the given draft type, compute a fairness score (the STDDEV), and return the best result. The lower the fairness score, the better. Use `--verbose` to see all of the possible options.

### Perpetual Snake Draft

`perpetual_snake_draft.py` computes the most fair assignments using a simple snake draft approach.

The snake draft works by mirroring the order at the end of each round. So the last period is round 1 goes first in round 2 and the last person in round 2 goes first in round 3.

Perpetual snake draft logic continues to mirror for however many rounds there are. Meaning the first 4 rounds would be:
 `[A, B, C], [C, B, A], [A, B, C], [C, B, A]`

### Temporary Snake Draft

`temporary_snake_draft.py` follows the same approach as described above for Perpetual Snake Draft. However, temporary snake draft logic only mirrors the 2nd round.

Meaning if the first 4 rounds would be:
 `[A, B, C], [C, B, A], [A, B, C], [A, B, C]`

### Linear Draft

`linear_draft.py` computes the most fair assignments using a linear draft approach.

In a linear draft approach, the order never changes and at the end of each round, you simply start over again at the beginning.

Meaning if the first 4 rounds would be:
 `[A, B, C], [A, B, C], [A, B, C], [A, B, C]`

## Setup

```sh
> curl -sSL https://install.python-poetry.org | python3 -
> poetry config virtualenvs.in-project true
> poetry install
```

## Usage

```sh
$ poetry run python draft/perpetual_snake_draft.py          
Path to CVS file [test/data/draft_zero.csv]: 
fairness score: 0.0
john: item 1, item 2
drew: item 3, item 4
casey: item 5, item 6
lynn: item 7, item 8
```

```sh
$ poetry run python draft/perpetual_snake_draft.py
Path to CVS file [test/data/draft_zero.csv]: test/data/draft_two.csv 
fairness score: 4.242640687119285
john: item 1
drew: item 2
casey: item 3, item 6
lynn: item 4, item 5
```

```sh
$ poetry run python draft/perpetual_snake_draft.py --verbose
Path to CVS file [test/data/draft_zero.csv]: test/data/draft_three.csv
INFO: Set debug level to DEBUG
DEBUG: Attempt: ('john', 'drew', 'casey', 'lynn')
DEBUG: Assignments: {'john': [('item 1', 1)], 'drew': [('item 2', 2), ('item 5', 3)], 'casey': [('item 3', 2)], 'lynn': [('item 4', 1), ('item 6', 4)]}
DEBUG: Scores: {'john': 1, 'drew': 5, 'casey': 2, 'lynn': 5}
DEBUG: Fairness: 2.0

DEBUG: Attempt: ('john', 'drew', 'lynn', 'casey')
DEBUG: Assignments: {'john': [('item 1', 1)], 'drew': [('item 2', 2), ('item 5', 3)], 'lynn': [('item 4', 1)], 'casey': [('item 3', 2), ('item 6', 5)]}
DEBUG: Scores: {'john': 1, 'drew': 5, 'lynn': 1, 'casey': 7}
DEBUG: Fairness: 3.0

DEBUG: Attempt: ('john', 'casey', 'drew', 'lynn')
DEBUG: Assignments: {'john': [('item 1', 1)], 'casey': [('item 2', 1), ('item 6', 5)], 'drew': [('item 5', 3)], 'lynn': [('item 4', 1), ('item 3', 2)]}
DEBUG: Scores: {'john': 1, 'casey': 6, 'drew': 3, 'lynn': 3}
DEBUG: Fairness: 2.0

DEBUG: Attempt: ('john', 'casey', 'lynn', 'drew')
DEBUG: Assignments: {'john': [('item 1', 1)], 'casey': [('item 2', 1)], 'lynn': [('item 4', 1), ('item 6', 4)], 'drew': [('item 5', 3), ('item 3', 4)]}
DEBUG: Scores: {'john': 1, 'casey': 1, 'lynn': 5, 'drew': 7}
DEBUG: Fairness: 3.0

DEBUG: Attempt: ('john', 'lynn', 'drew', 'casey')
DEBUG: Assignments: {'john': [('item 1', 1)], 'lynn': [('item 4', 1)], 'drew': [('item 2', 2), ('item 5', 3)], 'casey': [('item 3', 2), ('item 6', 5)]}
DEBUG: Scores: {'john': 1, 'lynn': 1, 'drew': 5, 'casey': 7}
DEBUG: Fairness: 3.0

DEBUG: Attempt: ('john', 'lynn', 'casey', 'drew')
DEBUG: Assignments: {'john': [('item 1', 1)], 'lynn': [('item 4', 1)], 'casey': [('item 2', 1), ('item 6', 5)], 'drew': [('item 5', 3), ('item 3', 4)]}
DEBUG: Scores: {'john': 1, 'lynn': 1, 'casey': 6, 'drew': 7}
DEBUG: Fairness: 3.1622776601683795

DEBUG: Attempt: ('drew', 'john', 'casey', 'lynn')
DEBUG: Assignments: {'drew': [('item 1', 1), ('item 5', 3)], 'john': [('item 2', 2)], 'casey': [('item 3', 2)], 'lynn': [('item 4', 1), ('item 6', 4)]}
DEBUG: Scores: {'drew': 4, 'john': 2, 'casey': 2, 'lynn': 5}
DEBUG: Fairness: 1.4142135623730951

DEBUG: Attempt: ('drew', 'john', 'lynn', 'casey')
DEBUG: Assignments: {'drew': [('item 1', 1), ('item 5', 3)], 'john': [('item 2', 2)], 'lynn': [('item 4', 1)], 'casey': [('item 3', 2), ('item 6', 5)]}
DEBUG: Scores: {'drew': 4, 'john': 2, 'lynn': 1, 'casey': 7}
DEBUG: Fairness: 2.6457513110645907

DEBUG: Attempt: ('drew', 'casey', 'john', 'lynn')
DEBUG: Assignments: {'drew': [('item 1', 1), ('item 5', 3)], 'casey': [('item 2', 1)], 'john': [('item 3', 3)], 'lynn': [('item 4', 1), ('item 6', 4)]}
DEBUG: Scores: {'drew': 4, 'casey': 1, 'john': 3, 'lynn': 5}
DEBUG: Fairness: 1.4142135623730951

DEBUG: Attempt: ('drew', 'casey', 'lynn', 'john')
DEBUG: Assignments: {'drew': [('item 1', 1), ('item 5', 3)], 'casey': [('item 2', 1)], 'lynn': [('item 4', 1)], 'john': [('item 3', 3), ('item 6', 5)]}
DEBUG: Scores: {'drew': 4, 'casey': 1, 'lynn': 1, 'john': 8}
DEBUG: Fairness: 3.3166247903554

DEBUG: Attempt: ('drew', 'lynn', 'john', 'casey')
DEBUG: Assignments: {'drew': [('item 1', 1), ('item 5', 3)], 'lynn': [('item 4', 1)], 'john': [('item 2', 2)], 'casey': [('item 3', 2), ('item 6', 5)]}
DEBUG: Scores: {'drew': 4, 'lynn': 1, 'john': 2, 'casey': 7}
DEBUG: Fairness: 2.6457513110645907

DEBUG: Attempt: ('drew', 'lynn', 'casey', 'john')
DEBUG: Assignments: {'drew': [('item 1', 1), ('item 5', 3)], 'lynn': [('item 4', 1)], 'casey': [('item 2', 1)], 'john': [('item 3', 3), ('item 6', 5)]}
DEBUG: Scores: {'drew': 4, 'lynn': 1, 'casey': 1, 'john': 8}
DEBUG: Fairness: 3.3166247903554

DEBUG: Attempt: ('casey', 'john', 'drew', 'lynn')
DEBUG: Assignments: {'casey': [('item 2', 1)], 'john': [('item 1', 1), ('item 6', 5)], 'drew': [('item 5', 3)], 'lynn': [('item 4', 1), ('item 3', 2)]}
DEBUG: Scores: {'casey': 1, 'john': 6, 'drew': 3, 'lynn': 3}
DEBUG: Fairness: 2.0

DEBUG: Attempt: ('casey', 'john', 'lynn', 'drew')
DEBUG: Assignments: {'casey': [('item 2', 1)], 'john': [('item 1', 1)], 'lynn': [('item 4', 1), ('item 6', 4)], 'drew': [('item 5', 3), ('item 3', 4)]}
DEBUG: Scores: {'casey': 1, 'john': 1, 'lynn': 5, 'drew': 7}
DEBUG: Fairness: 3.0

DEBUG: Attempt: ('casey', 'drew', 'john', 'lynn')
DEBUG: Assignments: {'casey': [('item 2', 1)], 'drew': [('item 1', 1), ('item 5', 3)], 'john': [('item 3', 3)], 'lynn': [('item 4', 1), ('item 6', 4)]}
DEBUG: Scores: {'casey': 1, 'drew': 4, 'john': 3, 'lynn': 5}
DEBUG: Fairness: 1.4142135623730951

DEBUG: Attempt: ('casey', 'drew', 'lynn', 'john')
DEBUG: Assignments: {'casey': [('item 2', 1)], 'drew': [('item 1', 1), ('item 5', 3)], 'lynn': [('item 4', 1)], 'john': [('item 3', 3), ('item 6', 5)]}
DEBUG: Scores: {'casey': 1, 'drew': 4, 'lynn': 1, 'john': 8}
DEBUG: Fairness: 3.3166247903554

DEBUG: Attempt: ('casey', 'lynn', 'john', 'drew')
DEBUG: Assignments: {'casey': [('item 2', 1)], 'lynn': [('item 4', 1)], 'john': [('item 1', 1), ('item 6', 5)], 'drew': [('item 5', 3), ('item 3', 4)]}
DEBUG: Scores: {'casey': 1, 'lynn': 1, 'john': 6, 'drew': 7}
DEBUG: Fairness: 3.1622776601683795

DEBUG: Attempt: ('casey', 'lynn', 'drew', 'john')
DEBUG: Assignments: {'casey': [('item 2', 1)], 'lynn': [('item 4', 1)], 'drew': [('item 1', 1), ('item 5', 3)], 'john': [('item 3', 3), ('item 6', 5)]}
DEBUG: Scores: {'casey': 1, 'lynn': 1, 'drew': 4, 'john': 8}
DEBUG: Fairness: 3.3166247903554

DEBUG: Attempt: ('lynn', 'john', 'drew', 'casey')
DEBUG: Assignments: {'lynn': [('item 4', 1)], 'john': [('item 1', 1)], 'drew': [('item 2', 2), ('item 5', 3)], 'casey': [('item 3', 2), ('item 6', 5)]}
DEBUG: Scores: {'lynn': 1, 'john': 1, 'drew': 5, 'casey': 7}
DEBUG: Fairness: 3.0

DEBUG: Attempt: ('lynn', 'john', 'casey', 'drew')
DEBUG: Assignments: {'lynn': [('item 4', 1)], 'john': [('item 1', 1)], 'casey': [('item 2', 1), ('item 6', 5)], 'drew': [('item 5', 3), ('item 3', 4)]}
DEBUG: Scores: {'lynn': 1, 'john': 1, 'casey': 6, 'drew': 7}
DEBUG: Fairness: 3.1622776601683795

DEBUG: Attempt: ('lynn', 'drew', 'john', 'casey')
DEBUG: Assignments: {'lynn': [('item 4', 1)], 'drew': [('item 1', 1), ('item 5', 3)], 'john': [('item 2', 2)], 'casey': [('item 3', 2), ('item 6', 5)]}
DEBUG: Scores: {'lynn': 1, 'drew': 4, 'john': 2, 'casey': 7}
DEBUG: Fairness: 2.6457513110645907

DEBUG: Attempt: ('lynn', 'drew', 'casey', 'john')
DEBUG: Assignments: {'lynn': [('item 4', 1)], 'drew': [('item 1', 1), ('item 5', 3)], 'casey': [('item 2', 1)], 'john': [('item 3', 3), ('item 6', 5)]}
DEBUG: Scores: {'lynn': 1, 'drew': 4, 'casey': 1, 'john': 8}
DEBUG: Fairness: 3.3166247903554

DEBUG: Attempt: ('lynn', 'casey', 'john', 'drew')
DEBUG: Assignments: {'lynn': [('item 4', 1)], 'casey': [('item 2', 1)], 'john': [('item 1', 1), ('item 6', 5)], 'drew': [('item 5', 3), ('item 3', 4)]}
DEBUG: Scores: {'lynn': 1, 'casey': 1, 'john': 6, 'drew': 7}
DEBUG: Fairness: 3.1622776601683795

DEBUG: Attempt: ('lynn', 'casey', 'drew', 'john')
DEBUG: Assignments: {'lynn': [('item 4', 1)], 'casey': [('item 2', 1)], 'drew': [('item 1', 1), ('item 5', 3)], 'john': [('item 3', 3), ('item 6', 5)]}
DEBUG: Scores: {'lynn': 1, 'casey': 1, 'drew': 4, 'john': 8}
DEBUG: Fairness: 3.3166247903554

fairness score: 1.4142135623730951
drew: item 1, item 5
john: item 2
casey: item 3
lynn: item 4, item 6
```