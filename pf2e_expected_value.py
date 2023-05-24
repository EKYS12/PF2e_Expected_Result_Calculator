'''
Title: PF2e Expected Value Calculator
Author: Yasser Siddiqui
Date: 2023-23-05
Description: This is a script that can spit out the probabilities of the tiers of success for a roll in pathfinder 2e with a given DC and modifier, and then use that to spit out the expected numerical result of the roll. Currently only works for checks where the results are constant numbers, like earn income. Does not work for random results, like damage.
'''

'''
First let's define all the functions in the script
'''

def get_dc():
    '''
    This function is just used to get the DC of a check.
    '''

    dc = 0
    while not (dc > 0):
        try:
            dc = int(input('What is the DC: '))
        except:
            print('DC must be a number')

    return dc

def get_mod():
    '''
    This function is just used to get the Players Modifier for the roll.
    '''

    mod = 0
    while not (mod > 0):
        try:
            mod = int(input('What is your modifier: '))
        except:
            print('Modifier must be a number')

    return mod

def get_values():
    '''
    This function is for getting the result values for the different tiers of
    success.
    '''

    crit_success = -1 
    while not (crit_success  > -1):
        try:
            crit_success = float(input('What is the crit success value: '))
        except:
            print('Value must be a number greater than -1')

    success = -1
    while not (success > -1):
        try:
            success = float(input('What is the success value: '))
        except:
            print('Value must be a number greater than -1')


    failure = -1
    while not (failure > -1):
        try:
            failure = float(input('What is the failure value: '))
        except:
            print('Value must be a number greater than -1')


    crit_failure = -1
    while not (crit_failure > -1):
        try:
            crit_failure = float(input('What is crit failure value: '))
        except:
            print('Value must be a number greater than -1')


    values = {
        'crit_success': crit_success,
        'success': success,
        'failure': failure,
        'crit_failure': crit_failure,
    }

    return values

def check_nat_20(face_list):
    '''
    This function will be used to help check for natural 20s in the 
    different success tiers lists in the get_probs function. The 
    arguement in the function is a list of dice face values.
    '''

    if 20 in face_list:
        return True
    else:
        return False

def check_nat_1(face_list):
    '''
    This function will be used to help check for natural 20s in the 
    different success tiers lists in the get_probs function. The 
    arguement in the function is a list of dice face values.
    '''
 
    if 1 in face_list:
        return True
    else:
        return False

def get_probs(dc: int, mod: int):
    '''
    This function is used to get the probabilities of the different
    tiers of success. It takes in the user inputed DC value and 
    player Modifier value and uses that to calculate the odds of the 4
    different tiers of success.
    '''

    # Here get the true DC for the actual dice roll.
    true_dc = dc - mod

    # Addictional DCs for Crit Success and Failure
    crit_success_dc = true_dc + 10
    crit_failure_dc = true_dc - 10 

    # List of every potential roll of the die
    dice = range(1, 21)

    # Lists for the different face values in each success tier
    crit_success = []
    success = []
    failure = []
    crit_failure = []

    # Loop to append the face values to their respective tiers
    for face in dice:
        if face >= true_dc:
            if face >= crit_success_dc:
                crit_success.append(face)
            else:
                success.append(face)
        else:
            if face <= crit_failure_dc:
                crit_failure.append(face)
            else:
                failure.append(face)

    # Nat 20s and 1s bump up and down a tier respectively
    if check_nat_20(success):
        success.remove(20)
        crit_success.append(20)

    elif check_nat_20(failure):
        failure.remove(20)
        success.append(20)

    elif check_nat_20(crit_failure):
        crit_failure.remove(20)
        failure.append(20)

    if check_nat_1(crit_success):
        crit_success.remove(1)
        success.append(1)

    elif check_nat_1(success):
        success.remove(1)
        failure.append(1)

    elif check_nat_1(failure):
        failure.remove(1)
        crit_failure.append(1)
    
    # Calculate probabilites of each tier
    crit_success_prob = len(crit_success)/20
    success_prob = len(success)/20
    failure_prob = len(failure)/20
    crit_failure_prob = len(crit_failure)/20

    probs = {
        'crit_success': crit_success_prob,
        'success': success_prob,
        'failure': failure_prob,
        'crit_failure': crit_failure_prob,
    }
    
    print('='*20)
    print(f'For DC {dc} with player modifier {mod}')
    print('='*20)
    print(f'Critical success chance is: {probs["crit_success"]*100}%')
    print(f'Success chance is:          {probs["success"]*100}%')
    print(f'Failure chance is:          {probs["failure"]*100}%')
    print(f'Critical failure chance is: {probs["crit_failure"]*100}%')
    print('='*20)

    if crit_success_prob + success_prob + failure_prob + crit_failure_prob != 1:
        print('='*20)
        print("Probablity doesn't add up to 1")
        print(f'dc: {dc}, mod {mod}')
        print('='*20)

    return probs

def get_expected_value(probs: dict, values: dict):
    '''
    This function takes the probability dictionary and the values dictionary
    and uses that to calculate the expected value of the roll.
    '''

    expected_value = 0
    for key in probs:
        expected_value += probs[key]*values[key]

    return expected_value

'''
Now that all the function have been defined, we can write out the rest of the code
'''

dc = get_dc()
mod = get_mod()
values = get_values()

probs = get_probs(dc, mod)

expected_value = get_expected_value(probs, values)

print(f'The Expected Value is: {expected_value}')
