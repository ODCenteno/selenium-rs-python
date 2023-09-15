# Installing web driver manually

### Chrome Driver
Visit [Chromelabs google webpage](https://googlechromelabs.github.io/chrome-for-testing/) and download the latest webdriver for your OS.
### Firefox Driver
Firefox use the **geckodriver** to manage the browser. You should [visit the repository](https://github.com/mozilla/geckodriver) and download the latest versión for your OS.
### Safari Driver
Safari and Safari Technology Preview each provide their own safaridriver executable. Make sure you already have the executable on your device:
* Safari’s executable is located at /usr/bin/safaridriver.
* Safari Technology Preview's executable is part of the application bundle’s contents.

### Edge Driver

Go to the [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) and download the latest versión for your OS.

--- 
## Use the driver with Selenium
Save the driver in a directory and get the directory's path.

Use the path to create a Service instance as:
```py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Create a service and browser instance
service_obj = Service('/Users/YourUSer/Documents/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service_obj)

# Visit a web page and finish interaction
driver.get('https://www.google.com/')
driver.close()
```


### Iniciar Selenium Webdriver - descargando el driver manualmente

Para realizar esto hay que descargar previamente el driver de la versión de Chrome instalada en el equipo. Se puede descargar desde https://googlechromelabs.github.io/chrome-for-testing/

https://chromedriver.chromium.org/downloads