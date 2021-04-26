def caesar(text, key):
    al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = text.replace(',', '').replace(' ', '').replace('\'', '').replace('.', '').upper()
    dec = ''
    for i in text:
        dec += al[(al.index(i) + key) % len(al)]
    return dec


def sm(i, pairs):
    pairs = pairs.upper().split(' ')
    for ij in pairs:
        print(i)
        if i in ij:
            if i == ij[1]:
                i = ij[0]
            elif i == ij[0]:
                i = ij[1]

            return i


def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3, pairs=""):
    ROTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
              1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
              2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
              3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
              }
    REFLECTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                  1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
                  2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
                  3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
                  4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',
                  }
    ui = ''
    text = text.upper().replace(',', '').replace(' ', '')

    for i in text:
        k = i

        if i in pairs.upper().replace(' ', ''):
            if pairs.upper().replace(' ', '').count(i) > 1:
                return 'Извините, невозможно произвести коммутацию'
            else:
                k = sm(i, pairs)
        shift3 = (shift3 + 1) % 26
        if rot3 == 2:
            if shift3 == 5:
                shift2 += 1
        if rot3 == 3:
            if shift3 == 22:
                shift2 += 1
        if rot3 == 1:
            if shift3 == 22:
                shift2 += 1
        if rot2 == 2:
            if shift2 == 4 and shift3 == 6 or shift2 == 4 and shift3 == 23 or shift2 == 4 and shift3 == 18:
                shift2 += 1
                if shift2 == 5:
                    shift1 += 1
        if rot3 == 3:
            if shift3 == 22:
                shift2 += 1
        if rot2 == 3:
            if shift2 == 21 and shift3 == 23 or shift2 == 21 and shift3 == 6 or shift2 == 21 and shift3 == 18:
                shift2 += 1
                if shift2 == 22:
                    shift1 += 1
        if rot3 == 1:
            if shift3 == 22:
                shift2 += 1
        if rot2 == 1:
            if shift2 == 21 and shift3 == 23 or shift2 == 21 and shift3 == 6 or shift2 == 21 and shift3 == 18:
                shift2 += 1
                if shift2 == 22:
                    shift1 += 1
        k = caesar(k, shift3)
        k = ROTORS[rot3][ROTORS[0].index(k)]
        k = caesar(k, shift2 - shift3)
        k = ROTORS[rot2][ROTORS[0].index(k)]
        k = caesar(k, shift1 - (shift2))
        k = ROTORS[rot1][ROTORS[0].index(k)]
        k = caesar(k, -(shift1))
        s = REFLECTORS[ref][REFLECTORS[0].index(k)]
        s = caesar(s, shift1)
        s = ROTORS[0][ROTORS[rot1].index(s)]
        s = caesar(s, shift2 - (shift1))
        s = ROTORS[0][ROTORS[rot2].index(s)]
        s = caesar(s, -(shift2) + shift3)
        s = ROTORS[0][ROTORS[rot3].index(s)]
        s = caesar(s, -shift3)
        ui += s
    if ui in pairs.upper().replace(' ', ''):
        ui = sm(ui, pairs)
    return ui


print(enigma('A', 1, 1, 0, 2, 0, 3, 0, 'AC'))

