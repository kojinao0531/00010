# Comment＝{command+/}
# print("hello world!")
# print("海賊王に俺はなる")

# # 演算
# print(1+1)
# print(10/2)

# 変数
# unko="hello world"

# print(unko)
# ログインIDなどで使える
# unko = "l_size"
# unko_length=0
# unko_timis=5.5

# # print(unko_timis)

# メモ
# print(type(unko))　
# print(type(unko_length))　イント
# print(type(onko_times))　フロート
# 同じタイプのものしか演算できない

# ブーリアン型  はい、いいえの判定
# unko_shitai =ture

# 条件分岐と関係演算子
# if else elif
# # ==,!=,<,>,>=,<=
# if unko_length > 6:
# 	print("ooi")
# elif unko_length == 0:
# 	print("nai")
# else:
# 	print("sukunai")

# # 関数
def unko_funnbaru(aug):
	unnko_status =aug

	if(unnko_status < 10):
	     return "mada daijyobu"
	else:
	    return "yabai"

# print(unko_funnbaru(12))	
# # type("unnko_status")  -元々入っている関数       

# listプログラムは0から始まる
unko_list = ["unko_small", "unko_medium", "unko_large"]
# print(unko_list[0])

# ループ分 for
# unko_funnbaru(5)
# unko_funnbaru(5)
# unko_funnbaru(5)

# for index in range (11):
# 	print(unko_funnbaru(index))

# for item in unko_list:
# 	print(item)
# with
# open()

# with open("./unko.txt" , "r") as file:
# 	print(file)




#class　＝　共通点のある機能を効率よく実装していくために変数や関数をまとめて型にはめたテンプレート
# クラスとインスタンスの関係
# SNSみたいなやつになる

# class Card:
# 	def __init__(self,date, eser_name):
# 		self.date = date
# 		self.user_name = user_name
# 	def message(self):
# 	    return "この投稿は"　+ self.user_name + "さんが" + self.date + "に投稿しました"	

# date_a = "2020-01-01"
# user_name_a = "Taro"
# card_a = Card(date_a, user_name_a)

# print(card_a.message

# import = モジュール

# モジュール：変数、関数、クラスなどを汎用的に使えるようにする。他人の書いたものを使う

# import math 円周率が表示される
# print(math.pi)

import numpy

munpy_list = [3, 1, 5, 10, 2093, 304 ,123]
print(numpy.sum(munpy_list))









