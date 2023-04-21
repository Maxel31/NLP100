text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics"
word_list = text.split() # 単語に分割
result = [len(word.strip(",.")) for word in word_list] # 各単語の文字数をresultに格納
print(result)