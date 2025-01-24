import random
import math


# Визначення функції Сфери
def sphere_function(x):
    return sum(xi**2 for xi in x)


# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    dimension = len(bounds)
    current_solution = [
        random.uniform(bounds[i][0], bounds[i][1]) for i in range(dimension)
    ]
    step_size_max = max([abs(bounds[i][0] - bounds[i][1]) for i in range(dimension)])
    current_value = func(current_solution)
    iter_count = 0
    for iter_num in range(iterations):
        iter_count += 1
        step_size = step_size_max / (iter_num + 1)  # Динамічне зменшення кроку
        neighbor = [
            max(
                min(
                    current_solution[i] + random.uniform(-step_size, step_size),
                    bounds[i][1],
                ),
                bounds[i][0],
            )
            for i in range(dimension)
        ]

        neighbor_value = func(neighbor)

        if iter_num > 2 and abs(neighbor_value - current_value) < epsilon:
            break

        if neighbor_value < current_value:
            current_solution, current_value = neighbor, neighbor_value

    print("Кількість ітерацій:", iter_count)
    return current_solution, current_value


# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    dimension = len(bounds)
    best_solution = [
        random.uniform(bounds[i][0], bounds[i][1]) for i in range(dimension)
    ]
    best_value = func(best_solution)
    iter_count = 0

    for _ in range(iterations):
        iter_count += 1

        candidate = [
            random.uniform(bounds[i][0], bounds[i][1]) for i in range(dimension)
        ]
        candidate_value = func(candidate)
        if abs(candidate_value - best_value) < epsilon:
            break
        if candidate_value < best_value:
            best_solution, best_value = candidate, candidate_value

    print("Кількість ітерацій:", iter_count)
    return best_solution, best_value


# Simulated Annealing
def simulated_annealing(
    func, bounds, iterations=1000, temp=1000, cooling_rate=0.99, epsilon=1e-6
):
    dimension = len(bounds)
    current_solution = [
        random.uniform(bounds[i][0], bounds[i][1]) for i in range(dimension)
    ]
    current_value = func(current_solution)
    best_solution, best_value = current_solution, current_value
    iter_count = 0
    step_size_max = max([abs(bounds[i][0] - bounds[i][1]) for i in range(dimension)])

    for iter_num in range(iterations):
        iter_count += 1
        # step_size = epsilon  # Крок фіксований
        step_size = step_size_max / (iter_num + 1)  # Динамічне зменшення кроку
        neighbor = [
            max(
                min(
                    current_solution[i] + random.uniform(-step_size, step_size),
                    bounds[i][1],
                ),
                bounds[i][0],
            )
            for i in range(dimension)
        ]
        neighbor_value = func(neighbor)

        # print(
        #     "Т:",
        #     round(temp, 4),
        #     "Сусід:",
        #     neighbor,
        #     "Значення:",
        #     round(current_value, 2),
        #     "Нове значення:",
        #     round(neighbor_value, 2),
        #     "Найкраще значення:",
        #     round(best_value, 2),
        # )

        if neighbor_value < current_value or random.random() < math.exp(
            (current_value - neighbor_value) / temp
        ):
            current_solution, current_value = neighbor, neighbor_value

        if current_value < best_value:
            best_solution, best_value = current_solution, current_value

        temp *= cooling_rate

        # Causes unaccurate results because of low fixed itteration count
        if temp < epsilon:
            break
    print("Кількість ітерацій:", iter_count)
    return best_solution, best_value


if __name__ == "__main__":
    # Межі для функції
    bounds = [(-5, 5), (-5, 5)]
    iterations_count = 10000

    # Виконання алгоритмів
    print("\nHill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds, iterations_count)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(
        sphere_function, bounds, iterations_count
    )
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(
        sphere_function, bounds, iterations_count
    )
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
