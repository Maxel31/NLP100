text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
word_list = text.split() # 単語に分割


# 単語の位置に応じて、1文字または2文字を取得する
one_char = [1, 5, 6, 7, 8, 9, 15, 16, 19] # 1文字の単語
result = {}
for i, word in enumerate(word_list): #forループでインデックスを取得
    if i+1 in one_char:
        result[word[0]] = i+1
    else:
        result[word[:2]] = i+1
        
print(result)
