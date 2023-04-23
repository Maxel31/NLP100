with open('popular-names.txt', 'r') as f:
    text = f.read()

# タブをスペースに置換
fixed_text = text.replace('\t', ' ')

with open('11.txt', 'w') as f:
    f.write(fixed_text)