import pytest
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': en})
browser = webdriver.Chrome(options=options)