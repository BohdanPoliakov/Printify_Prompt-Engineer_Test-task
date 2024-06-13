from flask import Flask
import openai

openai.api_key = 'sk-proj-b2gHKJQOLsiU1J6qW9vWT3BlbkFJnlShuSTgyHa06wI5OOHE'

app = Flask(__name__)


def generate_store_banner(store_name, store_description):
    prompt = (f"Generate an intriguing banner for the store \"{store_name}\", which specializes in "
              f"{store_description}. The banner text should be no longer than 50 characters, should avoid "
              f"copyright-infringing elements, and should consist of only 1 phrase.")

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

    return response['choices'][0]['message']['content'].strip()


# Endpoint
@app.route('/generate_banner')
def generate_banner():
    store_name = "Football 24/7"
    store_description = "interesting and fascinating football cards for child and adults"
    banner_text = generate_store_banner(store_name, store_description)
    return banner_text


if __name__ == '__main__':
    app.run(debug=True)


def routes():
    return None
