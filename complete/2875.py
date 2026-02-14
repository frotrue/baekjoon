a,b,c = map(int,input().split())
team = min(a//2,b)

Candidate = (a+b) - (team*3)
c -= Candidate

if c > 0:
    team -= (c+2)//3

print(max(team,0))