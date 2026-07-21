"""
题目：区间和
来源： https://kamacoder.com/problempage.php?pid=1070

算法：前缀和
思路：

时间复杂度：
空间复杂度：

备注：
"""


# n = int(input()) 这种写法在笔试中同样受欢迎，且更易读
# arr = [int(x) for x in input().split()] 或者 arr = list(map(int, input().split()))[:n] 也可以
# 下面的写法本质上是把整个输入文件当作一个巨大的字符串流（Stream），然后通过一个指针（index）手动控制进度。
# 这种方式在处理海量数据（比如 10^5 以上）时，比 input() 循环快得不止一点点。
# 这种方法避免了多次调用 input() 产生的系统调用开销。在 Python 这种解释型语言里，减少系统调用次数是提速的关键
#
# import sys
# input = sys.stdin.read # 这里没加 ()，因为你不是要现在就读数据，你只是想把 sys.stdin.read 这个“员工”改名叫 input
# def main():
#     # 使用 sys.stdin.read().split() 一次性读取，防止 input() 循环读取太慢
#     data = input().split()
#     index = 0
#
#     # read array
#     n = int(data[index])
#     index += 1
#     vec = []
#     for i in range(n):
#         vec.append(int(data[index+i]))
#     # 为什么要用 index += n,这道题最麻烦的地方在于：后面还有数据！读完这n个数后，你还要读后面的 a b 区间对，所以这边用指针便宜量
#     index += n
#
#     # build presum array
#     p = [0] * n
#     presum = 0
#     for i in range(n):
#         presum += vec[i]
#         p[i] = presum
#
# read the interval in a loop
#     results = []
#     while index < len(data):
#         a = int(data[index])
#         b = int(data[index+1])
#         index += 2
#
#         if a == 0:
#             sum_value = p[b]
#         else:
#             sum_value = p[b] - p[a-1]   # 可以看示例自己算下
#
#         results.append(sum_value)
#
#     for result in results:
#         print(result)


# 加上这行代码后：你既可以把这个文件当成程序直接跑，又可以把它当成一个“库”安全地被别人引用，而不会触发任何意外的副作用。
# It prevents unintended execution when the file is imported as a module.
# 因为被别人import的时候这个属性等于另一个文件名
# 只放“只在直接运行时才需要执行的代码”，比如测试代码，demo，main逻辑。比如print(add(1, 2))
# if __name__ == "__main__":
#     main()

# 本地调试，改成普通的input()
def main():
    n = int(input())
    vec = []
    for _ in range(n):
        vec.append(int(input()))

    p = [0] * n
    presum = 0
    for i in range(n):
        presum += vec[i]
        p[i] = presum

    while True:
        try:
            a, b = map(int, input().split())
            if a == 0:
                print(p[b])
            else:
                print(p[b] - p[a - 1])
        except EOFError:
            break


if __name__ == "__main__":
    main()





