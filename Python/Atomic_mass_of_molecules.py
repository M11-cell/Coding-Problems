
PERIODIC_TABLE = {
    'H': 1, 'He': 4, 'Li': 7, 'Be': 9, 'B': 11,
    'C': 12, 'N': 14, 'O': 16, 'F': 19, 'Ne': 20,
    'Na': 23, 'Mg': 24, 'Cl': 35
}


def molecule_mass(*elements : str) -> tuple[str, int]:
    """Compute the molecular mass from a sequence of elements passed as arguments.
    Subscript elemental notation is replaced with a '-'. 
     
    Arguments:
    elements    (list[str])   --   a list of periodic table elements.

    Returns:
    (tuple[str, int])         --   the first return value is the molecule as a string,
                                   and the second is its atomic mass.    

    >>> molecule_mass('H-2', 'O')
    ('H-2_O', 18)
    >>> molecule_mass('H-2')
    ('H-2', 2)
    >>> molecule_mass('Na', 'Cl')
    ('Na_Cl', 58)
    >>> molecule_mass('C-6', 'H-12', 'O-6')
    ('C-6_H-12_O-6', 180)
    >>> molecule_mass('H-2', 'O', 'C-1', 'N-1')
    ('H-2_O_C-1_N-1', 44)
    """

    parts = ''
    element = ''
    quantity = 0
    element_mass = 0
    sum = 0

    # TODO: Figure out which element is being evaluated 
    # TODO: Multiply that elements atomic number by the number of times its repeats

    #Take away: .split() will split string into a LIST 

        
#We have:
# Isolated element 
# Elemenent Quantitiy. 
# We want to find the total mass of the element 
# We wanna find the sum of molecule 


#We are missingz; 
# We also wanna concact the string together

    for element_chars in elements: # C-6

        if '-' in element_chars:
            parts = element_chars.split('-') # [H-2] --> ['H', '2']
            element = parts[0] # --> ['H']
            quantity = int(parts[1]) # --> ['2]
            element_mass = PERIODIC_TABLE[element] * quantity

        else:

            element = element_chars
            quantity = 1
            element_mass = PERIODIC_TABLE[element] * quantity

        sum += element_mass
        

    concact = ''
    

    # ('H-2', '0') --> elements_chars --> elements[0]
    for element_chars in elements:

        concact += (element_chars + '_')
        
    concact = concact[:-1]
    return (concact , sum)


if __name__ == '__main__':

    import doctest

    doctest.testmod(verbose=True)