def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

# Generate Fibonacci series up to the 10th number
fib_series = fibonacci(10)

# Display the results
for i, num in enumerate(fib_series):
    print(f"Fibonacci number {i}: {num}")

# Save the results to a file
with open("output_fibonacci.txt", "w") as f:
    for i, num in enumerate(fib_series):
        f.write(f"Fibonacci number {i}: {num}\n")