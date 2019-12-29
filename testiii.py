komb = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, "J": 11, 'Q': 12, 'K': 13,
        'A': 14}
v = input().split()


def suit(x):
    p = [x[i][-1:] for i in range(len(x))]
    if p.count(p[0]) == 5:
        return True
    else:
        return False


def flush(x):
    k = 0
    for i in v:
        k += komb[i[:-1]]
    if suit(x) == True and k == 60:
        print('Royal Flush')
        return True
    elif suit(x) == True and k != 60:
        w = sorted([komb[i[:-1]] for i in x])
        if all(int(a) - int(b) == -1 for a, b in zip(w, w[1:])) == True or all(
                int(a) - int(b) == -1 for a, b in zip(w, w[1:4])) == True and w[-1] == 14:
            print('Straight Flush')
            return True
        else:
            print()
            print('Flush')
            return True
    return False


def other(v):
    h = [i[:-1] for i in v]
    w = sorted([komb[i[:-1]] for i in v])
    f = None
    t = None
    tw = None
    for i in h:
        if h.count(i) == 4:
            f = True
        elif h.count(i) == 3:
            t = True
        elif h.count(i) == 2:
            tw = True
    if flush(v) == True:
        pass
    elif suit(v) == False and all(int(a) - int(b) == -1 for a, b in zip(w, w[1:])) == True or \
            all(int(a) - int(b) == -1 for a, b in zip(w, w[1:4])) == True and w[-1] == 14 and suit == False:
        print('Straight')
    elif f == True:
        print('Four of a Kind')
    elif t == True:
        for j in h:
            if h.count(j) == 2:
                print('Full House')
                break
        else:
            print('Three of a Kind')
            pass
    elif tw == True:
        j = None
        fj = []
        g = None
        for k in h:
            if h.count(k) == 2 and k not in fj:
                j = True
                fj.append(k)
                continue
        if j == True and len(fj) == 2:
            print('Two Pairs')
        else:
            print('Pair')
    else:
        print('High Card')


other(v)

# def other(x):
#    k = 0
#    h = [i[:-1] for i in x]
#    w = sorted([komb[i[:-1]] for i in x])
#    if  flush(x) == True:
#        pass
#    else:
#        f = None
#        t = None
#        tw =None
#        for i in h:
#            if h.count(i) == 4:
#                f = True
#                print('Four of a Kind')
#                break
#            elif h.count(i) == 3:
#                for j in h:
#                    t = True
#                    if j != i:
#                        g = h.count(j)
#                        if g == 2:
#                           tw = True
#                        print('Full House')
#
#                if i ==True:
#                    print('Full House')
#                    break
#                else:
#                    print('Three of a Kind')
#                    break
#
#
#            elif all(int(a) - int(b) == 1  for a, b in zip(w, w[1:])) == True:
#                print('Straight')
#                print(w)
#                break
#            elif h.count(i) == 2:
#                print(i)
#                j =None
#                for k in h:
#                    if k != i:
#                        if h.count(k) == 2:
#                            j =  True
#                            #print('Two Pairs')
#                            break
#                        else:
#                            continue
#                            #print('Pair')
#                if j == True:
#                    print('Two Pairs')
#                    break
#                else:
#                    print('Pair')
#                    break
#
#        else:
#            print('High Card')
