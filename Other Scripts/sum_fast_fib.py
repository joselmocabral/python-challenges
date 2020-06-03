def perimeter(n):
    sum_fib = 2
    initial_state = [1, 1]
    if n > 1:
        for x in range(1,n):
            var = initial_state[0]
            initial_state[0] = initial_state[1]
            initial_state[1] = initial_state[0] + var
            sum_fib += initial_state[1]      
    return 4 * sum_fib