# 快速排序
# 
# 基本思想：分而治之
# 流程简述：
# 1. 找到一个枢纽；（可以随机找一个，也可以从头从尾部开始选）
# 2. 左指针和右指针从两端开始向内进行搜索，当左指针找到一个比枢纽大的，右指针找到一个比枢纽小的，就它们进行交换，
#    直到两个指针相遇，就把枢纽放在相遇的地方。此时枢纽的位置就确定了，左侧的位置上的数字一定比枢纽小，右边的位
#    置上的数字一定比枢纽大。（这个步骤称为一次划分）
# 3. 可以把枢纽左右侧分别看成一个待排序的子序列，对它们分别进行一次划分。这时又会有两个枢纽位置有序，递归的执行
#    下去，直到所有的序列位置都有序。
# 复杂度分析：
# - 时间复杂度：O(n*logn)
# - 空间复杂度：O(logn)
# 不稳定

def partition(seq, left, right):
    # 选择左边第一个为枢纽
    pivot = seq[left]
    start = left + 1
    end = right
 
    while start <= end:
        # 从左向右找到一个比枢纽小的值
        while start <= end and seq[end] >= pivot:
            end -= 1

        # 从右向左找到一个比枢纽大的值
        while start <= end and seq[start] <= pivot:
            start += 1

        # 交换两个值
        if start <= end:
            seq[start], seq[end] = seq[end], seq[start]
    
    # 枢纽归位
    seq[left], seq[end] = seq[end], seq[left]
    return end

def quick_sort(seq, left, right):
    if left >= right:
        return

    pi = partition(seq, left, right)
    # 递归调用，对子序列划分
    quick_sort(seq, left, pi-1)
    quick_sort(seq, pi+1, right)


if __name__ == "__main__":
    seq = [i for i in range(10)]
    import random
    random.shuffle(seq)
    print(f"排序前: {seq}")
    quick_sort(seq, 0, len(seq)-1)
    print(f"排序后: {seq}")

# https://www.geeksforgeeks.org/python-program-for-quicksort/
# https://stackabuse.com/quicksort-in-python/