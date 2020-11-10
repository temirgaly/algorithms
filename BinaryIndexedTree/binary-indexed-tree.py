def BinaryIndexedTree(nums, n):
    tree = [0 for _ in range(n+1)]

    def getNext(index):
        return index + (index&-index)

    def getParent(index):
        return index - (index&-index)

    def update(index, val):
        index += 1
        while index <= n:
            tree[index] += val
            index = getNext(index)

    def sum(index):
        s=0
        index += 1
        while index:
            s += tree[index]
            index = getParent(index)
        return s
    
    for index, val in enumerate(nums):
        update(index, val)

    #get values in range [1,7]
    a = 1
    b = 7
    val = sum(b)-sum(a-1)
    print(val, tree)

def driver():
    nums = [1,3,4,8,6,1,4,2]
    N = 8
    BinaryIndexedTree(nums, N)


if __name__ == "__main__":
    driver()