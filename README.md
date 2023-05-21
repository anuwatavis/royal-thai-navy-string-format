<div align="center">
<img src="./docs/cover.png"/>
</div>

# RTNF (Royal Thai Navy String Format)
RTNF is a Python package that provides functions to convert datetime objects to the datetime and time formats used by the Royal Thai Navy.

# Installation
You can install RTNF using pip:
```bash
pip install rtnf
```

# Usage
```python
from datetime import datetime
from rtnf import to_rnt_date, to_rnt_time

# Convert datetime to Royal Thai Navy date format
current_datetime = datetime.now()
rnt_date = to_rnt_date(current_datetime)
print(rnt_date)  # Output: DDMMYYYY

# Convert datetime to Royal Thai Navy time format
current_datetime = datetime.now()
rnt_time = to_rnt_time(current_datetime)
print(rnt_time)  # Output: HHMM
```

# Contributing
Contributions to RTNF are welcome! If you find any issues or have suggestions for improvement, please create an issue or submit a pull request on the GitHub repository.

# License
RTNF is licensed under the MIT License.

