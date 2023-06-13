with open('hello.txt', 'w') as file:    # hello.txt 파일을 쓰기 모드(w)로 열기
    for i in range(1, 6):
        file.write('line {0}\.n'.format(i))
    
