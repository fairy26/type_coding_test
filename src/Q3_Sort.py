def main():
    # ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    l_idx, r_idx = 0, len(array) - 1  # 左右から走査するindex

    while l_idx < r_idx:
        while array[l_idx] < pivot and l_idx < len(array):  # 基準値以上の値までindexを進める
            l_idx += 1
        while array[r_idx] >= pivot and r_idx > 0:          # 基準値未満の値までindexを戻す
            r_idx -= 1

        if l_idx < r_idx:   # indexがぶつかってなければ見つかった値を入れ替える
            array[l_idx], array[r_idx] = array[r_idx], array[l_idx]

    l_arr = sort(array[:r_idx + 1]) # 左側（基準値未満）の配列をソート
    r_arr = sort(array[r_idx + 1:]) # 右側（基準値以上）の配列をソート
    
    return l_arr + r_arr
    # ここまで記述

if __name__ == '__main__':
    main()
