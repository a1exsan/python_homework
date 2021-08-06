
class Matrix:
    def __init__(self, data=[]):
        super().__init__()

        self.data = data

    def __str__(self):
        ret = []
        for i in self.data:
            for j in i[:-1]:
                ret.append(f'{str(j)}, ')
            ret.append(f'{i[-1]} \n')

        return ''.join(ret)

    def __add__(self, other):
        ret = []
        if len(other.data) != len(self.data) or len(other.data[0]) != len(self.data[0]):
            print("Error: different matrix size")
        else:
            for i, a in enumerate(self.data):
                ret.append([a[j] + b for j, b in enumerate(other.data[i])])
        return Matrix(ret)



mx1 = Matrix([[1,2,3,4], [2,2,2,2], [1,1,5,5]])
mx2 = Matrix([[1,1,1,1], [1,1,1,1], [1,1,1,1]])
mx3 = Matrix([[-1,-1,-1,-1], [-1,-1,-1,-1], [-1,-1,-1,-1]])
mx4 = Matrix([[-1,-1,-1], [-1,-1,-1], [-1,-1,-1]])

print(mx1)

print(mx1 + mx2 + mx3 + mx3)

print(mx1 + mx4)

