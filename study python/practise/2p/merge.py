# coding: utf-8

# 別のスクリプトによって作られたモジュール群（JavaScriptファイル）を合体する。
# 最後に、フレームワーク部分を合体して、コンテンツ等がロードして使えるJavaScriptファイルを完成させる。
# 
# 引数
# 第1引数：モジュール群のあるフォルダa
# 第2引数：フレームワークのファイル
# 第3引数：成果物のファイル名

# ファイルの例は次の通り
# ・モジュール： Copy_ColorMode.js
# ・フレームワーク: SystemDataCorrector.js
# ・成果物のファイル: conflictlib.js

import sys

if len(sys.argv) != 4:
	print("Error: Input folder path.")
	sys.exit()

path_modules_folder = sys.argv[1]
path_framework = sys.argv[2]
path_result    = sys.argv[3]

# 指定されたフォルダの配下にあるJavaScriptのファイルを全部集める
import glob
path_modules = glob.glob(path_modules_folder + '/**/*.js', recursive = True)

text_modules = ""

# モジュールを集めるための配列の宣言文を追加する
text_modules += "var systemDataCorrectModules = [];\n\n"

# モジュールを集める
from pathlib import Path
for path in path_modules:
	
	# ファイル名はクラス名と同じであるはずなので、これを利用してクラス名を決定
	pathobj = Path(path)
	class_name = pathobj.stem
	
	try:
		with open(path, 'r', encoding='utf-8') as f:
			# モジュールファイルの中身をコピーする
			text_modules += f.read()
			text_modules += "\n"
			# クラスをnewして配列に追加するコードを生成する
			text_modules += "systemDataCorrectModules.push(new %s());" % class_name
			text_modules += "\n\n"
	except:
		print("Invalid file: " + path)
		sys.exit()


# フレームワークのファイルを読み込んで合体する
try:
	with open(path_framework, 'r', encoding='utf-8') as f:
		# フレームワークファイルの中身をコピーする
		text_modules += f.read()
		text_modules += "\n"
except:
	print("Invalid file: " + path)
	sys.exit()


# print(text_modules)


# 完成した内容をファイルに書き込む
try:
	with open(path_result, 'w', encoding='utf-8') as f:
		f.write(text_modules)
except:
	print("Invalid file: " + path)
	sys.exit()


