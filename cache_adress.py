import math

def calculate_cache_address_format(address_size_bits, cache_size_bytes, block_size_bytes, associativity):
    """
    Calculate the tag, index, and block offset sizes for a cache.

    Parameters:
    address_size_bits (int): Size of the memory address in bits.
    cache_size_bytes (int): Total size of the cache in bytes.
    block_size_bytes (int): Size of each block or line in the cache in bytes.
    associativity (int): Level of associativity (1 for direct-mapped).

    Returns:
    tuple: (tag_size, index_size, block_offset_size)
    """
    if block_size_bytes == 0:
        raise ValueError("Block size cannot be zero.")

    # Calculate the number of blocks and the number of sets
    num_blocks = cache_size_bytes // block_size_bytes
    num_sets = num_blocks // associativity

    # Block offset size (in bits) is log2 of the block size
    block_offset_size = int(math.log2(block_size_bytes))

    # Index size (in bits) is log2 of the number of sets
    index_size = int(math.log2(num_sets))

    # Tag size is the remaining bits
    tag_size = address_size_bits - index_size - block_offset_size

    return tag_size, index_size, block_offset_size

def main():
    address_size_bits = int(input("Enter the total address size in bits: "))
    cache_size_bytes = int(input("Enter the cache size in bytes: "))
    block_size_bytes = int(input("Enter the block size in bytes: "))
    associativity = int(input("Enter the level of associativity (1 for direct-mapped): "))

    tag_size, index_size, block_offset_size = calculate_cache_address_format(
        address_size_bits, cache_size_bytes, block_size_bytes, associativity)

    print("\nCache Address Format Calculation:")
    print(f"Total Address Size: {address_size_bits} bits")
    print(f"Cache Size: {cache_size_bytes} bytes")
    print(f"Block Size: {block_size_bytes} bytes (also known as the 'Word Field' or 'Block Offset')")
    print(f"Associativity: {associativity}")

    print(f"\nTag Size: {tag_size} bits")
    print(f"Index Size: {index_size} bits (also called the 'Set Field')")
    print(f"Block Offset Size: {block_offset_size} bits (also known as the 'Word Field')")

    print("\nExplanation:")
    print("1. Tag Size: Calculated as the remaining bits after subtracting the index and block offset sizes from the total address size.")
    print("2. Index (Set Field) Size: Determines which set in the cache is used. Calculated as log2 of the number of sets.")
    print("3. Block Offset (Word Field) Size: Identifies the specific byte within a block. Calculated as log2 of the block size.")

if __name__ == "__main__":
    main()
