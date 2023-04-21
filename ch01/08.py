#ord()関数は、引数にUnicode文字を1つだけ取り、その文字に対応するUnicodeコードポイントを整数値で返す
def cipher(s):
    return "".join([chr(219 - ord(c)) if c.islower() else c for c in s])

# 暗号文の例
message1 = "Hello World!"
print("Original message:", message1)
print("Encrypted message:", cipher(message1))
print("Decrypted message:", cipher(cipher(message1)))

message2 = "NLP is so difficult!"
print("Original message:", message2)
print("Encrypted message:", cipher(message2))
print("Decrypted message:", cipher(cipher(message2)))