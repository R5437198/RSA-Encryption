import math as m
import random as r
import numpy as np
from sympy import sieve

def input_data(): #データ入力
    data = input("Type a original message >> ")
    data = data.encode('utf-8', 'replace').decode('utf-8')
    return(data)

def convert_char(char): #文字 -> 数字
    return([ord(i) for i in char])
        
def convert_number(num): #数字 -> 文字
    return([chr(i) for i in num])

def encrypto(data, N, E): #暗号化
    encrypted_data = [pow(i, E, N) for i in data]
    return (encrypted_data)

def decrypto(data, N, D): #復号化
    decrypted_data = [pow(i, D, N) for i in data]
    return (decrypted_data)
        
def lcm(x, y): #xとyの最小公倍数を求める
    return((x * y) // m.gcd(x, y))

def is_prime(x): #ミラーラビンテスト
    x = abs(x)
    
    #計算するまでもなく判定できるものははじく
    if x == 2: return True
    if x < 2 or x&1 == 0: return False

    #n-1=2^s*dとし（但しaは整数、dは奇数)、dを求める
    d = (x - 1) >> 1
    while d&1 == 0:
        d >>= 1
    
    #判定をk回繰り返す
    for i in range(100):
        a = r.randint(1,x-1)
        t = d
        y = pow(a, t, x)
        #[0,s-1]の範囲すべてをチェック
        while t != x-1 and y != 1 and y != x-1: 
            y = pow(y,2,x)
            t <<= 1
        if y != x-1 and t&1 == 0:
            return(False)
    return(True)

def generate_prime_mirror(): #素数生成
    while True:
        while True:
            p_number = np.random.randint(1000)
            if is_prime(p_number) == True:
                p = p_number
                break
            
        while True:
            q_number = np.random.randint(1000)
            if is_prime(q_number) == True:
                q = q_number
                break
        
        if p != q:
            break
    return (p, q)

def generate_prime_era(): #素数生成 
    p_number = [i for i in sieve.primerange(2, 100000)]
    q_number = p_number

    while True:
        p = r.choice(p_number)
        q = r.choice(q_number)
        if p != q:
            break
    return (p, q)
        
def generate_keys(): #鍵の生成
    p, q = generate_prime_mirror()
    N = p * q
    L = lcm(p-1, q-1)
    
    # 公開鍵
    for i in range(2, L):
        if m.gcd(i, L) == 1:
            E = i
            break
    
    # 秘密鍵
    for i in range(2, L):
        if (E * i) % L == 1:
            D = i
            break
    return (N, D, E)


if __name__ == '__main__':    
    N, D, E = generate_keys()
    print('Private_key >> %d, %d' % (D, N))
    print('Public_key >> %d, %d' % (E, N))

    data = input_data()
    data = convert_char(data)
    encrypted_data = encrypto(data, N, E)
    data = ''.join(map(str,encrypted_data))
    print("Encrypted_data >> " + str(data))

    decrypted_data = decrypto(encrypted_data, N, D)
    decrypted_data = convert_number(decrypted_data)
    data = ''.join(decrypted_data)
    print("Decrypted_data >> " + str(data))
