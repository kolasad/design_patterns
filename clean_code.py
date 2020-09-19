from constants import REQUIRED_DAYS_FROM_LAST_VISIT


def should_visit_doctor(days_from_last_visit, diseases: list = None):
    """

    :param days_from_last_visit:
    :param diseases:
    :return:
    """
    number_of_diseases = len(diseases) if diseases else 0  # get number of diseases if exists

    if days_from_last_visit > 1 and number_of_diseases > 3:
        return True
    elif days_from_last_visit > REQUIRED_DAYS_FROM_LAST_VISIT:
        return True
    return False


assert should_visit_doctor(3, diseases=['a', 'b', 'c', 'd']) is True
assert should_visit_doctor(9) is False
assert should_visit_doctor(12) is True


last_visited = True
if last_visited:
    print('True')

names = []
if names:
    print(names)  # will not print empty list

