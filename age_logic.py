<<<<<<< HEAD
from variables import *


def age_decision(age, gender):
    if age > 60:
        decision = decision_decline
    elif age < 18 and gender == "Male":
        decision = decision_decline
    else:
        decision = decision_approve

    return decision

=======
from variables import *


def age_decision(age, gender):
    if age > 60:
        decision = decision_decline
    elif age < 18 and gender == "Male":
        decision = decision_decline
    else:
        decision = decision_approve

    return decision

>>>>>>> 37acecf453e6c893182e304f3b3aebaaa9f01ac5
