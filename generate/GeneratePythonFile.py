# 创建一个txt文件，文件名为mytxtfile,并向文件写入msg
def text_create(name, msg=None):
    # 在 leetcode 文件夹下根据 leetcode 的提名创建一个 LeetCode_题号_题名文件
    print("输入名字: {}".format(name))
    # 替换名字的 '. ' 为 _
    name = name.replace('. ', '_')
    # 替换名字的 ' ' 为 _
    name = name.replace(' ', '_')
    name = 'LeetCode_' + name + '.py'
    file = open('../leetcode/' + name, 'w')
    file.write(msg if None else "class Solution:")  # msg也就是下面的Hello world!
    file.close()


text_create('78. Subsets')
