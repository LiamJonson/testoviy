def enigma(text, ref, rot1, rot2, rot3):
    ROTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
              1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
              2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
              3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO'}
    REFLECTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                  1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
                  2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
                  3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
                  4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',
                  }
    ui=''
    text = text.upper().replace(',', '').replace(' ', '')
    for i in text:
        k=i
        for i1 in [rot3, rot2, rot1]:
            print(i)
            k = ROTORS[i1][ROTORS[0].index(k)]
        s = REFLECTORS[ref][REFLECTORS[0].index(k)]
        for i2 in [rot1, rot2, rot3]:
            s = ROTORS[0][ROTORS[i2].index(s)]

        ui+=s

    return ui








print((enigma('Some encripted text', 1, 1, 2, 3)),end='')

