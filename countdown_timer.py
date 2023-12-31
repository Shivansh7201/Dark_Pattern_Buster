from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def detect_countdown_timer_with_format(url):
    driver = None  # Initialize the driver to None

    try:
        # Use Selenium with a web driver (e.g., ChromeDriver)
        driver = webdriver.Chrome()
        driver.get(url)

        # Countdown timer 
        countdown_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Time Left:")]'))
        )

        # Extract text from the identified element
        countdown_text = countdown_element.text

        return countdown_text

    except Exception as e:
        print(f"Error accessing {url}: {e}")
        return None

    finally:
        # Check if the driver is defined before quitting
        if driver:
            driver.quit()

# Example usage
url = "https://www.shoppingsquare.com.au/p_437911_HDMI_Splitter_1_In2_Out_Cable_Adapter_Converter_HD_1080_Multi_Display_Duplicator"
countdown_text = detect_countdown_timer_with_format(url)

if countdown_text:
    print("Detected Countdown Timer:")
    print(countdown_text)
else:
    print("No countdown timer detected.")
