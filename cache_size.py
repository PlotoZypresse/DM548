def calculate_cache_size(num_sets, block_size, associativity):
    """
    Calculate the cache size.

    Parameters:
    num_sets (int): Number of sets in the cache.
    block_size (int): Size of each block or line in the cache in bytes.
    associativity (int): Level of associativity (1 for direct-mapped).

    Returns:
    int: Cache size in bytes.
    """
    return num_sets * block_size * associativity

def main():
    num_sets = int(input("Enter the number of sets in the cache: "))
    block_size = int(input("Enter the block size in bytes: "))
    associativity = int(input("Enter the level of associativity (1 for direct-mapped): "))

    cache_size = calculate_cache_size(num_sets, block_size, associativity)

    print("\nCache Size Calculation:")
    print(f"Number of Sets: {num_sets}")
    print(f"Block Size: {block_size} bytes")
    print(f"Associativity: {associativity}")

    print("\nThe cache size is calculated as follows:")
    print(f"Cache Size = Number of Sets x Block Size x Associativity")
    print(f"Cache Size = {num_sets} x {block_size} x {associativity} = {cache_size} bytes")

if __name__ == "__main__":
    main()
