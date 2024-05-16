import ollama


def api_call(messages, model_name="llava:7b", temperature=0.5, max_tokens=150):
    try:
        # Execute the chat completion using the chosen model
        res = ollama.chat(
            model="llava:34b-v1.6",
            messages=messages,
        )

        decision = res['message']['content'].strip() if 'message' in res else None
        return decision

    except Exception as e:
        raise Exception(f"An error occurred: {e}")


# # Replace this payload with the actual messages sequence for your use case # # Test
# messages_payload = [
#     {"role": "system", "content": "You are a helpful and knowledgeable assistant. Always uwufy the text."},
#     {"role": "user", "content": "Please help me troubleshoot my JavaScript code."}
# ]
#
# # Example configuration: you might want to specify 'temperature' for more creative responses,
# # or 'max_tokens' for more concise outputs
# result = api_call(messages_payload, temperature=0.7, max_tokens=100)
# print(f"AI Analysis Result: '{result}'")