import os

all_file=[]

def create_file(name:str,path:str,content:str)->str:
    try:
        open(path+"/"+name,"w").write(content)
    except Exception as e: 
        return str(e)
    return "done"

def create_dir(name,path)->str:
    try:
        os.mkdir(path+"/"+name)
    except Exception as e:
        return str(e)
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
    
    pprint(create_dir(".venv","."))