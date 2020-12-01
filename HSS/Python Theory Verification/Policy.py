from abc import ABCMeta, abstractmethod

class Policy(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def select(self,joblist,nodelist):
        pass
    
def main():
    pass

if __name__ == '__main__':
    main()