# Simple R analysis (sample). Replace with your real steps.
library(dplyr)
library(readr)

clean_data <- function(input_csv, output_csv) {
  df <- read_csv(input_csv, show_col_types = FALSE)
  names(df) <- trimws(names(df))
  df <- distinct(df)
  numeric_cols <- names(df)[sapply(df, is.numeric)]
  for (col in numeric_cols) {
    med <- median(df[[col]], na.rm = TRUE)
    df[[col]][is.na(df[[col]])] <- med
  }
  write_csv(df, output_csv)
}

cat("Run: clean_data('raw.csv', 'clean.csv') in R\n")
