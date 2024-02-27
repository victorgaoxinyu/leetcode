def closeStrings(word1: str, word2: str) -> bool:
    m1 = {}
    m2 = {}
    for i in word1:
        m1[i] = m1.get(i, 0) + 1
    
    for i in word2:
        m2[i] = m2.get(i,0) + 1

    print(m1)
    print(m2)

    print(sorted(list(m1.values())))
    print(list(m2.values()))

    
    return (set(m1.keys()) == set(m2.keys())) and (list(m1.values()).sort() == list(m2.values()).sort())


word1 = 'a'
word2 = 'aa'

print(closeStrings(word1, word2))