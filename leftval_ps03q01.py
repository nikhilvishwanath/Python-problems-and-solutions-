#problem set 3 quesion 1
#algorithm is similar to searching in BST
def Leftval( x, avl):
    cmp = avl
    temp = avl
    if temp.isempty():
        return "None"

    if x < temp.value :
        if temp.left.isempty():
            return "None"
        elif x > temp.left.value:
            return temp.left.value
        else:
            return Leftval(x,temp.left)

    if x > temp.value :
        if temp.right.isempty():
            return temp.value
        elif temp.right.value > x :
            return temp.right.value
        else:
            return Leftval(x,temp.right)
