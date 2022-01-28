# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 08:18:07 2020

@author: 
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
               '*.jpg'　や　'*.txt'　とすると、対象の拡張子ファイル全てが対象となります。
               '*'　(アスタリスク)　とすると、すべての拡張子ファイルが対象となります。

'''


#グローバル変数宣言
BeforeFolder = r'D:\\'
AfterFolder  = r'H:\'
OutputFolder = AfterFolder
File         = '*'


###  以下、修正不要  ###





import pandas as pd
import numpy as np
import glob
import datetime
import hashlib
import os
from tqdm import tqdm
from time import sleep



''' 処理開始 '''

#処理開始時刻
print()
print('処理開始時刻 : ' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
print()
print()
StartTime = datetime.datetime.now().strftime('%Y%m%dT%H%M%S')
sleep(0.5)


#空のデータフレームを用意
Bef_df = pd.DataFrame(index=[], columns=['BeforePath', 'Hash'])
Aft_df = pd.DataFrame(index=[], columns=['AfterPath', 'Hash'])

#空のリストを用意
Bef_lst = []
Aft_lst = []


#ファイル一覧を取得
# - 前フォルダ
BefPath_lst = glob.glob(BeforeFolder + '\\**\\'+ File, recursive=True)
# BefFile_lst = [p for p in tqdm(BefPath_lst, desc='BeforePath') if os.path.isfile(p)]
# - 後フォルダ
AftPath_lst = glob.glob(AfterFolder + '\\**\\'+ File, recursive=True)
# AftFile_lst = [p for p in tqdm(AftPath_lst, desc='AfterPath') if os.path.isfile(p)]

#ハッシュ値の計算
# - 前フォルダ
for ItemPath in tqdm(BefPath_lst, desc='BeforeHash'):
    if os.path.isfile(ItemPath):
        with open(ItemPath, 'rb') as f:
            checksum = hashlib.sha256(f.read()).hexdigest().upper()
        Bef_lst.append([ItemPath, checksum])
# - 後フォルダ
for ItemPath in tqdm(AftPath_lst, desc='AfterHash'):
    if os.path.isfile(ItemPath):
        with open(ItemPath, 'rb') as f:
            checksum = hashlib.sha256(f.read()).hexdigest().upper()
        Aft_lst.append([ItemPath, checksum])

#リストをDF化
feat_cols = list(Bef_df.columns)
Bef_df = pd.DataFrame(np.asarray(Bef_lst), columns=feat_cols)
feat_cols = list(Aft_df.columns)
Aft_df = pd.DataFrame(np.asarray(Aft_lst), columns=feat_cols)

#ハッシュ値で結合
Output_df = pd.merge(Bef_df, Aft_df, on='Hash', how='outer', indicator=True)

#結果を出力(CSVで出力)
filename = OutputFolder + '\\' + StartTime + '_HashCheck.csv'
Output_df.to_csv(filename, header=True, index=False, encoding='utf_8_sig')


#処理終了時刻
print()
print()
print('ハッシュ一覧出力：' + filename)
print()
print('処理終了時刻 : ' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
