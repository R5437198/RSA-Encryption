import math as m
import random as r
import numpy as np

def input_data():
    """データの入力"""
    data = input("Type a original message >> ")
    data = data.encode('utf-8', 'replace').decode('utf-8')
    return(data)


class convert():
    """文字コードを変換"""
    def con_char(self, data):
        """文字 -> 数字"""
        self.data = [ord(self) for self in data]
        return(self.data)
        
    def con_number(self, data):
        """数字 -> 文字"""
        self.data = [chr(self) for self in data]
        return(self.data)
        
def lcm(x, y):
    """最小公倍数を求める"""
    lcm = ((x * y) // m.gcd(x, y))
    return(lcm)

def is_prime(x):
    """ミラーラビンテスト"""
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

def generate_prime():
    """素数生成"""
    
    """エラトステネスのふるい.ver"""
    """
    p_number = [i for i in s.primerange(2, 100000)]
    q_number = p_number

    while True:
        p = r.choice(p_number)
        q = r.choice(q_number)
        if p != q:
            break
    """
    
    """ミラーラビンテスト.ver"""
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
        
def generate_keys():
    """秘密鍵と公開鍵の生成"""
    global N, D, E
    p, q = generate_prime()
    N = p * q
    L = lcm(p-1, q-1)
    
    """公開鍵"""
    for i in range(2, L):
        if m.gcd(i, L) == 1:
            E = i
            break
    
    """秘密鍵"""
    for i in range(2, L):
        if (E * i) % L == 1:
            D = i
            break

    return (N, D, E)


def encrypto(data, N, E):
    """暗号化"""
    encrypted_data = [pow(i, E, N) for i in data]
    return (encrypted_data)

def decrypto(data, N, D):
    """復号化"""
    decrypted_data = [pow(i, D, N) for i in data]
    return (decrypted_data)

def main():
    N, D, E = generate_keys()
    print('Private_key >> %d, %d' % (D, N))
    print('Public_key >> %d, %d' % (E, N))

    data = input_data()
    d = convert()
    data = d.con_char(data)
    encrypted_data = encrypto(data, N, E)
    data = ''.join(map(str,encrypted_data))
    print("Encrypted_data >> " + str(data))

    decrypted_data = decrypto(encrypted_data, N, D)
    decrypted_data = d.con_number(decrypted_data)
    data = ''.join(decrypted_data)
    print("Decrypted_data >> " + str(data))

if __name__ == '__main__':    
    main()