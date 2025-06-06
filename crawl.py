from selenium import webdriver
from selenium.webdriver.common.by import By
import time


if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.set_window_size(1920, 1080)
    driver.get('https://www.historicaltechtree.com/')
    time.sleep(5)

    # Hide menu
    driver.execute_script("menu = document.querySelector('div.fixed.top-16'); menu.parentNode.removeChild(menu);")
    time.sleep(2)

    # First pass to load everything
    for x in range(0, 132000, 1900):
        print(f"1 x={x}")
        for y in range(0, 3000, 820):
            print(f"1 y={y}")

            # Pan
            driver.execute_script(f"document.querySelector('div.overflow-x-auto.overflow-y-auto').scrollTo({x}, {y});")
            time.sleep(1)

    # Second pass to save
    for x in range(0, 132000, 1900):
        print(f"2 x={x}")
        for y in range(0, 3000, 820):
            print(f"2 y={y}")

            # Pan
            driver.execute_script(f"document.querySelector('div.overflow-x-auto.overflow-y-auto').scrollTo({x}, {y});")
            time.sleep(1.5)

            # Screenshot
            driver.save_screenshot(f'{x:06}_{y:06}.png')
            time.sleep(0.5)

    # X: 0-132000 that's 69 columns
    # Y: 0-3000   that's 4 rows
    #     can only view about 839px vertically because header/footer
    # that's 276 images

    # TODO: Images don't load properly on the very left, need to re-crawl with higher overlap

    driver.quit()
