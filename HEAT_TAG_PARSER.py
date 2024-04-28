import re
import json

# Enhanced document parsing to handle more complex structures
document_content = """
# HEAT 1 INTRO SKULLY MEMORY AND DATA USAGE STRUCTURE
Memory usage in data structuring involves complex hierarchical storage which is essential for...
# DETAILS
This involves managing memory efficiently across different storage layers.
# RESPONSE
Effective memory structuring requires hierarchical data storage models.

# HEAT I DICTIONARY CODE TAGS
This section defines specific tags used across different modules in our system.
# DETAILS
Tags are essential for module communication.
# RESPONSE
Tags include: DATA_START, DATA_END, MODULE_BEGIN.
"""

# More robust regex pattern to capture additional context if available
pattern = r"# (HEAT \d+ [A-Z ]+|HEAT [I]+ [A-Z ]+)\s+(.*?)\s+(# DETAILS\s+(.*?))?\s+# RESPONSE\s+(.*?)\s+(?=#|$)"

# Perform the regex search and prepare data
matches = re.findall(pattern, document_content, re.DOTALL)
training_data = [
    {'prompt': f'{prompt} ' + (details or ''), 'response': response.strip()}
    for _, prompt, _, details, response in matches
]

# Output to JSON
with open('../training_data.json', 'w') as f:
    json.dump(training_data, f, indent=4)

print(f"Data prepared and saved for training. Found {len(training_data)} entries.")
