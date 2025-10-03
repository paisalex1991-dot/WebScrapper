import tkinter as tk
from tkinter import messagebox, filedialog
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import threading
import time

## text added for git testing


# Global variable for the results box
result_box = None

# Paths to your ChromeDriver and optional Chrome binary
CHROME_PATH = r"C:\01_PROGRAME\Chrome\chrome-win64\chrome-win64\chrome.exe"
CHROMEDRIVER_PATH  = r"C:\01_PROGRAME\Chrome\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Base URL
BASE_URL = "https://mcscertified.com/product-directory/"

def scrape_products_selenium():

    options = Options()
    options.binary_location = r"C:\01_PROGRAME\Chrome\chrome-win64\chrome-win64\chrome.exe"
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument("--disable-web-security")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, "Launching Chrome and scraping data...\n")
    result_box.update()

    # Selenium setup
    options = Options()
    if CHROME_PATH:
        options.binary_location = CHROME_PATH

    driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)
    time.sleep(5)
    driver.get(BASE_URL)

    all_products = []
    page_num = 1

    try:
        while True:
            result_box.insert(tk.END, f"Scraping page {page_num}...\n")
            result_box.update()

            # Wait for product items to load
            wait = WebDriverWait(driver, 15)
            wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-item")))

            # Extract product data
            product_items = driver.find_elements(By.CLASS_NAME, "product-item")
            if not product_items:
                break

            for item in product_items:
                # TODO: replace the following class names with actual ones from the site
                certification_number = item.find_element(By.CLASS_NAME, "cert-number").text
                manufacturer = item.find_element(By.CLASS_NAME, "manufacturer").text
                model_number = item.find_element(By.CLASS_NAME, "model-number").text
                technology = item.find_element(By.CLASS_NAME, "technology").text
                certification_period = item.find_element(By.CLASS_NAME, "cert-period").text
                scop = item.find_element(By.CLASS_NAME, "scop").text

                all_products.append({
                    "Certification Number": certification_number,
                    "Manufacturer": manufacturer,
                    "Model Number": model_number,
                    "Technology": technology,
                    "Certification Period": certification_period,
                    "SCOP": scop
                })

            # Try to click "Next" button
            try:
                next_btn = driver.find_element(By.LINK_TEXT, "Next")
                next_btn.click()
                page_num += 1
            except:
                break  # no more pages

        # Display results in the Tkinter text box
        result_box.delete("1.0", tk.END)
        for p in all_products:
            result_box.insert(tk.END, f"{p}\n")
        result_box.insert(tk.END, f"\nTotal products: {len(all_products)}")

        # Save to Excel
        df = pd.DataFrame(all_products)
        filename = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if filename:
            df.to_excel(filename, index=False)
            messagebox.showinfo("Saved", f"Data saved to {filename}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

    finally:
        driver.quit()

def start_scraping_thread():
    thread = threading.Thread(target=scrape_products_selenium)
    thread.start()

def main():
    global result_box
    root = tk.Tk()
    root.title("MCS Certified Product Scraper")
    root.geometry("800x600")

    # Buttons frame
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    scrape_button = tk.Button(button_frame, text="Scrape Products", command=start_scraping_thread, bg="blue", fg="white")
    scrape_button.pack(side="left", padx=10)

    clear_button = tk.Button(button_frame, text="Clear Results", command=lambda: result_box.delete("1.0", tk.END), bg="blue", fg="white")
    clear_button.pack(side="left", padx=10)

    # Results box with scrollbar
    result_frame = tk.Frame(root)
    result_frame.pack(pady=20)

    scrollbar = tk.Scrollbar(result_frame)
    scrollbar.pack(side="right", fill="y")

    result_box = tk.Text(result_frame, width=100, height=25, yscrollcommand=scrollbar.set)
    result_box.pack(side="left")
    scrollbar.config(command=result_box.yview)

    root.mainloop()

if __name__ == "__main__":
    main()