# Serca_BOJ26766

# input.txt 열기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 받기
herat = ''' @@@   @@@ 
@   @ @   @
@    @    @
@         @
 @       @ 
  @     @  
   @   @   
    @ @    
     @     '''                  # 하트를 변수에 저장하고
for n in range(int(input())):   # 반복할 수를 input 받아 반복해서
    print(herat)                # 하트의 개수를 출력한다