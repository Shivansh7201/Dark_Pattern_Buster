from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def process_source(source):
    soup = BeautifulSoup(source, "html.parser")
    text_elements = soup.find_all(text=True)
    processed_list = []

    for element in text_elements:
        temp = element.replace(" ", "").replace("\n", "")
        if temp != "":
            processed_list.append(temp)

    return processed_list

def trace(list_):
    return_list = []
    current = 0

    while current < len(list_):
        if list_[current][0] == "₹":
            return_list.append(f"{list_[current - 1]} {list_[current]}")
        current += 1

    return return_list

def find_hidden_costs(url):
    options = Options()
    options.add_argument('--headless')  # Run Chrome in headless mode (without a GUI)
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        source_code = driver.page_source
        processed_source = process_source(source_code)
        hidden_costs = trace(processed_source)

        if hidden_costs:
            print("Hidden costs detected:")
            for cost in hidden_costs:
                print(cost)
        else:
            print("No hidden costs detected.")

    finally:
        driver.quit()

# Example usage
url = 'https://www.amazon.in/Amazon-Brand-Tricycle-Cushioned-Guardrail/dp/B0CHRR6TW5/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.8186fc6f-32b7-4451-912e-9502be518ab0&pd_rd_r=7958db9c-8563-4e00-a109-304263b6c377&pd_rd_w=XCTj1&pd_rd_wg=DcxKH&pf_rd_p=8186fc6f-32b7-4451-912e-9502be518ab0&pf_rd_r=WV0JD8Y4AY751TKV12QF&qid=1704019620&refinements=p_n_format_browse-bin%3A30678570031&s=toys&sr=1-1&th=1'  # Replace with the URL of the page you want to check
find_hidden_costs(url)

