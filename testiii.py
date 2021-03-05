def kidds_encryption(text, reverse=False):
    sl = {'e': '8', 't': ';', 'h': '4', 'o': '‡', 's': ')', 'n': '*', 'a': '5', 'i': '6', 'r': '(',
          'f': '1', 'd': '†', 'l': '0', 'm': '9', 'b': '2', 'y': ':', 'g': '3', 'u': '?', 'v': '¶', 'c': '-', 'p': '.'}

    text = text.lower().replace(',', '').replace(' ', '').replace('\'', '').replace('x', '')
    k = [i for i in text]
    dec = ''
    if reverse == True:
        ty = {j:i for i,j in sl.items()}
        for i in k:
            dec += ty[i]
    for i in k:
        if i in sl:
            dec += sl[i]
    return dec


