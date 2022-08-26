import string

sym = string.digits.encode() + string.ascii_letters.encode() + string.punctuation.encode()

def get_pair_sum(sum: int) -> list:
    #ijkl
    res = []
    for i in sym:
        for j in sym:
            for k in sym:
                for l in sym:
                    num1 = ((j << 8) + i) & 0xFFFF
                    num2 = ((l << 8) + k) & 0xFFFF
                    n1n2 = (num1 + num2) & 0xFFFF
                    if n1n2 == sum:
                        pair = bytes(chr(i)+chr(j)+chr(k)+chr(l), "ascii")
                        res.append(pair)

    return res

def get_pair_mul(sum: int, input:list) -> list:
    #ijkl
    res = []
    for i in input:
        n1n2 = (i[0] * i[2]) & 0xFFFF
        if n1n2 == sum:
            res.append(i)

    return res

# s4 = get_pair_sum(0x9DE0)
# print(s4)
# s3 = get_pair_sum(0xB3D3)
# print(s3)
# s2 = get_pair_sum(0xCEA7)
# print(s2)
# s1 = get_pair_sum(0x8FE2)
# print(s1)

# print("============================")

# m4 = get_pair_mul(0x30F0, s4)
# print(m4)
# m3 = get_pair_mul(0x2B74, s3)
# print(m3)
# m2 = get_pair_mul(0x171C, s2)
# print(m2)
# m1 = get_pair_mul(0x31D8, s1)
# print(m1)

#cdef
m4 = [b'l0tm', b'l1tl', b'l2tk', b'l3tj', b'l4ti', b'l5th', b'l6tg', b'l7tf', b'l8te', b'l9td', b'lat<', b'lbt;', b'lct:', b'ldt9', b'let8', b'lft7', b'lgt6', b'lht5', b'lit4', b'ljt3', b'lkt2', b'llt1', b'lmt0', b'lnt/', b'lot.', b'lpt-', b'lqt,', b'lrt+', b'lst*', b'ltt)', b'lut(', b"lvt'", b'lwt&', b'lxt%', b'lyt$', b'lzt#', b'lAt\\', b'lBt[', b'lCtZ', b'lDtY', b'lEtX', b'lFtW', b'lGtV', b'lHtU', b'lItT', b'lJtS', b'lKtR', b'lLtQ', b'lMtP', b'lNtO', b'lOtN', b'lPtM', b'lQtL', b'lRtK', b'lStJ', b'lTtI', b'lUtH', b'lVtG', b'lWtF', b'lXtE', b'lYtD', b'lZtC', b'l!t|', b'l"t{', b'l#tz', b'l$ty', b'l%tx', b'l&tw', b"l'tv", b'l(tu', b'l)tt', b'l*ts', b'l+tr', b'l,tq', b'l-tp', b'l.to', b'l/tn', b'l:tc', b'l;tb', b'l<ta', b'l=t`', b'l>t_', b'l?t^', b'l@t]', b'l[tB', b'l\\tA', b'l]t@', b'l^t?', b'l_t>', b'l`t=', b'l{t"', b'l|t!', b't0lm', b't1ll', b't2lk', b't3lj', b't4li', b't5lh', b't6lg', b't7lf', b't8le', b't9ld', b'tal<', b'tbl;', b'tcl:', b'tdl9', b'tel8', b'tfl7', b'tgl6', b'thl5', b'til4', b'tjl3', b'tkl2', b'tll1', b'tml0', b'tnl/', b'tol.', b'tpl-', b'tql,', b'trl+', b'tsl*', b'ttl)', b'tul(', b"tvl'", b'twl&', b'txl%', b'tyl$', b'tzl#', b'tAl\\', b'tBl[', b'tClZ', b'tDlY', b'tElX', b'tFlW', b'tGlV', b'tHlU', b'tIlT', b'tJlS', b'tKlR', b'tLlQ', b'tMlP', b'tNlO', b'tOlN', b'tPlM', b'tQlL', b'tRlK', b'tSlJ', b'tTlI', b'tUlH', b'tVlG', b'tWlF', b'tXlE', b'tYlD', b'tZlC', b't!l|', b't"l{', b't#lz', b't$ly', b't%lx', b't&lw', b"t'lv", b't(lu', b't)lt', b't*ls', b't+lr', b't,lq', b't-lp', b't.lo', b't/ln', b't:lc', b't;lb', b't<la', b't=l`', b't>l_', b't?l^', b't@l]', b't[lB', b't\\lA', b't]l@', b't^l?', b't_l>', b't`l=', b't{l"', b't|l!']
#89ab
m3 = [b'g5l~', b'g6l}', b'g7l|', b'g8l{', b'g9lz', b'galR', b'gblQ', b'gclP', b'gdlO', b'gelN', b'gflM', b'gglL', b'ghlK', b'gilJ', b'gjlI', b'gklH', b'gllG', b'gmlF', b'gnlE', b'golD', b'gplC', b'gqlB', b'grlA', b'gsl@', b'gtl?', b'gul>', b'gvl=', b'gwl<', b'gxl;', b'gyl:', b'gzl9', b'gAlr', b'gBlq', b'gClp', b'gDlo', b'gEln', b'gFlm', b'gGll', b'gHlk', b'gIlj', b'gJli', b'gKlh', b'gLlg', b'gMlf', b'gNle', b'gOld', b'gPlc', b'gQlb', b'gRla', b'gSl`', b'gTl_', b'gUl^', b'gVl]', b'gWl\\', b'gXl[', b'gYlZ', b'gZlY', b'g:ly', b'g;lx', b'g<lw', b'g=lv', b'g>lu', b'g?lt', b'g@ls', b'g[lX', b'g\\lW', b'g]lV', b'g^lU', b'g_lT', b'g`lS', b'g{l8', b'g|l7', b'g}l6', b'g~l5', b'l5g~', b'l6g}', b'l7g|', b'l8g{', b'l9gz', b'lagR', b'lbgQ', b'lcgP', b'ldgO', b'legN', b'lfgM', b'lggL', b'lhgK', b'ligJ', b'ljgI', b'lkgH', b'llgG', b'lmgF', b'lngE', b'logD', b'lpgC', b'lqgB', b'lrgA', b'lsg@', b'ltg?', b'lug>', b'lvg=', b'lwg<', b'lxg;', b'lyg:', b'lzg9', b'lAgr', b'lBgq', b'lCgp', b'lDgo', b'lEgn', b'lFgm', b'lGgl', b'lHgk', b'lIgj', b'lJgi', b'lKgh', b'lLgg', b'lMgf', b'lNge', b'lOgd', b'lPgc', b'lQgb', b'lRga', b'lSg`', b'lTg_', b'lUg^', b'lVg]', b'lWg\\', b'lXg[', b'lYgZ', b'lZgY', b'l:gy', b'l;gx', b'l<gw', b'l=gv', b'l>gu', b'l?gt', b'l@gs', b'l[gX', b'l\\gW', b'l]gV', b'l^gU', b'l_gT', b'l`gS', b'l{g8', b'l|g7', b'l}g6', b'l~g5']
#4567
m2 = [b'3atm', b'3btl', b'3ctk', b'3dtj', b'3eti', b'3fth', b'3gtg', b'3htf', b'3ite', b'3jtd', b'3ktc', b'3ltb', b'3mta', b'3nt`', b'3ot_', b'3pt^', b'3qt]', b'3rt\\', b'3st[', b'3ttZ', b'3utY', b'3vtX', b'3wtW', b'3xtV', b'3ytU', b'3ztT', b'3Pt~', b'3Qt}', b'3Rt|', b'3St{', b'3Ttz', b'3Uty', b'3Vtx', b'3Wtw', b'3Xtv', b'3Ytu', b'3Ztt', b'3[ts', b'3\\tr', b'3]tq', b'3^tp', b'3_to', b'3`tn', b'3{tS', b'3|tR', b'3}tQ', b'3~tP', b'ta3m', b'tb3l', b'tc3k', b'td3j', b'te3i', b'tf3h', b'tg3g', b'th3f', b'ti3e', b'tj3d', b'tk3c', b'tl3b', b'tm3a', b'tn3`', b'to3_', b'tp3^', b'tq3]', b'tr3\\', b'ts3[', b'tt3Z', b'tu3Y', b'tv3X', b'tw3W', b'tx3V', b'ty3U', b'tz3T', b'tP3~', b'tQ3}', b'tR3|', b'tS3{', b'tT3z', b'tU3y', b'tV3x', b'tW3w', b'tX3v', b'tY3u', b'tZ3t', b't[3s', b't\\3r', b't]3q', b't^3p', b't_3o', b't`3n', b't{3S', b't|3R', b't}3Q', b't~3P']
#0123
m1 = [b'n0t_', b'n1t^', b'n2t]', b'n3t\\', b'n4t[', b'n5tZ', b'n6tY', b'n7tX', b'n8tW', b'n9tV', b'nat.', b'nbt-', b'nct,', b'ndt+', b'net*', b'nft)', b'ngt(', b"nht'", b'nit&', b'njt%', b'nkt$', b'nlt#', b'nmt"', b'nnt!', b'nAtN', b'nBtM', b'nCtL', b'nDtK', b'nEtJ', b'nFtI', b'nGtH', b'nHtG', b'nItF', b'nJtE', b'nKtD', b'nLtC', b'nMtB', b'nNtA', b'nOt@', b'nPt?', b'nQt>', b'nRt=', b'nSt<', b'nTt;', b'nUt:', b'nVt9', b'nWt8', b'nXt7', b'nYt6', b'nZt5', b'n!tn', b'n"tm', b'n#tl', b'n$tk', b'n%tj', b'n&ti', b"n'th", b'n(tg', b'n)tf', b'n*te', b'n+td', b'n,tc', b'n-tb', b'n.ta', b'n/t`', b'n:tU', b'n;tT', b'n<tS', b'n=tR', b'n>tQ', b'n?tP', b'n@tO', b'n[t4', b'n\\t3', b'n]t2', b'n^t1', b'n_t0', b'n`t/', b't0n_', b't1n^', b't2n]', b't3n\\', b't4n[', b't5nZ', b't6nY', b't7nX', b't8nW', b't9nV', b'tan.', b'tbn-', b'tcn,', b'tdn+', b'ten*', b'tfn)', b'tgn(', b"thn'", b'tin&', b'tjn%', b'tkn$', b'tln#', b'tmn"', b'tnn!', b'tAnN', b'tBnM', b'tCnL', b'tDnK', b'tEnJ', b'tFnI', b'tGnH', b'tHnG', b'tInF', b'tJnE', b'tKnD', b'tLnC', b'tMnB', b'tNnA', b'tOn@', b'tPn?', b'tQn>', b'tRn=', b'tSn<', b'tTn;', b'tUn:', b'tVn9', b'tWn8', b'tXn7', b'tYn6', b'tZn5', b't!nn', b't"nm', b't#nl', b't$nk', b't%nj', b't&ni', b"t'nh", b't(ng', b't)nf', b't*ne', b't+nd', b't,nc', b't-nb', b't.na', b't/n`', b't:nU', b't;nT', b't<nS', b't=nR', b't>nQ', b't?nP', b't@nO', b't[n4', b't\\n3', b't]n2', b't^n1', b't_n0', b't`n/']

# seg000:007F                 mov     al, byte ptr ds:input+0Fh ; ""
# seg000:0082                 mov     bl, byte ptr ds:input+0Eh ; ""
# seg000:0086                 cmp     al, bl
# seg000:0088                 jnz     error_exit
m4_1 = [i for i in m4 if i[2]==i[3]]
#print(m4_1)

# seg000:008C                 mov     al, byte ptr ds:input+1 ; ""
# seg000:008F                 cmp     al, 30h ; '0'
# seg000:0091                 jnz     error_exit
m1_1 = [i for i in m1 if i[1]==0x30]
#print(m1_1)

# seg000:0095                 mov     bl, byte ptr ds:input+6 ; ""
# seg000:0099                 add     al, 3
# seg000:009B                 cmp     al, bl
# seg000:009D                 jnz     short error_exit
m2_1 = [i for i in m2 if i[2]==0x33]
#print(m2_1)

# seg000:009F                 mov     al, byte ptr ds:input+4 ; ""
# seg000:00A2                 mov     bl, byte ptr ds:input+2 ; ""
# seg000:00A6                 cmp     al, bl
# seg000:00A8                 jnz     short error_exit
m1_1_1 = []
m2_1_1 = []
for i in m1_1:
    is_added = False
    for j in m2_1:
        if i[2] == j[0]:
            m2_1_1.append(j)
            is_added = True

    if is_added:
        m1_1_1.append(i)

#print(m1_1_1)
#print(m2_1_1)

# seg000:00AA                 mov     al, byte ptr ds:input+5 ; ""
# seg000:00AD                 dec     al
# seg000:00AF                 mov     bl, byte ptr ds:input+0Ah ; ""
# seg000:00B3                 cmp     al, bl
# seg000:00B5                 jnz     short error_exit

m2_1_1_1 = []
m3_1 = []
for i in m3:
    is_added = False
    for j in m2_1_1:
        if i[2] == (j[1]-1):
            #print(chr(i[2]))
            #print(chr(j[1]-1))
            m2_1_1_1.append(j)
            is_added = True

    if is_added:
        m3_1.append(i)

#print(m2_1_1_1)
#print(m3_1)

# seg000:00B7                 mov     al, byte ptr ds:input+9 ; ""
# seg000:00BA                 cmp     al, bl
# seg000:00BC                 jz      short error_exit

m3_1_1 = []
for i in m3_1:
    if i[1] != i[2]:
        m3_1_1.append(i)

#print(m3_1_1)

# seg000:00BE                 mov     al, byte ptr ds:input+0Bh ; ""
# seg000:00C1                 inc     al
# seg000:00C3                 mov     bl, byte ptr ds:input+0Ch ; ""
# seg000:00C7                 cmp     al, bl
# seg000:00C9                 jnz     short error_exit

m4_1_1 = []
m3_1_1_1 = []
for i in m3_1_1:
    is_added = False
    for j in m4_1:
        if (i[3]+1) == j[0]:
            m4_1_1.append(j)
            is_added = True

    if is_added:
        m3_1_1_1.append(i)

print(set(m4_1))
print(set(m3_1_1_1))
print(set(m2_1_1_1))
print(set(m1_1_1))
