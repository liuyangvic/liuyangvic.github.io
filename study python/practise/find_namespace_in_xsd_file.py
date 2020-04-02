import os

# Specify the directory which you want to extract the "prefix" "targetNamespace" "xsd file name"
# Ex: global_path = ".\\wsdl.release\\"
#global_path = ".\\XII1k_wsdl.release_schema\\"
global_path = ".\\pf2.2_wsdl.release_schema\\"

def traverse_files(path):

    for root,dirs,files in os.walk(path):
        pass
        #print(files)
    
    return files

def read_xsd_file(file):

    f = open(file,"r",encoding="utf-8_sig")
    lines = f.read()

    #print(lines)

    return lines

def find_namespace(lines):

    position = lines.find("targetNamespace=\"")

    if position == -1:
        print("targetNamespace NOT FOUND")
        return -1

    #print(position)

    splited_lines1 = lines.split("targetNamespace=\"",1)

    splited_lines2 = splited_lines1[1].split("\"",1)

    namespace = splited_lines2[0]
   
    
    #print(namespace)     

    return namespace

def find_prefix(lines, namespace):

    position = lines.find("\""+namespace+"\"")

    if position == -1:
        print("namespace NOT FOUND!")
        return -1

    #print(position)

    #print(lines[position-1:position+len(namespace)+1])

    # find prefix one the LEFT of targetNamespace. targetNamespace is in the end
    position2 = lines.find("xmlns:",position-15,position)

    #print(position2)

    splited_lines = lines[position2:position-1].split(":",1)

    check_length = len(splited_lines)

    if check_length == 2:
        prefix = splited_lines[1]
        return prefix

    # find prefix one the LEFT of targetNamespace. targetNamespace at the beginning
    position_r = lines.rfind("\""+namespace+"\"")
    
    position3 = lines.find("xmlns:",position_r-15,position_r)

    splited_lines = lines[position3:position_r-1].split(":",1)

    check_length = len(splited_lines)

    if check_length == 2:
        prefix = splited_lines[1]
        return prefix

    #print("prefix NOT FOUND!")
    return -1

def main():

    files = traverse_files(global_path)

    for i in files:

        #print(i)

        if (i.find(".Server.xsd") >0) | (i.find("Impl.xsd") > 0):
            #print("Skip",i)
            continue

        xsd_contents = read_xsd_file(global_path+i)

        target_namespace = find_namespace(xsd_contents)

        prefix = find_prefix(xsd_contents,target_namespace)

        if prefix == -1:
            print("prefix NOT FOUND!".ljust(20),target_namespace.ljust(100),i.ljust(50))
            continue
        
        print(prefix.ljust(20),target_namespace.ljust(100),i.ljust(50))

   
main()
