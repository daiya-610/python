# セクション5: 制御フローとコード構造

# ## コメント
# print('XXXXXXXXXXX')
# """
# test
# test
# test
# test
# """
# print('XXXXXXXXXXX')

# # Apple_price
# some_value = 100


# ## 1行が長くなる時 - 80文字以上の場合は次の行に書いた方がいい
# s = 'aaaaaaaaaaaaaaa' \
# + 'bbbbbbbbbbb'
# s2 = ('aaaaaaaaaaaaaaa'
# + 'bbbbbbbbbbb')
# print(s)
# print(s2)

# x = 1 + 1 + 1 + 1 + 1 + 1 + 1 \
#     + 1 + 1 + 1 + 1 + 1 + 1 + 1
# x2 = (1 + 1 + 1 + 1 + 1 + 1 + 1
#     + 1 + 1 + 1 + 1 + 1 + 1 + 1)
# print(x)
# print(x2)


# ## if文
# x = 0

# if x < 0:
#     print('negative')
# elif x == 0:
#     print('zero')
# else:
#     print('positive')

# a = 5
# b = 10

# if a > 0:
#     print('positive')
#     if b > 0:
#         print('b is positive')


# ## 比較演算子と論理演算子
# a = 1
# b = 1

# # a が b と等しい
# print(a == b)

# # a が b と異なる
# print(a != b)

# # a が b よりも小さい
# print(a < b)

# # a が b よりも大きい
# print(a > b)

# # a が b 以下である
# print(a <= b)

# # a が b 以上である
# print(a >= b)

# # a も b も真であれば真
# print(a > 0 and b > 0)

# # a または b が真であれば真
# print(a > 0 or b > 0)


# InとNotの使い所
# y = [1,2,3]
# x = 1

# if x in y:
#     print('in')

# if 100 not in y:
#     print('not in')

# a = 1
# b = 2

# # not は使用できるけど、好ましくない
# if not a == b:
#     print('Not equal')

# if  a != b:
#     print('Not equal')

# is_ok = True
# if is_ok :
#     print('hello')


# 値が入っていない判定をするテクニック
# is_ok = True
# False, 0, 0.0, '', [], (), {}, set()
# is_ok = 'aadd'

# if is_ok == True:
#     print('OK!')
# else:
#     print('No!')

# """
# is_ok = [1,2,3,4]
# # lengthの判定する必要がない
# if len(is_ok) > 0:
#     print('OK!')
# else:
#     print('No!')
# """


# ## Noneを判定する場合 - 変数に入れた値がNoneだった場合は「is」を使用する
# is_empty = None
# # print(help(is_empty))

# # if is_empty == None:
# #     print('None!!!')

# if is_empty is not None:
#     print('None!!!')

# print(1 == True)
# # オブジェクト同士が同じものにならないとTrueにならない
# print(1 is True)
# print(True is True)


# ## while文とcontinue文とbreak文
# # count = 0

# # while count < 5:
# #     print(count)
# #     count += 1

# count = 0
# while True:
#     if count >= 5:
#         break

#     if count == 2:
#         count += 1
#         continue

#     print(count)
#     count += 1
#     """
#     出力結果:0 1 3 4
#     """


# ## while else文
# count = 0
# while count < 5:
#     print(count)
#     count += 1
# else:
#     print('done')


# ## input関数
# while True:
#     word = input('Enter:')
#     if word == 'ok':
#         break
#     print('next')

# while True:
#     word = input('Enter:')
#     num = int(word)
#     if num == 100:
#         break
#     print('next')

# ## for文とbreak文とcontinue文
# some_list = [1, 2, 3, 4, 5]

# i = 0
# while i < len(some_list):
#     print(some_list[i])
#     i += 1

# 反復処理 イテレータ
# for i in some_list:
#     print(i)

# for s in 'abcde':
#     print(s)

# for word in ['My', 'name', 'is', 'Mike']:
#     if word == 'name':
#         continue
#     print(word)

# ## for else文
# for fruit in ['apple', 'banana', 'orange']:
#     if fruit == 'banana':
#         print('stop eating')
#         break
#     print(fruit)
# else:
#     print('I ate all!')


# ##range関数
# num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in num_list:
#     print(i)

# for i in range(2, 10, 3):
#     print(i)

# rangeで入ってくる数字を使用しない場合は「_」を使用する
# for _ in range(10):
#     print('hello')


# enumerate関数
# i = 0
# for fruit in ['apple', 'banana', 'orange']:
#     print(i, fruit)
#     i += 1

# enumerate関数を使用すると上記のコードを簡潔に書くことができる
# for i, fruit in enumerate(['apple', 'banana', 'orange']):
#     print(i, fruit)


# ## zip関数
# days = ['Mon', 'Tue', 'Wed']
# fruits = ['apple', 'banana', 'orange']
# drinks = ['coffee', 'tea', 'beer']

# # for i in range(len(days)):
# # print(days[i], fruits[i], drinks[i])

# # zip関数を使用すると上記のコードを簡潔に書くことができる
# for day, fruit, drink in zip(days, fruits, drinks):
#     print(day, fruit, drink)


# ## 辞書をfor文で処理する
# d = {'x': 100, 'y': 200}

# # 辞書にはメソッドでitems()を使用できる。items()を使用するとキーと値を取得できる。
# print(d.items())

# for k, v in d.items():
#     print(k, ':', v)


# ## 関数を定義する
# def say_something():
#     s = 'hi'
#     return s


# result = say_something()
# print(result)


# def what_is_this(color):
#     if color == 'red':
#         return 'tomato'
#     elif color == 'green':
#         return 'green pepper'
#     else:
#         return "I don't know"


# result = what_is_this('green')
# print(result)

# ## 関数の引数と返り値の宣言
# num: int = 10

# # (-> int)を指定することで、返り値の型を指定できる


# def add_num(a: int, b: int) -> int:
#     return a + b

# r = add_num(10, 20)
# print(r)


# ## 位置引数とキーワード引数とデフォルト引数
# def menu(entree, drink, dessert):
#     print(entree)
#     print(drink)
#     print(dessert)


# # menu('beef', 'beer', 'ice')
# menu(entree='beef', dessert='beer', drink='ice')

# # 引数のデフォルト値を設定する
# def menu(entree='beef', drink='wine', dessert='ice'):
#     print(entree)
#     print(drink)
#     print(dessert)


# menu('chicken', drink='beer')

# ## デフォルト引数の注意点
# def test_func(x, l=[]):
#     # l = []が読み込まれ、lにyのリストが入る。x:100, l=[]
#     l.append(x)
#     return l


# y = [1, 2, 3]
# r = test_func(100, y)
# print(r)
# # 出力結果:[1, 2, 3, 100]

# y = [1, 2, 3]
# r = test_func(200, y)
# print(r)
# # 出力結果:[1, 2, 3, 200]

# r = test_func(100)
# print(r)
# # # 出力結果:[100]

# r = test_func(100)
# print(r)
# # # 出力結果:[100, 100]
# """
# ! 注意: Listはデフォルト引数を与えるべきではない。
# """


# # Listにデフォルト引数を与える場合は、以下のようにする
# def test_func(x, l=None):
#     if l is None:
#         l = []
#     l.append(x)
#     return l


# r = test_func(100)
# print(r)
# # # 出力結果:[100]

# r = test_func(100)
# print(r)
# # # 出力結果:[100, 100]


# ## 位置引数のタプル化
# def say_something(word, *args):
#     print('word:', word)
#     for arg in args:
#         print(arg)


# say_something('Hi', 'Mike', 'Nance')

# # こんな方法もある
# t = ('Mike', 'Nance')
# say_something('Hi', *t)
# # 出力結果:word: Hi \ Mike \ Nance


# ## キーワード引数の辞書化
# def menu(entree='beef', drink='wine'):
#     print(entree, drink)


# menu(entree='beef', drink='beer')


# def menu(**kwargs):
#     # print(kwargs)
#     for k, v in kwargs.items():
#         print(k, v)


# d = {
#     'entree': 'beef',
#     'drink': 'ice coffee',
#     'dessert': 'ice'
# }

# menu(**d)
# # 出力結果:entree beef \ drink ice coffee \ dessert ice
# # dが展開されて辞書化される。for文でキーと値を取得できる
# # **dを使用することで、辞書を展開して渡すことができる
# # これをキーワード引数の辞書化という


# def menu(food, *args, **kwargs):
#     print(food)
#     print(args)
#     print(kwargs)


# menu('banana', 'apple', 'orange', entree='beef', drink='coffee')
# # 出力結果:banana \ ('apple', 'orange') \ {'entree': 'beef', 'drink': 'coffee'}
# # foodにbananaが入り、*argsにapple, orangeが入り、**kwargsにentree, drinkが入る
# # *argsはタプル化され、**kwargsは辞書化される
# # このように引数を受け取ることができる


# ## Docstringsとは
# def example_func(param1, param2):
#     """Example function with types documented in the docstring.

#     Args:
#         param1 (int): The first parameter.
#         param2 (str): The second parameter.

#     Returns:
#         bool: The return value. True for success, False otherwise.

#     """
#     print(param1)
#     print(param2)
#     return True


# # ドキュメントを表示する
# # 引数の型や返り値の型を記述する
# print(example_func.__doc__)


# ## 関数内関数
# def outer(a, b):
#     def plus(c, d):
#         return c + d

#     r1 = plus(a, b)
#     r2 = plus(b, a)
#     print(r1 + r2)


# outer(1, 2)


# ## クロージャー
# def outer(a, b):
#     def inner():
#         return a + b

#     return inner


# f = outer(1, 2)
# r = f()
# print(r)
# # 出力結果:3
# # クロージャーとは、関数の中に関数を定義すること
# # 用途：関数内で変数を保持することができる。引数に入れた値をあとから実行できる


# def circle_area_func(pi):
#     def circle_area(radius):
#         return pi * radius * radius

#     return circle_area


# cal1 = circle_area_func(3.14)
# cal2 = circle_area_func(3.141592)

# print(cal1(10))
# print(cal2(10))


# ## デコレーター
# def print_info(func):
#     def wrapper(*args, **kwargs):
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result

#     return wrapper


# @print_info
# def add_num(a, b):
#     return a + b


# r = add_num(10, 20)
# print(r)

# print('start')
# r = add_num(10, 20)
# print('end')

# print(r)
# 出力結果:30
# デコレーターとは、関数を修飾するためのもの
# 他の関数を引数に取る関数を作成することができる


# def print_more(func):
#     def wrapper(*args, **kwargs):
#         print('func:', func.__name__)
#         print('args:', args)
#         print('kwargs:', kwargs)
#         result = func(*args, **kwargs)
#         print('result:', result)
#         return result

#     return wrapper


# @print_more
# @print_info
# def add_num(a, b):
#     return a + b


# r = add_num(10, 20)
# print(r)
# 複数のデコレーターを使用する場合は、上から順番に実行される


# ## ラムダ
# l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']


# def change_words(words, func):
#     for word in words:
#         print(func(word))


# # def sample_func(word):
# #     return word.capitalize()

# # sample_func = lambda word: word.capitalize()

# # change_words(l, sample_func)

# change_words(l, lambda word: word.capitalize())
# change_words(l, lambda word: word.lower())
# # 出力結果:Mon \ Tue \ Wed \ Thu \ Fri \ Sat \ Sun
# # ラムダ式とは、無名関数を作成するためのもの
# # 1行で書くことができる


# ## ジェネレーター
# l = ['Good morning', 'Good afternoon', 'Good night']

# # for i in l:
# #     print(i)

# # print('#############')


# def greeting():
#     yield 'Good morning'
#     yield 'Good afternoon'
#     yield 'Good night'


# # for g in greeting():
#     # print(g)
# # 出力結果:Good morning \ Good afternoon \ Good night
# # ジェネレーターとは、イテレータを作成するためのもの
# # イテレータとは、反復処理を行うためのもの
# # ジェネレーターは、yieldを使用して値を返す

# g = greeting()
# print(next(g))
# print('#############')
# # print(next(g))


# def counter(num=10):
#     for _ in range(num):
#         yield 'run'


# c = counter()
# print(next(c))
# print('#############')
# print(next(c))
# print('#############')
# print(next(c))
# print('#############')
# print(next(g))
# print('#############')
# print(next(c))

# # ジェネレーターは、next()を使用して値を取得する
# # ジェネレーターは、値を取得するたびに次の値を取得する
# # for文を使用せずとも、他の処理を挟むことができる


# ## リスト内包表記
# t = (1, 2, 3, 4, 5)

# r = []
# for i in t:
#     if i % 2 == 0:
#         r.append(i)

# print(r)


# r = [i for i in t if i % 2 == 0]
# print(r)
# 出力結果:[1, 2, 3, 4, 5]
# リスト内包表記とは、リストを簡潔に書くためのもの
# リスト内包表記を使用することで、for文を使用せずにリストを作成することができる
# 短いfor文であれば、リスト内包表記を使用することができる

# t2 = (5, 6, 7, 8, 9, 10)

# r = []
# for i in t:
#     for j in t2:
#         r.append(i * j)

# print(r)

# r = [i * j for i in t for j in t2]
# print(r)
# # 出力結果:[5, 6, 7, 8, 9, 10, 10, 12, 14, 16, 18, 20, 15, 18, 21, 24, 27, 30, 20, 24, 28, 32, 36, 40, 25, 30, 35, 40, 45, 50]


# ## 辞書内包表記
# w = ['mon', 'tue', 'wed']
# f = ['coffee', 'milk', 'water']

# d = {}
# for x, y in zip(w, f):
#     d[x] = y

# print(d)


# d = {x: y for x, y in zip(w, f)}
# print(d)
# # 出力結果:{'mon': 'coffee', 'tue': 'milk', 'wed': 'water'}
# # 辞書内包表記とは、辞書を簡潔に書くためのもの
# # 辞書内包表記を使用することで、for文を使用せずに辞書を作成することができる

# ## 集合内包表記
# s = set()

# for i in range(10):
#     if i % 2 == 0:
#         s.add(i)

# print(s)

# s = {i for i in range(10) if i % 2 == 0}
# print(s)
# # 出力結果:{0, 2, 4, 6, 8}
# # 集合内包表記とは、集合を簡潔に書くためのもの
# # 集合内包表記を使用することで、for文を使用せずに集合を作成することができる
# # 集合は、重複を許さない
# # 集合は、順序を持たない
# # 集合は、{}を使用


# ## ジェネレータ内包表記
# def g():
#     for i in range(10):
#         yield i


# g = g()

# g = (i for i in range(10))
# print(type(g))
# print(next(g))
# # 出力結果:<class 'generator'>
# # 出力結果:0
# # ジェネレータ内包表記とは、ジェネレータを簡潔に書くためのもの
# # ジェネレータ内包表記を使用することで、for文を使用せずにジェネレータを作成することができる
# # ジェネレータ内包表記は、()を使用

# g = tuple(i for i in range(10))
# print(type(g))
# # 出力結果:<class 'tuple'>
# # tuple関数の場合は、かっこの前にtupleを記述する


# ## 名前空間とスコープ
# """
# Test Test ############################################################
# """
# animal = 'cat'


# def f():
#     """
#     Test func doc ############################################################
#     """
#     # print(animal)
#     global animal
#     animal = 'dog'
#     print('after', animal)
#     print('local', locals())
#     print(f.__name__)
#     print(f.__doc__)


# f()
# print('global:', animal)
# print('global:', globals())
# # 名前空間について
# # 名前空間とは、変数が定義されている場所
# # 名前空間には、グローバルスコープとローカルスコープがある
# # グローバルスコープとは、関数の外側のスコープ
# # ローカルスコープとは、関数の中のスコープ
# # 関数内でグローバル変数を使用する場合は、globalを使用する
# # 関数内でローカル変数を使用する場合は、locals()を使用する
# # 関数内で関数名を取得する場合は、__name__を使用する
# # 関数内で関数のドキュメントを取得する場合は、__doc__を使用する


# ## 例外処理
# l = [1, 2, 3]
# i = 5

# try:
#     l[0]
# except IndexError as ex:
#     print("Don't worry: {}".format(ex))
# except NameError as ex:
#     print(ex)
# except Exception as ex:
#     print('other:{}'.format(ex))
# else:
#     print('done')
# finally:
#     print('clean up')

# # 例外処理について
# # try:の中に例外が発生する可能性がある処理を記述する
# # except:の中に例外が発生した場合の処理を記述する
# # else:の中に例外が発生しなかった場合の処理を記述する
# # finally:の中に例外が発生してもしなくても実行する処理を記述する
# # exceptは複数記述することができる
# # except Exception as ex:とすることで、全ての例外をキャッチすることができる
# 参照：https://docs.python.org/3/library/exceptions.html


# ## 独自例外の作成
# class UppercaseError(Exception):
#     pass


# def check():
#     words = ['APPLE', 'orange', 'banana']
#     for word in words:
#         if word.isupper():
#             raise UppercaseError(word)


# try:
#     check()
# except UppercaseError as ex:
#     print('This is my fault. Go next')
