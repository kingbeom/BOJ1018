import sys
input=sys.stdin.readline
n,m=map(int, input().split())
mapp=[list(input()) for _ in range(n)]
b_chk=[['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B']]
w_chk=[['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W']]
solve=[]
def chk(y,x,b_cnt,w_cnt):
    for a in range(8):
        for b in range(8):
            if mapp[y+a][x+b] != b_chk[a][b]:
                b_cnt+=1
            elif mapp[y+a][x+b] != w_chk[a][b]:
                w_cnt+=1
    if b_cnt>=w_cnt:
        cnt=w_cnt
    elif w_cnt>=b_cnt:
        cnt=b_cnt
    b_cnt=0
    w_cnt=0

    return cnt

for y in range(n):
    for x in range(m):
        y_chk=y+8
        x_chk=x+8
        if y_chk>n or x_chk>m:
            continue
        solve.append(chk(y,x,0,0))

print(min(solve))