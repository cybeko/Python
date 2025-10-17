methods = (
    lambda n: sum(n) / len(n),
    lambda n: (n[0] * n[1] * n[2] * n[3]) ** 0.25,
    lambda n: len(n) / sum(1 / x for x in n)
)

data = (1, 2, 3, 4)

def get_max_method(data, methods):
    results = [method(data) for method in methods]
    return results 

all_results = get_max_method(data, methods)

print("Method results:", all_results)
print("Max Result:", max(all_results))
