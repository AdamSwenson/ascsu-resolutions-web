import sys
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")
sys.path.append("/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts")
import os
from ResolutionManager.config.Configuration import Configuration

from sqlalchemy import create_engine

from ResolutionManager.Repositories.DocumentRepository import DocumentRepository

def add_path():
    data = ''
    with open("../private/paths.txt", "r") as text_file:
        #read whole file to a string
        data = text_file.read()

    sys.path.append(data)
    sys.stdout.write(data + "\n")

def main():
#     print(sys.path)
#     import ResolutionManager.Repositories.DocumentRepository.DocumentRepository as d
    con = Configuration()
#     sys.stdout.write(f"{con.dsn}")


    print(con.configuration)





if __name__ == '__main__':
#     add_path()
    main()
