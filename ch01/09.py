import random

# 単語の先頭と末尾の文字以外をランダムに入れ替える関数
def shuffle_word(word):
    if len(word) <= 4:
        return word
    else:
        middle = list(word[1:-1])
        random.shuffle(middle)
        return word[0] + ''.join(middle) + word[-1]

# スペースで区切られた単語列をランダムに並び替える関数
def shuffle_sentence(sentence):
    words = sentence.split()
    shuffle_words = [shuffle_word(word) for word in words]
    return ' '.join(shuffle_words)

# 実行例
sentence = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
ans = shuffle_sentence(sentence)
print("original sentence:", sentence)
print("shuffled sentence:", ans)