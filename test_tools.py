import os

all_file=[]

def create_file(name:str,path:str,content:str)->str:
    try:
        open(path+"/"+name,"w").write(content)
    except Exception as e: 
        return str(e)
    return "done"

def create_dir(name:str,path:str)->str:
    try:
        os.mkdir(path+"/"+name)
    except Exception as e:
        return str(e)
    return "done"

def edit_file(path:str,start_no:int,end_no:int,content:str)->str:
    temp=open(path,"r").read().split("\n")
    pprint(open(path,"r").read())
    print(temp[:start_no],temp[end_no+1:len(temp)-1])
    if len(temp)<start_no:
        print(len(temp))
        open(path,"a").write(content+"\n")
    else:
        print(temp)
        temp=temp[:start_no]+[content]+temp[end_no+1:len(temp)-1]
        print(temp)
        open(path,"w").writelines(list(map(lambda x:x+"\n",temp)))
    pprint(open(path,"r").read())
    return "done"

def insert_to_file(path:str,index:int,content:str)->str:
    temp=open(path,"r").read().split("\n")
    pprint(open(path,"r").read())
    if len(temp)<index:
        print(len(temp))
        open(path,"a").write(content+"\n")
    else:
        print(temp)
        temp=temp[:index]+[content]+temp[index:len(temp)-1]
        print(temp)
        open(path,"w").writelines(list(map(lambda x:x+"\n",temp)))
    pprint(open(path,"r").read())
    return "done"

def files_tool(path):
    global all_file
    all_file=[path+"/"+i for i in os.listdir(path)]

    def get_allfiles1(path):
        for i in open(".foldignore","r").read().split("\n"):
            if i in path:
                return False
        try:
            os.listdir(path)
        except:
            return False
        for i in os.listdir(path):
            temp=path+"/"+i
            if get_allfiles1(temp):
                for j in os.listdir(temp):
                    all_file.append(temp+"/"+j)
        return True
    get_allfiles1(path)
    
    return all_file


if __name__=="__main__":
    from pprint import pprint
    
    # pprint(create_dir(".venv","."))
    pprint(edit_file("test.txt",2,3,"lsc1\nasl2"))