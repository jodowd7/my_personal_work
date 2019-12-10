def google_search(k):
    import os
    import selenium
    os.path.dirname(os.path.abspath(__file__))
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    # get the path of ChromeDriverServer
    # dir=os.path.dirname(__file__) --> manually placed chromedriver.exe in C:\Python34\Scripts
    # create a new chrome session
    # driver=webdriver.chrome
    driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
    driver.implicitly_wait(30)
    driver.maximize_window()
    # navigate to the application home page
    driver.get("http://www.google.com")
    # get the search  textbox  via right click and INSPECT page, navigate to Elements tab input "name"= "q"
    search_field = driver.find_element_by_name("q")
    # enter search keyword and submit
    search_field.send_keys(k)
    search_field.submit()
    # get the list of elements which are displayed after the search
    # currently on result page using find_elements_by_class_name method
    lists = driver.find_elements_by_class_name("r")
    # get the number of elements found
    print("Found " + str(len(lists)) + " searches:")

    # iterate through each element and print the text that is
    # name of the search

    i = 0
    for listitem in lists:
        print(listitem.get_attribute("innerHTML"))
        i = i + 1
        if (i > 10):
            break

    # close the browser window
    driver.quit()

google_search('houston, tx')