def merge_k_lists(lists):
    # 各リストの「次に処理する位置」を記録するポインタ（すべて0からスタート）
    pointers = [0] * len(lists)
    result = []

    while True:
        min_val = float('inf')  # 最小値の初期値（無限大）
        min_list_idx = -1       # 最小値を持つリストのインデックス

        # すべてのリストの「先頭」を1つずつチェック
        for i in range(len(lists)):
            # そのリストがまだ未処理の要素を持っている場合
            if pointers[i] < len(lists[i]):
                current_val = lists[i][pointers[i]]
                # 暫定の最小値より小さければ更新
                if current_val < min_val:
                    min_val = current_val
                    min_list_idx = i

        # すべてのリストを最後まで処理し終えたら終了
        if min_list_idx == -1:
            break

        # 見つかった最小値を結果に追加し、そのリストのポインタを1つ進める
        result.append(min_val)
        pointers[min_list_idx] += 1

    return result

def ssdf(lists):
    pointers = [0] * len(lists)
    result = []

    while True:
        min_val = float("inf")
        min_list_idx = -1

        for i in range(len(lists)):
            if pointers[i] < len(lists[i]):
                current_val = lists[i][pointers[i]]
                if current_val < min_val:
                    min_val = current_val
                    min_list_idx = i

        if min_list_idx == -1:
            break