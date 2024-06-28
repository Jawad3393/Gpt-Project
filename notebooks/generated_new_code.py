Certainly! Here is a Python file that demonstrates how to use OpenAI's API to generate an essay based on two sample essays provided as input:

```python
import openai

# Set your OpenAI API key
api_key = 'YOUR_API_KEY'
openai.api_key = api_key

def generate_essay(sample_essay1, sample_essay2):
    # Specify the prompt for the API
    prompt = f"Write a well-structured essay that combines the ideas from the following two sample essays:\n\n{sample_essay1}\n\n{sample_essay2}\n\n"

    # Call the OpenAI API to generate the new essay
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=500
    )

    new_essay = response.choices[0].text
    return new_essay

if __name__ == '__main__':
    # Sample essays as input
    sample_essay1 = """
    Sample Essay 1: 
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Sed eget tellus at odio ultricies lobortis. 
    """

    sample_essay2 = """
    Sample Essay 2:
    Integer vitae lacus in lectus mollis pretium. Vivamus auctor suscipit libero, a ornare justo sagittis ut. 
    """

    # Generate a new essay based on the sample essays
    new_essay = generate_essay(sample_essay1, sample_essay2)

    # Display the newly generated essay
    print("New Essay:")
    print(new_essay)
```

Make sure to replace `'YOUR_API_KEY'` with your actual OpenAI API key in the code. This script defines a function `generate_essay` that takes two sample essays as input, combines them into a prompt for the OpenAI API, and generates a new essay based on the provided samples. The generated essay is then printed to the console.