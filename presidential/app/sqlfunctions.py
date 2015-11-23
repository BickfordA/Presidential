

def canidateNamePair(list):
    outlist = []
    for element in list:
        outlist.append(element.encode('ascii', 'ignore'))
    return outlist
