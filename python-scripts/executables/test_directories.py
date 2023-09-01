import sys
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")
sys.path.append("/home/forge/.local/lib/python3.8/site-packages")
from sqlalchemy import create_engine

# from ResolutionManager.Repositories.DocumentRepository import DocumentRepository

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

    print('done')





if __name__ == '__main__':
#     add_path()
    main()
