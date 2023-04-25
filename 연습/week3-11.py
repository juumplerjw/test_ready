with open('fescape.txt', 'r') as f:
    content = f.read()
    print('\"fescape.txt\"\n\t' + content.replace('\n', ''))