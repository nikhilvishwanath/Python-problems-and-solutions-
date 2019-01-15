# We will be using search method and we will store the path
# in new array, so whatever part from root  will be common for both
# will tell us about all the small ancestors. From these we will
# choose the last ancestor which will be least common ancestor.

def ancestor(avl,x,y):
    #writing down the path from root to given numbers in tree
    a = path(avl,x)
    b = path(avl,y)
    i = 0
    a.insert(0,["root",avl.value])
    b.insert(0,["root",avl.value])
    print(a,b)

    # to check whether the given numbers are in tree or not
    if a.pop()[1] != x:
        return  (" %d is not in Tree" %x)
    if b.pop()[1] != y:
        return ("%d is not in Tree" %y)

    # to check all the common ancestors and return the least
    for i in range(min(len(a),len(b))):
        if a[i] != b[i]:
            return a[i-1][1]
    return a[i][1]

#path function is similar to search algorithm
#it adds one more entry along with the number
#that it is on left or right side of its parent 
def path(avl, x):
  if avl.isempty():
    return None
  if avl.value == x:
    return [["V",avl.value]]
  if avl.value < x:
    return [["R",avl.right.value]] + path(avl.right, x)
  else:
    return [["L",avl.left.value]] + path(avl.left, x)
