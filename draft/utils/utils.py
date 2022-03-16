import math
import logging
import statistics


def get_first_preference(person, reserved_items):
    """gets person's most prefered item after removing any already claimed items"""
    try:
        pref = person[~person.isin(reserved_items)].iloc[0]
        return None if isinstance(pref, float) and math.isnan(pref) else pref
    except IndexError:
        return None


def linear_order(people, rounds, cur_round=1):
    if cur_round < rounds:
        return people + linear_order(people=people, rounds=rounds, cur_round=cur_round + 1)
    else:
        return people


def temporary_snake_order(people, rounds, cur_round=1):
    if cur_round < rounds:
        maybe_reverse = people[::-1] if cur_round <= 2 else people
        return people + temporary_snake_order(people=maybe_reverse, rounds=rounds, cur_round=cur_round + 1)
    else:
        return people


def perpetual_snake_order(people, rounds, cur_round=1):
    if cur_round < rounds:
        return people + perpetual_snake_order(people=people[::-1], rounds=rounds, cur_round=cur_round + 1)
    else:
        return people


def get_all_possible_items(df):
    """gets all items listed by people and excludes nulls"""
    all_items = set()
    for col in df:
        all_items.update(set(df[col].dropna().unique()))
    return all_items


def get_priority(df, person, item):
    """gets a rank value for a"""
    try:
        return df[df[person] == item].index[0] + 1
    except IndexError:
        return len(df[person]) + 1


def compute_fairness(all_assignments):
    scoring = {
        person: sum([assignment[1] for assignment in assignments]) for person, assignments in all_assignments.items()
    }
    logging.debug(f"Scores: {scoring}")
    return statistics.stdev(scoring.values())


def get_all_linear_draft_permutations(people):
    return [people[i:] + people[:i] for i in range(len(people))]
