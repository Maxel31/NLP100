#与えられたシーケンス（文字列やリストなど）からn-gramを作る関数
def n_gram(sequence, n): # sequenceで様々なリストを扱えるようにする
    return [sequence[i:i+n] for i in range(len(sequence)-n+1)]

text1 = "paraparaparadise"
text2 = "paragraph"

#それぞれのbi-gramの集合をX,Yとする
X = n_gram(text1, 2)
Y = n_gram(text2, 2)

# セット(Set)に変換(重複する要素を削除)
set_X = set(X)
set_Y = set(Y)

# 和集合の計算
union_set = set_X.union(set_Y)
print("和集合:", union_set)

# 積集合の計算
intersection_set = set_X.intersection(set_Y)
print("積集合:", intersection_set)

# 差集合の計算
difference_set = set_X.difference(set_Y)
print("X-Yの差集合:", difference_set)

difference_set = set_Y.difference(set_X)
print("Y-Xの差集合:", difference_set)

#’se’というbi-gramがXおよびYに含まれるかどうかを調べる
if "se" in set_X:
    print("Xにseは含まれる")
else:
    print("Xにseは含まれない")

if "se" in set_Y:
    print("Yにseは含まれる")
else:
    print("Yにseは含まれない")
