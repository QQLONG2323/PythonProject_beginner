ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5

def add(a, b) -> float:
    return a + b

class Tool():
    ONE = 6
    TWO = 7
    THREE = 8
    FOUR = 9
    FIVE = 10
    
    @staticmethod
    def add(a, b) -> float:
        return a + b
    
    @classmethod
    def a(cls) -> None:
        print(cls.ONE)
        print(cls.TWO)
        print(cls.THREE)
        print(cls.FOUR)
        print(cls.FIVE)