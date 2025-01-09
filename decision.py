<<<<<<< HEAD
import json
from age_logic import age_decision
from salary_logic import salary_decision
from variables import *

with open('data.json', 'r') as file:
    data = json.load(file)

color = data['color']
customer_type = data['customer_type']
salary = data['salary']
age = data['age']
gender = data['gender']
age_logic_decision = age_decision(age,gender)
salary_logic_decision = salary_decision(salary,customer_type,color)



def final_decision(age_decision,salary_decision):
    if age_decision == decision_approve and salary_decision == decision_approve:
        decision = decision_approve
    else:
        decision = decision_decline
    result = {
        "policy_decision":decision
    }
    return result

=======
import json
from age_logic import age_decision
from salary_logic import salary_decision
from variables import *

with open('data.json', 'r') as file:
    data = json.load(file)

color = data['color']
customer_type = data['customer_type']
salary = data['salary']
age = data['age']
gender = data['gender']
age_logic_decision = age_decision(age,gender)
salary_logic_decision = salary_decision(salary,customer_type,color)



def final_decision(age_decision,salary_decision):
    if age_decision == decision_approve and salary_decision == decision_approve:
        decision = decision_approve
    else:
        decision = decision_decline
    result = {
        "policy_decision":decision
    }
    return result

>>>>>>> 37acecf453e6c893182e304f3b3aebaaa9f01ac5
print(final_decision(age_logic_decision,salary_logic_decision))