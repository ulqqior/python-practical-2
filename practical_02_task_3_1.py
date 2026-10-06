import sys
import timeit

def memory_comparison():
    sizes = [1_000, 10_000, 100_000, 1_000_000]
    
    print("=" * 60)
    print(f"{'N':>12} | {'list (байт)':>14} | {'gen (байт)':>12} | {'Ratio':>8}")
    print("-" * 60)
    
    for n in sizes:
        data_list = [x**2 for x in range(n)]
        data_gen = (x**2 for x in range(n))
        
        list_size = sys.getsizeof(data_list)
        gen_size = sys.getsizeof(data_gen)
        
        print(f"{n:>12,} | {list_size:>14,} | {gen_size:>12,} | {list_size / gen_size:>7.0f}x")
    print("=" * 60)

def performance_comparison():
    n = 500_000
    
    time_list = timeit.timeit(
        lambda: sum([x ** 2 for x in range(n)]),
        number=5,
    )
    
    time_gen = timeit.timeit(
        lambda: sum((x ** 2 for x in range(n))),
        number=5,
    )
    
    print(f"\nsum() для {n:,} елементів (середнє з 5 запусків):")
    print(f" list comprehension: {time_list:.4f} c")
    print(f" generator expression: {time_gen:.4f} c")
    faster = "list" if time_list < time_gen else "generator"
    print(f" Швидше: {faster}")

def practical_usage():
    words = [
        "Python", "ітератор", "генератор", "yield", "comprehension",
        "дані", "пам'ять", "ефективність", "конвеєр", "ліниві",
        "обчислення", "протокол", "об'єкт", "клас", "функція",
    ]
    
    longest = max(words, key=lambda w: len(w))
    print(f"\nНайдовше слово: '{longest}' ({len(longest)} символів)")
    
    all_nonempty = all(len(w) > 0 for w in words)
    print(f"Всі слова непорожні: {all_nonempty}")
    
    has_long = any(len(w) > 15 for w in words)
    print(f"Є слово > 15 символів: {has_long}")
    
    csv_line = ",".join(w for w in words)
    print(f"CSV: {csv_line}")
    
    total_length = sum(len(w) for w in words)
    print(f"Сума довжин: {total_length}")
    
    word_lengths = {w: len(w) for w in words}
    print(f"Довжини: {word_lengths}")
    
    even_squares_sum = sum(x**2 for x in range(1, 101) if x % 2 == 0)
    print(f"\nСума квадратів парних від 1 до 100: {even_squares_sum}")

def main():
    print(">>> Порівняння використання пам'яті <<<")
    memory_comparison()
    print("\n>>> Порівняння продуктивності <<<")
    performance_comparison()
    print("\n>>> Практичні приклади <<<")
    practical_usage()

if __name__ == "__main__":
    main()