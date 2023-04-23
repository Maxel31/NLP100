with open('popular-names.txt', 'r') as f:
    lines = f.readlines()

with open('col1.txt', 'w') as f1, open('col2.txt', 'w') as f2:
    for line in lines:
        cols = line.split('\t')
        
        # 1列目をファイルに書き込む
        f1.write(cols[0] + '\n')
        
        # 2列目をファイルに書き込む
        f2.write(cols[1] + '\n')