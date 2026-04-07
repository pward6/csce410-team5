"""
Shakespeare Compression Test

Converts Shakespeare dataset to a posting list and compresses with vByte.
"""

from utils.posting_list import text_to_posting_list
from compression.vByte import PostingListCompressor


def main():
    # Read the Shakespeare text
    print("Reading Shakespeare text...")
    with open("data/t8.shakespeare.txt", "r", encoding="utf-8") as f:
        text = f.read()

    # Convert to posting list
    print("Converting to posting list...")
    posting_list = text_to_posting_list(text, doc_id=1)

    # Compress with vByte
    print("Compressing with vByte...")
    compressor = PostingListCompressor()
    compressed = compressor.compress_posting_list(posting_list, use_gaps=True)
    
    # Get compression ratio
    ratio = compressor.get_compression_ratio(posting_list, compressed)
    
    # Calculate statistics
    total_positions = sum(
        len(positions)
        for doc_pos in posting_list.values()
        for positions in doc_pos.values()
    )
    original_bytes = total_positions * 4
    compressed_bytes = sum(
        len(b) for term_bytes in compressed.values()
        for b in term_bytes.values()
    )

    # Verify decompression works
    decompressed = compressor.decompress_posting_list(compressed, use_gaps=True)
    match = posting_list == decompressed

    # Print results
    print("\n" + "=" * 70)
    print("vByte Compression Results - Shakespeare Text")
    print("=" * 70)
    print(f"Text size: {len(text)} characters")
    print(f"Words: {len(text.split())}")
    print(f"Unique terms: {len(posting_list)}")
    print(f"Total positions: {total_positions}")
    print(f"\nOriginal size: {original_bytes:,} bytes")
    print(f"Compressed size: {compressed_bytes:,} bytes")
    print(f"Compression ratio: {ratio:.4f}")
    print(f"Size reduction: {100 * (1 - ratio):.1f}%")
    print(f"Decompression verified: {match}")
    print("=" * 70)


if __name__ == "__main__":
    main()
