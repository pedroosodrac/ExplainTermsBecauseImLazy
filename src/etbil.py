import openai
from typing import List


# Prompts
system_prompt = "You are an assistant responsible for helping extract important information from texts accurately and according to specified criteria. You always use only common words and make complex information easier to understand. Your answers are extremely short single paragraphs."
summarize_prompt = "The following text is taken from the terms and conditions section. Just extract information from the text about the user without making a list. Ignore all information that talks about the text itself. Ignore all information that contains contact information, such as phone numbers and URLs."
micro_prompt = f"{summarize_prompt} Your final text needs to answer the following questions: what the user can or cannot do and what the company can or cannot do?"
macro_prompt = f"{summarize_prompt} Your final text must be extremely short, succinct and summarize only the most important points of the terms and conditions. Write as if you are briefly explaining the terms to the user. Your text needs to be coherent."
shorten_prompt = "The following text is taken from the terms and conditions section. You just need to shorten it. Write as if you were explaining the content of the text to the user and be as succinct as possible. Your text needs to be coherent."


def read_txt(file_path: str) -> str:
    """
    Read the contents of a text file and return it as a string.

    Args:
        file_path (str): The path to the text file to be read.

    Returns:
        str: The content of the text file as a string, with leading/trailing whitespaces removed.
    """
    # Open the specified text file in read mode with UTF-8 encoding
    with open(file_path, "r", encoding="utf8") as file:
        # Read the contents of the file and remove leading/trailing whitespaces
        text_content = file.read().strip()

    return text_content


def split_text(text: str, max_segment_length: int = 4000) -> List[str]:
    """
    Split the input text into segments based on specified conditions.

    Args:
        text (str): The input text to be segmented.
        max_segment_length (int, optional): The maximum length of each segment. Defaults to 16000.

    Returns:
        List[str]: A list of segmented text based on specified conditions.
    """
    # Define characters that indicate the end of a sentence
    sentence_endings = ".!?"

    # Split the input text into lines
    lines = text.split("\n")

    # Initialize a list to store segmented text
    segmented_text = []

    # Iterate through each line in the input text
    for index, line in enumerate(lines):
        # Check if the line has meaningful content
        if len(line) > 1:
            # Check conditions for line segmentation
            if len(segmented_text) == 0 or segmented_text[-1][-1] in sentence_endings or line[0].isupper():
                # Append the line to segmented_text if it meets the conditions
                segmented_text.append(line)
            else:
                # Concatenate the current line with the previous one
                segmented_text[-1] = " ".join([segmented_text[-1], line])

    # Initialize a list to store the final segmented text
    final_segments = []

    # Iterate through each segment in the segmented text
    for segment in segmented_text:
        # Check conditions for creating a new segment
        if len(final_segments) == 0 or len(final_segments[-1] + segment) > max_segment_length:
            # Append the segment to final_segments if it meets the conditions
            final_segments.append(segment.strip())
        else:
            # Concatenate the current segment with the previous one
            final_segments[-1] = "\n".join([final_segments[-1], segment.strip()])

    return final_segments


def summarizer(content: str, prompt: str = "micro") -> str:
    """
    Generate a summary based on provided content and prompt type using OpenAI's GPT-3.5 model.

    Args:
        content (str): The content to be summarized.
        prompt (str, optional): The prompt type for the summarization. Defaults to "micro".

    Returns:
        str: The summarized content based on the provided prompt and input content.

    Raises:
        ValueError: If the prompt provided is not a string.
    """
    # Import the OpenAI library and initialize the client
    client = openai.OpenAI()

    # Map prompt types to their respective prompt values
    prompt_types = {"micro": micro_prompt, "macro": macro_prompt, "shorten": shorten_prompt}

    # Check if the prompt type is valid and set the appropriate prompt
    if isinstance(prompt, str):
        prompt = prompt_types.get(prompt)
    else:
        raise ValueError("Prompt should be a string")

    # Generate completion using OpenAI's chat completion API
    completion = client.chat.completions.create(
        model="gpt-4",  # You can also uses "gpt-3.5-turbo-16k"
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"{prompt}\n\n#Text\n{content}"}
        ]
    )

    return completion.choices[0].message.content.strip()


def summarize_terms(text: str) -> str:
    """
    Generate a comprehensive summary based on segmented analysis of the input text.

    Args:
        text (str): The text to be segmented and summarized.

    Returns:
        str: A final summary based on individual segment summaries.
    """
    # Segment the input text into smaller parts
    splited_text = split_text(text)

    # If there are multiple segments
    if len(splited_text) > 1:
        # Generate summaries for each segment using the "micro" prompt
        summaries_list = [summarizer(i, prompt="micro") for i in splited_text]

        # Combine individual segment summaries into a single text and generate a final summary
        final_summary = summarizer("\n".join(summaries_list), prompt="macro")
    else:
        # Generate a final summary directly for a single segment
        final_summary = summarizer(splited_text[0], prompt="macro")

    # Check if the final summary length exceeds 800 characters and create a shorter summary if needed
    if len(final_summary) > 800:
        final_summary = summarizer(final_summary, prompt="shorten")

    return final_summary
