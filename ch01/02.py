text1 = "パトカー"
text2 = "タクシー"
result = "".join([a + b for a, b in zip(text1, text2)])
print(result)

# zip関数は単語が3つ以上の場合でも同様
text3 = "クレーン"
result2 = "".join([a + b + c for a, b, c in zip(text1, text2, text3)])
print(result2)