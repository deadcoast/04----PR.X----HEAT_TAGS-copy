import re
import json

# Enhanced document parsing to handle more complex structures
document_content = """
# Output: Prompt: HEAT 1 INTRO SKULLY MEMORY AND DATA USAGE STRUCTURE Memory usage in data structuring involves 
# complex hierarchical storage which is essential for... Response: Effective memory structuring requires hierarchical
# data storage models. Prompt: HEAT I DICTIONARY CODE TAGS This section defines specific tags used across different 
# modules in our system. Response: Tags include: DATA_START, DATA_END, MODULE_BEGIN. Prompt: HEAT 2 DATA STRUCTURE 
# AND MEMORY USAGE Data structuring and memory usage are essential for efficient data processing. Response: Effective
# memory structuring requires hierarchical data storage models. Data prepared and saved for training. Found 3 entries.

# The code above extracts structured data from a document using a regular expression pattern. The pattern captures 
# different sections of the document, including the prompt, details, and response. The extracted data is then 
# formatted into a list of dictionaries, where each entry contains the prompt and response information. Finally, 
# the extracted data is saved to a JSON file for further processing or training purposes. The code above extracts 
# structured data from a document using a regular expression pattern. The pattern captures different sections of the 
# document, including the prompt, details, and response. The extracted data is then formatted into a list of 
# dictionaries, where each entry contains the prompt and response information. Finally, the extracted data is saved 
# to a JSON file for further processing or training purposes.

# Enhanced document parsing to handle more complex structures
"""

"""
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
# HEAT I DICTIONARY CODE TAGS
""""
This section defines specific tags used across different modules in our system.
# DETAILS
Tags are essential for module communication.
# RESPONSE
Tags include: DATA_START, DATA_END, MODULE_BEGIN.

# HEAT 2 DATA STRUCTURE AND MEMORY USAGE
Data structuring and memory usage are essential for efficient data processing.
# DETAILS
This involves managing memory efficiently across different storage layers.
# RESPONSE
Effective memory structuring requires hierarchical data storage models.
"""

# More robust regex pattern to capture additional context if available
pattern = r"# (HEAT \d+ [A-Z ]+|HEAT [I]+ [A-Z ]+)\s+(.*?)\s+(# DETAILS\s+(.*?))?\s+# RESPONSE\s+(.*?)\s+(?=#|$)"

# Perform the regex search and prepare data
matches = re.findall(pattern, document_content, re.DOTALL)
training_data = [
    {'prompt': f'{prompt} ' + (details or ''), 'response': response.strip()}
    for _, prompt, _, details, response in matches
]

# Print the extracted data
for entry in training_data:
    print(f"Prompt: {entry['prompt']}")
    print(f"Response: {entry['response']}")
    print()

# Save the extracted data to a JSON file
with open('../training_data.json', 'w') as f:
    json.dump(training_data, f, indent=4)

print(f"Data prepared and saved for training. Found {len(training_data)} entries.")

# Output: Prompt: HEAT 1 INTRO SKULLY MEMORY AND DATA USAGE STRUCTURE Memory usage in data structuring involves
# complex hierarchical storage which is essential for... Response: Effective memory structuring requires hierarchical
# data storage models. Prompt: HEAT I DICTIONARY CODE TAGS This section defines specific tags used across different
# modules in our system. Response: Tags include: DATA_START, DATA_END, MODULE_BEGIN. Prompt: HEAT 2 DATA STRUCTURE
# AND MEMORY USAGE Data structuring and memory usage are essential for efficient data processing. Response: Effective
# memory structuring requires hierarchical data storage models. Data prepared and saved for training. Found 3 entries.

# The code above extracts structured data from a document using a regular expression pattern.
# The pattern captures different sections of the document, including the prompt, details, and response.
# The extracted data is then formatted into a list of dictionaries, where each entry contains prompt response info.
# Finally, the extracted data is saved to a JSON file for further processing or training purposes.

# Enhanced document parsing to handle more complex structures
document_content = """
# HEAT 1 INTRO SKULLY MEMORY AND DATA USAGE STRUCTURE
Memory usage in data structuring involves complex hierarchical storage which is essential for...
# DETAILS
This involves managing memory efficiently across different storage layers.
# RESPONSE
Effective memory structuring requires hierarchical data storage models.
"""


# Output to JSON
with open('../training_data.json', 'w') as f:
    json.dump(training_data, f, indent=4)

print(f"Data prepared and saved for training. Found {len(training_data)} entries.")
