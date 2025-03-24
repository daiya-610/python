# # # ファイルの作成と書き込み

# # open(): ファイルを開く
# # 'w' モード: 書き込み専用モード（既存のファイルがあれば上書き）
# f = open('test.txt', 'w')

# # write(): ファイルに文字列を書き込む
# f.write('Test\n')  # "Test" を書き込み、改行を追加

# # print() を使ってファイルに書き込む
# # - sep='#': 各単語の間を '#' で区切る
# # - end='!': 文末を '!' にする（デフォルトの改行を変更）
# # - file=f: 出力先を標準出力ではなくファイルに指定
# print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)

# # ファイルを閉じる（重要）
# f.close()


# # with ステートメントでファイルを開く

# # with を使うことで、ファイルを自動的に閉じることができる
# # 'w' モード: 書き込み専用（既存のファイルがあれば上書き）
# with open('test.txt', 'w') as f:
#     # ファイルに文字列を書き込む
#     f.write('Test\n')  # "Test" を書き込み、改行を追加

# # with ステートメントを使うと、ブロックを抜けた時点で
# # 自動的にファイルが閉じられるため、明示的に close() を呼ぶ必要がない


# # ファイルの読み込み
# # 読み込むためのサンプルデータ
# s = """\
# AAA
# BBB
# CCC
# DDD
# """

# # ※ 事前に test.txt にデータを書き込む場合は以下を実行（コメントアウトを外す）
# # with open('test.txt', 'w') as f:
# #     f.write(s)  # 文字列 s をファイルに書き込む

# # 'r' モードでファイルを開く（読み込み専用）
# with open('test.txt', 'r') as f:
#     # read() でファイルの内容を一気に読み込む
#     # print(f.read())  # ※ 一括で読み込む場合（コメントアウト解除で確認可）

#     # 2文字ずつ読み込む処理
#     while True:
#         chunk = 2  # 2文字ずつ読み込む
#         line = f.read(chunk)  # 指定したサイズ分だけデータを読み込む
#         print(line)  # 読み込んだ内容を出力
#         if not line:  # データがなくなったら終了
#             break


# # # seek() を使ってファイルの読み取り位置を移動する
# # 読み込むためのサンプルデータ
# s = """\
# AAA
# BBB
# CCC
# DDD
# """

# # 'r' モードでファイルを開く（読み込み専用）
# with open('test.txt', 'r') as f:
#     # tell(): 現在のファイルポインタ（読み取り位置）を取得
#     print(f.tell())  # 最初の位置（0）

#     # 1文字読み込む（最初の 'A'）
#     print(f.read(1))  # 出力: A

#     # seek(5): ファイル内の5バイト目に移動（インデックスは0から始まる）
#     f.seek(5)
#     print(f.read(1))  # 出力: B（"BBB" の2文字目の 'B'）←A,A,A, ,(改行コード入って) B,B,B,

#     # seek(14): 14バイト目に移動
#     f.seek(14)
#     print(f.read(1))  # 出力: D（"DDD" の最後の 'D'）

#     # seek(15): 15バイト目に移動
#     f.seek(15)
#     print(f.read(1))  # 出力: 改行コード ←D,D,D , A,A,A,

#     # 再び seek(5) に移動
#     f.seek(5)
#     print(f.read(1))  # 出力: B（再び "BBB" の2文字目の 'B' を読み込む）


# # ファイルの書き込み・読み込みモード（'r+'）

# # 書き込むサンプルデータ
# s = """\
# AAA
# BBB
# CCC
# DDD
# """

# # 'r+' モード: 読み込み & 書き込み（既存のファイルが必要）
# # - ファイルが存在しない場合はエラーになる
# # - 読み込んだ後に書き込みが可能（上書きされる）
# with open('test.txt', 'r+') as f:
#     # ファイルの内容を全て読み込む（最初に現在の内容を確認）
#     print("=== Before Writing ===")
#     print(f.read())  # 現在のファイル内容を出力

#     # ファイルの先頭に移動（seek(0)）
#     f.seek(0)

#     # ファイルに新しいデータを書き込む（上書き）
#     f.write(s)

#     # 再度先頭に戻って書き込み後の内容を確認
#     f.seek(0)
#     print("=== After Writing ===")
#     print(f.read())  # 上書き後のファイル内容を出力


# # テンプレート
# テンプレートを使用して文字列を動的に置換する

# import string  # string モジュールをインポート

# # 'email_template.txt' を読み込む（テンプレートファイル）
# # - with ステートメントを使用してファイルを開く（自動的に close される）
# with open('python/udemy01/sec08_file_operation/design/email_template.txt') as f:
#     # string.Template を使用してテンプレートを作成
#     t = string.Template(f.read())

# # テンプレートの変数を置換
# # - ${name} -> 'Mike'
# # - ${contents} -> 'How are you?'
# contents = t.substitute(name='Mike', contents='How are you?')

# # 置換後の結果を出力
# print(contents)


# # # CSVファイルへの書き込みと読み込み
# import csv  # csv モジュールをインポート

# with open('test.csv', 'w') as csv_file:
#     fiealdnames = ['col1', 'col2', 'col3']  # ヘッダ行のデータ
#     writer = csv.DictWriter(csv_file, fieldnames=fiealdnames)
#     writer.writeheader()  # ヘッダ行を書き込む
#     writer.writerow({'col1': 'A', 'col2': 1, 'col3': 2})  #

# with open('test.csv', 'r') as csv_file:
#     # csv.reader() でファイルオブジェクトを作成
#     reader = csv.reader(csv_file)

#     # データ行を1行ずつ読み込む
#     for row in reader:
#         print(row)


# # ファイル操作
# import os  # os モジュールをインポート
# import pathlib
# import glob
# import shutil

# # os.path.exists('test.txt')  # ファイルが存在するか確認
# # print(os.path.isdir('design'))  # ファイルが存在するか確認
# # print(os.chdir(os.path.dirname(os.path.abspath(__file__))))  # ファイルが存在するか確認
# # print("Current directory:", os.getcwd())
# # os.rename('test.txt', 'renamed.txt')  # ファイル名を変更
# # os.symlink('renamed.txt', 'symlink.txt')  # シンボリックリンクを作成
# # /Users/dd/work/python/udemy01/sec08_file_operation/design

# # os.mkdir('test_dir')  # ディレクトリを作成
# # os.rmdir('test_dir')  # ディレクトリを削除

# # pathlib.Path('empty.txt').touch()  # 空のファイルを作成
# # os.remove('empty.txt')  # ファイルを削除

# # os.mkdir('test_dir')  # ディレクトリを作成
# # os.mkdir('test_dir/test_dir2')  # ディレクトリを作成
# # print(os.listdir('test_dir'))  # ディレクトリ内のファイル一覧を取得
# # pathlib.Path('test_dir/test_dir2/empty.txt').touch()  # 空のファイルを作成
# # shutil.copy('test_dir/test_dir2/empty.txt',
# #             'test_dir/test_dir2/empty2.txt')
# # print(glob.glob('test_dir/test_dir2/*'))  # ディレクトリ内のファイル一覧を取得

# # ディレクトリ削除
# # shutil.rmtree('test_dir')  # ディレクトリを削除

# print(os.getcwd())


# tarfileの圧縮展開
import os
import tarfile

# os.mkdir('test_dir')
# with文とopen関数を使ったファイル作成
# with open('test_dir/test.txt', 'w') as f:
#     f.write('test')


# os.mkdir('test_dir/sub_dir')
# with open('test_dir/sub_dir/sub_test.txt', 'w') as f:
#     f.write('sub')

# with tarfile.open('test.tar.gz', 'w:gz') as tr:
#     tr.add('test_dir')

# 上記で圧縮したファイルをターミナルで展開するコマンド
# tar zxvf test.tar.gz -C /tmp

# 上記で圧縮したファイルをコードでファイルの展開
# with tarfile.open('test.tar.gz', 'r:gz') as tr:
#     # tr.extractall(path='test_tar')
#     with tr.extractfile('test_dir/sub_dir/sub_test.txt') as f:
#         print(f.read())


# # zipfileの圧縮展開
# import glob
# import zipfile

# with zipfile.ZipFile('test.zip', 'w') as z:
#     # z.write('test_dir')
#     # z.write('test_dir/text.txt')
#     for f in glob.glob('text_dir/**', recursive=True):
#         # print(f)
#         z.write(f)

# with zipfile.ZipFile('test.zip', 'r') as z:
#     # z.extractall('zzz2')
#     with z.open('tst_dir/test.txt') as f:
#         print(f.read())


# # tempfile
# import tempfile

# # with tempfile.TemporaryFile(mode='w') as t:
# #     t.write('hello')
# #     t.seek(0)
# #     print(t.read())

# # with tempfile.NamedTemporaryFile(delete=False) as t:
# #     with open(t.name, 'w+') as f:
# #         f.write('test\n')
# #         f.seek(0)
# #         print(f.read())

# # with tempfile.TemporaryDirectory() as td:
# #     print(td)

# temp_dir = tempfile.mkdtemp()
# print(temp_dir)


# # subprocessでコマンドを実行する
# import subprocess

# subprocess.run(['ls', '-al'])


# datetime
# import datetime

# now = datetime.datetime.now()
# print(now)
# print(now.isoformat())
# print(now.strftime('%d/%m/%y-%H%M%S%f'))

# today = datetime.date.today()
# print(today)
# print(today.isoformat())
# print(now.strftime('%d/%m/%y'))

# t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
# print(t)
# print(t.isoformat())
# print(now.strftime('%H_%M_%S_%f'))

# print(now)
# d = datetime.timedelta(weeks=1)
# d = datetime.timedelta(days=1)
# print(now - d)

# import time
# print('###')
# time.sleep(1)
# print('###')

# 使用用途 - バックアップファイル名の作成
# import datetime
# import os
# import shutil

# now = datetime.datetime.now()

# file_name = 'test.txt'

# if os.path.exists(file_name):
#     shutil.copy(file_name, "{}.{}".format(
#         file_name, now.strftime('%Y_%m_%d_%H_%M_%S')
#     ))

# with open(file_name, 'w') as f:
#     f.write('test')
