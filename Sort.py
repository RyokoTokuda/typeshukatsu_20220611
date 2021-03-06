def main():
    #ランダムに並べられた重複のない整数の配列
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
    while True:
        fwd_idx = 0
        bwd_idx = -1
        for fwd in array:
            if fwd >= pivot:
                fwd_idx = array.index(fwd)
                for bwd in reversed(array):
                    if bwd < pivot:
                        bwd_idx = array.index(bwd)
                        break
                    
                if fwd_idx - bwd_idx == 1:
                    if len(array) == 2:
                        return array
                    else:
                        return sort(array[:fwd_idx]) + sort(array[fwd_idx:])
                else:
                    array[fwd_idx], array[bwd_idx] = array[bwd_idx], array[fwd_idx]   
    # ここまで記述

if __name__ == '__main__':
    main()