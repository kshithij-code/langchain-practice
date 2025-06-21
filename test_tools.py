import os
from langchain_core.tools import tool

all_file=[]

from pydantic import BaseModel

class CreateFileInput(BaseModel):
    file_name: str
    file_content: str
    file_path: str = "."  # default value


@tool(args_schema=CreateFileInput)
def create_file(file_name:str, file_content:str, file_path:str='D:\\visual\\gem_agent\\') -> str:
    """
    Create a file with the given name at the specified path and write the provided content to it.

    Args:
        name (str): The name of the file to create.
        path (str): The directory path where the file will be created.
        content (str): The content to write into the file.

    Returns:
        str: "done" if successful, otherwise the exception message.
    """
    try:
        open(os.path.join(file_path,file_name),"w").write(file_content)
    except Exception as e: 
        return str(e)
    return "done"

def create_dir(name:str, path:str) -> str:
    """
    Create a directory with the given name at the specified path.

    Args:
        name (str): The name of the directory to create.
        path (str): The parent directory path where the new directory will be created.

    Returns:
        str: "done" if successful, otherwise the exception message.
    """
    try:
        os.mkdir(path+"/"+name)
    except Exception as e:
        return str(e)
    return "done"

def edit_file(path:str, start_no:int, end_no:int, content:str) -> str:
    """
    Replace lines in a file from start_no to end_no (inclusive) with the provided content.

    Args:
        path (str): The file path to edit.
        start_no (int): The starting line number (0-based index).
        end_no (int): The ending line number (0-based index).
        content (str): The content to insert in place of the specified lines.

    Returns:
        str: "done" after editing the file.
    """
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

def insert_to_file(path:str, index:int, content:str) -> str:
    """
    Insert content into a file at the specified line index.

    Args:
        path (str): The file path to edit.
        index (int): The line index (0-based) at which to insert the content.
        content (str): The content to insert.

    Returns:
        str: "done" after inserting the content.
    """
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
    """
    List all files in the given directory, recursively, ignoring paths listed in '.foldignore'.

    Args:
        path (str): The root directory path to search for files.

    Returns:
        list: A list of file paths found under the given directory.
    """
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
    
