
# bootcamp_Hemang_Dahiya

# Bootcamp Repository
## Folder Structure
- **homework/** → All homework contributions will be submitted here.
- **project/** → All project contributions will be submitted here.
- **class_materials/** → Local storage for class materials. Never pushed to
GitHub.

## Homework Folder Rules
- Each homework will be in its own subfolder (`homework0`, `homework1`, etc.)
- Include all required files for grading.
## Project Folder Rules
- Keep project files organized and clearly named.

- Keep project files organized and clearly named.

## Data Storage (Homework 5)

### Folder Structure

- `data/raw/` — This folder stores raw CSV files saved directly from the source DataFrame as a common, human-readable format.
- `data/processed/` — This folder stores Parquet files, which are optimized for efficient storage and faster read/write performance in data processing pipelines.

### Formats Used and Why

- **CSV**  
  - Chosen for its wide compatibility and ease of use.  
  - Easy to inspect manually and share with collaborators.  
  - Stored in `data/raw/` as the “raw” version of the dataset.

- **Parquet**  
  - A columnar binary format providing better compression and faster IO.  
  - Preferred for intermediate or processed data in workflows.  
  - Stored in `data/processed/` for downstream analytical tasks.

Using both formats ensures reproducibility and balances accessibility with performance.

### Environment-Driven Paths

- The notebook reads the folder paths from environment variables defined in a `.env` file:
DATA_DIR_RAW=data/raw
DATA_DIR_PROCESSED=data/processed

- These environment variables are loaded in the notebook with the `dotenv` package, allowing flexible path configuration without hardcoding.

- All reading (`read_df()`) and writing (`write_df()`) utility functions use these environment variables to locate files, ensuring portability and easy configuration for different systems or collaborators.


