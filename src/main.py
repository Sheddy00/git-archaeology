# Main module
def greet(name: str) -> str:
    return f"Hello, {name}!"

def compute(x: int, y: int) -> int:
    return x * y + (x - y)

if __name__ == "__main__":
    print(greet("World"))
    print(compute(6, 7))
# 1777225435
