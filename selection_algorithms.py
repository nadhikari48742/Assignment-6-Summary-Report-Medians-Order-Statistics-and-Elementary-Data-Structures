import random
import time


def partition(arr, pivot):
    less = []
    equal = []
    greater = []

    for value in arr:
        if value < pivot:
            less.append(value)
        elif value > pivot:
            greater.append(value)
        else:
            equal.append(value)

    return less, equal, greater


def randomized_quickselect(arr, k):
    """
    Returns the k-th smallest element in arr.
    k is 1-based.
    """
    if not arr:
        raise ValueError("Array is empty.")
    if k < 1 or k > len(arr):
        raise ValueError("k is out of range.")

    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    less, equal, greater = partition(arr, pivot)

    if k <= len(less):
        return randomized_quickselect(less, k)
    elif k <= len(less) + len(equal):
        return pivot
    else:
        return randomized_quickselect(greater, k - len(less) - len(equal))


def median_of_medians(arr):
    """
    Finds a good pivot using the Median of Medians method.
    """
    if len(arr) <= 5:
        return sorted(arr)[len(arr) // 2]

    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = []

    for group in groups:
        sorted_group = sorted(group)
        medians.append(sorted_group[len(sorted_group) // 2])

    return deterministic_select(medians, (len(medians) + 1) // 2)


def deterministic_select(arr, k):
    """
    Returns the k-th smallest element in arr using
    Median of Medians.
    k is 1-based.
    """
    if not arr:
        raise ValueError("Array is empty.")
    if k < 1 or k > len(arr):
        raise ValueError("k is out of range.")

    if len(arr) <= 5:
        return sorted(arr)[k - 1]

    pivot = median_of_medians(arr)
    less, equal, greater = partition(arr, pivot)

    if k <= len(less):
        return deterministic_select(less, k)
    elif k <= len(less) + len(equal):
        return pivot
    else:
        return deterministic_select(greater, k - len(less) - len(equal))


def generate_random_array(size):
    return [random.randint(1, 100000) for _ in range(size)]


def generate_sorted_array(size):
    return list(range(1, size + 1))


def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))


def test_algorithm(algorithm, arr, k):
    start = time.perf_counter()
    result = algorithm(arr, k)
    end = time.perf_counter()
    return result, end - start


def empirical_analysis():
    sizes = [100, 500, 1000, 2000]

    print("EMPIRICAL ANALYSIS")
    print("=" * 60)

    for size in sizes:
        print(f"\nInput Size: {size}")

        test_cases = {
            "Random": generate_random_array(size),
            "Sorted": generate_sorted_array(size),
            "Reverse Sorted": generate_reverse_sorted_array(size)
        }

        k = size // 2

        for case_name, arr in test_cases.items():
            arr_copy_1 = arr[:]
            arr_copy_2 = arr[:]

            det_result, det_time = test_algorithm(deterministic_select, arr_copy_1, k)
            rand_result, rand_time = test_algorithm(randomized_quickselect, arr_copy_2, k)

            print(f"{case_name}:")
            print(f"  Deterministic Select -> Result: {det_result}, Time: {det_time:.6f} seconds")
            print(f"  Randomized Quickselect -> Result: {rand_result}, Time: {rand_time:.6f} seconds")


def main():
    sample = [12, 3, 5, 7, 4, 19, 26, 3, 7]
    k = 4

    print("Sample Array:", sample)
    print(f"{k}-th smallest using Deterministic Select:", deterministic_select(sample, k))
    print(f"{k}-th smallest using Randomized Quickselect:", randomized_quickselect(sample, k))

    print("\n")
    empirical_analysis()


if __name__ == "__main__":
    main()