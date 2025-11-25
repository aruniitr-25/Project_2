Here is a copy-paste format README for your GitHub repository based on the provided Python script.

-----

#  Fragment Length Distribution Rescaler

This Python script is designed for visualizing and comparing **fragment length distributions** in genomics data. It reads distributions from three files—a **reference histogram**, an **original query BED file**, and a **rescaled output BED file**—calculates the normalized frequencies for each, and generates a comparative plot using `matplotlib`.

The core utility lies in the `get_frequencies` function, which can interpret both pre-normalized histogram files and raw genomic interval files (like BED) to extract the distribution of fragment lengths. It implements a **"smart counting" logic** to determine the fragment length from either the 4th or 5th column of a standard BED file.

##  Features

  * **Multi-File Input:** Compares three different fragment length distributions: Reference, Original Query, and Rescaled Output.
  * **Flexible Data Reading:** Automatically handles both plain text histogram files and gzipped BED files.
  * **Smart Length Extraction:** Extracts fragment length from the 4th or 5th column of a BED file, providing robustness for different data conventions.
  * **Distribution Normalization:** Calculates normalized frequencies (probabilities) for raw BED files.
  * **High-Quality Visualization:** Generates a comparative plot using `matplotlib` to visually assess the quality of the rescaling process.

##  Configuration & Requirements

### File Configuration (Within the script)

The script relies on three specific files based on the internal configuration:

| Variable | Default Value | Format | Description |
| :--- | :--- | :--- | :--- |
| `REF_FILE` | `"reference.hist"` | Text (`Length Probability`) | The target distribution (already normalized). |
| `QUERY_FILE` | `"query.bed.gz"` | Gzip/BED | The original, un-rescaled genomic data. |
| `OUTPUT_FILE` | `"query.rescaled.bed"` | Text/BED | The output of the rescaling process. |

### Requirements

This script requires the following Python libraries:

```bash
pip install matplotlib
pip install gzip  # (usually built-in)
```

##  Usage

1.  **Ensure Files Exist:** Make sure the three configured input files (`reference.hist`, `query.bed.gz`, `query.rescaled.bed`) are present in the same directory as the script.

2.  **Run the Script:**

    ```bash
    python your_script_name.py
    ```

3.  **Result:** The script will print status updates and save the final comparison chart as **`final_result_plot.png`**.

##  Plot Output Example

The generated plot displays the three distributions:

  * **Reference (Green Line):** The target distribution that the other files should ideally match.
  * **Original Query (Purple Line):** The distribution before any rescaling or correction.
  * **Rescaled Output (Blue Stars):** The distribution after processing, which should closely overlay the Reference distribution if the rescaling was successful.

### Example Visualization

##  Core Logic: `get_frequencies`

The `get_frequencies` function is responsible for parsing the different file types:

1.  **Histogram Files (`.hist`):** Reads two columns (`Length` and `Probability`). The data is already normalized.
2.  **BED Files (`.bed`/`.bed.gz`):**
      * Iterates through lines, splitting by whitespace.
      * Attempts to extract the fragment length (read length or insert size) from **column 4** (index 3) or **column 5** (index 4).
      * Tallies the count for each length.
      * **Normalizes** the counts by dividing by the total number of fragments read to get the final frequency distribution.

-----

