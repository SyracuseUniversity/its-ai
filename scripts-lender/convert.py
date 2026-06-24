import pandas as pd
import json
import pathlib

INPUT_PATH: pathlib.Path = pathlib.Path("data-lender/spreadsheet.xlsx")
OUTPUT_PATH: pathlib.Path = pathlib.Path("data-lender/spreadsheet.json")

df: pd.DataFrame = pd.read_excel(INPUT_PATH, sheet_name=0)

# Replace NaN with None so JSON serializes cleanly
df = df.where(df.notna(), other=None)

records: list[dict] = df.to_dict(orient="records")

OUTPUT_PATH.write_text(json.dumps(records, indent=2, default=str))
print(f"Wrote {len(records)} rows to {OUTPUT_PATH}")
