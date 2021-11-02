# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 08:18:07 2020

@author: XXXXXX
"""
'''
【説明書】
<フォルダー構成について>
本PGMは特にフォルダ構成を指定しません。

<本PGMで必要な設定について>
以下、本PGMでの設定です。

BeforeFolder : 移動前のファイルがある最上位フォルダを　r'フォルダパス'　で記載ください。
               配下のフォルダをすべて検索します。

AfterFolder  : 移動後のファイルがある最上位フォルダを　r'フォルダパス'　で記載ください。
               配下のフォルダをすべて検索します。

OutputFolder : ハッシュ比較の結果ファイルの出力先を　r'フォルダパス'　で記載ください。

File         : 検索対象のファイルを　'TEST.jpg'　や　'TEST.txt'　など記載ください。
               '*.jpg'　や　'*.txt'　とすると、対象の拡張子ファイルが対象となります。
               ''　(ブランク)　とすると、すべての拡張子ファイルが対象となります。

'''


#グローバル変数宣言
BeforeFolder = r'D:\\'
AfterFolder  = r'H:\XXXXX'
OutputFolder = AfterFolder
File         = '*'


###  以下、修正不要  ###





import pandas as pd
import glob
import datetime
import hashlib
import os
from tqdm import tqdm



''' 処理開始 '''

#処理開始時刻
print('処理開始時刻')
print(datetime.datetime.now())
StartTime = datetime.datetime.now().strftime('%Y_%m_%dT%H_%M')



#空のデータフレームを用意
Before_df = pd.DataFrame(index=[], columns=['BeforePath', 'Hash'])
After_df = pd.DataFrame(index=[], columns=['AfterPath', 'Hash'])

#ファイル一覧を取得
# - 前フォルダ
BeforePath_list = glob.glob(BeforeFolder + '\\**\\'+ File, recursive=True)
BeforeFile_list = [p for p in tqdm(BeforePath_list, desc='BeforePath') if os.path.isfile(p)]
# - 後フォルダ
AfterPath_list = glob.glob(AfterFolder + '\\**\\'+ File, recursive=True)
AfterFile_list = [p for p in tqdm(AfterPath_list, desc='AfterPath') if os.path.isfile(p)]

#ハッシュ値の計算
# - 前フォルダ
for ItemPath in tqdm(BeforeFile_list, desc='BeforeHash'):
    with open(ItemPath, 'rb') as f:
        checksum = hashlib.sha256(f.read()).hexdigest()
        tmp_se = pd.Series([ItemPath, checksum], index=Before_df.columns)
        Before_df = Before_df.append(tmp_se, ignore_index=True)
# - 後フォルダ
for ItemPath in tqdm(AfterFile_list, desc='AfterHash'):
    with open(ItemPath, 'rb') as f:
        checksum = hashlib.sha256(f.read()).hexdigest()
        tmp_se = pd.Series([ItemPath, checksum], index=After_df.columns)
        After_df = After_df.append(tmp_se, ignore_index=True)

#ハッシュ値で結合
Output_df = pd.merge(Before_df, After_df, on='Hash', how='outer', indicator=True)

#結果を出力(CSVで出力)
filename = OutputFolder + '\\' + StartTime + '_HashCheck.csv'
Output_df.to_csv(filename, header=True, index=False, encoding='utf_8_sig')


#処理終了時刻
print("ハッシュ一覧出力：" + filename)
print('処理終了時刻')
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M.%S'))
