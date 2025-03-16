# import文とAS
# パターン1
# import lesson_package.utils

# r = lesson_package.utils.say_twice('hello')

# print(r)

# パターン2
# from lesson_package import utils

# r = utils.say_twice('hello')

# print(r)

# パターン3 functionだけをimportする
# from lesson_package.utils import say_twice

# r = say_twice('hello')

# print(r)
# パターン3の場合は、関数名だけで呼び出せるので、
# 同じファイル内で定義された関数とコンフリクトする可能性がある。
# その場合は、パターン1やパターン2を使うとよい。


# パターン4 ASを使う
# from lesson_package import utils as u

# r = u.say_twice('hello')

# print(r)

# パターン4の場合、uとするとどんなモジュールかわかりにくい。
# 長いモジュール名を短くしたい場合に使うとよい。


# 絶対パスと相対パスのImport
# from lesson_package.tools import utils
# from lesson_package.talk import human

# r = utils.say_twice('hello')
# print(r)

# print(human.sing())
# print(human.cry())


# アスタリスクのインポートと__init__.pyと__all__の意味
# from lesson_package.talk import animal
# from lesson_package.talk import *

# print(animal.sing())
# print(animal.cry())

# # *を使うと、__init__.pyに__all__を定義していないと、
# # すべてのモジュールがimportされる。
# # __all__ = ['animal']を定義している場合は、
# # animalモジュールだけがimportされる。
# # __all__ = ['animal', 'human']とすると、
# # animalとhumanがimportされる。
# # __all__ = []とすると、importされるモジュールはない。


# ImportErrorの使い所
# try:
#     from lesson_package import utils
# except ImportError:
#     from lesson_package.tools import utils

# print(utils.say_twice('word'))

# 古いバージョン等でモジュールが見つからない場合に、
# 他のモジュールをimportするようにすることができる。
# ただし、モジュールが見つからない場合は、
# ImportErrorが発生するので、
# それをキャッチする必要がある。


# 組み込み関数
# # print(globals())
# # デフォルトで用意されている関数の中身について
# # https://docs.python.org/ja/3/library/functions.html

# import builtins
# builtins.print()

# ranking = {
#     'A': 100,
#     'B': 85,
#     'C': 95
# }

# print(ranking.get('A'))
# print(sorted(ranking, key=ranking.get))
# # 出力結果: ['B', 'C', 'A']
# # key=ranking.getで、rankingの値を取得して、
# # それをソートする。

# print(sorted(ranking, key=ranking.get, reverse=True))
# # 出力結果: ['A', 'C', 'B']
# # reverse=Trueで、逆順にソートする。


# 標準ライブラリ
# # 参考：https://docs.python.org/ja/3/library/index.html

# # 　例）defaultdict... https://docs.python.org/ja/3/library/collections.html#collections.defaultdict
# s = "fdjsagrthyrtghyrgt"

# d = {}
# for c in s:
#     if c not in d:
#         d[c] = 0
#     d[c] += 1
# print(d)

# d = {}
# for c in s:
#     d.setdefault(c, 0)
#     d[c] += 1
# print(d)
# # 出力結果: {'f': 1, 'd': 1, 'j': 1, 's': 1, 'a': 1, 'g': 3, 'r': 2, 't': 2, 'h': 2, 'y': 3}

# from collections import defaultdict

# d = defaultdict(int)

# for c in s:
#     d[c] += 1
# print(d)

# print(d['y'])
# # 出力結果: 3
# # 標準ライブラリのdefaultdictを使うと、
# # 初期値を設定することができる。
# # ここでは、intを指定しているので、初期値は0になる。


# importする際の記述方法
# import collections
# import os
# import sys

# import lesson_package
# # 他のチームが作ったパッケージ

# import config
# # 自分が作ったパッケージ

# # 標準ライブラリとサードパーティのライブラリ、自作のライブラリの順に並べる
# # 各グループはアルファベット順に並べる
# # 標準ライブラリ、サードパーティのライブラリ、自作のライブラリの間には空行を入れる

# print(collections.__file__)
# print(lesson_package.__file__)
# print(config.__file__)

# print(sys.path)


# # # __name__と__main__
# import lesson_package.talk.animal
# import config


# def main():
#     lesson_package.talk.animal.sing()


# if __name__ == '__main__':
#     main()

# """
# # __name__は、モジュールが実行されたときに、
# # そのモジュールの名前が入る。
# # ただし、importされたときは、モジュール名が入る。
# # __main__は、モジュールが実行されたときに、
# # '__main__'が入る。
# # つまり、if __name__ == '__main__':の中身は、
# # モジュールが実行されたときだけ実行される。
# # 他のモジュールからimportされたときは、実行されない。
# # このように、他のモジュールからimportされたときに、
# # 実行されないようにするために、
# # if __name__ == '__main__':を使う。
# """


# # # クラスの定義
# class Person(object):
#     def say_something(self):
#         print('hello')
# # Python2の名残から、objectを書いておくとよい。
# # Person(object)とすることで、objectクラスを継承している。


# person = Person()
# person.say_something()
# # 下記の記述よりも、
# # 上記のpersonというオブジェクトを使った方が、
# # クラスの使い回しができる。
# # このpersonというものが、何ができるのか
# # メソッドとしてつけてやった方がオブジェクト指向という意味でわかりやすい。


# def person(name):
#     if name == 'A':
#         print('hello')
# # こちらの関数でやりたいことはできるが、
# # この関数を使い回すことはできない。
# # この関数を使い回すためには、
# # クラスを使った方がよい。


# クラスの初期化とクラスの変数
# class Person(object):

#     def __init__(self, name):
#         self.name = name
#         print(self.name)

#     def say_something(self):
#         print('I am {}. hello'.format(self.name))
#         self.run(3)

#     def run(self, num):
#         print('run' * num)


# person = Person('Mike')
# person.say_something()


# # コンストラクタとデストラクタ
# class Person(object):
#     # コンストラクタ インスタンスが生成されるときに実行される
#     def __init__(self, name):
#         self.name = name
#         print(self.name)

#     def say_something(self):
#         print('I am {}. hello'.format(self.name))
#         self.run(3)

#     def run(self, num):
#         print('run' * num)

#     # デストラクタ インスタンスが削除されるときに実行される
#     def __del__(self):
#         print('good bye')


# person = Person('Mike')
# person.say_something()

# del person
# # インスタンスが削除されると、デストラクタが実行される。
# # del personを書かないと、'##########'が実行後に'good bye'が表示される。
# # del personを書くと、'good bye'が実行後に'##########'が表示される。
# print('##########')


# # クラスの継承
# # class Car(object):
# #     def run(self):
# #         print('run')


# # class ToyotaCar(Car):
# #     pass


# # class TeslaCar(Car):
# #     def run(self):
# #         # 継承したメソッドを上書きする
# #         print('super fast')

# #     def auto_run(self):
# #         print('auto run')


# # car = Car()
# # car.run()

# # toyota_car = ToyotaCar()
# # toyota_car.run()

# # tesla_car = TeslaCar()
# # tesla_car.run()
# # tesla_car.auto_run()
# # 出力結果: run
# # 出力結果: run
# # 出力結果: super fast
# # 出力結果: auto run

# # クラスの継承を使うことで、
# # 他のクラスのメソッドを使い回すことができる。
# # また、継承したメソッドを上書きすることもできる。
# # さらに、継承したクラスに新しいメソッドを追加することもできる。

# class Car(object):
#     def __init__(self, model=None):
#         self.model = model

#     def run(self):
#         print('run')


# class ToyotaCar(Car):
#     def run(self):
#         print('fast')


# class TeslaCar(Car):
#     def __init__(self, model='Model S', enable_auto_run=False):
#         # self.model = model
#         # 親で呼び出しているinitを呼び出す
#         super().__init__(model)
#         self.enable_auto_run = enable_auto_run

#     def run(self):
#         # 継承したメソッドを上書きする
#         print('super fast')

#     def auto_run(self):
#         print('auto run')


# car = Car()
# car.run()

# print('############')
# toyota_car = ToyotaCar('Lexus')
# print(toyota_car.model)
# toyota_car.run()

# print('############')
# tesla_car = TeslaCar('Model S')
# print(tesla_car.model)
# tesla_car.run()
# tesla_car.auto_run()


# # # プロパティを使った属性の設定
# # class Car(object):
# #     def __init__(self, model=None):
# #         self.model = model

# #     def run(self):
# #         print('run')


# # class ToyotaCar(Car):
# #     def run(self):
# #         print('fast')


# # class TeslaCar(Car):
# #     def __init__(self, model='Model S', enable_auto_run=False):
# #         # self.model = model
# #         super().__init__(model)
# #         # self.enable_auto_run = enable_auto_run
# #         # アンダースコアをつけることで、プライベート変数にする
# #         self._enable_auto_run = enable_auto_run

# #     # @propertyをつけることで、
# #     # プロパティとして使える
# #     @property
# #     def enable_auto_run(self):
# #         # プライベート変数を返すことで、
# #         # 読み込みはできるが、書き込みはできないようになる
# #         return self._enable_auto_run

# #     # 書き換えるためには、
# #     # @プロパティ名.setterを使う
# #     @enable_auto_run.setter
# #     def enable_auto_run(self, is_enable):
# #         self._enable_auto_run = is_enable

# #     def run(self):
# #         print('super fast')

# #     def auto_run(self):
# #         print('auto run')


# # tesla_car = TeslaCar('Model S')
# # tesla_car.enable_auto_run = True
# # print(tesla_car.enable_auto_run)


# class Car(object):
#     def __init__(self, model=None):
#         self.model = model

#     def run(self):
#         print('run')


# class ToyotaCar(Car):
#     def run(self):
#         print('fast')


# class TeslaCar(Car):
#     def __init__(self, model='Model S',
#                  enable_auto_run=False,
#                  passwd='123'):
#         super().__init__(model)
#         # self._enable_auto_run = enable_auto_run
#         self.passwd = passwd
#         self.__enable_auto_run = enable_auto_run

#     # @propertyをつけることで、
#     # プロパティとして使える
#     @property
#     def enable_auto_run(self):
#         # プライベート変数を返すことで、
#         # 読み込みはできるが、書き込みはできないようになる
#         return self._enable_auto_run

#     # 書き換えるためには、
#     # @プロパティ名.setterを使う
#     @enable_auto_run.setter
#     def enable_auto_run(self, is_enable):
#         # パスワードを使って認証を行う
#         if self.passwd == '456':
#             self._enable_auto_run = is_enable
#         else:
#             raise ValueError

#     def run(self):
#         # print(self.__enable_auto_run)
#         print('super fast')

#     def auto_run(self):
#         print('auto run')

# # ゲッターとセッターを使うことで、
# # プロパティの読み書きを制限することができる。
# tesla_car = TeslaCar('Model S', passwd='456')
# # tesla_car.enable_auto_run = True
# # print(tesla_car.enable_auto_run)
# # print(tesla_car.__enable_auto_run)
# # tesla_car.run()
# # アンダースコアが1個の場合は、
# # 外部からアクセスできないようになる。
# # アンダースコアが2個の場合は、
# # クラス内からはアクセスできるが、一度オブジェクトを生成してからアクセスしようと思ってもできない。


# # # クラスを構造体として扱うときの注意点
# class Car(object):
#     def __init__(self, model=None):
#         self.model = model

#     def run(self):
#         print('run')


# class ToyotaCar(Car):
#     def run(self):
#         print('fast')


# class TeslaCar(Car):
#     def __init__(self, model='Model S', enable_auto_run=False):
#         super().__init__(model)
#         self.__enable_auto_run = enable_auto_run

#     @property
#     def enable_auto_run(self):
#         return self._enable_auto_run

#     @enable_auto_run.setter
#     def enable_auto_run(self, is_enable):
#         self._enable_auto_run = is_enable

#     def run(self):
#         print('super fast')

#     def auto_run(self):
#         print('auto run')


# tesla_car = TeslaCar('Model S')
# tesla_car.__enable_auto_run = 'XXXXXXXXXX'
# # クラス内で定義されている__enable_auto_runはここでは呼び出されいない。
# # 新しく定義された形となっている
# print(tesla_car.__enable_auto_run)


# class T(object):
#     pass


# t = T()
# t.name = 'Mike'
# t.age = 20
# print(t.name, t.age)


# # # ダックタイピング
# class Person(object):
#     def __init__(self, age=1):
#         self.age = age

#     def drive(self):
#         if self.age >= 18:
#             print('ok')
#         else:
#             raise Exception('No drive')


# class Baby(Person):
#     def __init__(self, age=1):
#         if age < 18:
#             super().__init__(age)
#         else:
#             raise ValueError


# class Adult(Person):
#     def __init__(self, age=18):
#         if age >= 18:
#             super().__init__(age)
#         else:
#             raise ValueError


# baby = Baby()
# adult = Adult()


# class Car(object):
#     def __init__(self, model=None):
#         self.model = model

#     def run(self):
#         print('run')

#     def ride(self, person):
#         person.drive()


# car = Car()
# car.ride(adult)
# # car.ride(adult) → adult は Adult クラスのインスタンスとして生成され、age=18 がスーパークラスに渡される。
# # person.drive() が呼び出され、if 文で age の判定が行われる。


# # # 抽象クラス
# import abc


# class Person(metaclass=abc.ABCMeta):
#     def __init__(self, age=1):
#         self.age = age

#     @abc.abstractmethod
#     def drive(self):
#         pass


# class Baby(Person):
#     def __init__(self, age=1):
#         if age < 18:
#             super().__init__(age)
#         else:
#             raise ValueError

#     def drive(self):
#         raise Exception('No drive')


# class Adult(Person):
#     def __init__(self, age=18):
#         if age >= 18:
#             super().__init__(age)
#         else:
#             raise ValueError

#     def drive(self):
#         print('ok')


# baby = Baby()
# adult = Adult()


# class Car(object):
#     def __init__(self, model=None):
#         self.model = model

#     def run(self):
#         print('run')

#     def ride(self, person):
#         person.drive()


# car = Car()
# car.ride(adult)

# 抽象クラスを使うことで、「Person のサブクラスは drive() を必ず実装する」というルールを強制できます。
# |  | 抽象クラスなし（元のコード） | 抽象クラスあり（修正後） |
# |---|---|---|
# | `drive()` の扱い | `Person` に実装されており、すべてのサブクラスが継承 | 各サブクラスで明示的に実装する必要がある |
# | `Baby` クラスの問題 | `drive()` を持たないが、`Person` を継承しているため呼び出し可能 | `Baby` でも `drive()` を実装しなければならない |
# | バグの可能性 | `Baby` が `drive()` を持つことで誤動作の可能性あり | `drive()` の実装を強制するため、予期しない動作を防げる |
# | `Person` のインスタンス化 | 可能（`p = Person()` が動く） | 不可能（`Person` は抽象クラスのため直接インスタンス化できない） |


# # # 多重継承
# class Person(object):
#     def talk(self):
#         print('talk')

#     def run(self):
#         print('person run')


# class Car(object):
#     def run(self):
#         print('run')

# # PersonCarRobotはPersonとCarを継承
# # 引数にPersonとCarを取っているが、先に左側のクラスのメソッドが呼ばれる
# # 実行されたら右側の引数が呼ばれることはなく、実行されない


# class PersonCarRobot(Person, Car):
#     def fly(self):
#         print('fly')


# person_car_robot = PersonCarRobot()
# person_car_robot.talk()  # Personのtalk()が呼ばれる
# person_car_robot.run()  # メソッド解決順序（MRO）により、Personのrun()が呼ばれる（Carのrun()は無視される）
# person_car_robot.fly()  # PersonCarRobotのfly()が呼ばれる


# # クラス変数とインスタンス変数の違い
# # クラス変数の例
# class Person(object):
#     # クラス全体で共有されるクラス変数
#     kind = 'human'

#     def __init__(self, name):
#         self.name = name  # インスタンスごとに異なる値を持つインスタンス変数

#     def who_are_you(self):
#         print(self.name, self.kind)


# # インスタンスを作成し、クラス変数が共有されることを確認
# a = Person('A')
# a.who_are_you()  # 出力: A human

# b = Person('B')
# b.who_are_you()  # 出力: B human


# # クラス変数の影響による問題
# class T(object):
#     words = []  # クラス変数（すべてのインスタンスで共有される）

#     def add_word(self, word):
#         self.words.append(word)  # クラス変数に追加


# # インスタンスを作成し、それぞれのインスタンスで値を追加
# c = T()
# c.add_word('add 1')
# c.add_word('add 2')

# d = T()
# d.add_word('add 3')
# d.add_word('add 4')

# # 出力: ['add 1', 'add 2', 'add 3', 'add 4']
# # c と d は別のインスタンスだが、クラス変数を共有してしまっている
# print(c.words)


# # クラス変数の共有を避ける解決策
# class T(object):
#     def __init__(self):
#         self.words = []  # インスタンスごとに異なるリストを作成

#     def add_word(self, word):
#         self.words.append(word)


# # インスタンスごとに独立したリストを持つ
# c = T()
# c.add_word('add 1')
# c.add_word('add 2')
# print(c.words)  # 出力: ['add 1', 'add 2']

# d = T()
# d.add_word('add 3')
# d.add_word('add 4')
# print(d.words)  # 出力: ['add 3', 'add 4']


# # # クラスメソッドとスタティックメソッド
# class Person(object):
#     kind = 'human'  # クラス変数（全インスタンスで共有）

#     def __init__(self):
#         self.x = 100  # インスタンス変数（各インスタンスごとに異なる値を持つ）

#     # クラスメソッド: クラス変数を扱うためのメソッド
#     @classmethod
#     def what_is_your_kind(cls):
#         return cls.kind  # cls を使ってクラス変数を参照


# # インスタンスとクラスからクラスメソッドを呼び出す
# a = Person()
# print(a.what_is_your_kind())  # 出力: human

# b = Person  # クラスをそのまま参照
# print(b.what_is_your_kind())  # 出力: human

# # クラス変数の直接参照
# print(Person.kind)  # 出力: human


# # スタティックメソッドの例
# def about(year):
#     print('about human {}'.format(year))  # 年を指定して出力


# class Person(object):
#     kind = 'human'

#     def __init__(self):
#         self.x = 100

#     @classmethod
#     def what_is_your_kind(cls):
#         return cls.kind

#     # スタティックメソッド: インスタンスやクラスに依存しない独立したメソッド
#     @staticmethod
#     def about(year):
#         print('about human {}'.format(year))


# # クラスメソッドの確認
# a = Person()
# print(a.what_is_your_kind())  # 出力: human

# b = Person
# print(b.what_is_your_kind())  # 出力: human

# # スタティックメソッドの呼び出し
# Person.about(1999)  # 出力: about human 1999


# # 特殊メソッド（マジックメソッド）

# class Word(object):
#     def __init__(self, text):
#         self.text = text  # インスタンス変数として文字列を保持

#     # __str__: インスタンスをprint()で表示するときの文字列を定義
#     def __str__(self):
#         return 'Word!!!!'  # 通常の文字列ではなく、固定の文字列を返す

#     # __len__: len() を使用したときの動作を定義
#     def __len__(self):
#         return len(self.text)  # インスタンス変数の文字列の長さを返す

#     # __add__: + 演算子を定義（2つのWordオブジェクトを結合）
#     def __add__(self, word):
#         return self.text.lower() + word.text.lower()  # 小文字に変換して連結

#     # __eq__: == 演算子を定義（2つのWordオブジェクトが等しいか判定）
#     def __eq__(self, word):
#         return self.text.lower() == word.text.lower()  # 小文字に変換して比較


# # インスタンスの作成
# w = Word('test')
# w2 = Word('test')

# # __str__ の動作確認（print() で出力）
# print(w)  # 出力: Word!!!!

# # __len__ の動作確認
# print(len(w))  # 出力: 4（文字列 'test' の長さ）

# # __add__ の動作確認（+ 演算子による結合）
# print(w + w2)  # 出力: testtest（小文字に変換されて連結）

# # __eq__ の動作確認（== 演算子による比較）
# print(w == w2)  # 出力: True（小文字 'test' 同士なので等しい）
