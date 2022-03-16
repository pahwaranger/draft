import math
import itertools
import logging

import click
import pandas

from draft.utils import utils


def determine_assignments_for_sorting(df, people, items_per_person, all_items):
    assignments = {}
    reserved_items = []
    skipped = []
    for person in utils.perpetual_snake_order(people, items_per_person)[: len(all_items)]:
        if person not in assignments:
            assignments[person] = []
        item = utils.get_first_preference(df[person], reserved_items=reserved_items)
        if item is not None:
            priority = utils.get_priority(df, person, item)
            reserved_items.append(item)
            assignments[person].append((item, priority))
        else:
            skipped.append(person)
    for person in skipped:
        item = sorted(list(set(all_items) - set(reserved_items)))[0]
        priority = utils.get_priority(df, person, item)
        reserved_items.append(item)
        assignments[person].append((item, priority))
    return assignments


def permute_draft_order(df):
    people = list(df.columns)
    all_items = utils.get_all_possible_items(df)
    items_per_person = math.ceil(1.0 * len(all_items) / len(people))
    attempts = []
    for sorting in list(itertools.permutations(people)):
        logging.debug(f"Attempt: {sorting}")
        assignments = determine_assignments_for_sorting(df, sorting, items_per_person, all_items)
        logging.debug(f"Assignments: {assignments}")
        fairness = utils.compute_fairness(assignments)
        logging.debug(f"Fairness: {fairness}\n")
        attempts.append((fairness, assignments))
    return attempts


def get_fairest_attempt(attempts):
    return sorted(attempts, key=lambda attempt: attempt[0])[0]


@click.command()
@click.option(
    "--file_path",
    default="test/data/draft_zero.csv",
    prompt="Path to CVS file",
    help="Path to CSV file.",
)
@click.option("--verbose", is_flag=True, default=False, help="Verbose mode.")
def main(file_path, verbose):
    if verbose:
        logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)
        logging.info("Set debug level to DEBUG")
    else:
        logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
    df = pandas.read_csv(file_path)
    fairness, assignments = get_fairest_attempt(permute_draft_order(df))
    print(f"fairness score: {fairness}")
    for person, assignment in assignments.items():
        one_line = ", ".join([item[0] for item in assignment])
        print(f"{person}: {one_line}")


if __name__ == "__main__":
    main()
