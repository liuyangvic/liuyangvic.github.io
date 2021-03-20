# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 19:58:21 2021

@author: 182304
"""

import xlrd # read excel lib
import openpyxl # modify exist excel lib

#read excel info
read_file = '01_イニシアティブ_本部内業界活動.xlsx'
read_sheet1_name1 = "タスク・運営委員リスト_202011"
max_rows = 60

#write excel info
write_file = 'pm_project_jp_listOK.xlsx'
writeh_sheet1_name = "Page 1"

sample_data = []

"""
auth_account_pair_2 = []
auth_account_pair_3 = []
"""

def open_read_excel():
        try:
                read_excel = xlrd.open_workbook(filename=read_file) # open excel file
                print("This excel includes following sheets:",read_excel.sheet_names()) #print including sheets name
                return read_excel

        except Exception as e:
                print("FAILED open Excel:",e)
                return -1
            
def open_write_excel():
        try:
                print("****************************************")
                write_excel = openpyxl.load_workbook(filename=write_file) # open excel file
                write_excel.active = 0 # sheet index #1st from 0
                write_sheet = write_excel.active
                print("This excel includes following sheets:",write_excel.active.title) #print including sheets name
                
                """
                for cell in list(write_sheet.columns)[1]:
                    print(cell.value)
                """    
                
                """
                for cell in list(write_sheet.rows)[0]:
                    if cell.value == "承認希望期限" :
                        cell.value =  "承認希望期限_modified"
                    print(cell.value)
                """
                """
                for i in range(begin_row,write_sheet.nrows):
                        for j in range(begin_column,write_sheet.ncols):
                                if sheet1.cell(i,j).value != "":
                                    sample_data.append([sheet1.cell(0,j).value,sheet1.cell(i,j).value])
                                    print([sheet1.cell(0,j).value,sheet1.cell(i,j).value])                
                """
                begin_column = 1
                begin_row = 2
                
                
                cnt = 1
                for j in range(begin_column,158):
                    if  (write_sheet.cell(1,j).value == "終了実績日時") | (write_sheet.cell(1,j).value == "終了予定日時") :
                        for i in sample_data:                            
                            if i[0]== "終了日" :
                                #print(i[0],",",i[1])
                                write_sheet.cell(cnt+1,j).value = i[1]
                                cnt=cnt+1
                print("終了実績日時 write completed!")
                
                cnt = 1
                for j in range(begin_column,158):
                    if  (write_sheet.cell(1,j).value == "開始実績日時") | (write_sheet.cell(1,j).value == "開始予定") :
                        for i in sample_data:                            
                            if i[0]== "開始日" :
                                print(i[0],",",i[1])
                                write_sheet.cell(cnt+1,j).value = i[1]
                                cnt=cnt+1
                print("開始実績日時 write completed!")
                
                cnt = 1
                for j in range(begin_column,158):
                    if  write_sheet.cell(1,j).value == "プロジェクトメンバ" :
                        for i in sample_data:                            
                            if i[0]== "担当者" :
                                #print(i[0],",",i[1])
                                write_sheet.cell(cnt+1,j).value = i[1]
                                cnt=cnt+1
                cnt = 1
                for j in range(begin_column,158):
                    if  write_sheet.cell(1,j).value == "管理レベル" :
                        for i in sample_data: 
                            if cnt < max_rows :
                                #print(i[0],",",i[1])
                                write_sheet.cell(cnt+1,j).value = "部署"
                                cnt=cnt+1
                cnt = 1
                for j in range(begin_column,158):
                    if  write_sheet.cell(1,j).value == "ステータス" :
                        for i in sample_data:
                            if cnt < max_rows :                            
                                #print(i[0],",",i[1])
                                write_sheet.cell(cnt+1,j).value = "OPEN"
                                cnt=cnt+1
                cnt = 1
                for j in range(begin_column,158):
                    if  write_sheet.cell(1,j).value == "プロジェクト名" :
                        for i in sample_data:                            
                            if i[0]== "委員・イニシアティブ" :
                                #print(i[0],",",i[1])
                                write_sheet.cell(cnt+1,j).value = i[1]
                                cnt=cnt+1
                cnt = 1
                for j in range(begin_column,158):
                    if  write_sheet.cell(1,j).value == "部門名" :
                        for i in sample_data:                            
                            if i[0]== "部署" :
                                #print(i[0],",",i[1])
                                write_sheet.cell(cnt+1,j).value = i[1]
                                cnt=cnt+1
                cnt = 1
                for j in range(begin_column,158):
                    if  write_sheet.cell(1,j).value == "本部・ユニット名" :
                        for i in sample_data:                            
                            if cnt < max_rows :
                                #print(i[0],",",i[1])
                                write_sheet.cell(cnt+1,j).value = "臨床開発本部"
                                cnt=cnt+1
                cnt = 1
                combo = []
                x=0
                y=0
                z=0
                for j in range(begin_column,158):
                    if  write_sheet.cell(1,j).value == "説明" :
                        for i in sample_data:
                                                     
                                if i[0]== "業界団体URL" :
                                    print(i[1])
                                    combo.insert(x,"【業界団体URL】\n"+str(i[1])+"\n")
                                    print(combo[x])
                                    x=x+1
                                    
                                x=0
                                if i[0]== "団体2" :
                                    print(i[1])
                                    combo.insert(x,str(combo[x])+"【団体2】\n"+str(i[1])+"\n")
                                    print(combo[x])
                                    x=x+1
                                    
                                x=0
                                if i[0]== "団体3" :
                                    print(i[1])
                                    combo.insert(x,str(combo[x])+"【団体3】\n"+str(i[1])+"\n")
                                    print(combo[x])
                                    write_sheet.cell(cnt+1,j).value = combo[x]
                                    cnt=cnt+1    
                                    x=x+1
                        """
                        for k in range(0,10):             
                            print(combo[k])
                            write_sheet.cell(cnt+1,j).value = combo[k]
                            cnt=cnt+1               
                        """
                
                """
                print("before:" ,write_sheet.cell(column=0,row=0).value)
                #write_sheet  = write_excel.worksheets[0]
                write_sheet.cell(0,row=0).value = "afterxxx"
                print("before:" ,write_sheet.cell(column=0,row=0).value)
                """
                #print("This excel includes following sheets:",write_excel.sheet_names()) #print including sheets name
                write_excel.save(filename=write_file)
                print("all write completed!")
                return 0

        except Exception as e:
                print("FAILED open Excel:",e)
                return -1

def close_write_excel(write_excel):
        try:
                return write_excel.save(filename=write_file) # open excel file

        except Exception as e:
                print("FAILED open Excel:",e)
                return -1
            
def read_1_sheet(wb):
               
        ###　variable parameters when sheet modified ###　
        sheet1 = wb.sheet_by_name(read_sheet1_name1) # specify sheet by sheet name
        print("=============Sheet %s============="%read_sheet1_name1)
        begin_row = 1 #
        #end_row = 10 #
        begin_column = 0 #
        #end_column = 10 #
        ###　variable parameters when sheet modified ###　
                
        print("Reading sheet:",sheet1.name, "has" ,sheet1.nrows, "rows" ,sheet1.ncols, "colums" )
        max_rows = sheet1.nrows
        
        for i in range(begin_row,sheet1.nrows):
                for j in range(begin_column,sheet1.ncols):
                        #if sheet1.cell(i,j).value != "":
                            sample_data.append([sheet1.cell(0,j).value,sheet1.cell(i,j).value,i])
                            #print([sheet1.cell(0,j).value,sheet1.cell(i,j).value])
                        
                            """
                            auth_value = sheet1.cell(i,begin_column-1).value
                            account_value = sheet1.cell(begin_row-1,j).value
                            limit_value = sheet1.cell(i,j).value
                            print(auth_value,",",account_value,",",limit_value)
    
                            # transform limit value        
                            if limit_value == '◎':
                                    limit_value = '2'
                            elif limit_value == '○':
                                    limit_value = '1'
                            elif limit_value =='×':
                                    limit_value = '0'
                            else:
                                    print('illegal limit value has read:'+limit_value)
                                    limit_value = ''
    
                            auth_account_pair_1.append([auth_value,account_value,limit_value])                        
                            """                    
        print("=============read sample data completed=============")
                   
def main():
        
        read_excel = open_read_excel()

        if read_excel != -1:
                read_1_sheet(read_excel)
                """
                read_2_sheet(wb)
                read_3_sheet(wb)
                """
        
        write_excel = open_write_excel()        
        #close_write_excel(write_excel)

main()
