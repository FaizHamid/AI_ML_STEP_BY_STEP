### Purpose
This repository is a collection of teaching materials (Jupyter notebooks and small example scripts) for an applied ML course. These instructions help AI coding agents make focused, low-risk edits that respect the repository's pedagogical structure.

### Big picture
- **Structure**: material is organized into folders like [B_Python with AI](B_Python%20with%20AI) and [C_Applied Data Science with Python/10_01_SOL_Feature_Engineering_with_Solution.ipynb](C_Applied%20Data%20Science%20with%20Python/10_01_SOL_Feature_Engineering_with_Solution.ipynb). Notebooks are the primary artifacts.
- **Data flow**: Notebooks load CSVs (example: `HousePrices.csv`) and create a shared `df` variable across cells; many examples show `pandas`, `numpy`, `sklearn`, `seaborn`, `matplotlib` and `scipy` usage.

### Editing conventions (must-follow)
- Prefer adding new standalone `.py` modules for reusable logic instead of modifying many notebook cells. This keeps examples reproducible and testable.
- When editing notebooks: do not delete or alter cell metadata ids (cells contain `#VSC-...` ids). Avoid reordering cells unless necessary; add new explanatory cells at the end.
- `df` is used widely as the primary DataFrame variable. Avoid changing its type or shape unexpectedly across cells — instead create new columns or new variables (`df2`, `df_scaled`).

### Common patterns & examples
- Feature-engineering demo: see [C_Applied Data Science with Python/10_01_SOL_Feature_Engineering_with_Solution.ipynb](C_Applied%20Data%20Science%20with%20Python/10_01_SOL_Feature_Engineering_with_Solution.ipynb). Examples use `df['sepal_area'] = ...`, `LabelEncoder`, `MinMaxScaler` and `sns.histplot`.
- CSV usage: scripts call `pd.read_csv("HousePrices.csv")` — ensure relative paths remain correct when adding code.

### Developer workflows
- Install runtime deps (typical): `pip install pandas numpy scikit-learn seaborn matplotlib scipy jupyterlab`
- Run a notebook interactively in VS Code (recommended) or execute headless for CI with:
  - `python -m nbconvert --to notebook --execute "path/to/notebook.ipynb" --ExecutePreprocessor.timeout=600`
  - or use `papermill` when parameterization is needed.

### Testing & safety
- There are no project unit tests. Make small, reviewable changes and prefer creating `.py` modules with simple example scripts that can be run independently.
- Clear notebook outputs before large PRs (or keep outputs minimal) to reduce noisy diffs.

### Git / PR guidance
- Use feature branches; PRs should be small and focused (one learning objective or bugfix per PR).
- When modifying notebooks, include a short description of the manual verification steps (e.g., which cells to run and expected output snippets).

### What not to do
- Do not attempt to refactor the entire collection into a single application. This repo is educational; changes should preserve the lesson flow and examples.
- Do not remove or rename notebooks without confirming the course structure.

### When in doubt
- If a change touches many notebooks or students' examples, open an issue describing the proposed change and wait for manual review.

---
If you'd like, I can: (a) scan and merge any existing agent guidance files if present, (b) add a small CONTRIBUTING note, or (c) create a `requirements.txt` listing detected imports. Which should I do next?
