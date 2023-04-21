#与えられたシーケンス（文字列やリストなど）からn-gramを作る関数
def n_gram(sequence, n): # sequenceで様々なリストを扱えるようにする
    return [sequence[i:i+n] for i in range(len(sequence)-n+1)]

# ”I am an NLPer”という文から単語bi-gram，文字bi-gramを得る
text = "I am an NLPer"
words = text.split() # 単語に分割
char = list(text.replace(" ", "")) # 空白を消して文字列をリストに変換
word_bigram = n_gram(words, 2)
char_bigram = n_gram(char, 2)

print("word_bigram: ", word_bigram)  
print("char_bigram: ", char_bigram) 