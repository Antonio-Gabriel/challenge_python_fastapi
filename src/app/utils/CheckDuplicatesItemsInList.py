def checkDuplicatesItemsInList(listOfElems):
    """Check if given list contains any duplicates"""
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True
