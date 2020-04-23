import xlrd

file = 'P2Pカラーモード(自動生成用).xlsx'
copy_color_mode = []


def read_excel():
        try:
                wb = xlrd.open_workbook(filename=file) # open excel file
                print("This excel includes following sheets:",wb.sheet_names()) #print including sheets name
                return wb

        except Exception as e:
                print("FAILED open Excel:",e)
                return -1
        
def read_auto_generate_sheet(wb):
               
        ###　variable parameters when sheet modified ###　
        sheet_name = "CopyMode禁則(自動生成用)"
        sheet1 = wb.sheet_by_name(sheet_name) # specify sheet by sheet name
        print("=============Sheet %s============="%sheet_name)
        begin_row = 4 #
        end_row = 13 #
        begin_column = 0 #
        end_column = 3 #
        ###　variable parameters when sheet modified ###　
                
        print("Reading sheet:",sheet1.name, "has" ,sheet1.nrows, "rows" ,sheet1.ncols, "colums" )

        for j in range(begin_column,end_column):
                for i in range(begin_row,end_row):
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

                        copy_color_mode.append([auth_value,account_value,limit_value])                        
                        
                        
def main():
        
        wb = read_excel()

        if wb != -1:
                read_fx_sheet(wb)
                read_ibg_sheet(wb)
                read_mn_sheet(wb)

main()
