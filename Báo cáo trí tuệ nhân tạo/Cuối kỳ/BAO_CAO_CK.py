import numpy 
import itertools

def queens_check(list):
    result = 0 # đếm số lời giải
    # kiểm tra lời giải
    for k in list:
        fitness = 0 # đếm số vị trí không phù hợp
        for i in range(len(k) - 1):
            for j in range(i + 1, len(k)):
                if (k[j] == k[i])  or (k[j] == k[i] + (j - i))  or (k[j] == k[i] - (j - i)):
                    fitness += 1
                    break
            if fitness != 0: break
        # nếu tất cả phù hợp thì in kết quả
        if fitness == 0:
            result += 1
            for f1 in range(len(k)):
                for f2 in range(len(k)):
                    if f2 == k[f1]:
                        print('Q', end=' ')
                    else: print('.', end=' ')
                print('')
            print('---------------')
    if result == 0:
        print('Bài toán không có lời giải')
    else:
        print('Có tổng số lời giải là {0} (bao gồm đối xứng)'.format(result))


def Queen(N):
    # tạo bàn cờ
    # 1 0 0 0
    # 0 1 0 0
    # 0 0 1 0
    # 0 0 0 1
    # board = [0,1,2,3]
    board = numpy.arange(0,N)
    # hoán vị các vị trí quân trên bàn cờ
    l = list(itertools.permutations(board))
    # kiểm tra và in kết quả
    queens_check(l)


def main():
    N = int(input('Nhập số quân hậu: '))
    Queen(N)

if __name__ == "__main__": main()