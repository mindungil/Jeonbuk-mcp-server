Generate an Excel workbook using a Python script. Returns a markdown hyperlink for downloading the generated file.

Template structure:
```python
# Allowed packages
import numpy as np
from openpyxl import Workbook

# Import here other xlsx packages you need, but do not import other packages that are not allowed.

# Buffer to save excel file, previously defined in the server.py file
XLSX_BUFFER = xlsx_buffer # Do not modify this line, it is defined in the server.py file

def excel():
    # Initialize a new Workbook instance
    wb = Workbook()

    # Apply the required data transformations to build the Excel workbook based on the user's request.
    # Create the necessary worksheets, populate tables, add charts, and format cells for clarity and visual appeal.

    # Save the Excel workbook
    wb.save(XLSX_BUFFER) # Do not modify this line, it is defined in the server.py file

    return f"Excel file created successfully!"

# Invoke the function to generate the Excel file
excel()
```

Provide a complete Python script following this template to generate your Excel workbook.