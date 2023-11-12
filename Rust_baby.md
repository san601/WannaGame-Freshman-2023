# WannaGame
## RUST BABY

Level: medium

Description: A baby rust challenge for you to warmup

Author: dream

[chall](https://cnsc.uit.edu.vn/ctf/files/43b4b85f6a4d1aea6dd0a82268aa6ef7/chall.rs?token=eyJ1c2VyX2lkIjo4NTksInRlYW1faWQiOm51bGwsImZpbGVfaWQiOjE2OH0.ZVDgWg.Wipge7Z5SxImNhPRsghIeKV2o_k)

### Solution

Let's examine the main function in that Rust file

```rust=
fn main() {
    println!("Simple flagchecker");
    println!("What is the flag?");

    let stdin = io::stdin();
    let input = stdin.lock().lines().next().unwrap().unwrap();
    
    let matrix = create_matrix_from_string(&input);
    let result = multiply_matrix(&matrix, &get_predefined());

    if is_equal(&result, &get_result()) {
        println!("The flag is correct!");
    } else {
        println!("The flag is incorrect!");
    }
}
```

It can be seen that our input will be convert to a matrix of number and mulptiply with a predefined matrix.

The predefined matrix:

```rust=
fn get_predefined() -> [[u32; MATRIX_SIZE]; MATRIX_SIZE] {
    [
        [1, 3, 3, 7, 3, 3, 7, 3],
        [3, 3, 7, 3, 3, 7, 3, 1],
        [3, 7, 3, 3, 7, 3, 1, 3],
        [7, 3, 3, 7, 3, 1, 3, 3],
        [3, 3, 7, 3, 1, 3, 3, 7],
        [3, 7, 3, 1, 3, 3, 7, 3],
        [7, 3, 1, 3, 3, 7, 3, 3],
        [3, 1, 3, 3, 7, 3, 3, 7],
    ]
}
```

The result matrix:
```rust=
fn get_result() -> [[u32; MATRIX_SIZE]; MATRIX_SIZE] {
    [
        [2914, 3090, 2760, 2742, 2966, 2840, 2890, 3078],
        [3184, 3232, 3126, 3110, 3172, 3128, 3132, 3176],
        [3041, 3053, 3039, 2997, 3057, 3057, 2987, 3039],
        [3122, 3054, 3048, 3102, 3050, 3064, 3038, 3002],
        [3119, 3151, 3233, 3159, 3169, 3155, 3245, 3239],
        [3282, 3110, 3214, 3256, 3186, 3204, 3188, 3300],
        [3003, 3043, 2931, 2941, 3137, 3067, 3041, 2927],
        [2296, 2202, 2434, 2722, 2754, 2280, 2286, 2346],
    ]
}
```

Our task is to find a matrix so that when it multiply with the predefined matrix, the result is the other matrix. 

We know that:

A * B = X <=> A = X * B^-1

So our task is to calculate X * B^-1 with B is the predefined matrix and X is the result matrix.

Last step, our task is to find matrix A and convert it to ascii characters.

### Code

```python=
import numpy as np
B = np.array([
        [1, 3, 3, 7, 3, 3, 7, 3],
        [3, 3, 7, 3, 3, 7, 3, 1],
        [3, 7, 3, 3, 7, 3, 1, 3],
        [7, 3, 3, 7, 3, 1, 3, 3],
        [3, 3, 7, 3, 1, 3, 3, 7],
        [3, 7, 3, 1, 3, 3, 7, 3],
        [7, 3, 1, 3, 3, 7, 3, 3],
        [3, 1, 3, 3, 7, 3, 3, 7],
    ])
X = np.array([
        [2914, 3090, 2760, 2742, 2966, 2840, 2890, 3078],
        [3184, 3232, 3126, 3110, 3172, 3128, 3132, 3176],
        [3041, 3053, 3039, 2997, 3057, 3057, 2987, 3039],
        [3122, 3054, 3048, 3102, 3050, 3064, 3038, 3002],
        [3119, 3151, 3233, 3159, 3169, 3155, 3245, 3239],
        [3282, 3110, 3214, 3256, 3186, 3204, 3188, 3300],
        [3003, 3043, 2931, 2941, 3137, 3067, 3041, 2927],
        [2296, 2202, 2434, 2722, 2754, 2280, 2286, 2346],
    ])
A = np.matmul(X, np.linalg.inv(B))

for i in range(8):
        for j in range(8):
                print(chr(round(A[i][j])), end='')
```

And we got our flag:
```W1{Just_a_simple_flagchecker_chall_for_the_start_of_Freshman!!!}```
