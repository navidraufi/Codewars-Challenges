# With list ls and 3 towns to visit they can make a choice between: .

# The sums of distances are then: 162, 163, 165, 165, 167, 168, 170, 172, 173, 175.

# The biggest possible sum taking a limit of 174 into account is then 173 and the distances of the 3 corresponding towns is [55, 58, 60].


def alphanumeric(password):
    
    
    if len(password.split()) > 1 or password.strip() == "":
        return False
    
    if not password.isalnum():
        return False            

    return True
    

print(alphanumeric(""))