def get_stages():
    """
    returns a list with string representations of the 
    """
    
    noose = """
    ________
    |        |
    |        
    |       
    |       
    |       
    |
    -------------------
    """
    head = """
    ________
    |        |
    |        O 
    |       
    |       
    |       
    |
    -------------------
    """
    leftarm = """
    ________
    |        |
    |        O
    |       /
    |       
    |       
    |
    -------------------
    """

    rightarm = """
    ________
    |        |
    |        O
    |       / \ 
    |        
    |        
    |
    -------------------
    """
    chest = """
    ________
    |        |
    |        O
    |       /|\ 
    |       
    |       
    |
    -------------------
    """
    torso = """
    ________
    |        |
    |        O
    |       /|\ 
    |        | 
    |       
    |
    -------------------
    """    
    leftleg = """
    ________
    |        |
    |        O
    |       /|\ 
    |        |
    |       / 
    |
    -------------------
    """    
    rightleg = """
    ________
    |        |
    |        O
    |       /|\ 
    |        |
    |       / \ 
    |
    -------------------
    """

    new_stages = [noose, head, leftarm, rightarm, chest, torso, leftleg, rightleg]

    return new_stages

def rip():
    return """
                ________
                |        |
                |        O
                |       /|\ 
                |        |
                |       / \ 
                |
                |      R.I.P.
                -------------------
    """

def full():
    return """
                        ________
                        |        |
                        |        O
                        |       /|\ 
                        |        |
                        |       / \ 
                        |
                        |      
                        -------------------
    """