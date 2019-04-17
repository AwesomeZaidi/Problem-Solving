
test_input = [
    {'name': 'Trey', 'manager': None},
    {'name': 'Paul', 'manager': 'Trey'},
    {'name': 'Peter', 'manager': 'Trey'},
    {'name': 'Mary', 'manager': 'Trey'},
    {'name': 'Joe', 'manager': 'Paul'},
    {'name': 'Larry', 'manager': 'Paul'},
    {'name': 'Alex', 'manager': None},
    {'name': 'Jesse', 'manager': 'Alex'},
    {'name': 'Henry', 'manager': 'Alex'},
    {'name': 'Moe', 'manager': 'Larry'},
]

""" 
Trey
    Paul
        Joe
        Larry
            Moe
    Peter
    Mary
Alex
    Jesse
    Henry
"""

def find_top_level_managers(managers_list):
    top_level_managers = {}
    for manager in managers_list:   
        if manager['manager'] == None:
            top_level_managers[manager['name']] = manager
    
    return top_level_managers.keys()
    
    
def find_employees(manager):
#     go through our initial dictionary
    for person in test_input:
        if person.manager == manager:
            top_level_managers.manager += person
#         if the employees manager is in our top_level_managers
      
    return top_level_managers

    
print(find_top_level_managers(test_input)) 
# def list_managers(managers_list):
    
#     loop through list of objects
#         store tabs, innitially 0
#         store currentManager
#         check if 'manager' is None
#             set tabs to 0
#             print the name
#             assign currentManager
#         if the next empolyees manager is the currentManager
#             append 4 spaces to the tab var
#             print out the tab, then the employee
#             assign currentManager

