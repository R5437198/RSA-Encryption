# RSA Encryption : RSA暗号
暗号理論を勉強しているとRSA暗号が出てきたのですが、アルゴリズムを見ると簡単にそうだったので作ってみました。アルゴリズムについてはググってください。
無駄にclass化してたりとめちゃくちゃです。時間があるときに再構築しときます。ちなみに素数生成の部分で時間がかかります。randomライブラリ使用してるのが原因かな。

## 関数の説明
気が向いたら詳しく書きます。

### con_char()
文字 -> アスキーコードに変換する.
  
### con_number()
アスキーコード -> 文字に変換する.

### input_data()
平文を入力させる.

### lcm(x, y)
x と y の最小公倍数を求める.

### is_prime(x)
ミラーラビンテストで素数か,判定を行う.

### generate_prime()
素数を生成する.生成の仕方として,「エラトステネスのふるい」を用いる方法と「ミラ
ーラビンテスト」を用いる方法を記述している.

- エラトステネスのふるい
「エラトステネスのふるい」を用いて,ある範囲内の素数を生成し,そのなかからランダ
ムで p と q の数字を選ぶ方法を用いている.念のため,p と q の数字が同じになった
場合の処理を記述している.

- ミラーラビンテスト
ランダムに数字を生成し,ミラーラビンテストを用いて素数と判定されるまで,数字を生
成し続ける方法を用いている.p と q それぞれ同じ処理を繰り返す.

### generate_keys()
公開鍵と秘密鍵を生成する.

### encryoto(data, N, E)
暗号化を行う.

### decrypto(data, N, D)
復号化を行う. 

## 参考サイト
プログラム組むにあたって色々なサイトを参考にした記憶があるのですが、作成したのは約2年前で覚えていません。暇なときに調べときます。
