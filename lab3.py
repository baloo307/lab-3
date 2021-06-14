text = 'ДУМАЕТСЯЧТОКАЖДОМУЧИТАТЕЛЮДАННОГОПОСОБИЯДОВОДИЛОСЬСДАВАТЬКАКИЕЛИБОЭКЗАМЕНЫИВЫВСЕБ'
kw = 'ДИПЛОМАНТ'
sorted_kw = list(kw)
temp = ""
code = ""
dct = {}
sorted_kw.sort()

for k in kw:
    dct[k] = list(text[0:9])
    text = text[9:len(text)]
    
new_dct = {w:dct[w] for w in sorted_kw}

new_lst = [[] for i in range(0, 9)]
    
for v in new_dct.values():
    i = 0
    for w in v:
        new_lst[i].append(w)
        i += 1
        
for i in new_lst:
    code += temp.join(i) + " "
print(code)
