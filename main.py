def has_duplicates(lst):
    # 将列表转换为集合，利用集合元素唯一性判断是否有重复
    return len(set(lst)) < len(lst)
# 测试用例
test_cases = [
    [1, 2, 3, 4, 5],  # 无重复元素
    [1, 2, 2, 3, 4],  # 有重复元素
    ["a", "b", "c", "a"],  # 有重复元素（字符串）
    []  # 空列表
]
# 调用函数并打印测试结果
for case in test_cases:
    print(f"列表 {case} 是否有重复元素：{has_duplicates(case)}")
