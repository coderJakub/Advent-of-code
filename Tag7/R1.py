
def getValue(c):
    twoPair1 ='.'
    threePair = '.'
    fourPair = '.'
    twoPair2='.'

    for i in range(len(c)):
        for j in range(i+1,len(c)):
            if c[i]==c[j]:
                if twoPair1==c[i]:
                    if threePair==c[i]:
                        if fourPair==c[i]:
                            return 7
                        else:
                            fourPair=c[i]
                    else:
                        threePair=c[i]
                elif twoPair2==c[i]:
                    return 6
                    twoPair=c[i]
                elif twoPair1=='.':
                    twoPair1=c[i]
                else:
                    twoPair2=c[i]
    if twoPair1=='.':
        return 1
    if threePair=='.' and twoPair2=='.':
        return 2
    if threePair=='.' and twoPair2!='.':
        return 3
    if threePair!='.' and twoPair2=='.':
        if fourPair=='.':
            return 4
        return 5
    return 0

