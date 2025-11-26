def split_by_capitals(formula):
    t = []
    splited_formula = []
    for char in formula:
        if char.isupper():
            if t:
                splited_formula.append(''.join(t))
            t = [char]
        else:
            t.append(char)
    if t:
        splited_formula.append(''.join(t))
    return splited_formula
def split_at_number(formula):
    digits = []
    letters = []
    for char in formula:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
    if digits == []:
        digits.append("1")
    return ''.join(letters), int(''.join(digits))



def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_molecule(molecular_formula):
    atom_counts = {}
    for atom in split_by_capitals(molecular_formula):
        atom_name, atom_count = split_at_number(atom)
        atom_counts[atom_name] = atom_counts.get(atom_name, 0) + atom_count
    return atom_counts
