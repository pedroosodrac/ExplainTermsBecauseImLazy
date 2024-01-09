<h1> Explain Terms Because Im Lazy </h2>


<h2> Introduction </h4>

Tame the legalese beast with this Python script! Powered by OpenAI's GPT, it expertly condenses even the most extensive terms and conditions into concise, user-friendly summaries. Ideal for the time-pressed, the efficiency-minded, and those who simply prefer to skip the legalese, this tool empowers you to grasp key points quickly and accurately. Reclaim your time, embrace understanding, and procrastinate with confidence – clarity is just a click away.

<h2> Why not just use ChatGPT? </h4>

Although ChatGPT is a powerful tool, this project offers several distinct advantages. The first is that it automates the process of segmenting and simplifying texts, saving time and effort on manual interaction and eliminating the need to create and refine prompts from scratch. It also has no text size limit, which means it can handle infinitely larger documents than ChatGPT. Importantly, it ensures accurate summaries, something ChatGPT sometimes struggles with when it wrongly preserves or ignores information. Furthermore, this code is extremely adaptable and serves as a basis for other projects that involve processing long texts, extending its usefulness beyond simplifying terms and conditions.

<h2> How It Works </h4>

The script offers a user-friendly interface, requiring only your OpenAI key and the text you want to simplify. With a single function call, it automates the entire process:

**Text Extraction**: Seamlessly extracts content from the designated text file.

**Intelligent Segmentation**: Divides the text into logical sections for focused summarization.

**GPT-Powered Summarization**: Utilizes OpenAI's GPT model and tailored prompts to generate concise and accurate summaries.

**Terms and Conditions Mastery**: Expertly handles terms and conditions documents, crafting comprehensive yet digestible summaries.

**Length Management**: Ensures clarity by shortening summaries that exceed 800 characters.

<h2> Application </h4>

In the [terms-and-conditions](terms-and-conditions) folder there are two real [Google](https://policies.google.com/terms/archive?hl=en-US) examples ready to use in txt format. Both were chosen because they are from different dates and present considerably different content. Applying the code in the file [January_5_2022.txt](terms-and-conditions/January_5_2022.txt) the result was the following:

> You can use Google's services like apps and sites if you respect the terms, laws, and other's rights. You own your content, but Google can host and change it under certain conditions. If your content violates intellectual property rights, your account can be suspended. You're responsible for the security of your Google Account. Google can analyze your content for improving services and ads. You can quit Google's services anytime, and your privacy is respected. If you don't follow the terms, Google can suspend your account. Any changes in terms will be communicated to you. If you don't agree, you can stop using services and close your account. Any disputes fall under specific legal jurisdictions.

Applying the code in the file [September_20_1999.txt](terms-and-conditions/September_20_1999.txt) the result was the following:

> You can use Google's services for non-commercial purposes and must use them at your own risk. Google can modify or terminate your services or accounts, especially if you violate any terms or provide false information. If inactive for 90 days, Google can delete your email account. You'll bear all risks and any costs resulting from third-party claims triggered by your actions, providing indemnity to Google. Google can alter the Terms of Service, and they will hold effect if written and signed by the company.

Having cloned this repository, to use it you just need to add your OpenAI key to the [.env](.env) file and use the [main.py](src/main.py) file to simplify any terms and conditions you want.

<h2> GPT Model Choice </h4>

Both GPT-3.5 and GPT-4 produce similar results. However, although GPT-3.5 is cheaper, GPT-4 more accurately summarizes the text. Each generated code costs less than a tenth of a dollar and is produced in less than 1 minute. To save money, a free alternative would be to use the prompts from the [etbil.py](src/etbil.py) file in ChatGPT. However, this method requires manual intervention and is not automatic.
