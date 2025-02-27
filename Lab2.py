#Hayden Seiberlich - Lab 2 Foundations
#9/19/24
#Exploring Sets in Python

#Unionizes set A and B
def set_union (A,B):
    return A.union(B)

#Function finds all unique values to make into a union.
def union(A, B):
    result = []
    for x in A:
        if x not in B:
            result = result + list(str(x))
    for x in B:
        result = result + list(str(x))
    return result

#Function finds all unique values to make into a list
# into a set union. This is less accurate but possible.
def list_union(A, B):
    result = []
    for x in A:
        if x not in B:
            result = result + list(str(x))
    for x in B:
        result = result + list(str(x))
    return result


#Tester for first two functions.
def Test01():
    #Curly brackets show a union/set.
    A = {1, 2, 8}
    B = {1, 2, 3, 4, 5}
    print(set_union(A,B))
    #Square brackets show a list, not a union.
    A = [1, 2, 8]
    B = [1, 2, 4, 5, 6]
    print(list_union(A,B))

#Test Call
Test01()

#Function to find where sets intersect.
def set_intersection(A, B):
    result = []
    for x in A:
        if x in B:
            result = result + list(str(x))
    return result

#Function to show what elements of set A
#are not in set B
def set_difference(A,B):
    result = []
    for x in A:
        if x not in B:
            result = result + list(str(x))
    return result

#Function to show if A is a subset of B
def set_isSubSet(A,B):
    return A.issubset(B)

def isProperSubset(A,B):
    if A == B:
        return True
    else:
        return False


#Optional Tester
def Test02():
    A = {1, 2, 3, 4}
    B = {1, 4, 5, 6}
    print(set_intersection(A,B))
    print(set_difference(A,B))
    A = {1, 2, 3}
    B = {1, 2, 3, 4}
    print(set_isSubSet(A,B))
    print(isProperSubset(A,B))

#Test Caller
Test02()