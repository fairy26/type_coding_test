def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    start_idx = 0                       # 探索開始位置のindex
    end_idx = len(sorted_array) - 1     # 探索終了位置のindex
    
    # 両端を絞り込んで探索する
    while start_idx <= end_idx:
        mid_idx = (start_idx + end_idx) // 2    # 探索範囲の中間位置のindex = 探索対象と比較する位置
        
        # 探索範囲の中間の値が探索対象の値と一致したらそのindexを返す
        if sorted_array[mid_idx] == target_number:
            return mid_idx

        # 一致しなければ、探索範囲の中間の値と探索対象の大小を比較し探索範囲を更新
        if sorted_array[mid_idx] < target_number:
            start_idx = mid_idx + 1     # 中間値以上の範囲に絞る
        else:
            end_idx = mid_idx - 1       # 中間値以下の範囲に絞る
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
