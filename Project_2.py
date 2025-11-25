import matplotlib.pyplot as plt
import gzip
import sys

# --- CONFIGURATION ---
REF_FILE = "reference.hist"
QUERY_FILE = "query.bed.gz"
OUTPUT_FILE = "query.rescaled.bed"

def get_frequencies(filename, is_gzip=False, file_type="bed"):
    """
    Reads a file and returns a dictionary of lengths and their normalized frequencies.
    Handles 'smart counting' for messy BED files.
    """
    print(f"Reading {filename}...")

    counts = {}
    total_count = 0

    try:
        # Open with gzip or normal open
        if is_gzip:
            f = gzip.open(filename, "rt")
        else:
            f = open(filename, "r")

        with f:
            for line in f:
                # Skip empty lines or headers
                if not line.strip() or line.startswith("#") or line.startswith("track"):
                    continue

                parts = line.split() # Split by whitespace/tabs

                try:
                    if file_type == "hist":
                        # FORMAT: Length <space> Probability
                        # This file is ALREADY a probability distribution.
                        length = int(parts[0])
                        prob = float(parts[1])
                        counts[length] = prob
                        total_count = 1 # Dummy value so we don't normalize twice

                    else:
                        # FORMAT: BED file
                        # We need to count the occurrences of each length
                        length = None

                        # --- SMART COUNTING LOGIC (Same as your main script) ---
                        try:
                            # Try column 3 (index 3)
                            length = int(parts[3])
                        except (ValueError, IndexError):
                            try:
                                # Try column 4 (index 4) if col 3 failed
                                length = int(parts[4])
                            except (ValueError, IndexError):
                                continue # Skip bad line

                        if length is not None:
                            counts[length] = counts.get(length, 0) + 1
                            total_count += 1

                except (ValueError, IndexError):
                    continue

    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return {}, 0

    # Normalize counts to frequencies (if it was a BED file)
    frequencies = {}
    if file_type == "bed" and total_count > 0:
        for length, count in counts.items():
            frequencies[length] = count / total_count
    else:
        frequencies = counts # Already normalized

    return frequencies, total_count

# --- MAIN EXECUTION ---

# 1. Read all three files
#    Reference is a histogram file
ref_freqs, _ = get_frequencies(REF_FILE, is_gzip=False, file_type="hist")

#    Query is a gzipped BED file
query_freqs, query_total = get_frequencies(QUERY_FILE, is_gzip=True, file_type="bed")

#    Output is a normal BED file
out_freqs, out_total = get_frequencies(OUTPUT_FILE, is_gzip=False, file_type="bed")


# 2. Prepare data for plotting (sorting X axis)
def prepare_plot_data(freq_dict):
    x = sorted(freq_dict.keys())
    y = [freq_dict[k] for k in x]
    return x, y

ref_x, ref_y = prepare_plot_data(ref_freqs)
query_x, query_y = prepare_plot_data(query_freqs)
out_x, out_y = prepare_plot_data(out_freqs)


# 3. Create the Plot
print("Generating plot...")
plt.figure(figsize=(12, 6))

# Plot Reference (Green Line)
plt.plot(ref_x, ref_y, color='green', label='Reference', linewidth=2, alpha=0.8)

# Plot Original Query (Purple Line)
plt.plot(query_x, query_y, color='purple', label=f'Original Query (n={query_total:,})', linewidth=1.5, alpha=0.7)

# Plot Rescaled Output (Blue Stars)
# We use a scatter plot for the stars so they stand out
plt.scatter(out_x, out_y, color='skyblue', label=f'Rescaled Output (n={out_total:,})', marker='*', s=40, zorder=5)

# Formatting the graph
plt.title("Fragment Length Distribution: Rescaling Results", fontsize=14)
plt.xlabel("Fragment Length (bp)", fontsize=12)
plt.ylabel("Normalized Frequency", fontsize=12)
plt.xlim(0, 700) # Limit x-axis to 700 like the example
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

# Save the plot
output_image = "final_result_plot.png"
plt.savefig(output_image, dpi=300)
print(f"Done! Plot saved to '{output_image}'")

# plt.show() # Uncomment this if you are running locally and want to see the window