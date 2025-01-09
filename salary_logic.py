from variables import *

def salary_decision(salary,customer_type,color):
    if salary < 5000:
        decision = decision_decline
    elif customer_type == "Self Employed" and salary < 100000:
        decision = decision_decline
    elif salary < 50000 and color == "Black":
        decision = decision_decline
    else:
        decision = decision_approve
    
    return decision 
