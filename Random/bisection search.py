import time
begin = time.time()
def bisection_search(n):
    low = 0
    high = 1000
    guess = int(low + high / 2)
    count_guesses = 1
    while guess != n:
        if n > guess:
            low = guess
        else:
            high = guess
        guess = int((low + high) / 2)
        count_guesses += 1
    print(guess,"-->", count_guesses)
    return(count_guesses)

lst = list()
for i in range(1000):
    lst.append(bisection_search(i))
    print(lst[i])

print(lst, len(lst))
for i in range(1, 16):
    print(i, "-->", lst.count(i))

time.sleep(0)
end = time.time()

print(f"Total runtime is {end - begin}")