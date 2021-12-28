word1 = 'bark'
word2 = 'krab'

''' sposób 1
    metoda z sortowaniem '''

if len(word1) != len(word2): #warunek jest potrzebny, żeby w tym wypadku niepotrzebnie nie sortować
    print('nie')
else:
    print('tak') if sorted(word1) == sorted(word2) else print('nie')


#wersja ze zliczaniem - mniejsza złożoność algorytmu
word1 = 'bark'
word2 = 'krab'

if len(word1) != len(word2): #warunek jest potrzebny, żeby w tym wypadku niepotrzebnie nie sortować
    print('nie')
else:
    w1 = [0] * 26
    w2 = [0] * 26

    # kod ASCII a=97 chcę zapisać pod indeksem 0, więc od ord(97)-97

    for char in word1:
        w1[ord(char)-97] += 1


    for char in word2:
        w2[ord(char)-97] += 1

    print('tak') if w1 == w2 else print('nie')