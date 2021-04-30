import random
import re


def randomise_developers_into_groups(names_input, team_leads):
    set_names = set(map(str, re.split(r"\s|[,]", names_input.strip(' ,'))))
    set_team_leads = set(map(str, re.split(r"\s|[,]", team_leads.strip(" ,"))))
    list_names = list(set_names)
    list_team_leads = list(set_team_leads)
    result = {}

    # # use_case1: if requirement involves having team leads in the original list
    # for member in list_names[:]:
    #     if member in list_team_leads:
    #         result.update({member: []})
    #         list_names.remove(member)
    #
    # for name in list_team_leads[:]:  # remove non existent team lead names entered with valid existing team lead names
    #     if name not in result.keys():
    #         list_team_leads.remove(name)

    # use_case2: if requirement does not include team leads in the original list
    for lead in list_team_leads:
        result.update({lead: []})
        if lead in list_names:  # in case a mad user still input team lead names in original list
            list_names.remove(lead)

    try:
        if list_team_leads == ['']:  # for use_case2, when a user does not enter any team lead name
            raise ZeroDivisionError
        divisor = len(list_names) // len(list_team_leads)
        for name in list_names[:]:
            person = random.choice(list_names)
            a = result.get(list_team_leads[0])  # TypeError for use_case1
            if not (len(a) < divisor or len(list_team_leads) == 1):
                list_team_leads.pop(0)
                a = result.get(list_team_leads[0])
            a.append(person)
            list_names.remove(str(person))
    except ZeroDivisionError:
        return 'You did not provide any team lead'
    except TypeError:
        return 'Provided team leads does not exist in the initial list'
    return result


# def run_tests():
#     testcases = (
#         (
#             ("1 2 3 4 5 6", "3 4"),
#             (["3", "4"], 4, 2)
#         )
#     )
#
#     for testcase in testcases:
#         ((names_input, team_leads), (list_team_leads, team_size, num_teams)) = testcase
#
#         result = randomise_developers_into_groups(names_input, team_leads)
#         assert sorted(result.keys()) == sorted(list_team_leads)
#
#         union = set()
#         for lead in list_team_leads:
#             assert len(result[lead]) >= num_teams
#             union |= set(result[lead])
#         assert len(union) == team_size


if __name__ == '__main__':
    # Use Case 1
    # names = input("Enter names separated by space or comma including your preferred team leads: ")
    # team_leaders = input('Enter the team lead names you provided earlier, separated by space or comma: ')

    # Use Case 2
    names = input("Enter names separated by space or comma excluding your team leads: ")
    team_leaders = input('Enter team lead names separated by space or comma: ')

    print(randomise_developers_into_groups(names, team_leaders))
