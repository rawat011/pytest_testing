def yield_with_ret():
    x = 5
    y = 6
    for i in range(x):
        yield i

    return y

gen = yield_with_ret()

while True:
    try:
        i = next(gen)
        print(f"Yielded: {i}")
    except StopIteration as e:
        print(f"Returned Value: {e.value}")
        break
