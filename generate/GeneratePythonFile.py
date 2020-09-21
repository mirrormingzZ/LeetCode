# 创建一个 py 文件，文件名为 LeetCode_xxx_xxx.py ,并向文件写入 class Solution: ...
def text_create(name, content=None):
    # 在 leetcode 文件夹下根据 leetcode 的提名创建一个 LeetCode_题号_题名文件
    print("输入名字: {}".format(name))
    # 替换名字的 '. ' 为 _
    name = name.replace('. ', '_')
    # 替换名字的 ' ' 为 _
    name = name.replace(' ', '_')
    name = 'LeetCode_' + name + '.py'
    file = open('../leetcode/' + name, 'w')
    file.write(content if None else "class Solution:")
    file.close()


text_create('538. Convert BST to Greater Tree')
