from typing import Dict

def romanToInteger(origin_roman: str) -> int:
    roman: Dict[str, int] = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    result: int = 0
    i: int = 0
    length_of_origin_roman: int = len(origin_roman)
    
    while (i < length_of_origin_roman):
        number1: int = roman[origin_roman[i]]
        
        if (i + 1 < length_of_origin_roman):
            number2: int = roman[origin_roman[i + 1]]
            if (number1 >= number2):
                result += number1
                i += 1
            else:
                result += number2 - number1
                i += 2
        else:
            result += number1
            i += 1
    return result

def main() -> None:
    roman: str = "MCMXCIV"
    arabic: int = romanToInteger(origin_roman=roman)
    print(arabic)
    
if __name__ == "__main__":
    main()