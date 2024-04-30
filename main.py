from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import pytz
import time
import random
#Constants
pageLoadTime=3 #How long you want each page to take before inputting (currently set to 3 seconds)
ca_timezone=pytz.timezone('America/Los_Angeles')
available_numbers = list(range(101))
mcdonalds_sentences = [
    "I had a wonderful experience at this McDonald's. The staff were friendly and the food was delicious.",
    "This McDonald's location is outstanding. The service is impeccable and the food is consistently delicious!",
    "The staff at this McDonald's were incredibly friendly and accommodating, making my visit enjoyable.",
    "I highly recommend dining at this McDonald's. The staff provided excellent service and the food was great.",
    "The service at this McDonald's was exceptional. The staff went above and beyond to ensure a pleasant experience.",
    "This McDonald's exceeded my expectations. The staff were attentive and the food was delicious.",
    "The atmosphere at this McDonald's was inviting and the food was fresh and flavorful.",
    "I had a fantastic experience at this McDonald's. The staff were courteous and the food was served promptly.",
    "The staff at this McDonald's were welcoming and efficient, making my visit enjoyable.",
    "I had a positive experience at this McDonald's. The staff were attentive and the food was delicious.",
    "This McDonald's is my go-to spot for a quick and tasty meal. The staff are always friendly and efficient.",
    "The staff at this McDonald's were friendly and helpful, creating a pleasant dining experience.",
    "I was thoroughly impressed by this McDonald's. The staff were efficient and the dining area was clean.",
    "This McDonald's location is my favorite. The staff always make me feel welcome and the food is consistently good.",
    "I had a great experience at this McDonald's. The staff were courteous and the food was delicious.",
    "The service at this McDonald's was outstanding. The staff were attentive and the food was served quickly.",
    "I had a wonderful meal at this McDonald's. The food was fresh and the service was prompt.",
    "The staff at this McDonald's were friendly and efficient, making my visit enjoyable.",
    "This McDonald's location is exceptional. The staff are always friendly and the food is consistently delicious.",
    "I had a great time at this McDonald's. The staff were friendly and the service was excellent.",
    "The service at this McDonald's was exceptional. The staff were friendly and accommodating.",
    "This McDonald's location is outstanding. The service is impeccable and the food is consistently delicious!",
    "The food at this McDonald's was delicious and the staff were friendly and attentive.",
    "I had an enjoyable dining experience at this McDonald's. The staff were welcoming and the food was great.",
    "This McDonald's is one of my favorites. The staff are always friendly and the food is consistently good.",
    "The staff at this McDonald's were friendly and helpful, making my visit pleasant.",
    "I had a satisfying meal at this McDonald's. The food was tasty and the service was efficient.",
    "The service at this McDonald's was exceptional. The staff were friendly and attentive.",
    "This McDonald's location is top-notch. The staff are friendly and the food is always fresh and tasty.",
    "I had a great experience at this McDonald's. The staff were welcoming and the food was delicious.",
    "The service at this McDonald's was exceptional. The staff were friendly and accommodating.",
    "This McDonald's location is outstanding. The service is impeccable and the food is consistently delicious!",
    "I had a wonderful experience at this McDonald's. The staff were friendly and the food was delicious.",
    "The staff at this McDonald's were incredibly friendly and accommodating, making my visit enjoyable.",
    "I highly recommend dining at this McDonald's. The staff provided excellent service and the food was great.",
    "The service at this McDonald's was exceptional. The staff went above and beyond to ensure a pleasant experience.",
    "This McDonald's exceeded my expectations. The staff were attentive and the food was delicious.",
    "The atmosphere at this McDonald's was inviting and the food was fresh and flavorful.",
    "I had a fantastic experience at this McDonald's. The staff were courteous and the food was served promptly.",
    "The staff at this McDonald's were welcoming and efficient, making my visit enjoyable.",
    "I had a positive experience at this McDonald's. The staff were attentive and the food was delicious.",
    "This McDonald's is my go-to spot for a quick and tasty meal. The staff are always friendly and efficient.",
    "The staff at this McDonald's were friendly and helpful, creating a pleasant dining experience.",
    "I was thoroughly impressed by this McDonald's. The staff were efficient and the dining area was clean.",
    "This McDonald's location is my favorite. The staff always make me feel welcome and the food is consistently good.",
    "I had a great experience at this McDonald's. The staff were courteous and the food was delicious.",
    "The service at this McDonald's was outstanding. The staff were attentive and the food was served quickly.",
    "I had a wonderful meal at this McDonald's. The food was fresh and the service was prompt.",
    "The staff at this McDonald's were friendly and efficient, making my visit enjoyable.",
    "This McDonald's location is exceptional. The staff are always friendly and the food is consistently delicious.",
    "I had a great time at this McDonald's. The staff were friendly and the service was excellent.",
    "The service at this McDonald's was exceptional. The staff were friendly and accommodating."
]
def generate_unique_transaction_number():
    # Generate a random index within the range of available numbers
    random_index = random.randint(0, len(available_numbers) - 1)
    # Pop and return the number at the random index from the available numbers list
    unique_number = available_numbers.pop(random_index)
    print(unique_number)
    return unique_number

def generate_unique_mcdonalds_sentence(available_sentences):
    # Check if there are available sentences left
    if available_sentences:
        random_index = random.randint(0, len(available_sentences) - 1)
        unique_sentence = available_sentences.pop(random_index)
        return unique_sentence
    else:
        print("No more McDonald's sentences available.")
        return None
def reset_available_numbers():
    # Reset the available numbers list to contain numbers from 0 to 100
    available_numbers.extend(range(101))
def storeInfo(store_id):
  input_element = driver.find_element(By.ID,"InputStoreID")
  input_element.click()
  input_element.send_keys(store_id)
  time.sleep(.2)
  # Register num
  RegisterNum = ["1","2","13"]
  input_element = driver.find_element(By.ID,"InputRegisterNum")
  input_element.click()
  input_element.send_keys(RegisterNum[random.randint(0,2)])
  time.sleep(.2)
  dropdownMonth= driver.find_element(By.ID,'InputMonth')
  dropdownDay= driver.find_element(By.ID,'InputDay')
  dropdownHour=driver.find_element(By.ID,'InputHour')
  dropdownMinute=driver.find_element(By.ID,'InputMinute')

  # Month
  dropdown = Select(dropdownMonth)
  dropdown.select_by_index(random.randint(1,4))
  time.sleep(.2)
  # Day
  dropdown = Select(dropdownDay)
  dropdown.select_by_index(random.randint(1,28))
  time.sleep(.2)
  # Time Hour
  dropdown = Select(dropdownHour)
  dropdown.select_by_index(random.randint(12,23))
  time.sleep(.2)

  # Time Minutes
  dropdown = Select(dropdownMinute)
  dropdown.select_by_index(random.randint(0,59))
  time.sleep(.2)

  # Order
  input_element = driver.find_element(By.ID,"InputTransactionNum")
  input_element.click()
  input_element.send_keys(str(generate_unique_transaction_number()))
  time.sleep(.2)

   # Amount 1
  input_element = driver.find_element(By.ID,"AmountSpent1")
  input_element.click()
  input_element.send_keys(str(random.randint(5,10)))
  time.sleep(.2)

  # Amount 2
  input_element = driver.find_element(By.ID,"AmountSpent2")
  input_element.click()
  input_element.send_keys(str(random.randint(0,99)))
  time.sleep(.2)
  NextButton()
def enterSurveyCode(surveyInfo):
    # Split the code into groups of 5 digits each
    groups_of_five = [surveyInfo['code'][i:i + 5] for i in range(0, len(surveyInfo['code']) - 1, 5)]

    # Add the remaining digit to the last group
    groups_of_five.append(surveyInfo['code'][-1])

    print("Survey Code: ", groups_of_five)

    # Iterate over each group and send it to the corresponding input element
    for i, group in enumerate(groups_of_five, start=1):
        input_element = driver.find_element(By.ID, f"CN{i}")
        input_element.click()
        input_element.send_keys(group)
        time.sleep(0.2)
    NextButton()
def rateSatisfaction():
  time.sleep(pageLoadTime)
  labels = driver.find_elements(By.CSS_SELECTOR, "label[for^='R'][for$='.5']")
  # Loop through each label element and click it
  for label in labels:
    label.click()
  time.sleep(.5)
  NextButton()
def randomItem():
  time.sleep(pageLoadTime)
  # Find all checkbox elements
  checkboxes = driver.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
  random.shuffle(checkboxes)
  checkboxes_to_select=checkboxes[:2]
  for checkbox in checkboxes_to_select:
     driver.execute_script("arguments[0].click();",checkbox)
     time.sleep(.5)
  NextButton()

#textR000345 Did an employee visit your table after you received your order?
def employeeVisit():
    time.sleep(pageLoadTime)
    try:
        input_element = driver.find_element(By.ID, "R000345.1")
        driver.execute_script("arguments[0].click();",input_element)
        NextButton()
    except NoSuchElementException:
        pass  # Element not found, do nothing

def eap():
    time.sleep(pageLoadTime)
    try:
        check = driver.find_element(By.ID, 'textR016000')
        if check.get_attribute("innerText") == 'Did you experience a problem during your visit?':
            input_element = driver.find_element(By.ID, "R016000.2")
            driver.execute_script("arguments[0].click();",input_element)
            NextButton()
    except NoSuchElementException:
        pass  # Element not found, do nothing
def mcdonaldsRewards():
   time.sleep(pageLoadTime)
   label_element = driver.find_element(By.ID, "R000444.1")
   driver.execute_script("arguments[0].click();", label_element)
   NextButton()
def mcondalsAsk():
   time.sleep(pageLoadTime)
   label_element = driver.find_element(By.ID, "R000473.1")
   driver.execute_script("arguments[0].click();", label_element)
   NextButton()
def employeeThank():
   time.sleep(pageLoadTime)
   label_element = driver.find_element(By.ID, "R000474.1")
   driver.execute_script("arguments[0].click();", label_element)
   NextButton()
def whatOrder(surveyOption):
  surveyOption = int(surveyOption)
  if(surveyOption==1):
     print("Breakfast option 1")
     id='R000504'
  else:
     print("Burgers option 2")
     id='R000505'
  time.sleep(pageLoadTime)
  label_element = driver.find_element(By.ID, id)
  driver.execute_script("arguments[0].click();", label_element)
  NextButton()
def howOrder():
   time.sleep(pageLoadTime)
   random_index= random.randint(1,3)
   label_element = driver.find_element(By.ID, f"R000455.{random_index}")
   driver.execute_script("arguments[0].click();", label_element)
   NextButton()
   time.sleep(pageLoadTime)
   if(random_index==2):
      shuffle= random.choice([1,3])
      label_element = driver.find_element(By.ID, f"R004000.{shuffle}")
      driver.execute_script("arguments[0].click();", label_element)
      NextButton()
   else:
      random_index= random.randint(1,3)
      label_element = driver.find_element(By.ID, f"R004000.{random_index}")
      driver.execute_script("arguments[0].click();", label_element)
      NextButton()
def commentReview():
  time.sleep(pageLoadTime)
  input_element = driver.find_element(By.ID,"S081000")
  input_element.click()
  text = generate_unique_mcdonalds_sentence(mcdonalds_sentences)
  print('Review: ',text)
  input_element.send_keys(text)
  NextButton()
def numOfVisits():
   time.sleep(pageLoadTime)
   random_index = random.randint(1,4)
   radio_button = driver.find_element(By.ID,f"R020000.{random_index}")
   driver.execute_script("arguments[0].click();", radio_button)
   NextButton()
def favoriteRestaurant():
   time.sleep(pageLoadTime)
   random_index = random.randint(1,4)
   radio_button = driver.find_element(By.ID,f"R000387.{random_index}")
   driver.execute_script("arguments[0].click();", radio_button)
   NextButton()
def currentState(id):
    try:
       driver.find_element(By.ID,id)
       return True
    except NoSuchElementException:
        return False
def NextButton():
  NextButton = driver.find_element(By.ID,"NextButton");
  NextButton.click();
def driveThruPull():
   time.sleep(pageLoadTime)
   radio_button = driver.find_element(By.ID,"R000026.2")
   driver.execute_script("arguments[0].click();", radio_button)
   NextButton()
def correctStore():
   time.sleep(pageLoadTime)
   radio_button = driver.find_element(By.ID,"R000060.1")
   driver.execute_script("arguments[0].click();", radio_button)
   NextButton()
def checkAndRunQuestions(surveyOption):
    survey_done = False
    remaining_questions = possibleQuestions.copy()  # Make a copy of the original dictionary
    while not survey_done:
        for question_id, question_function in list(remaining_questions.items()):
            try:   
                driver.find_element(By.ID, question_id)
                if(question_id == 'textBlock800'):
                   question_function(surveyOption)
                else:
                    question_function()
                if(question_id == 'textBlock9475'):
                   survey_done = True
                # Remove the answered question from the dictionary
                if(question_id!='textBlock300'):
                   remaining_questions.pop(question_id, None)
            except NoSuchElementException:
                continue  # Move to the next question if the current one is not found
def get_survey_info(survey_info):
    for i in range(1, numOfSurveys + 1):
        while True:
            code = input(f"Enter the survey code for survey {i} (26 digits, no dashes or spaces): ")
            if len(code) != 26:
                print("Invalid code length. Please enter a 26-digit code.")
            else:
                break
        option = input(f"Enter the number 1 (breakfast) or 2 (lunch) for survey {i}: ")
        survey_info.append({"code": code, "option": option})
def read_survey_info(survey_info):
    filename = 'voiceReceipts.txt'  # Name of the file containing survey information
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            code = lines[i].strip()  
            option = lines[i+1].strip()  
            survey_info.append({"code": code, "option": option})
def demographics():
  dropdownGender= driver.find_element(By.ID,'R022000')
  dropdownAge= driver.find_element(By.ID,'R023000')
  dropdownAge2=driver.find_element(By.ID,'R000206')
  dropdownIncome=driver.find_element(By.ID,'R024000')
  dropdownPlace=driver.find_element(By.ID,'R025000')

  # Gender
  dropdown = Select(dropdownGender)
  dropdown.select_by_index(random.randint(1,2))
  time.sleep(.2)
  # Age
  dropdown = Select(dropdownAge)
  dropdown.select_by_index(random.randint(1,5))
  time.sleep(.2)
  # Age2
  dropdown = Select(dropdownAge2)
  dropdown.select_by_index(random.randint(1,2))
  time.sleep(.2)
  # Income
  dropdown = Select(dropdownIncome)
  dropdown.select_by_index(random.randint(1,6))
  time.sleep(.2)
  # Race
  dropdown = Select(dropdownPlace)
  dropdown.select_by_index(random.randint(1,5))
  time.sleep(.2)
  NextButton()
# options=Options()
# PROXY='100.1.53.24:5678';
options=webdriver.ChromeOptions() 
# options.add_argument('--proxy-server=%s' % PROXY)
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")
options.add_argument("--log-level=3")  # Suppress console messages
# options.add_experimental_option("detach",True)
service=Service("chromedriver.exe")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver=webdriver.Chrome(service=service,options=options)
possibleQuestions = {
    "textR001000": rateSatisfaction,
    "textR000444": mcdonaldsRewards,
    "textR000473": mcondalsAsk,
    "textR001000": rateSatisfaction,
    "textR000474": employeeThank,
    "textBlock300": rateSatisfaction,
    "textBlock900": rateSatisfaction,
    "textBlock800": whatOrder,
    "textBlock850": randomItem,
    "textBlock825": randomItem,
    "textBlock875": randomItem,
    "textBlock885": randomItem,
    "textR016000": eap,
    "textBlock1500": rateSatisfaction,
    "textS081000": commentReview,
    "textR000345": employeeVisit,
    "textBlock8200": numOfVisits,
    "textR000387": favoriteRestaurant,
    "textBlock9475": rateSatisfaction,
    "textS000100":howOrder,
    "textR000026": driveThruPull,
    "textBlock9500": demographics,
    "textR000060": correctStore
}

#=========================================================================Code Begins==================================================
# numOfSurveys = int(input("Enter the number of surveys you wish to input: "))
choice = input("Enter 1 for survey_codes | Enter 2 for no survey_codes: ");
if(choice=="1"):
    survey_info =[]
    read_survey_info(survey_info)
    print("Survey:",survey_info)
    time.sleep(2)
    count = 1
    for survey in survey_info:
        driver.get('https://www.mcdvoice.com/')
        time.sleep(1.5)
        enterSurveyCode(survey)  # Enter the survey code for the current survey
        time.sleep(1)
        checkAndRunQuestions(survey['option']);
        time.sleep(1)
        driver.quit()
        current_time = datetime.now(ca_timezone)
        current_time_12_hour = current_time.strftime("%Y-%m-%d %I:%M:%S %p")
        print("Survey " + str(count) + " finished at " + current_time_12_hour)
        count+=1
        driver=webdriver.Chrome(service=service,options=options)
else:
    numOfSurvey=int(input("Enter number of surveys you wish for it to run "))
    store_id= input("Enter store ID: ")
    count=1
    for i in range(numOfSurvey):
       random_index = random.randint(1,2)
       driver.get('https://www.mcdvoice.com/Index.aspx?POSType=PieceMeal')
       time.sleep(1)
       storeInfo(store_id)
       time.sleep(1)
       checkAndRunQuestions(random_index)
       time.sleep(1)
       driver.quit()
       current_time = datetime.now(ca_timezone)
       current_time_12_hour = current_time.strftime("%Y-%m-%d %I:%M:%S %p")
       print("Survey " + str(count) + " finished at " + current_time_12_hour)
       count+=1
       driver=webdriver.Chrome(service=service,options=options)




