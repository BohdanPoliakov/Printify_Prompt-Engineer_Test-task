import openai
# this is my active chatGPT key
openai.api_key = 'sk-proj-b2gHKJQOLsiU1J6qW9vWT3BlbkFJnlShuSTgyHa06wI5OOHE'


def generate_store_banner(store_name, store_description):
    prompt = (f"Generate an intriguing banner for the store \"{store_name}\", which specializes in "
              f"{store_description}. The banner text should be no longer than 50 characters, should avoid "
              f"copyright-infringing elements, and should consist of only 1 phrase.")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=20,
            temperature=0.9,
            n=1,
            stop=None,
            timeout=10
        )

        banner_text = response['choices'][0]['message']['content'].strip()

        if len(banner_text) > 50:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-16k",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=10,
                temperature=0.9,
                n=1,
                stop=None,
                timeout=10
            )
            banner_text = response['choices'][0]['message']['content'].strip()

        return banner_text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


store_name = "Football 24/7" # or you can use: store_name = input("Store Name:\n")
store_description = "interesting and fascinating football cards for children and adults"
# or you can use: store_description = input("Store Description:\n")
banner_text = generate_store_banner(store_name, store_description)

if banner_text:
    print(banner_text.encode('utf-8', 'ignore').decode('utf-8', 'ignore'))
else:
    print("Failed to generate store banner.")
