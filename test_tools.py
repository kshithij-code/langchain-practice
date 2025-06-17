from os import listdir

all_file=[]

def files_tool(path):
    global all_file
    all_file=[path+"/"+i for i in listdir(path)]

    def get_allfiles1(path):
        for i in open(".foldignore","r").read().split("\n"):
            if i in path:
                return False
        try:
            listdir(path)
        except:
            return False
        for i in listdir(path):
            temp=path+"/"+i
            if get_allfiles1(temp):
                for j in listdir(temp):
                    all_file.append(temp+"/"+j)
        return True
    get_allfiles1(path)
    
    return all_file


if __name__=="__main__":
    from pprint import pprint
    
    pprint(files_tool("./my-app"))