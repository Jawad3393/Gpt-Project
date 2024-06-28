import os
from openai import OpenAI

def read_specification(file_path):
    """This reads the specification from the file"""
    with open(file_path, 'r') as file:
        return file.read()

def generate_prompt(specification):
    """This is the personality for the AI and what it should do"""
    prompt = (
        "You are a Python developer. Based on the following specification, "
        "generate a Python file.\n\n"
        "Specification:\n"
        f"{specification}\n\n"
        "Make sure the file is commented and easy to understand."
    )
    return prompt

def call_openai_api(client, prompt):
    """Calls the API to generate code based on the spec."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def save_to_file(content, file_path):
    """Saves the generated content to a file"""
    with open(file_path, 'w') as file:
        file.write(content)

def main(specification_file, output_file):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Read the specification
    specification = read_specification(specification_file)

    # Generate the prompt
    prompt = generate_prompt(specification)

    # Call the OpenAI API
    generated_code = call_openai_api(client, prompt)

    # Save the generated code to a file
    save_to_file(generated_code, output_file)

    print(f"Generated code has been saved to {output_file}")

# Example usage:
specification_file = "specification.txt"  # Path to the specification file
output_file = "generated_code25.py"         # Path to the output file

main(specification_file, output_file)