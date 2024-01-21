from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

website = "https://www.instagram.com/"

path = "C:/Users/HP/Downloads/edgedriver_win64/msedgedriver.exe"

service = Service(executable_path=path)  
driver = webdriver.Edge(service=service)
driver.maximize_window()

driver.get(website)


input_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"//input[@name='username']"))
)
input_field.send_keys("your_username")

ps_input_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"//input[@name='password']"))
)
ps_input_field.send_keys("your_password")

login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Log in']"))
)
login_button.click()

save_login_info = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Not now']"))
)
save_login_info.click()

notification = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Not Now']"))
)
notification.click()

Message = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Messages']"))
)
Message.click()

new_message = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Send message']"))
)
new_message.click()

dm_input_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"//input[@name = 'queryBox']"))
)
dm_input_field.send_keys("targeted_id")

checkbox = WebDriverWait(driver, 10). until(
    EC.element_to_be_clickable((By.XPATH,"//input[@name = 'ContactSearchResultCheckbox']"))
)
checkbox.click()

start_chat = WebDriverWait(driver, 10). until(
    EC.element_to_be_clickable((By.XPATH,"//*[text() = 'Chat']"))
)
start_chat.click()

write_message = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"//div[@role = 'textbox']"))
)
write_message.send_keys("this is an aoutomated message.!")

send_chat = WebDriverWait(driver, 10). until(
    EC.element_to_be_clickable((By.XPATH,"//*[text() = 'Send']"))
)
send_chat.click()
