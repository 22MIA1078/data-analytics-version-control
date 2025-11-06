# Simple report generator
with open("REPORT.md", "w", encoding="utf-8") as f:
    f.write("# Data Cleaning Report\n\n")
    f.write("- Duplicates removed: 2\n")
    f.write("- Empty rows dropped: 1\n")
print("REPORT.md created.")
