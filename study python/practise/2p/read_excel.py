"""
Sample禁則Lib(Copy ColorMode禁則)
===
禁則pattern：

to_be_set_cl_value
is limited(制約され) by
limited_by_cl_value,limited_by_cl_value2, limited_by_cl_value3 etc.

it will fianlly be correctted（修正され） to
correct_to_cl_value.

after it is corrected,
affected_cl_value1, affected_cl_value2, affected_cl_value3 etc.
will also be changed（影響され）

"""
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
        end_row = 7 #
        begin_column = 0 #
        end_column = 3 #
        ###　variable parameters when sheet modified ###　
                
        print("Reading sheet:",sheet1.name, "has" ,sheet1.nrows, "rows" ,sheet1.ncols, "colums" )

        for i in range(begin_row,end_row+1):
                # old product cl value
                to_be_set_cl_value = sheet1.cell(i,begin_column).value
                # can be limited by cl1 cl2 cl3 etc.
                limited_by_cl_value = sheet1.cell(i,begin_column+1).value
                # finally it will be correct to following value
                correct_to_cl_value = sheet1.cell(i,begin_column+2).value
                # it will also also
                affected_cl_value = sheet1.cell(i,begin_column+3).value
                print(str(to_be_set_cl_value).ljust(10),",",str(limited_by_cl_value).ljust(10),",",str(correct_to_cl_value).ljust(10),",",str(affected_cl_value).ljust(10)) 

                copy_color_mode.append([to_be_set_cl_value,limited_by_cl_value,correct_to_cl_value,affected_cl_value])

def trans_to_be_set_cl_value(in_value,out_value):

                # transform spec(仕様) to num(実装)      
                if in_value == '◎':
                        out_value = '2'
                elif in_value == '○':
                        limit_value = '1'
                elif in_value =='×':
                        out_value = '0'
                else:
                        print('illegal in_value has read:'+in_value)
                        in_value = ''

                        return -1

                return out_value
        
def trans_to_limited_by_cl_value(in_value,out_value):

                # transform spec(仕様) to num(実装)      
                if in_value == '◎':
                        out_value = '2'
                elif in_value == '○':
                        limit_value = '1'
                elif in_value =='×':
                        out_value = '0'
                else:
                        print('illegal in_value has read:'+in_value)
                        in_value = ''

                        return -1

                return out_value
        
def trans_to_affected_cl_value(in_value,out_value):

                # transform spec(仕様) to num(実装)      
                if in_value == '◎':
                        out_value = '2'
                elif in_value == '○':
                        limit_value = '1'
                elif in_value =='×':
                        out_value = '0'
                else:
                        print('illegal in_value has read:'+in_value)
                        in_value = ''

                        return -1

                return out_value
        
def trans_to_affected_cl_value(in_value,out_value):

                # transform spec(仕様) to num(実装)      
                if in_value == '◎':
                        out_value = '2'
                elif in_value == '○':
                        limit_value = '1'
                elif in_value =='×':
                        out_value = '0'
                else:
                        print('illegal in_value has read:'+in_value)
                        in_value = ''

                        return -1

                return out_value

                        
def main():
        
        wb = read_excel()

        if wb != -1:
                read_auto_generate_sheet(wb)

main()
