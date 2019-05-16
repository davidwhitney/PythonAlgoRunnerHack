import importlib
import inspect
import logging

runtime = importlib.import_module('runtime')

def main():    
    print("Python AlgoRuntime")

    rt = runtime.Runtime()
    rt.execute()

if __name__ == '__main__':
    logging.basicConfig(filename='runtime.log',level=logging.INFO)    
    logging.getLogger().addHandler(logging.StreamHandler())
    main()