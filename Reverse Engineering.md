# WannaGame Freshman 2023
## YOUR CHOICE

Level: hard

Description: All choices are yours

Author: Okoonzz

[chall](https://cnsc.uit.edu.vn/ctf/files/eaa4690e4341165c8bd8864b6097ea32/rev01?token=eyJ1c2VyX2lkIjo4NTksInRlYW1faWQiOm51bGwsImZpbGVfaWQiOjE3Mn0.ZVBVgA.s1uKlf_9v0L_8BV6NLwj6Ofkuj4)


Đây là một bài khá hay và khó đối với newbie như mình. Mình cũng không kịp làm trong thời gian của giải mặc dù được mấy anh cho hint khá nhiều. Anyway đây là write up chi tiết cho bài này và khuyến khích các bạn tự thử làm trước.

### Solution

Sau khi chạy thử chương trình, mình thấy rằng chương trình sẽ cho nhập vào 5 giá trị theo format (00-47). Tức là với số hàng chục thì từ 0-4, hàng đơn vị từ 0-7.

![image](https://hackmd.io/_uploads/HybjqCam6.png)

Dùng IDA mở lên xem thử thì thấy được đây là đoạn code nhập và kiểm tra input.

![image](https://hackmd.io/_uploads/ByUP0ATQa.png)

Dòng code được đánh dấu được dùng để set cái gì đó về 1.

Kiểm tra tiếp tục đoạn code tiếp theo, có vẻ như đây là đoạn code check 5 số input thỏa điều kiện và in ra flag. 

![image](https://hackmd.io/_uploads/Hy_a0C6m6.png)


Ở đây có thể thấy biến v16 và hàm sub_1369 là nơi kiểm tra điều kiện. Tiếp tục đọc code từ hàm sub_1369.

![image](https://hackmd.io/_uploads/BkrDJJRQ6.png)

Với một chút suy luận và hint từ ban tổ chức, có thể thấy đây là một bài toán đặt 8 quân hậu lên bàn cờ vua 64 ô. Tuy nhiên đề bài chỉ cho input 5 vị trí, có lẽ là vị trí 5 quân hậu sao cho thỏa điều kiện không có quân nào ăn được quân nào. Mình thử vẽ ra excel thì thấy rằng chỉ được nhập vào vị trí từ hàng 4 trở lên.

![image](https://hackmd.io/_uploads/Byv7GyRQ6.png)

Như vậy có thể suy ra được rằng sẽ có 3 quân hậu được đặt tại 3 dòng cuối và nhiệm vụ của mình là phải tìm được vị trí đặt 3 quân đấy và nhập vào chương trình vị trí của quân hậu ở 5 dòng còn lại.

Quay lại với đoạn code check input bên trên, để ý sẽ thấy có hàm sub_21A8 và hàm sub_21D6 làm nhiệm vụ kiểm tra tại vị trí i và j xem có quân hậu ở đó hay không. Input để check là a1.

![image](https://hackmd.io/_uploads/r1DbNJRm6.png)

Như vậy có thể xác định được vị trí của bàn cờ vua trong stack dựa vào a1. Mình quay lại hàm main để xem và xác định được v37 là nơi cần tìm trong stack.

![image](https://hackmd.io/_uploads/HkHRVkA7p.png)


Tiếp theo mình dùng Ghidra để xác định địa chỉ của dòng code trên. 

Cho bạn nào chưa biết cách dùng Ghidra để xác định địa chỉ của instruction thì các bạn vào GDB -> starti -> vmmap và copy địa chỉ ở khu vực Start

![image](https://hackmd.io/_uploads/Sk4PUy0QT.png)

Sau đó vào Ghidra chọn Window -> Memory map -> Set Image Base (house icon) và paste địa chỉ vừa copy sang.

![image](https://hackmd.io/_uploads/r1w2I1CQT.png)

Quay lại với challenge, sau khi xác định và copy được địa chỉ, mình vào gdb để set breakpoint ngay tại vị trí đó để lấy tham số được truyền vào function, tức là register RDI.

![image](https://hackmd.io/_uploads/S177rJRXa.png)

Sau khi chương trình chạm breakpoint, mình kiểm tra khoảng 80 dòng tiếp theo trong stack để tránh sót bất cứ ô nào.

![image](https://hackmd.io/_uploads/BkqOwJRQ6.png)

Như vậy các ô nhớ mà tại điểm đó có số 1 thay vì 0 chính là quân hậu được đặt sẵn. Từ stack có thể suy ra dược bàn cờ vua lúc đầu như sau:

![image](https://hackmd.io/_uploads/r1LCwk0Qp.png)


### Code

```python=1
# code to solve 8 queens problem
def is_safe(board, row, col):
    if 1 in board[row]:
        return False

    if 1 in [board[i][col] for i in range(8)]:
        return False

    for i in range(8):
        for j in range(8):
            if board[i][j] == 1 and abs(row - i) == abs(col - j):
                return False

    return True

def solve(board, row):
    if row == 5:
        print_solution(board)
        return

    for col in range(8):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve(board, row + 1)
            board[row][col] = 0

def print_solution(board):
    for i in range(5):
        for j in range(8):
            if (initial_board[i][j] == 1):
                print(str(i) + str(j), end=' ')

# Given initial board
initial_board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
]

# Start solving from row 0 to row 4
solve(initial_board, 0)
```

Chạy code mình thu được dãy 5 số là vị trí của 5 quân hậu cần tìm.


```output=
04 12 27 33 46 
```

Thử chạy chương trình và nhập vào thì thu được flag:

![image](https://hackmd.io/_uploads/BJ9enRaQp.png)

Mặc dù giải lần này đề khá khó so với freshman nhưng mình cũng đã học được khá nhiều thứ. Hi vọng các bạn cũng sẽ học được gì đó từ challenge này. Thanks for reading.