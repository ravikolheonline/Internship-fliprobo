#!/usr/bin/env python
# coding: utf-8

# # Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data. This task will be done in following steps: 
# 1. First get the webpage https://www.naukri.com/
# 2. Enter “Data Analyst” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the location” field.
# 3. Then click the search button.
# 4. Then scrape the data for the first 10 jobs results you get. 
# 5. Finally create a dataframe of the scraped data. 

# In[1]:


import pandas as pd
import numpy as np
import selenium
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException 
from selenium.webdriver.common.by import By
import time


# In[4]:


driver= webdriver.Chrome(r"C:\Users\Dell\Downloads\chromedriver.exe")


# In[5]:


driver.get("https://www.naukri.com/")


# In[6]:


designation =driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Analyst')


# In[7]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys('Bengalore')


# In[8]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[9]:


job_title1=[]
job_location1=[]
company_name1=[]
experienced_required1=[]


# In[10]:


#Scaping the job_title from given page
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title1.append(title)
#Scaping the job_locaion from given page
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location1.append(location)
#Scaping the company_name from given page
company_tags=driver.find_elements(By.XPATH, '//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    name=i.text
    company_name1.append(name)
#Scaping the experienced_required from given page
experience_tags=driver.find_elements(By.XPATH, '//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[0:10]:
    exp=i.text
    experienced_required1.append(exp)


# In[11]:


print(len(job_title1))
print(len(job_location1))
print(len(company_name1))
print(len(experienced_required1))


# In[12]:


df=pd.DataFrame({'Title':job_title1, 'Location':job_location1,  'Company_name':company_name1, 'Experience':experienced_required1})
df


# # Q2: Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data. This task will be done in following steps:
# 1. First get the webpage https://www.naukri.com/
# 2.  Enter “Data Scientist” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the location” field.
# 3. Then click the search button.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.
# Note: All of the above steps have to be done in code. No step is to be done manually.

# In[13]:


driver= webdriver.Chrome(r"C:\Users\Dell\Downloads\chromedriver.exe")


# In[14]:


driver.get("https://www.naukri.com/")


# In[15]:


designation =driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Scientist')


# In[16]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys('Bengalore')


# In[17]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[18]:


job_title=[]
job_location=[]
company_name=[]
experienced_required=[]


# In[19]:


#Scaping the job_title from given page
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
#Scaping the job_locaion from given page
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
#Scaping the company_name from given page
company_tags=driver.find_elements(By.XPATH, '//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    name=i.text
    company_name.append(name)
#Scaping the experienced_required from given page
experience_tags=driver.find_elements(By.XPATH, '//span[@class="ellipsis fleft expwdth"]')
for i in experience_tags[0:10]:
    exp=i.text
    experienced_required.append(exp)


# In[20]:


print(len(job_title))
print(len(job_location))
print(len(company_name))
print(len(experienced_required))


# In[21]:


df=pd.DataFrame({'Title':job_title, 'Location':job_location,  'Company_name':company_name, 'Experience':experienced_required})
df

Q3: In this question you have to scrape data using the filters available on the webpage as shown below: 
        You have to use the location and salary filter. 
        You have to scrape data for “Data Scientist” designation for first 10 job results. 
        You have to scrape the job-title, job-location, company name, experience required.
        The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs 
 The task will be done as shown in the below steps: 
        1. first get the webpage https://www.naukri.com/
        2. Enter “Data Scientist” in “Skill, Designations, and Companies” field. 
        3. Then click the search button. 
        4. Then apply the location filter and salary filter by checking the respective boxes 
        5. Then scrape the data for the first 10 jobs results you get. 
        6. Finally create a dataframe of the scraped data.
        Note: All of the above steps have to be done in code. No step is to be done manually.
# In[68]:


driver= webdriver.Chrome(r"C:\Users\Dell\Downloads\chromedriver.exe")


# In[69]:


driver.get(" https://www.naukri.com/")


# In[70]:


designation= driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Scientist')


# In[71]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys('Delhi/NCR')


# In[66]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[57]:


title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
titles1=[]
for i in title_tags:
    titles1.append(i.text)


# In[58]:


Exp_tag=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
experience1=[]
for i in Exp_tag:
    experience1.append(i.text)


# In[59]:


location_tag=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
location1=[]
for i in location_tag:
    location1.append(i.text)


# In[60]:


company_tag=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
company1=[]
for i in company_tag:
    company1.append(i.text)


# In[61]:


print(len(titles1),len(location1),len(company1),len(experience1))

df=pd.DataFrame({'Title':titles1, 'Location':location1,  'Company_name': company1, 'Experience':experience1})
df
# In[62]:


df=pd.DataFrame({'Title':titles1, 'Location':location1,  'Company_name': company1, 'Experience':experience1})
df

# Scaping the job_title from given page
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title2.append(title)
#Scaping the experienced_required from given page
salary_offered=driver.find_elements(By.XPATH, '//span[@class="ellipsis fleft "]')
for i in salary_offered[0:10]:
    salary = i.text
salary_offered2.append(salary)
#Scaping the job_locaion from given page
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location2.append(location)
#Scaping the company_name from given page
company_tags=driver.find_elements(By.XPATH, '//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    name=i.text
    company_name2.append(name)
# In[ ]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys('Delhi/NCR')


# In[ ]:


salary_offered=driver.find_elements(By.XPATH, '//span[@class="ellipsis fleft "]')
salary.send_keys('“3-6” ')


# In[12]:


#Scaping the job_title from given page
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title2.append(title)
#Scaping the experienced_required from given page
salary_offered=driver.find_elements(By.XPATH, '//span[@class="ellipsis fleft "]')
for i in salary_offered[0:10]:
    salary = i.text
salary_offered2.append(salary)
#Scaping the job_locaion from given page
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location2.append(location)
#Scaping the company_name from given page
company_tags=driver.find_elements(By.XPATH, '//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    name=i.text
    company_name2.append(name)

Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes: 
 1. Brand 2. Product Description  3.  Price
The attributes which you have to scrape is ticked marked in the below image
To scrape the data you have to go through following steps:
1. Go to Flipkart webpage by url : https://www.flipkart.com/ 
2. Enter “sunglasses” in the search field where “search for products, brands and more”  is written and click the search icon 
3. After that you will reach to the page having a lot of sunglasses.From this page you can scrap the required data as usual. 
4. After scraping data from the first page, go to the “Next” Button at the bottom other page , then click on it.
5. Now scrape data from this page as usual 
6. Repeat this until you get data for 100 sunglasses. 
# In[39]:


import pandas as pd
import numpy as np
import selenium
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException 
from selenium.webdriver.common.by import By
import time


# In[49]:


driver= webdriver.Chrome(r"C:\Users\Dell\Downloads\chromedriver.exe")


# In[50]:


driver.get("https://www.flipkart.com/")


# In[51]:


designation=driver.find_element(By.CLASS_NAME,"_3704LK")
designation.send_keys('sunglasses')


# In[53]:


search=driver.find_element(By.CLASS_NAME,"_34RNph")
search.click()


# In[54]:


Brand2=[]
Product_Description2=[]
Price2=[] 


# In[71]:


#Scaping the Brand from given page
Brand_name=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in Brand_name[0:100]:
    Br_name=i.text
    Brand2.append(Br_name)
#Scaping the Price from given page
Price_details=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in Price_details[0:100]:
    pr_details=i.text
    Price2.append(pr_details)
#Scaping the Product_Description from given page
Product_Description_details=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in Product_Description_details[0:100]:
    description=i.text
    Product_Description2.append(description)
search=driver.find_element(By.XPATH,'//a[@class="ge-49M"]')
search.click()


# In[72]:


print(len(Brand2))
print(len(Price2))
print(len(Product_Description2))


# In[75]:


Brand=Brand2[:100]
Product_Description=Product_Description2[:100]
Price=Price2[:100] 


# In[76]:


print(len(Brand))
print(len(Price))
print(len(Product_Description))


# In[77]:


df=pd.DataFrame({'Brand':Brand, 'Product_Description':Product_Description,  'Price':Price})
df


# In[ ]:




# Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link: 
https://www.flipkart.com/apple-iphone-11-black-64-gb/product- reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market place=FLIPKART
As shown in the above page you have to scrape the tick marked attributes
These are: 1. Rating 2. Review summary 3. Full review 4. You have to scrape this data for first 100 reviews.
# In[ ]:


import pandas as pd
import numpy as np
import selenium
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException 
from selenium.webdriver.common.by import By
import time


# In[7]:


driver= webdriver.Chrome(r"C:\Users\Dell\Downloads\chromedriver.exe")


# In[8]:


driver=webdriver.Chrome("chromedriver")
driver.get("https://www.flipkart.com/")


# In[12]:


driver.get("https://www.flipkart.com/apple-iphone-11-black-64-gb/product- reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market place=FLIPKART")


# In[ ]:


designation= driver.find_element(By.CLASS_NAME,"_3704LK")
designation.send_keys('iphone11')


# In[ ]:


search=driver.find_element(By.CLASS_NAME,"_34RNph")
search.click()


# In[ ]:


Rating=[]
Review_summary=[] 
Full_review=[]


# In[ ]:


#Scaping the rating  from given page
Rating_number=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in Rating_number[0:100]:
    rating_num=i.text
    Rating.append(rating_num)
#Scaping the Review_summary from given page
Review_summary_details=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in Review_summary_details[0:100]:
    summery=i.text
    Review_summary.append(summery)
#Scaping the Full review from given page
Full_review_details=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in Full_review_details[0:100]:
    review=i.text
    Full_review.append(review)


# In[ ]:


print(len(Rating))
print(len(Review_summary))
print(len(Full_review))


# In[ ]:


df=pd.DataFrame({'Ratings':Rating, 'Review summary':Review_summary,  'Full review':Full_review})
df


# In[ ]:


# Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link: 
https://www.flipkart.com/apple-iphone-11-black-64-gb/product- reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market place=FLIPKART
As shown in the above page you have to scrape the tick marked attributes
These are: 1. Rating 2. Review summary 3. Full review 4. You have to scrape this data for first 100 reviews.


# In[22]:


driver=webdriver.Chrome("chromedriver")
driver.get("https://www.flipkart.com/")


# In[76]:


ratings = driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
review_summary = driver.find_elements(By.CLASS_NAME,"_2-N8zT")
full_review = driver.find_elements(By.CLASS_NAME,"t-ZTKy")


# In[105]:


# for holding the resultant list
rating_list1 = []
review_list2= []
fill_review_list3= []


# In[106]:


for i in range(len(ratings)):
    rating_list1.append([ratings[i].text])
    review_list2.append([review_summary[i].text])
    fill_review_list3.append([full_review[i].text.replace("\n","")])


# In[107]:


print(len(rating_list1))
print(len(review_list2))
print(len(fill_review_list3))


# In[109]:


rating_list1 


# In[110]:


review_list2


# In[111]:


fill_review_list3


# In[112]:


Df=pd.DataFrame({})
Df['RATINGS']=rating_list1[:100]
Df['REVIEW_SUMMARY']=review_list2[:100]
Df['FULL_REVIEW']=fill_review_list3[:100]
Df


# In[ ]:


Q6: Scrape data for first 100 sneakers you find when you visit flipkart.com and search for “sneakers” in the search field. 
You have to scrape 3 attributes of each sneaker: 1. Brand 2. Product Description 3. Price 
As shown in the below image, you have to scrape the above attributes. 


# In[ ]:


driver= webdriver.Chrome(r"C:\Users\Dell\Downloads\chromedriver.exe")


# In[ ]:


driver.get(" https://www.flipkart.com/")


# In[167]:


designation=driver.find_element(By.CLASS_NAME,"_3704LK")
designation.send_keys('sneakers')


# In[ ]:


search=driver.find_element(By.CLASS_NAME,"_34RNph")
search.click()


# In[ ]:


page_url = "https://www.flipkart.com/search?q=sneakers&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off" + str(page)
    driver.get(page_url)


# In[96]:


Brand3=[]
Product_Description3=[]
Price3=[] 


# In[101]:


#Scaping the Brand from given page
Brand_name=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in Brand_name[0:100]:
    Br_name=i.text
    Brand3.append(Br_name)
#Scaping the Product_Description from given page
Product_Description_details=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in Product_Description_details[0:100]:
    description=i.text
    Product_Description3.append(description)
#Scaping the Price from given page
Price_details=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in Price_details[0:100]:
    pr_details=i.text
    Price3.append(pr_details)
search=driver.find_element(By.XPATH,'//a[@class="ge-49M"]')
search.click()


# In[102]:


print(len(Brand3))
print(len(Product_Description3))
print(len(Price3))


# In[106]:


S_Brand=Brand3[:100]
S_Product_Description=Product_Description3[:100]
S_Price=Price3[:100] 


# In[107]:


print(len(S_Brand))
print(len(S_Price))
print(len(S_Product_Description))


# In[108]:


df=pd.DataFrame({'Brand':S_Brand, 'Product_Description':S_Product_Description,  'Price':S_Price})
df

Q7: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. 
Then  set CPU Type filter to “Intel Core i7” as shown in the below image: 
After setting the filters scrape first 10 laptops data. 
You have to scrape 3 attributes for each laptop:
1. Title 2. Ratings 3. Price 
# In[70]:


driver= webdriver.Chrome(r"C:\Users\Dell\Downloads\chromedriver.exe")


# In[71]:


driver.get("https://www.amazon.in/")


# In[72]:


search_tag=driver.find_element(By.XPATH,'//input[@id="twotabsearchtextbox"]')
search_tag


# In[73]:


search_tag.send_keys("laptops")


# In[74]:


search_btn=driver.find_element(By.XPATH,'//input[@id="nav-search-submit-button"]')
search_btn


# In[75]:


search_btn.click()


# In[76]:


driver.get("https://www.amazon.in/s?k=laptops&ref=nb_sb_noss_2")


# In[77]:


filter_button=driver.find_elements(By.XPATH,"//a[@class='a-link-normal s-navigation-item']")
for i in filter_button:
    if i.text=='Intel Core i7':
        i.click()
        break


# In[36]:


filter_button=driver.find_elements(By.XPATH,"//a[@class='a-link-normal s-navigation-item']")
for i in filter_button:
    if i.text=='Intel Core i9':
        i.click()
        break


# In[78]:


urls=[]
for i in driver.find_elements(By.XPATH,'//a[@class="a-link-normal a-text-normal"]'):
    urls.append(i.get_attribute("href"))


# In[79]:


urls


# In[80]:


len(urls)


# In[95]:


title2=[]
Ratings2=[]
Price2=[]


# In[83]:


title_tag=driver.find_elements(By.XPATH,'//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]')
for i in title_tag:
    title2.append(i.text.replace("/n",""))
title2


# In[89]:


rating2=[]


# In[ ]:


ratings_tags=driver.find_element(By.XPATH,'//span[@class="a-size-base s-underline-text"]')
for i in ratings_tags:
    rating2.append(i.text)
rating2


# In[92]:


for i in urls[:10]:
    driver.get(i)
    time.sleep(2)
    
    try:
        ratings_tags=driver.find_element(By.XPATH,'//span[@class="a-size-base"]')
        ratings.append(ratings_tags.text)
    except:
        ratings.append('-')


# In[96]:


price_tag=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for i in price_tag:
    Price2.append(i.text)
Price2


# In[97]:


print(len(title2))
print(len(Ratings2))
print(len(Price2))


# In[ ]:


df_laptop=pd.DataFrame({})
df_laptop['Title']=title[:10]
df_laptop['Ratings']=ratings[:10]
df_laptop['Price']=price[:10]
df_laptop


# In[ ]:


designation=driver.find_element(By.CLASS_NAME,"a-js a-audio a-video a-canvas a-svg a-drag-drop a-geolocation a-history a-webworker a-autofocus a-input-placeholder a-textarea-placeholder a-local-storage a-gradients a-transform3d a-touch-scrolling a-text-shadow a-text-stroke a-box-shadow a-border-radius a-border-image a-opacity a-transform a-transition null")
designation.send_keys('Laptop')


# In[ ]:


designation=driver.find_elements(By.CLASS_NAME,"nav-input nav-progressive-attribute")
designation.send_keys('Laptop')


# In[ ]:


Title=[] 
Ratings=[] 
Price=[] 


# In[ ]:


#Scaping the Title from given page
title_name=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_name[0:10]:
    title=i.text
    Title.append(title)
#Scaping the rating  from given page
Rating_number=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in Rating_number[0:100]:
    rating_num=i.text
    Ratings.append(rating_num)
#Scaping the Price from given page
Price_details=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in Price_details[0:100]:
    pr_details=i.text
    Price.append(pr_details)


# In[ ]:


df=pd.Dataframe({'Title':Title,'Ratings':Ratings, 'Price':Price})
df


# In[ ]:




Q8: Write a python program to scrape data for Top 1000 Quotes of All Time. 
The above task will be done in following steps:
1.First get the webpage https://www.azquotes.com/ 
2. Click on Top Quotes 
3.Than scrap a) Quote b) Author c) Type Of Quotes 
# In[108]:


driver= webdriver.Chrome(r"C:\Users\Dell\Downloads\chromedriver.exe")


# In[109]:


driver.get("https://www.azquotes.com/")


# In[ ]:


top_quotes=driver.find_element(By.XPATH,'//[@class="front"]')


# In[ ]:


search=driver.find_element(By.XPATH,'//[@class="front"]')
search.click()


# In[114]:


Quote2=[] 
Author_name2=[] 
Type_Of_Quotes2=[]


# In[119]:


#Scaping the Quote  from given page
quote_title=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in quote_title[0:100]:
    title4=i.text
    Quote2.append(title4)
#Scaping the Author from given page
Author_name=driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in Author_name[0:100]:
    author1=i.text
    Author_name2.append(author1)
#Scaping the Type Of Quotes from given page
types_of_quote=driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in types_of_quote[0:100]:
    types=i.text
    Type_Of_Quotes2.append(types)


# In[120]:


print(len(Quote2)) 
print(len(Author_name2)) 
print(len(Type_Of_Quotes2))


# In[121]:


df=pd.DataFrame({'Quote':Quote2, 'Author':Author_name2,  'Type of Quotes':Type_Of_Quotes2})
df

Q9: Write a python program to display list of respected former Prime Ministers of India
    (i.e. Name, Born-Dead, Term of office, Remarks) 
    from https://www.jagranjosh.com/. 
 This task will be done in following steps: 
1. First get the webpage https://www.jagranjosh.com/ 
2. Then You have to click on the GK option 
3. Then click on the List of all Prime Ministers of India
4. Then scrap the mentioned data and make the DataFrame.
# In[137]:


driver= webdriver.Chrome(r"C:\Users\Dell\Downloads\chromedriver.exe")


# In[140]:


driver.get("https://www.jagranjosh.com/")


# In[145]:


search=driver.find_element(By.TEXT,"GK")
search.click()


# In[ ]:


Priminister_Name=[]
Born-Dead=[]
Term_of_office=[]
Remarks=[]


# In[ ]:


html(/body/iframe[1])


# In[ ]:


#Scaping the primeminister name  from given page
Name=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in Name[0:10]:
    title=i.text
    Priminister_Name.append(title)
#Scaping the Born_dead period from given page
Born_Dead_period=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in Born_Dead_period[0:10]:
    period=i.text
    Born-Dead.append(period)
#Scaping the Term_of_office from given page
Term_of_office_period=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in Term_of_office_period[0:10]:
    period1=i.text
    Term_of_office.append(period1)
#Scaping the Remarks from given page
remark_title=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in remark_title[0:10]:
    title3=i.text
    Remarks.append(title3)


# In[ ]:


print(len(Priminister_Name))
print(len(Born-Dead))
print(len(Term_of_office))
print(len(Remarks))


# In[ ]:


df=pd.DataFrame({'Priminster Name':Priminister_Name, 'Born_dead':Born-Dead,  'Term of Office':Term_of_office, 'Remarks':Remarks})
df

Q10: Write a python program to display list of 50 Most expensive cars in the world
    (i.e. Car name and Price) from https://www.motor1.com/ 
This task will be done in following steps:
1. First get the webpage https://www.motor1.com/ 
2. Then You have to click on the List option from Dropdown menu on left side.
3. Then click on 50 most expensive cars in the world..
4. Then scrap the mentioned data and make the dataframe. 
# In[128]:


driver= webdriver.Chrome(r"C:\Users\Dell\Downloads\chromedriver.exe")


# In[129]:


driver.get(" https://www.motor1.com/")


# In[130]:





# In[ ]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


carname=[]
carprice=[]


# In[ ]:


#Scaping the job_carname from given page
car_name=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in car_name[0:50]:
    title=i.text
    carname.append(title)
#Scaping the carprice for given car from given page
car_price =driver.find_elements(By.XPATH, '//span[@class="ellipsis fleft "]')
for i in car_price[0:50]:
    car_price = i.text
carprice.append(car_price)


# In[ ]:


print(len(car_name))
print(len(car_price))


# In[ ]:


df=pd.DataFrame({'Car Name':carname, 'Price':price})
df

