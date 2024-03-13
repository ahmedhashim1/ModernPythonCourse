from collections.abc import Iterator


def my_range(start: int, end: int, step: int = 1) -> Iterator[int]:
    for i in range(start, end + 1, step):
        yield i


a: Iterator[int] = my_range(1, 10)
print(next(a))
print(next(a))
print(next(a))

print(type(a))
