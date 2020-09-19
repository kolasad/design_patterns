from constants import REQUIRED_DAYS_FROM_LAST_VISIT


def should_visit_doctor(days_from_last_visit, diseases: list = None):
    """

    :param days_from_last_visit:
    :param diseases:
    :return:
    """
    number_of_diseases = len(diseases) if diseases else 0

    if days_from_last_visit > 1 and number_of_diseases > 3:
        return True
    elif days_from_last_visit > REQUIRED_DAYS_FROM_LAST_VISIT:
        return True
    return False


print(should_visit_doctor(3, ['a', 'b', 'c', 'd']))
print(should_visit_doctor(9))
print(should_visit_doctor(12))

# snake_case
# CamelCase
# pascalCase
