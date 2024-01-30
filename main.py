from flask import Flask, request, jsonify
from transformers import BertForSequenceClassification, BertTokenizerFast,pipeline
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import json
import time

app = Flask(__name__)


model = BertForSequenceClassification.from_pretrained("./models")
tokenizer = BertTokenizerFast.from_pretrained("./models")
final_model = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)


def check_dark_patterns(text_nodes):
    category_mapping_count = {"Urgency": 0, "Not Dark Pattern": 0, "Scarcity": 0, "Misdirection": 0, "Social Proof": 0,
                              "Obstruction": 0, "Sneaking": 0, "Forced Action": 0}

    for text in text_nodes:
        predicted_value = final_model(text)
        print(predicted_value)
        category_mapping_count[predicted_value[0]["label"]]+=1

    return category_mapping_count


@app.route('/', methods=['POST', 'GET'])
def home():
    return "Welcome! to Dark Pattern Bluster API."

@app.route('/predict', methods=['GET'])
def predict():
    ecom_url = str(request.args.get('url'))
    output = scrape_visible_content(ecom_url)
    print(output)
    output = check_dark_patterns(output)
    return jsonify(output)


def scrape_visible_content(url):
    # Set up Selenium webdriver with headless option
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the URL
    try:
        driver.get(url)
    except Exception as e:
        print(f"An error occurred: {e}")

    # Scroll down to load all content (you might need to adjust the sleep time based on the site)
    scroll_height = driver.execute_script(
        "return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        new_scroll_height = driver.execute_script(
            "return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
        if new_scroll_height == scroll_height:
            break
        scroll_height = new_scroll_height

    # Get the visible text content after scrolling
    visible_text = driver.find_element('tag name', 'body').text.split("\n")
    print(type(visible_text))

    # Close the webdriver
    driver.quit()
    return visible_text



if __name__ == '__main__':
    app.run(port=4040)
