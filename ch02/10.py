# ファイルを開く
with open('popular-names.txt', 'r') as f:
    lines = f.readlines()

# リストの要素数を取得
num_lines = len(lines)
print("行数:", num_lines)
