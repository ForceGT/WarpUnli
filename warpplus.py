import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options




def getthefreebies():
    time.sleep(10)  # waits for page load
    canvas = firefox.find_element_by_class_name("xterm-helper-textarea")
    canvas.send_keys("")  # to focus on the textarea
    canvas.send_keys(key)  # send user key
    canvas.send_keys(Keys.RETURN)  # imitate Enter

def runagain():
    button = firefox.find_element_by_css_selector("#restart-bar > button:nth-child(1)")
    button.click()
    getthefreebies()


if __name__ == "__main__":
	options = Options()
	options.headless = True # Makes it quite /headless
    firefox = webdriver.Firefox(options=options)
    firefox.get("https://thepremiumxcom.ramashankark.repl.run/")
    # key = "4d3490fd-4690-47ac-8ea4-4ff24a329e36"
    print("\n\n\n Welcome to the Warp+ Data Credit Script "
          "All you have to do is enter your ID and enter the number of times you want the script to run"
          "The total data credited will be 2x the number of runs"
          "Use at your own risk\n\n\n Make sure you have GeckoDriver for Firefox and selenium installed"
		  "You can install selenium by pip and get GeckoDriver from Mozilla's Github Page"
          "NOTE:You can edit the time.sleep and set the number of seconds "
          "to wait for the page load according to your internet speed\n\n\n\n\n\n"
          "Made with <3 by ForceGT(Find me on Github) \n\n")
    key = input("Enter the key: ")
    n = int(input("Enter the number of times you want the script to run: "))
    getthefreebies()
    for i in range(0, n-1):
        print(f"Here goes Run No {i+1}")
        runagain()
    print(f"\n\nThe script ran for {n} time(s).\n Total data credited is: {2*n}")

