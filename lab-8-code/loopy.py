
def rec(lst):
    print (lst, len(lst))
    lst.append('moxie')
    rec(lst)

def rec2():

    while True:
        print ("and again...")
        
rec([])
