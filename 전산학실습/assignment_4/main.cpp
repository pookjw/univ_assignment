#include <iostream>

/*
 
 matrix
 Tested on macOS 10.14.1 Beta (18B50c), Xcode 10.1 beta 2 (10O35n)
 
 20182217 정보보안암호수학과 김진우
 some codes are copied from lecture_note_C_v20180917.pdf
 
 Usage:
 ./matrix [number]
 
 [number] means rows, cols of Square matrices. (REQUIRED)
 Square matrices will be automatically created.
 
 */

int** createMatrix(int ROWS, int COLS)
{
    int** A = NULL;
    A = (int**)malloc(sizeof(int*) * ROWS);
    if (A == NULL)
        return A;
    int r;
    for(r=0; r<COLS; r++)
    {
        *(A + r) = NULL;
        *(A + r) = (int*)malloc(sizeof(int) * COLS);
        if(*(A + r) == NULL)
        {
            A = NULL;
            return A; }
    }
    return A;
}

void defineMatrix(int** A, int VALUE, int ROWS, int COLS){
    *(*(A + ROWS) + COLS) = VALUE;
}

void showMatrix(int** A, int ROWS, int COLS)
{
    int r, c;
    for(r=0; r<ROWS; r++)
    {
        for(c=0; c<COLS; c++){
            if ( c == COLS - 1 ){ // the last 'space'
                printf("%2d", *(*(A + r) + c));
            }else{
                printf("%2d ", *(*(A + r) + c));
            }
        }
        printf("\n");
    }
}

void sumMatrix(int** A, int** B, int** C, int ROWS, int COLS){
    int r, c;
    for(r=0; r<ROWS; r++)
        for(c=0; c<COLS; c++)
            *(*(C + r) + c) = *(*(A + r) + c) + *(*(B + r) + c);
}

void subMatrix(int** A, int** B, int** D, int ROWS, int COLS){
    int r, c;
    for(r=0; r<ROWS; r++)
        for(c=0; c<COLS; c++)
            *(*(D + r) + c) = *(*(B + r) + c) - *(*(A + r) + c);
}

void mulMatrix(int** A, int** B, int** E, int A_ROWS, int A_COLS, int B_ROWS, int B_COLS){
    int a, b, c;
    int x, y;
    for(a=0; a<A_ROWS; a++){
        for (b=0; b<B_COLS; b++){
            for (c=0; c<A_COLS; c++){ // equal to `for (c=0; c<B_ROWS; c++){`.
                x = *(*(A + a) + c);
                y = *(*(B + c) + b);
                *(*(E + a) + b) = *(*(E + a) + b) + (x*y);
            }
        }
    }
}

void deleteMatrix(int*** A, int ROWS){
    if (*A == NULL)
        return;
    int r;
    for(r=0; r<ROWS; r++)
    {
        free(*(*A + r));
        *(*A + r) = NULL;
    }
    free(*A);
    *A = NULL;
}

int main(int argc, const char * argv[]) {
    // ./matrix []
    std::string a = argv[1];
    int n = atoi(argv[1]);
    
    int r, c;
    
    // Define A
    int A_ROWS = n;
    int A_COLS = n;
    int** A = NULL;
    A = createMatrix(A_ROWS, A_COLS);
    for(r=0; r<A_ROWS; r++)
        for(c=0; c<A_COLS; c++)
            defineMatrix(A, r+c, r, c);
    
    // Define B
    int B_ROWS = n;
    int B_COLS = n;
    int** B = NULL;
    B = createMatrix(B_ROWS, B_COLS);
    for(r=0; r<B_ROWS; r++)
        for(c=0; c<B_COLS; c++)
            defineMatrix(B, 6-(r+c), r, c);
    
    // Print A
    printf("Matrix of A:\n");
    showMatrix(A, A_ROWS, A_COLS);
    printf("\n");
    
    // Print B
    printf("Matrix of B:\n");
    showMatrix(B, B_ROWS, B_COLS);
    printf("\n");
    
    // Get A + B = C
    int C_ROWS = n;
    int C_COLS = n;
    int** C = NULL; // Define C
    C = createMatrix(C_ROWS, C_COLS); // Define C
    sumMatrix(A, B, C, C_ROWS, C_COLS);
    printf("Matrix of A + B:\n");
    showMatrix(C, C_ROWS, C_COLS);
    printf("\n");
    
    // Get B - A = D
    int D_ROWS = n;
    int D_COLS = n;
    int** D = NULL; // Define C
    D = createMatrix(D_ROWS, D_COLS); // Define C
    subMatrix(A, B, D, D_ROWS, D_COLS);
    printf("Matrix of B - A:\n");
    showMatrix(D, D_ROWS, D_COLS);
    printf("\n");
    
    // Get A * B = E
    int E_ROWS = n;
    int E_COLS = n;
    int** E = NULL; // Define C
    E = createMatrix(E_ROWS, E_COLS); // Define C
    for(r=0; r<E_ROWS; r++)
        for(c=0; c<E_COLS; c++)
            defineMatrix(E, 0, r, c); // Define all values as 0
    mulMatrix(A, B, E, A_ROWS, A_COLS, B_ROWS, B_COLS);
    printf("Matrix of A * B:\n");
    showMatrix(E, E_ROWS, E_COLS);
    printf("\n");
    
    // Delete A, B, C, D, E
    deleteMatrix(&A, A_ROWS);
    deleteMatrix(&B, B_ROWS);
    deleteMatrix(&C, C_ROWS);
    deleteMatrix(&D, D_ROWS);
    deleteMatrix(&E, E_ROWS);
    return 0;
}
