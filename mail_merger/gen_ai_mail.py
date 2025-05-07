# NOTE: This file is use to generate the mail by ai according to the data parse by excel_sheet_reader
import os
import cohere


def mailGenerator(receiver_name, sender_name, sender_post, subject):
    """Function will generate the mail automatically based on name and subject"""

    # Retrieve the API key from the environmental variable
    api_key = os.getenv("generative-ai")
    if not api_key:
        return "API key not found."

    # Initialize the Cohere client
    cohere_client = cohere.Client(api_key)
    prompt = f"Write a professional email from {sender_name}, an {sender_post}, to {receiver_name} about {subject}. The email should be personalized to {receiver_name} and must be free of grammatical errors."

    try:
        response = cohere_client.generate(prompt=prompt)
        if hasattr(response, "generations"):
            return response.generations[0].text
        else:
            return "Failed to generate mail."
    except Exception as e:
        return f"An error occurred: {str(e)}"


def automated_mail_generator(receiver_name, sender_name, sender_post, subject):
    """Wrapper function to generate mail and return it"""
    return mailGenerator(receiver_name, sender_name, sender_post, subject)


if __name__ == "__main__":
    pass