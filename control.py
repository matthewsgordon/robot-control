# Function to return robot direction from sensor values
# Matthew Gordon
# 24840416
# 12/11/21
def choose_action(s1: float, s2: float, s3: float, s4: float,t:float) -> str:
    # Check mutiple sensor combinations first to ensure the system returns correct values
    # Scenario 16 
    if s1 <=t and s2 <=t and s3 <=t and s4 <= t:
        return "Trapped"
    # Scenario 15   
    elif s1 > t and s2 > t and s3 > t and s4 > t:
        return "Continue"
    # Scenario 11
    elif s1 <=t and s2 <=t and s4 <= t:
        return "S"
    # Scenario 12
    elif s1 <=t and s2 <=t and s3 <= t:
        return "W"
    # Scenario 13
    elif s1 <=t and s3 <=t and s4 <= t:
        return "E"
    # Scenario 14
    elif s2 <=t and s3 <=t and s4 <= t:
        return "N"
    # Scenario 5
    elif s1 <=t and s2 <= t:
        return "SW"
    # Scenario 6
    elif s1 <=t and s3 <= t:
        return "E or W"
    # Scenario 7
    elif s1 <=t and s4 <= t:
        return "SE"
    # Scenario 8
    elif s2 <=t and s3 <= t:
        return "NW"
    # Scenario 9
    elif s2 <=t and s4 <= t:
        return "N or S"
    # Scenario 10
    elif s3 <=t and s4 <= t:
        return "NE"
    # Scenario 1
    if s1 <= t:
        return "S"
    # Scenario 2
    elif s2 <= t:
        return "W"
    # Scenario 3
    elif s3 <= t:
        return "N"
    # Scenario 4
    elif s4 <= t:
        return "E"


 