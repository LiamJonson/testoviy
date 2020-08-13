def skob(string):
    m = {'(': ')', '{': '}', '[': ']'}
    st = []
    k = []
    for j, i in enumerate(string, 1):
        if i in m:
            st.append(i)
            k .append(j)
        elif i in m.values():
            if st:
                if m[st[-1]] == i:
                    st.pop()
                    k.pop()
                    continue
                elif m[st.pop()] != i:
                    return j

            else:
                return j
    if not st:
        return 'Success'
    else:
        return k[-1]

print(skob(input()))


