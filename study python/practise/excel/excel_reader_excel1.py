import xlrd

file = 'example.xlsx'
auth_account_pair_1 = []
auth_account_pair_2 = []
auth_account_pair_3 = []

def read_excel():
        try:
                wb = xlrd.open_workbook(filename=file) # open excel file
                print("This excel includes following sheets:",wb.sheet_names()) #print including sheets name
                return wb

        except Exception as e:
                print("FAILED open Excel:",e)
                return -1
        
def read_1_sheet(wb):
               
        ###　variable parameters when sheet modified ###　
        sheet_name = "1"
        sheet1 = wb.sheet_by_name(sheet_name) # specify sheet by sheet name
        print("=============Sheet %s============="%sheet_name)
        begin_row = 4 #
        end_row = 9 #
        begin_column = 2 #
        end_column = 6 #
        ###　variable parameters when sheet modified ###　
                
        print("Reading sheet:",sheet1.name, "has" ,sheet1.nrows, "rows" ,sheet1.ncols, "colums" )
           
        for i in range(begin_row,end_row):
                for j in range(begin_column,end_column):
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
                        
def read_2_sheet(wb):
             
        ###　variable parameters when sheet modified ###　
        sheet_name = "2"
        sheet1 = wb.sheet_by_name(sheet_name) # specify sheet by sheet name
        print("=============Sheet %s============="%sheet_name)
        begin_row = 4 #
        end_row = 9 #
        begin_column = 2 #
        end_column = 7 #
        ###　variable parameters when sheet modified ###　
                
        print("Reading sheet:",sheet1.name, "has" ,sheet1.nrows, "rows" ,sheet1.ncols, "colums" )
           
        for i in range(begin_row,end_row):
                for j in range(begin_column,end_column):
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

                        auth_account_pair_2.append([auth_value,account_value,limit_value])    


def read_3_sheet(wb):

        ###　variable parameters when sheet modified ###　
        sheet_name = "3"
        sheet1 = wb.sheet_by_name(sheet_name) # specify sheet by sheet name
        print("=============Sheet %s============="%sheet_name)
        begin_row = 4 #
        end_row = 10 #
        begin_column = 2 #
        end_column = 7#
        ###　variable parameters when sheet modified ###　
                
        print("Reading sheet:",sheet1.name, "has" ,sheet1.nrows, "rows" ,sheet1.ncols, "colums" )
           
        for i in range(begin_row,end_row):
                for j in range(begin_column,end_column):
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

                        auth_account_pair_3.append([auth_value,account_value,limit_value])    

                        
def main():
        
        wb = read_excel()

        if wb != -1:
                read_1_sheet(wb)
                read_2_sheet(wb)
                read_3_sheet(wb)

main()
