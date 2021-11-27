import math
import numpy as np


class ConvertText:
    """文字コードを変換"""

    @staticmethod
    def convert_to_number(text):
        """ 文字 -> 数字 """
        number = [ord(string) for string in text]
        return number

    @staticmethod
    def convert_to_string(text):
        """ 数字 -> 文字 """
        string = [chr(string) for string in text]
        return string

    @staticmethod
    def convert_list_to_text(x):
        """ リストから要素を抜き出す """
        return str(''.join(map(str, x)))


class Calculate:
    """ 計算する """

    @classmethod
    def generate_prime(cls, upper_limit=10000):
        """ 素数生成 - ミラーラビンテスト """
        while True:
            while True:
                p_number = np.random.randint(upper_limit)
                if cls.is_prime(p_number):
                    p = p_number
                    break
            while True:
                q_number = np.random.randint(upper_limit)
                if cls.is_prime(q_number):
                    q = q_number
                    break
            if p != q:
                break
        return p, q

    @staticmethod
    def is_prime(n):
        sqrt_n = math.ceil(math.sqrt(n))
        for i in range(2, sqrt_n):
            if n % i == 0:
                return False
        return True


class Crypt:
    """ 暗号化・復号化を行う """

    @classmethod
    def crypt(cls):
        key_generation, encryption, decryption = cls.generate_keys()
        print("")
        print('Public_key >> %d' % encryption)
        print('Private_key >> %d' % decryption)
        raw_text = input("Type a text >> ")
        print('raw_text >>>', raw_text)

        # 暗号化
        number = ConvertText.convert_to_number(raw_text)
        encrypted_data = cls.encrypt(number, key_generation, encryption)
        print("Encrypted_data >> ", ConvertText.convert_list_to_text(encrypted_data))
        # 復号化
        decrypted_data = cls.decrypt(encrypted_data, key_generation, decryption)
        text = ConvertText.convert_to_string(decrypted_data)
        print("Decrypted_data >> " + ConvertText.convert_list_to_text(text))

    @staticmethod
    def encrypt(data, key_generation, encryption):
        """ 暗号化 """
        encrypted_data = [pow(i, encryption, key_generation) for i in data]
        return encrypted_data

    @staticmethod
    def decrypt(data, key_generation, decryption):
        """復号化"""
        decrypted_data = [pow(i, decryption, key_generation) for i in data]
        return decrypted_data

    @staticmethod
    def generate_keys():
        """ 秘密鍵と公開鍵の生成 """
        # 公開鍵と秘密鍵の片割れ
        encryption, decryption = 0, 0
        # 素数
        prime_1, prime_2 = Calculate.generate_prime()
        # 暗号化アルゴリズム
        key_generation = prime_1 * prime_2
        # 最小公倍数
        least_common_multiple = math.lcm(prime_1-1, prime_2-1)
        # 公開鍵
        for i in range(2, least_common_multiple):
            if math.gcd(i, least_common_multiple) == 1:
                encryption = i
                break
        # 秘密鍵
        for i in range(2, least_common_multiple):
            if (encryption * i) % least_common_multiple == 1:
                decryption = i
                break
        return key_generation, encryption, decryption


if __name__ == '__main__':    
    Crypt.crypt()
