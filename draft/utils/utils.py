import logging
import statistics

def get_first_preference(person, reserved_items):
    try:
        return person[~person.isin(reserved_items)].iloc[0]
    except IndexError:
        return None

def draft_order(people, rounds, cur_round=1):
    if cur_round<rounds:
        return people + draft_order(people=people[::-1], rounds=rounds, cur_round=cur_round+1)
    else:
        return people

def get_all_possible_items(df):
    all_items = set()
    for col in df:
        all_items.update(set(df[col].unique()))
    return all_items

def get_priority(df, person, item):
    return df[df[person]==item].index[0] + 1

def compute_fairness(all_assignments):
    scoring = {
        person: sum(assignment[1] for assignment in assignments)
        for person, assignments in all_assignments.items()
    }
    logging.debug(scoring)
    return statistics.stdev(scoring.values())
