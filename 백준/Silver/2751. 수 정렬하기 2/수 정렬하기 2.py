import sys 
arr=[]
n=int(input())
#한 줄에 1개 있는 int값 입력 받고
arr= [int(sys.stdin.readline()) for i in range(n)]
#리스트를 정렬한 것을 int->str로 바꾸어 조인으로 char으로 바꾼다
sys.stdout.write("\n".join(map(str, sorted(arr))))