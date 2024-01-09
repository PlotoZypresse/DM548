def calculate_direct_mapped_cache_lines(cache_size, block_size):
    """
    Calculate the number of lines in a direct-mapped cache.

    Parameters:
    cache_size (int): Total size of the cache in bytes.
    block_size (int): Size of each block or line in the cache in bytes.

    Returns:
    int: Number of lines in the cache.
    """
    if block_size == 0:
        raise ValueError("Block size cannot be zero.")

    return cache_size // block_size

def calculate_n_way_cache_parameters(cache_size, block_size, n_way):
    """
    Calculate the number of sets and lines per set in an n-way set associative cache.

    Parameters:
    cache_size (int): Total size of the cache in bytes.
    block_size (int): Size of each block or line in the cache in bytes.
    n_way (int): The number of lines in each set (associativity of the cache).

    Returns:
    tuple: (number_of_sets, lines_per_set)
    """
    if block_size == 0 or n_way == 0:
        raise ValueError("Block size and n-way cannot be zero.")

    total_lines = cache_size // block_size
    number_of_sets = total_lines // n_way
    lines_per_set = n_way

    return number_of_sets, lines_per_set

def main():
    # User inputs for cache and block size
    cache_size = int(input("Enter the cache size in bytes: "))
    block_size = int(input("Enter the block size in bytes: "))

    # Direct-Mapped Cache Calculation
    direct_mapped_lines = calculate_direct_mapped_cache_lines(cache_size, block_size)
    print("Direct-Mapped Cache Lines:", direct_mapped_lines)

    # User input for n-way set associative cache
    n_way = int(input("Enter the level of associativity (n) for the n-way set associative cache: "))
    n_way_sets, lines_per_set = calculate_n_way_cache_parameters(cache_size, block_size, n_way)
    print("N-Way Set Associative Cache - Number of Sets:", n_way_sets, "Lines Per Set:", lines_per_set)

if __name__ == "__main__":
    main()

