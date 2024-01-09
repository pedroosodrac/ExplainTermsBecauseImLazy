from etbil import *
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Read the contents of the specified text file
text = read_txt("../terms-and-conditions/January_5_2022.txt")

# Generate a comprehensive summary for the read text
summarized_text = summarize_terms(text)

# Print the final summarized text
print(summarized_text)
