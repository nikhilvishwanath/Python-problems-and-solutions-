def FirstWords(string):
    '''
    State 0 : ready to scan the word, space after fullstop.
    state 1 : after fullstop.
    state 2 : ignore the words if not followed by fullstop.
    state 3 : space after full stop
    '''
    s = string
    state = 0
    word =[]
    l = []
    for i in range(len(s)):

        if state == 1 and s[i].isdigit():
            state = 2
        if s[i].isspace() and state == 0:
            state = 2
            l.append(''.join(word))
            word = []
        if state == 0 and s[i].isspace() == False:
            print(s[i])
            word.append(s[i])
        if s[i].isspace() and state == 1:
            state = 0
        if  s[i] ==".":
            state = 1

    return l
