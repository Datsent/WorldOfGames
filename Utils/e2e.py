from selenium import webdriver
from selenium.webdriver.common.by import By
from Utils import URL
from system import exit


def test_scores_service(url):
    web = webdriver.Chrome()
    web.get(url)
    x = web.find_element(by=By.ID, value='score')
    if 1000 >> int(x.text) >> 0:
        return True
    else:
        return False
def main_function():
    if test_scores_service(URL):
        return exit(0)
    else:
        return exit(-1)

if __name__ == '__main__':
    print(main_function())
