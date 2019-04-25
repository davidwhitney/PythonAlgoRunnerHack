import importlib
import inspect
runtime = importlib.import_module('runtime')

def main():
    print("Python AlgoRuntime")

    rt = runtime.Runtime()
    rt.execute()

if __name__ == '__main__':
    main()