import random
import numpy as np
# author: Bùi Thành Được

# tạo lớp lưu các trạng thái tìm đường
class State:
    def __init__(self, route, distance, right):
        self.route = route # mảng lưu vết các thành phố
        self.right = right # biến trạng thái để biết đi đến đích chưa # Bucharest
        self.distance = distance # mảng lưu khoảng cách của từng đoạn đường giữa các thành phố

    # Tính khoảng cách từ điểm xuất phát đến đích
    def Cal_distance(self):
        if self.right == False: return 99999 # nếu không tìm đến đích thì không tính khoảng cách
        count = 0
        for i in self.distance:
            count += i
        return count

    # In ra quãng đường đi từ điểm xuất phát đến đích
    def Print_route(self, citylist):
        if self.right == False:
            print('not find path')
            return # nếu không tìm đến đích thì báo không tìm thấy đường đi

        for i in self.route:
            print(citylist[i], end=' ')

    # In ra mảng lưu khoảng cách giữa các thành phố đã đi qua
    def print_Distance(self):
        print(self.distance)


# thuật toán leo đồi
def hill_clibing(matrix, home, target):
    open = [] # mảng tạm đang xét
    close = [] # mảng lưu vết tìm đường
    distance = [0] # mảng lưu khoảng cách các thành phố đã đi
    right = False # biến kiểm tra xem đến đích chưa
    index = home # biến lưu thành phố cuối cùng đã đi qua
    close.append(index) # lưu thành phố bắt đầu đi
    if home == target: return State(close,distance,True)
    while True:
        # tìm các thành phố liền kề thành phố đang đứng cho vào mảng open
        for i in range(len(matrix)):
            if matrix[index][i] > 0:
                open.append(i)

        # xóa các thành phố đã đi qua trong mảng open
        for i in close:
            for j in open:
                if i == j:
                    open.remove(j)

        # nếu mảng open trống thì dừng lại
        if not open :break

        # chọn ngẫu nhiên 1 thành phố trong mảng open
        # lấy ra cho vào biến city
        city = random.choice(open)
        
        # lưu khoảng cách vào mảng distance
        distance.append(matrix[index][city])
        # lưu thành phố vào mảng close
        close.append(city)

        # di chuyển con trỏ đến thành phố vừa đến
        index = city

        # nếu thành phố vừa đến là đích cần tìm thì gắn cờ right = true và thoát vòng lặp
        if index == target:
            right = True
            break
        
        # xóa mảng open rồi lặp lại
        open.clear()
    
    # trả về quảng đường, khoảng cách và trạng thái đến đích
    return State(close, distance, right)

# hàm tối ưu thuật toán
def optimize(matrix, home, target, citylist):
    
    # đặt trạng thái tốt nhất là trạng thái đầu tiền
    best_state = hill_clibing(matrix, home, target)
    
    # dùng vòng lặp để tìm ra trạng thái tốt hơn
    for i in range(10000):
        state = hill_clibing(matrix, home, target)
        if state.Cal_distance() < best_state.Cal_distance():
            best_state = state

    # In kết quả
    best_state.Print_route(citylist)
    print('\ndistance ' + str(best_state.Cal_distance()))


def main():
    Matrix = np.zeros((13,13))
    Matrix[0][1] = 71
    Matrix[0][12] = 75
    Matrix[1][0] = 71
    Matrix[1][2] = 151
    Matrix[2][1] = 151
    Matrix[2][3] = 99
    Matrix[2][6] = 80
    Matrix[2][12] = 140
    Matrix[3][2] = 99
    Matrix[3][4] = 211
    Matrix[4][3] = 211
    Matrix[4][5] = 101
    Matrix[5][4] = 101
    Matrix[5][6] = 97
    Matrix[5][7] = 138
    Matrix[6][2] = 80
    Matrix[6][5] = 97
    Matrix[6][7] = 146
    Matrix[7][5] = 138
    Matrix[7][6] = 146
    Matrix[7][8] = 120
    Matrix[8][7] = 120
    Matrix[8][9] = 75
    Matrix[9][8] = 75
    Matrix[9][10] = 70
    Matrix[10][9] = 70
    Matrix[10][11] = 111
    Matrix[11][10] = 111
    Matrix[11][12] = 118
    Matrix[12][0] = 75
    Matrix[12][2] = 140
    Matrix[12][11] = 118
    citylist = ['Zerind','Oradea','Sibiu','Fagaras','Bucharest','Pitesti','Rimnicu Vilcea','Craiova','Drobeta','Mehahadia','Lugoj','Timisoara','Arad']
    # 0   Zerind
    # 1   Oradea
    # 2   Sibiu
    # 3   Fagaras
    # 4   Bucharest
    # 5   Pitesti
    # 6   Rimnicu Vilcea
    # 7   Craiova
    # 8   Drobeta
    # 9   Mehahadia
    # 10  Lugoj
    # 11  Timisoara
    # 12  Arad

    optimize(Matrix, 0, 4, citylist)


if __name__ == "__main__": main()