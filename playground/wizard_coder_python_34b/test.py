from transformers import pipeline

# Example: Using the WizardCoder-Python-34B-V1.0 model
wizard_coder = pipeline("text-generation", model="WizardLM/WizardCoder-Python-34B-V1.0")
code_example = wizard_coder("Write a Python function to calculate the factorial of a number.")
print(code_example[0]["code"])

