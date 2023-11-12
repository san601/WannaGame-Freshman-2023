use std::io;
use std::io::BufRead;

const MATRIX_SIZE: usize = 8;

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

fn create_matrix_from_string(input: &str) -> [[u32; MATRIX_SIZE]; MATRIX_SIZE] {
    let mut matrix: [[u32; MATRIX_SIZE]; MATRIX_SIZE] = [[0; MATRIX_SIZE]; MATRIX_SIZE];

    let bytes = input.as_bytes();
    let mut index = 0;

    for i in 0..MATRIX_SIZE {
        for j in 0..MATRIX_SIZE {
            let value = if index < bytes.len() {
                bytes[index] as u32
            } else {
                0
            };

            matrix[i][j] = value;
            index += 1;
        }
    }

    matrix
}

fn multiply_matrix(matrix1: &[[u32; MATRIX_SIZE]; MATRIX_SIZE], matrix2: &[[u32; MATRIX_SIZE]; MATRIX_SIZE]) -> [[u32; MATRIX_SIZE]; MATRIX_SIZE] {
    let mut result: [[u32; MATRIX_SIZE]; MATRIX_SIZE] = [[0; MATRIX_SIZE]; MATRIX_SIZE];

    for i in 0..MATRIX_SIZE {
        for j in 0..MATRIX_SIZE {
            for k in 0..MATRIX_SIZE {
                result[i][j] += matrix1[i][k] * matrix2[k][j];
            }
        }
    }

    result
}

fn is_equal(matrix1: &[[u32; MATRIX_SIZE]; MATRIX_SIZE], matrix2: &[[u32; MATRIX_SIZE]; MATRIX_SIZE]) -> bool {
    for i in 0..MATRIX_SIZE {
        for j in 0..MATRIX_SIZE {
            if matrix1[i][j] != matrix2[i][j] {
                return false;
            }
        }
    }

    true
}

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