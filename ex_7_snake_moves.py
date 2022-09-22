rows, cols = [int(x) for x in input().split()]
snake_word = input()

index = 0
matrix_snake = []
for i in range(rows):
    matrix_snake.append([])

    for j in range(cols):
        if i % 2 == 0:
            matrix_snake[i].append(snake_word[index % len(snake_word)])


        else:
            matrix_snake[i].append(snake_word[index % len(snake_word)])
        index = index + 1

for i in range(len(matrix_snake)):
    if i % 2 != 0:
        matrix_snake[i].reverse()
    print(''.join(matrix_snake[i]))
