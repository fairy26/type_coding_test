for num in range(1, 101):
    string = ''

    # ここから記述
    if num % 15 == 0:   # 数字が15の倍数なら'FizzBuzz'を出力
        string = 'FizzBuzz'
    elif num % 3 == 0:  # 数字が3の倍数なら'Fizz'を出力
        string = 'Fizz'
    elif num % 5 == 0:  # 数字が5の倍数なら'Buzz'を出力
        string = 'Buzz'
    else:               # それ以外はその数字を出力
        string = str(num)
    # ここまで記述

    print(string)
