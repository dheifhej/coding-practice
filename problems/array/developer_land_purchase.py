# 在一个城市区域内，被划分成了n * m个连续的区块，每个区块都拥有不同的权值，代表着其土地价值。目前，有两家开发公司，A 公司和 B 公司，希望购买这个城市区域的土地。
# 现在，需要将这个城市区域的所有区块分配给 A 公司和 B 公司。
# 然而，由于城市规划的限制，只允许将区域按横向或纵向划分成两个子区域，而且每个子区域都必须包含一个或多个区块。 为了确保公平竞争，你需要找到一种分配方式，使得 A 公司和 B 公司各自的子区域内的土地总价值之差最小。
# 注意：区块不可再分。
# 输入描述
# 第一行输入两个正整数，代表 n 和 m。
# 接下来的 n 行，每行输出 m 个正整数。
# 输出描述
# 请输出一个整数，代表两个子区域内土地总价值之间的最小差距。
# 输入示例
# 3 3
# 1 2 3
# 2 1 3
# 1 2 3
# 输出示例
# 0

# 核心思路：把二维降为一维
# 题目要求把矩阵分成两部分，且只能按横向或纵向划分。
# 横着切： 不管每一行里面长什么样，我们只关心“这一行总价值是多少”。
# 竖着切： 不管每一列里面长什么样，我们只关心“这一列总价值是多少”。
# 整个矩阵总和 = sum
# 切出来的一边总和 = horizontalCut
# 另一边总和 = sum - horizontalCut
# import sys
#
# input = sys.stdin.read
#
#
# def main():
#     data = input().split()
#     index = 0
#
#     n = int(data[index])
#     index += 1
#     vec = []
#     for i in range(n):
#         vec.append(int(data[index + i]))
#     index += n
#
#     p = [0] * n
#     presum = 0
#     for i in range(n):
#         presum += vec[i]
#         p[i] = presum
#
#     results = []
#     while index < len(data):
#         a, b = int(data[index]), int(data[index + 1])
#         index += 2
#
#         if a == 0:
#             results.append(p[b])
#         else:
#             results.append(p[b] - p[a - 1])
#
#     for result in results:
#         print(result)
#
#
# if __name__ == "__main__":
#     main()

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    sum = 0
    vec = []
    for i in range(n):
        row = []
        for j in range(m):
            num = int(data[idx])
            idx += 1
            row.append(num)
            sum += num
        vec.append(row)

    result = float('inf')

    count = 0
    # 行切分
    for i in range(n):

        for j in range(m):
            count += vec[i][j]
            # 遍历到行末尾时候开始统计
            if j == m - 1:
                result = min(result, abs(sum - 2 * count))

    count = 0
    # 列切分
    for j in range(m):

        for i in range(n):
            count += vec[i][j]
            # 遍历到列末尾时候开始统计
            if i == n - 1:
                result = min(result, abs(sum - 2 * count))

    print(result)


if __name__ == "__main__":
    main()

