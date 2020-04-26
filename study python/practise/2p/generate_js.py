from read_excel import copy_color_mode # read excel1
from js_builder import JsBuilder # JavaScript build helper class
from datetime import datetime

def generate_plugin(js_builder, sheet_name, sheet_info):
    js_builder.write_code('//# @brief introduction: Exce11 '+sheet_name+' sheet')
    js_builder.write_code('//# @input parameter: XXX')
    js_builder.write_code('//# @output parameter: YYY')
    js_builder.write_code('//# @return: API call result: 0 - excecuted successfully, -1 - error finish')
    with js_builder.block('class Copy_ColorMode'):
            js_builder.write_line()
        #for i in range(len(sheet_info)+1):

            with js_builder.block('getSupportedKeys()',  newline=False):
                #js_builder.write_code('SetLimit = '+'\"'+sheet_info[i][2]+'\"')
                js_builder.write_code('return 0')
            js_builder.write_line() 

 
            with js_builder.block('getRequiredKeys()',  newline=False):
                #js_builder.write_code('SetLimit = '+'\"'+sheet_info[i][2]+'\"')
                js_builder.write_code('return 0')
            js_builder.write_line()


            with js_builder.block('correct(expected, required, corrected, failure)',  newline=False):
                #js_builder.write_code('SetLimit = '+'\"'+sheet_info[i][2]+'\"')
                js_builder.write_code('return 0')
            js_builder.write_line()
            
            """
            if  i == 0:
                with js_builder.block('if(AuthValue == '+'\"'+sheet_info[i][0]+'\"'+' && AccountValue =='+'\"'+sheet_info[i][1]+'\"'+')',  newline=False):
                    js_builder.write_code('SetLimit = '+'\"'+sheet_info[i][2]+'\"')
                    js_builder.write_code('return 0')
                js_builder.write_line()        
            elif i == len(sheet_info) :
                with js_builder.block('else', newline=False):
                    js_builder.write_code('WARN(\"NO such Auth Auccount Combination!\")')
                    js_builder.write_code('SetLimit = \"\"')
                    js_builder.write_code('return -1')
                js_builder.write_line()   
            else:
                with js_builder.block('else if(AuthValue == '+'\"'+sheet_info[i][0]+'\"'+' && AccountValue =='+'\"'+sheet_info[i][1]+'\"'+')',  newline=False):
                    js_builder.write_code('SetLimit = '+'\"'+sheet_info[i][2]+'\"')
                    js_builder.write_code('return 0')
                js_builder.write_line()
            """
    js_builder.write_line()    

def generate_framework(js_builder):
    #js_builder.write_code('//# @brief introduction: Exce11 '+sheet_name+' sheet')
    #js_builder.write_code('//# @input parameter: XXX')
    with js_builder.block('class SystemDataCorrector'):
        
        with js_builder.block('constructor(modules)',  newline=False): #TBD modules
            #js_builder.write_code('SetLimit = '+'\"'+sheet_info[i][2]+'\"')
            js_builder.write_code('return 0')
        js_builder.write_line()

        with js_builder.block('getSupportedKeys()',  newline=False): 
            #js_builder.write_code('SetLimit = '+'\"'+sheet_info[i][2]+'\"')
            js_builder.write_code('return ret')
        js_builder.write_line()

        with js_builder.block('getRequiredKeys()',  newline=False): 
            #js_builder.write_code('SetLimit = '+'\"'+sheet_info[i][2]+'\"')
            js_builder.write_code('return ret')
        js_builder.write_line()

        with js_builder.block('correct(expected, required, corrected, failure)',  newline=False):  #TBD
            #js_builder.write_code('SetLimit = '+'\"'+sheet_info[i][2]+'\"')
            js_builder.write_code('return ret')
        js_builder.write_line()
    
    js_builder.write_line() 

def generate_excel1_cpp():

    s = JsBuilder()
    #s.write_line('//# @class excel1_limit')
    s.write_line('//# @generate date:'+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    s.write_line()
    
    #s.write_line('#include \"excel1_limit.h\"') 
    #s.write_line()

    s.write_line('var systemDataCorrectModules = [];')
    s.write_line()

    """
    with s.block('void excel1_limit::~excel1_limit(void)'):
        s.write_line()
    s.write_line()
    """

    #1 sheet Copy_ColorMode
    generate_plugin(s,"1",copy_color_mode)

    #
    s.write_line('systemDataCorrectModules.push(new Copy_ColorMode());')
    #
    generate_framework(s)

                    
    #print(s.get_value())

    excel1_cpp = open("excel1_limit.js","w+")
    excel1_cpp.writelines(s.get_value())
    excel1_cpp.close()

generate_excel1_cpp()
