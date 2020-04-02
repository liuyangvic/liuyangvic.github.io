from excel_reader_excel1 import auth_account_pair_1,auth_account_pair_2,auth_account_pair_3 # read excel1
from cpp_builder import CppBuilder # cpp build helper class
from datetime import datetime

def generate_sheet_api(cpp_builder, sheet_name, sheet_info):
    cpp_builder.write_code('//# @brief introduction: Exce11 '+sheet_name+' sheet')
    cpp_builder.write_code('//# @input parameter: XXX')
    cpp_builder.write_code('//# @output parameter: YYY')
    cpp_builder.write_code('//# @return: API call result: 0 - excecuted successfully, -1 - error finish')
    with cpp_builder.block('int excel1_limit::Auth_Account_1(const string AuthValue, const string AccountValue,const string& SetLimit)'):
        cpp_builder.write_line()
        for i in range(len(sheet_info)+1):
            if  i == 0:
                with cpp_builder.block('if(AuthValue == '+'\"'+sheet_info[i][0]+'\"'+' && AccountValue =='+'\"'+sheet_info[i][1]+'\"'+')',  newline=False):
                    cpp_builder.write_code('SetLimit = '+'\"'+sheet_info[i][2]+'\"')
                    cpp_builder.write_code('return 0')
                cpp_builder.write_line()        
            elif i == len(sheet_info) :
                with cpp_builder.block('else', newline=False):
                    cpp_builder.write_code('WARN(\"NO such Auth Auccount Combination!\")')
                    cpp_builder.write_code('SetLimit = \"\"')
                    cpp_builder.write_code('return -1')
                cpp_builder.write_line()   
            else:
                with cpp_builder.block('else if(AuthValue == '+'\"'+sheet_info[i][0]+'\"'+' && AccountValue =='+'\"'+sheet_info[i][1]+'\"'+')',  newline=False):
                    cpp_builder.write_code('SetLimit = '+'\"'+sheet_info[i][2]+'\"')
                    cpp_builder.write_code('return 0')
                cpp_builder.write_line()
    cpp_builder.write_line()    


def generate_excel1_cpp():

    s = CppBuilder()
    s.write_line('//# @class excel1_limit')
    s.write_line('//# @generate date:'+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    s.write_line()
    
    s.write_line('#include \"excel1_limit.h\"') 
    s.write_line()

    with s.block('void excel1_limit::excel1_limit(void)'):
        s.write_line()
    s.write_line()

    with s.block('void excel1_limit::~excel1_limit(void)'):
        s.write_line()
    s.write_line()

    #1 sheet
    generate_sheet_api(s,"1",auth_account_pair_1)

    #2 sheet
    generate_sheet_api(s,"2",auth_account_pair_2)

    #3 sheet
    generate_sheet_api(s,"3",auth_account_pair_3)

                    
    #print(s.get_value())


    excel1_cpp = open("excel1_limit.cpp","w+")
    excel1_cpp.writelines(s.get_value())
    excel1_cpp.close()

generate_excel1_cpp()
