# WannaGame Freshman 2023
## YOUR CHOICE

Level: hard

Description: All choices are yours

Author: Okoonzz

[chall](https://cnsc.uit.edu.vn/ctf/files/eaa4690e4341165c8bd8864b6097ea32/rev01?token=eyJ1c2VyX2lkIjo4NTksInRlYW1faWQiOm51bGwsImZpbGVfaWQiOjE3Mn0.ZVBVgA.s1uKlf_9v0L_8BV6NLwj6Ofkuj4)

This challenge is actually quite hard and fun for me. I wasn't have enough time to solve this in the contest eventhough there was a ton of hint for me. Anyway, this is my attempt to make a writeup for this challenge, hope you guys enjoy it.

### Solution

After running the file, we know that the program allows 5 inputs in the format of (00-47), which means the first digit cannot exceed 4 and the second digit cannot exceed 7. This can be the first hint for us.

![image](https://hackmd.io/_uploads/HybjqCam6.png)

Using IDA, the part where it get and check input is shown:

![image](https://hackmd.io/_uploads/ByUP0ATQa.png)

The highlighted row might set something to 1. This is our second hint.

Continue checking, this might be the part of code where the program checks 5 input with some constraints and print the flag if correct.

![image](https://hackmd.io/_uploads/Hy_a0C6m6.png)

We can see v16 and sub_1369 are the place where the program checking our input. Continue surfing through sub_1369.

![image](https://hackmd.io/_uploads/BkrDJJRQ6.png)

With some observation and hints, we can see that this is the code to solve [the 8 queens puzzle](http://www.datagenetics.com/blog/august42012/). However, the program only takes 5 parameters as input and if we draw this in MS Excel, it is clear that we can't input any position at the last 3 rows. 

![image](https://hackmd.io/_uploads/Byv7GyRQ6.png)

This might be the indicator that there are 3 queens that was placed at the last 3 rows and our task is to find those queens' position and provide the other 5 queens' position as input.


Back to the code, we can see that sub_21A8 and sub_21D5 use a1 as input to check if there is any queen at position (i, j)

![image](https://hackmd.io/_uploads/r1DbNJRm6.png)

Như vậy có thể xác định được vị trí của bàn cờ vua trong stack dựa vào a1. Mình quay lại hàm main để xem và xác định được v37 là nơi cần tìm trong stack.
It is clear that we can use a1 to find the initial board with 3 queens on the stack. Let's get back to main function and there we go, v37 is what we need.

![image](https://hackmd.io/_uploads/HkHRVkA7p.png)

Next, I'll use Ghidra to get the exact address of those line of code so that we can use to set some breakpoints later.

For those who don't know how to use Ghidra to get the address of some instructions, you guys can go to GDB -> starti -> vmmap and copy the first address at Start section.

![image](https://hackmd.io/_uploads/Sk4PUy0QT.png)

Then use Ghidra, select Window -> Memory map -> Set Image Base (house icon) and paste that address into.

![image](https://hackmd.io/_uploads/r1w2I1CQT.png)

Back to the challenge, after knowing the exact address, use GDB to set a breakpoint at that address to get the parameter to the call, which is RDI register.

![image](https://hackmd.io/_uploads/S177rJRXa.png)

Examine about 80 next address in the stack so that nothing on the board is left.

![image](https://hackmd.io/_uploads/BkqOwJRQ6.png)

We can infer to the original board with ones mean there are queens on the position and zeros mean empty positions.

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

Output:


```output=
04 12 27 33 46 
```

And we got our flag:

![image](https://hackmd.io/_uploads/BJ9enRaQp.png)

Eventhough this challenge is quite hard for freshers but I have learnt a lot. Hope you guys like this writeup. Thanks for reading.

