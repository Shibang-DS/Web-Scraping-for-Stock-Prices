# Web-Scraping-for-Stock-Prices
_Web scraping_ is a data extraction method that collects data from websites only. It is mainly used for data mining and collecting useful comments from major websites. Web scraping can also be used for personal use. **Python** includes an excellent library called **BeautifulSoup** for downloading important data from web pages. In this project, we will use the web to extract the real time value of stocks and save it to an Excel file using a Python library **pandas**.
- To begin with, we will import the necessary libraries.
- Then we get the URLs stored in the list.
- We assign the URL to the soup object which then gets the relevant data from the given URL based on the class id we provide.
- Then store the data in CSV file using pandas dataframe.
