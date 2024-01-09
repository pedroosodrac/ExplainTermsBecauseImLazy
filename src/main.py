from etbil import *
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Read the contents of the specified text file
text = read_txt("../terms-and-conditions/January 5, 2022.txt")

# Generate a comprehensive summary for the read text
summarized_text = summarize_terms(text)

# Print the final summarized text
print(summarized_text)

# September 20, 1999.txt
# You can use Google's services for non-commercial purposes and must use them at your own risk. Google can modify or terminate your services or accounts, especially if you violate any terms or provide false information. If inactive for 90 days, Google can delete your email account. You'll bear all risks and any costs resulting from third-party claims triggered by your actions, providing indemnity to Google. Google can alter the Terms of Service, and they will hold effect if written and signed by the company.

# January 5, 2022.txt
# You can use Google's services like apps and sites if you respect the terms, laws, and other's rights. You own your content, but Google can host and change it under certain conditions. If your content violates intellectual property rights, your account can be suspended. You're responsible for the security of your Google Account. Google can analyze your content for improving services and ads. You can quit Google's services anytime, and your privacy is respected. If you don't follow the terms, Google can suspend your account. Any changes in terms will be communicated to you. If you don't agree, you can stop using services and close your account. Any disputes fall under specific legal jurisdictions.