assignments = []

rows = 'ABCDEFGHI'
cols = '123456789'

"""
    Helper function and arrays from the lecture
"""
def cross(a, b):
    return [s+t for s in a for t in b]

boxes = cross(rows, cols)

#diagonal units
diagonal_unit_1 = []
diagonal_unit_2 = []

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]

for i in range(0,9):
    diagonal_unit_1.append(rows[i]+cols[i])
    diagonal_unit_2.append(rows[8-i]+cols[i])
diagonal_units = [diagonal_unit_1]+[diagonal_unit_2]

unitlist = row_units + column_units + square_units + diagonal_units
#print (unitlist)
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)



#print (diagonal_unit_1)
#print (diagonal_unit_2)
#------------------------------------------------------------------
def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # Find all instances of naked twins
    #display(values)
    #print (column_units)
    # Eliminate the naked twins as possibilities for their peers
    #let's go through each individual box

    twinArray = []

    for row in row_units:
        for box in row:
            if len(values[box]) == 2:
                for boxIterate in row:
                    if len(values[boxIterate]) == 2 and values[box] == values[boxIterate] and boxIterate != box:
                        twinArray.append(box)
                        remove_elements_row(values,row, boxIterate)


    for col in column_units:
        for box in col:
            if len(values[box]) == 2:
                for boxIterate in col:
                    if len(values[boxIterate]) == 2 and values[box] == values[boxIterate] and boxIterate != box:
                        remove_elements_col(values,col, boxIterate)


    for sqr in square_units:
        for box in sqr:
            if len(values[box]) == 2:
                for boxIterate in sqr:
                    if len(values[boxIterate]) == 2 and values[box] == values[boxIterate] and boxIterate != box:
                        remove_elements_sqr(values, sqr, boxIterate)

    #print ()
    #display(values)
    #print(peers)
    return values    
"""
    localSet = set([])
    for box in boxes:
        #if the length of the box is 2 it is a possible twin
        if len(values[box]) == 2:
            # lets go through and find if it has a twin among it's peers
            for peerBox in peers[box]:
                # if a peer box also has a length of 2 it is a possible twin
                if len(values[peerBox]) == 2 and values[peerBox] == values[box]:
                    # remove the values in this box from the rest of the peer boxes
                    #remove_elements(values,box)  
                    if peerBox not in localSet:
                        localSet.add(peerBox)
                    #print (peerBox)  
                    #print (values[peerBox])
    print (localSet)
"""


"""
    for box in boxes:
        #if the length of the box is 2 it is a possible twin
        if len(values[box]) == 2:
            # lets go through and find if it has a twin among it's peers
            for peerBox in peers[box]:
                # if a peer box also has a length of 2 it is a possible twin
                if len(values[peerBox]) == 2 and values[peerBox] == values[box]:
                    # remove the values in this box from the rest of the peer boxes
                    remove_elements(values,box)
"""



def remove_elements_row(values, row, boxIterate):
    for box in row:
        if len(values[box]) > 2 and values[boxIterate] != values[box]:
            for i in values[boxIterate]:
                localString = values[box].replace(i, '')
                values[box] = localString


def remove_elements_col(values, col, boxIterate):
    for box in col:
        if len(values[box]) > 2 and values[boxIterate] != values[box]:
            for i in values[boxIterate]:
                localString = values[box].replace(i, '')
                values[box] = localString

def remove_elements_sqr(values, sqr, boxIterate):
    for box in sqr:
        if len(values[box]) > 2 and values[boxIterate] != values[box]:
            for i in values[boxIterate]:
                localString = values[box].replace(i, '')
                values[box] = localString


def remove_elements(values, box):
    """
        This function takes a sudoku grid and a box, and uses this to eliminate 
        values in the box from it's peers.
        Helper function for naked twins. 
    """
    #print (box)
    #print ("remove from>>>>>>>>>>>>>>>>>>>>>")
    #print (values [box])
    # iterate through the peers of the given box ###Not efficent way of solving this###
    for i in values[box]:
        # go through the two values from the twin ###Not efficent way####
        #print (values[peerBox])   
        for colPeer in column_units:
            if box in colPeer:
                for peerBox in colPeer:
                    if values[box] != values[peerBox] and  str(i) in values[peerBox]: #len(values[peerBox]) > 1:
                        localString = values[peerBox].replace(i,'')
                        values[peerBox] = localString

        for rowPeer in row_units:
            if box in rowPeer:
                for peerBox in rowPeer:
                    if values[box] != values[peerBox] and str(i) in values[peerBox]: #len(values[peerBox]) > 1:
                        localString = values[peerBox].replace(i,'')
                        values[peerBox] = localString

        for squarePeer in square_units :
            if box in squarePeer:
                for peerBox in squarePeer:
                    if values[box] != values[peerBox] and str(i) in values[peerBox]: #len(values[peerBox]) > 1:
                        localString = values[peerBox].replace(i,'')
                        values[peerBox] = localString                
"""
        for peerBoxLocal in peers[box]:
            if values[box] != values[peerBoxLocal] and len(values[peerBoxLocal]) > 1:
                #print ("inside remover")
                if i in values[peerBoxLocal]:
                    localString = values[peerBoxLocal].replace(i,"")
                    # replace each values in the peers list that are also in the twin box
                    values[peerBoxLocal]= localString

"""
def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    values = []
    all_digits = '123456789'
    for c in grid:
        if c == '.':
            values.append(all_digits)
        elif c in all_digits:
            values.append(c)
    assert len(values) == 81
    return dict(zip(boxes, values))
    pass

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return
    pass

def eliminate(values):
    singleVal=[]
    actualVal=[]
    for k in values:
        if len(values[k]) == 1 :
            #print (k)
            singleVal.append(k)
            actualVal.append(values[k])
    
    #print (singleVal) 
    #print (actualVal)
    #print (peers)
    lengthOfSingleVal = len(singleVal) #get length of array
    indexOfSingleVal = 0
    while indexOfSingleVal < lengthOfSingleVal:
        key = singleVal[indexOfSingleVal]
        value = actualVal[indexOfSingleVal]
        for k in peers:
            if k != key and key in peers[k]:
                peers[k].remove(key)
                newString = values[k].replace(value,'')
                values[k] = newString
        indexOfSingleVal += 1
    return values

    pass

def only_choice(values):
    singleVal=[]
    actualVal=[]
    for k in values:
        if len(values[k]) == 1 :
            singleVal.append(k)
            actualVal.append(values[k])
            
    counter = 0
    
    for unit in unitlist:
        localArray = ''
        localSet= set([])
        possibleSet = set([1,2,3,4,5,6,7,8,9])
        possibleArray = '123456789'
        for box in unit:
            if len(values[box]) == 1:
                localArray += str(values[box])
                localSet.add(values[box])
        for s in localArray:
            if s in possibleArray:
                locStr = possibleArray.replace(s,"")
                possibleArray = locStr
        
        for i in possibleArray:
            counter = 0
            for box in unit:
                if (i in values[box]):
                    counter += 1
                    holdBox = box
            if (counter ==1):
                values[holdBox] = i
                        
                
        """for box in unit:
            if len(values[box]) != 1:
                #print (values[box])
                for x in localArray:
                    boxValue = values[box].replace(x, '')
                    values[box] = boxValue
                    #print (values[box])"""

    #print(values)
    return values
    pass

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        # Use the Eliminate Strategy
        values = eliminate(values)
        # Use the Only Choice Strategy
        values = only_choice(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values    
    pass

def search(values):
    values = reduce_puzzle(values)
    
    if values is False:
        return False
    bool = True
    for k in values:
        if len(values[k]) == 1:
            bool &=True
        else :
            bool &=False
    if bool is True:
        return values
    # Choose one of the unfilled squares with the fewest possibilities
    #minBox 
    #print(boxes)

    foundG1 = False
    
    for b in boxes:
        if len(values[b]) > 1:
            if foundG1 is False:
                minBox = b
                foundG1 = True
            if len(values[b]) < len(values[minBox]):
                minBox = b

    #print(minBox)
    for value in values[minBox]:
        #print(value)
        new_sudoku = values.copy()
        new_sudoku[minBox] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt
    pass

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    #display(values)
    #print ()

    eliminate(values)
    #display(values)
    #print()

    only_choice(values)
    #display(values)
    #print()

    search(values)
    #reduce_puzzle(values)
    display(values)
    print()

    return values
if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    for box in values:
        assign_value(values, box, values[box])
    
    display(values)

    visualize_assignments(values)  

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
