Project 2 Verification: Plotting Results

Goal: Visually verify the success of the rescaling pipeline by generating a comparative plot. This script reads the original data, the reference target, and your final output, plotting them together to confirm that the output matches the target distribution.

🚀 Features

Smart Parsing: Automatically handles BED files with inconsistent column formatting (e.g., read names in column 3 vs. 4).

Multi-Format Support: Reads both plain text histograms (.hist) and compressed BED files (.bed.gz).

Publication-Ready Visualization: Generates a high-quality PNG graph with proper labels, legends, and styling.

📂 File Structure

File

Description

plot_results.py

The Python script that calculates frequencies and generates the plot.

reference.hist

Input: The target distribution (Green Line).

query.bed.gz

Input: The original noisy dataset (Purple Line).

query.rescaled.bed

Input: Your cleaned/filtered dataset (Blue Stars).

final_result_graph.png

Output: The resulting visualization image.

🛠 Prerequisites

You need Python 3 and the matplotlib library.

To install the required library:

pip install matplotlib


⚙️ Usage

Ensure files are present:
Make sure plot_results.py is in the same folder as your three data files (reference.hist, query.bed.gz, and query.rescaled.bed).

Run the script:

python3 plot_results.py


📊 Understanding the Output

The script generates an image named final_result_graph.png.

<span style="color:green">Green Line (Reference):</span> This is the target "perfect" distribution.

<span style="color:purple">Purple Line (Original Query):</span> This is your starting data. It likely has a large "junk" peak around fragment length ~50-80bp.

<span style="color:skyblue">Blue Stars (Rescaled Output):</span> This is your final processed data.

Success Criteria: The blue stars should overlap the green line almost perfectly.

Failure Criteria: If the blue stars still follow the purple line's "junk" peak, the filtering step in the main pipeline failed.
