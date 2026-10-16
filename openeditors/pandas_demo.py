# Pandas - Pandas is a python library used for working with structured data.
# pandas works on data that looks like a table.

# EG: CSV Files, Excel Files, Databases, Data analysis projects

# import pandas as pd
#Pandas series- 1D labeled data structure
# marks = pd.Series([80, 90, 70, 75])
# print(marks)
# print(marks.iloc[1])
# #ilo- position

# import pandas as pd
# marks = pd.Series(
#   [80, 90, 70],
#   index = ["Apple", "Banana", "Carrot"]
# )
# print(marks.loc["Banana"])
# iloc - position
# loc- label

# import pandas as pd
# marks = pd.Series([80, 90, 70])
# print(marks + 5)
# print(marks * 2)
# print(marks - 10)

# import pandas as pd
# data = {
#   "Name": ["A", "B", "C"],
#   "Age": [21, 22, 23],
#   "Marks": [85, 90, 95]
# }
# df = pd.DataFrame(data)
# print(df)
# print(df[["Name", "Marks"]])
# print(df.iloc[0])

# Accessing specific data
# print(df.loc[1, "Marks"])

# Reading CSV files(comma sepperated values)
# Name,Age,Marks
#A, 21, 85
#B, 22, 90
#C, 23, 95

# import pandas as pd
# df = pd.read_csv("annual.csv")
# print(df.head(5))
# print(df.tail(5))
# print(df.info())
# print(df.describe())

# Data Cleaning Basics
# Finding Missing Values
# import pandas as pd
# df = pd.read_csv("annual.csv")
# # print(df.isnull())
# print(df.isnull().sum())

# # Removing Mising rows
# df = df.dropna()
# # Filling Missing values
# df["year"] = df["year"].fillna(2026)
# df["height"] = df["height"].fillna(df["height"].mean())

# import pandas as pd
# df = pd.read_csv("annual.csv")
# Duplicate Data
# print(df.duplicated())

# Remove Duplicates
# df = df.drop_duplicates()

# Changing column names
# df = df.rename(columns={
#   "industry_code_ANZSIC": "ANZ"
# })
# print(df.head())

# Filter
# result = df[df["year"]>2011]
# print(result)


#1. Web scraping- Web craping is a process of automatically collecting information 
# from websites using program

# Where is Web Scraping used?
# Extracting article headlines
# Collecting products data
# Gathering job listing
# Collecting Publicly available research Data

#2. Request Module- The request library alloes python to send HTTP request to websites
# and receive their responses.

# Sending a request to website

# import requests

# url = "https://www.brandforce.com/domain/Username.com/"
# responses = requests.get(url)
# print(responses.status_code)
# print(responses.text)

#Add basic Error handling
# import requests

# url = "https://www.brandforce.com/domain/Username.com/"
# try:
#   responses = requests.get(url, timeout=10)
#   responses.raise_for_status()
#   print(responses.text)
# except requests.RequestException as error:
#   print("Request failed: ", error)


# BeautifulSoup: Requests download the HTML, but we need a convenient way to find a 
# particular elements inside it. That's where BeautifulSoup helps

# from bs4 import BeautifulSoup

# html = """
#    <!doctype html>
# <html>

#         <head>

#                 <meta charset="utf-8">
#                 <meta http-equiv="X-UA-Compatible" content="IE=edge">
#                 <meta name="viewport" content="width=device-width, initial-scale=1">
#                 <meta name="description" content="This domain name is for sale! Contact us now to acquire this great brand name.">
#                 <base href="https://www.brandforce.com/">

#                                 <link rel="shortcut icon" href="https://files.efty.com/market/uploads/favicon/9aaf316b71ec8727c651033a15c131f0.png"  />

#                 <title>Username.com is for sale | www.brandforce.com</title>

#         <!-- Altcha -->
#         <script async defer src="https://cdn.jsdelivr.net/gh/altcha-org/altcha/dist/altcha.min.js" type="module"></script>
#         <link href="css/altcha.css" rel="stylesheet">

#                 <!-- jQuery -->
#                 <!--<script src="https://code.jquery.com/jquery-2.0.2.min.js"></script>-->
#                 <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>

#                 <!-- Bootstrap -->
#                 <!-- Latest compiled and minified CSS -->
#                 <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

#                 <!-- Latest compiled and minified JavaScript -->
#                 <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

#                 <!-- Font-Awesome -->
#                 <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">

#                 <!-- No UI slider -->
#                 <link href="https://www.brandforce.com/css/nouislider.min.css" rel="stylesheet">
#                 <script src="https://www.brandforce.com/js/nouislider.min.js"></script>

#                 <!-- wNumb number formatting -->
#                 <script src="https://www.brandforce.com/js/wNumb.js"></script>

#                 <!-- Custom + Common Css -->
#                 <link rel="stylesheet" type="text/css" href="https://www.brandforce.com/css/page_specific/efty_market_themes/borgen/style.css">
#                 <link rel="stylesheet" type="text/css" href="https://www.brandforce.com/css/page_specific/efty_market_themes/loading_spinner.css">
#                 <link href='https://fonts.googleapis.com/css?family=Lato:400,700,900,100,300' rel='stylesheet' type='text/css'>

#                 <!--[if lt IE 9]>
#                       <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
#                       <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
#                     <![endif]-->



#         <!-- Efty infrastructure UA -->
#         <script async src="https://www.googletagmanager.com/gtag/js?id=UA-51651642-1"></script>
#         <script>
#             window.dataLayer = window.dataLayer || [];
#             function gtag(){dataLayer.push(arguments);}
#             gtag('js', new Date());

#             gtag('config', 'UA-51651642-1');
#         </script>

#         <!-- ./Efty infrastructure UA -->

#         <!-- /Efty user GA4 / UA -->
#                     <!-- GA4 -->
#             <script async src="https://www.googletagmanager.com/gtag/js?id=G-PQD1GKD73G"></script>
#             <script>
#                 window.dataLayer = window.dataLayer || [];
#                 function gtag(){dataLayer.push(arguments);}
#                 gtag('js', new Date());

#                 gtag('config', 'G-PQD1GKD73G');
#             </script>

#                 <!-- /Efty user GA4 / UA -->



#                 <script type="text/javascript" src="https://www.brandforce.com/odf/js/odf.js"></script><script>Odf.set('website_base_url', 'https://www.brandforce.com/');$(document).ready(function() {Odf.init();});</script>                     

#         </head><!-- EFTY MARKET THEME BORGEN -->
#         <body>

#                 <div id="preloader">
#                         <div id="status">
#                                 <div class="spinner">
#                                   <div class="spinner-wrapper">
#                                         <div class="rotator">
#                                           <div class="inner-spin"></div>
#                                           <div class="inner-spin"></div>
#                                         </div>
#                                   </div>
#                                 </div>
#                         </div>
#                 </div>

#                 <style>

#                         /* Overrule CSS with custom colors from Efty user */

#                         .btn_buy {
#                                 background: #1c7ce6;
#                                 border-color: #1c7ce6;
#                                 color: #ffffff;
#                         }
#                         .efty-lto-stack {
#                                 display: inline-flex;
#                                 flex-direction: column;
#                                 align-items: stretch;
#                                 gap: 6px;
#                         }
#                         .efty-lto-tagline {
#                                 margin-top: 14px;
#                         }
#                         .efty-lto-price {
#                                 margin: 10px 0 0;
#                                 font-size: 15px;
#                                 line-height: 1.4;
#                         }
#                         .efty-lto-price strong {
#                                 font-size: 18px;
#                         }
#                         .efty-lto-price .suffix {
#                                 font-size: 0.72em;
#                                 font-weight: 600;
#                         }
#                         .efty-lto-tagline img {
#                                 max-width: 140px;
#                                 height: auto;
#                         }
#                         .efty-lto-modal-backdrop {
#                                 display: none;
#                                 position: fixed;
#                                 inset: 0;
#                                 background: rgba(15, 23, 42, 0.7);
#                                 align-items: flex-start;
#                                 justify-content: center;
#                                 padding: 32px 20px;
#                                 overflow-y: auto;
#                                 z-index: 100000;
#                         }
#                         .efty-lto-modal-backdrop.is-open {
#                                 display: flex;
#                         }
#                         .efty-lto-modal-panel {
#                                 background: #fff;
#                                 width: 100%;
#                                 max-width: 1100px;
#                                 position: relative;
#                                 margin: auto;
#                                 max-height: calc(100vh - 64px);
#                                 border-radius: 16px;
#                                 overflow: hidden;
#                                 box-shadow: 0 24px 80px rgba(15, 23, 42, 0.35);
#                         }
#                         .efty-lto-modal-header {
#                                 position: absolute;
#                                 top: 8px;
#                                 right: 8px;
#                                 padding: 0;
#                                 border-bottom: 0;
#                                 z-index: 2;
#                         }
#                         .efty-lto-modal-close {
#                                 border: 0;
#                                 background: transparent;
#                                 font-size: 28px;
#                                 line-height: 1;
#                         }
#                         .efty-lto-iframe {
#                                 width: 100%;
#                                 height: min(75vh, 900px);
#                                 min-height: 320px;
#                                 border: 0;
#                                 display: block;
#                         }
#                         @media (max-width: 767px) {
#                                 .efty-lto-modal-backdrop {
#                                         padding: 12px;
#                                 }
#                                 .efty-lto-modal-panel {
#                                         max-height: calc(100vh - 24px);
#                                 }
#                                 .efty-lto-iframe {
#                                         height: calc(100vh - 96px);
#                                         min-height: 420px;
#                                 }
#                         }

#                         .checkbox label::before, .checkbox label::after {
#                                 top:0;
#                         }

#                 </style>


#                 <!-- Header Section Started -->
#                 <header>
#                         <div class="container">
#                                 <div class="row">
#                                         <div class="col-md-4 col-sm-4 col-xs-5">
#                                                                                                         <a href="https://www.brandforce.com"><img src="https://files.efty.com/market/uploads/logo/9aaf316b71ec8727c651033a15c131f0.png" class="img-responsive"></a>
#                                                                                         </div>
#                                         <div class="col-md-8 col-sm-8 col-xs-7">
#                                                                                                 <ul class="list-inline call-us text-right">
#                                                         <li class="call-tx hidden-xs"> <img src="img/efty_market_themes/borgen/1.png">  <span>Call us </span> and we'll help you secure the  <br>
#                                                                         perfect domain name for your business.
#                                                         </li>
#                                                         <li class="number"> 
#                                                                 +1 (310) 362-9548                                              </li>
#                                                 </ul>
#                                                                                         </div>
#                                 </div>
#                         </div>
#                 </header>
#                 <!-- Header Collapsed -->

#                 <section class="desktop_domain_bg" style="background:url(https://files.efty.com/market/uploads/background/9aaf316b71ec8727c651033a15c131f0.jpg) center center no-repeat;background-size: cover;"></section>

#                 <section class="desktop_domain">
#                         <div class="container">
#                                 <div class="white-bg">
#                                         <div class="row ">
#                                                 <div class="col-md-8 space10 side_border">
#                                                         <h3 class="main_title crummer"><a href="https://www.brandforce.com" title="www.brandforce.com">www.brandforce.com</a> > <a href="https://www.brandforce.com/search/" title="">Domain overview</a> > Username.com</h3>

#                                                                                                                         <h2 class="main_title_h2 space0">Username.com</h2>


#                                                         <p class="space30 lht25 f16">
#                                                                 This domain name is for sale! Contact us now to acquire this great brand name.                                                  </p>
#                                                 </div>
#                                                                                                 <div class="col-md-4 space80">
#                                                         <div class="text-center btn_ri">
#                                                                 <a class="btn btn_buy" href="#" id="srcoll_offer">Make an offer</a>
#                                                         </div>
#                                                 </div>
#                                                                                         </div>
#                                         <div class="row">
#                                                 <div class="col-md-12 space50">
#                                                         <img src="img/efty_market_themes/borgen/divider.png" class="img-responsive center-block" width="100%">
#                                                 </div>
#                                         </div>



#                                         <div class="row" id="offer_form">
#                                                 <div class="col-md-12 space30">
#                                                         <p class="f18 text-orange space20">Make an offer on</p>
#                                                         <h3 class="main_title text-black space0">Username.com</h3>

#                                                         <p class="f15">
#                                                                 To make an offer, please complete the form below
#                                                         </p>
#                                                 </div>
#                                         </div>
#                                         <div class="row">
#                                                 <div class="col-md-12">

#                                                 <form action="ajaxa/landing_themes/add_inquiry_cap/" method="post" class="odf_ajax detail_form" data-target="form_feedback">                                                     

#                                                         <input type="hidden" name="domain_id" value="3855013">  
#                                                         <input type="hidden" name="user_id" value="10979">

#                                                         <div id="form_feedback">
#                                                         </div>

#                                                                 <div class="row">
#                                                                         <div class="col-md-6">
#                                                                                 <div class="form-group">
#                                                                                         <p>Name *</p>
#                                                                                         <input type="text" name="name" class="form-control">
#                                                                                 </div>
#                                                                         </div>
#                                                                         <div class="col-md-6">
#                                                                                 <div class="form-group">
#                                                                                         <p>Email *</p>
#                                                                                         <input type="mail" name="email" class="form-control">
#                                                                                 </div>
#                                                                         </div>
#                                                                 </div>
#                                                                 <div class="row">
#                                                                         <div class="col-md-6">
#                                                                                 <div class="form-group">
#                                                                                         <p>Phone number</p>
#                                                                                         <input type="text" name="phone" class="form-control">
#                                                                                 </div>
#                                                                         </div>
#                                                                         <div class="col-md-6">
#                                                                                 <div class="form-group">
#                                                                                         <p>Offer <span>Offers can only be made in USD</span> </p>
#                                                                                         <input type="text" placeholder="Offer in USD" name="offer" class="form-control">
#                                                                                 </div>
#                                                                         </div>
#                                                                 </div>
#                                                                 <div class="row">
#                                                                         <div class="col-md-12">
#                                                                                 <div class="form-group">
#                                                                                         <p>Message</p>
#                                                                                         <textarea class="form-control" rows="5"name="message"> </textarea>
#                                                                                 </div>
#                                                                         </div>
#                                                                 </div>


#                                 <div class="altcha-wrapper theme-borgen">
#                                     <altcha-widget
#                                             challengeurl="https://sentinel-w5bmbzne6a7cs.azurewebsites.net/v1/challenge?apiKey=key_1jcc7jkd200a1tg7mhs"
#                                             name="altcha"
#                                     ></altcha-widget>
#                                 </div>

#                                                                 <div class="row">

#                                                                         <div class="col-md-6 col-sm-12">
#                                                                           <input type="submit" class="btn btn_buy" value="Submit offer" style="margin-top:8px !important;">
#                                                                         </div>

#                                                                 </div>

#                                                         </form>
#                                                 </div>
#                                         </div>
#                                                                                 <div class="row space30"></div>
#                                 </div>
#                                 <div class="space80"></div>
#                         </div>
#                 </section>

#                 <footer>
#                         <div class="container">
#                                 <div class="row">
#                                                                                 <div class="col-md-4">
#                                                 <ul class="list-inline social">
#                                                                                                                                </ul>
#                                         </div>
#                                         <div class="col-md-4 text-center number">
#                                                                                                 <h4>+1 (310) 362-9548</h4>
#                                                                                                 <ul class="list-inline">
#                                                         <li><a href="" title="" class="text-blue" target="_blank"></a></li>
#                                                         <li>|</li>
#                                                         <li><a href="mailto:sales@brandforce.com" class="text-blue">sales@brandforce.com</a></li>
#                                                 </ul>
#                                         </div>
#                                                                         <div class="col-md-12 text-center">

#                                         <a href="/contact/" title="Contact">
#                                                 Contact
#                                         </a>
#                                                                                 <br><a href="/about-us/" title="About us">Aboutus</a>
#                                                                                 <br><a href="/cus/1/our-services/" title="Our Services">Our Services</a>
#                                                                         </div>
#                         </div>
#                 </footer>

#                 <!-- Addition JavaScript will placed below -->
#                 <script type="text/javascript">

#                         $('.carousel').carousel({
#                           interval: 3000,
#                           pause: false
#                         })

#                         $("a#srcoll_offer").click(function() {
#                                 $('html, body').animate({
#                                         scrollTop: $("#offer_form").offset().top
#                                 }, 500);
#                                 return false;
#                         });
#                 </script>

#                 <script>

#                         // Show preloader when Escrow BIN button is pressed
#                         $( document ).ready(function() {
#                                 $('.efty-buy-btn').click(function(e) {
#                                         e.preventDefault();
#                                         $('div#preloader').show();
#                                         $('div#preloader').fadeTo(0, 0.8);
#                                         $('div#preloader #status').show();
#                                         Odf.ajax.post('https://www.brandforce.com/ajaxa/transactions/initiate_eftypay/', 'div#response_bin', {
#                                                 domain_id: '2amjp',
#                                                 user_id: '8gz'
#                                         });
#                                         return false;
#                                 });

                                           
#                                 $( '#escrow_pay, #bin_dan, input[type="submit"], [class*="dan"]' ).click(function() {
#                                         $('div#preloader').show();
#                                         $('div#preloader').fadeTo( 0, 0.8);
#                                         $('div#preloader #status').show();
#                                 });

#                                 $( document ).ajaxComplete(function() {
#                                         $('div#preloader').hide();
#                                         $('div#preloader #status').hide();
#                                 });

#                         });

#                 </script>





#                 <!--
# <script> (function (d) {
#         var s = d. createtlement("script");
#         s.setAttribute("data-account","00000000");
#         s.setAttribute("sre", "https://cdn.userway.org/widget.js");
#         (d.body || d.head).appendChild(s):
# (document) </script>
# <noscript>Please ensure Javascript is enabled for purposes of <a href="https://userway.org">website accessibility</a></noscript>
# -->
# <style>body{display: none;}</style>
# <script type="text/javascript" src="https://bf.use-dash.com/efty/script.js?v=1.2"></script>
# <link href="https://bf.use-dash.com/efty/style.css?v=1.2" rel="stylesheet" type="text/css">     </body>

# </html>

# <div id="stats_div" style="display:none;"></div>
# <script>

#         $( document ).ready(function() {

#                 Odf.ajax.get('https://www.brandforce.com/ajax/visitors/create/', 'div#stats_div', { domain_id: '3855013' });

#         });

# </script>
# """

# soup = BeautifulSoup(html, "html.parser")
# print(soup.title)
# print(soup.title.get_text())
# # print(soup.h1.get_text())
# print(soup.p.get_text())

#Important Beautifuisoup methods
#1. find()- finds the first matching element
# soup.find("p")
# #2. find_all()- Finds all matching elements
# soup.find_all("p")
#3. get_text()- Extract text
#4. get()- Extracts an attribute
# link = soup.find("a")
# print(link.get("href"))

# Extracting websites Data

# import requests
# from bs4 import BeautifulSoup

# url = "https://www.brandforce.com"
# response = requests.get(url, timeout=10)
# response.raise_for_status()
# soup = BeautifulSoup(response.text, "html.parser")
# title = soup.title.get_text(strip=True)
# heading = soup.find("h1").get_text(strip=True)
# print("Page Title: ", title)
# print("Heading: ", heading)

# Extracting 

# url = "https://www.brandforce.com"
# response = requests.get(url, timeout=10)
# response.raise_for_status()
# soup = BeautifulSoup(response.text, "html.parser")
# links = soup.find_all("a")
# for link in links:
#   text = link.get_text(strip=True)
#   url = link.get("href")
#   print("Link Text: ", text)
#   print("URL: ", url)

# Email Automation
# import smtplib 
# from email.message import EmailMessage
# #EmailMessage()- Creates an email message
# sender = "1rn22ad011.dchaitanyarajendra@gmail.com"
# password = " "
# receiver = "chaitanyarajendra011@gmail.com"

# msg = EmailMessage()
# msg["Subject"] = "Preparation Email"
# msg["From"] = sender
# msg["To"] = receiver
# msg.set_content("Hello. this is a preparation email using Python")
# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
# #SMTP_SSL- Connects to Gmail's SMTP server using port 465
#   server.login(sender, password)
#   #login()- Log in using your email and app password
#   server.send_message(msg)
#   #send_message()- Sends the email
# print("Email Sent Successfully.")

#Send email with an attachment

# import smtplib 
# from email.message import EmailMessage
# sender = "1rn22ad011.dchaitanyarajendra@gmail.com"
# password = " "
# receiver = "chaitanyarajendra011@gmail.com"

# msg = EmailMessage()
# msg["Subject"] = "Preparation Email"
# msg["From"] = sender
# msg["To"] = receiver
# msg.set_content("Hello. this is a preparation email using Python")

# #Attach a PDF or Word Document
# file_path = r"C:\Users\Lenovo\Downloads\Chaitanya_resume@.pdf"

# with open(file_path, "rb") as file:
#   file_data = file.read()

# msg.add_attachment(
#   file_data,
#   maintype="application",
#   subtype="pdf",
#   filename="Chaitanya_resume@"
# )
# #Send email
# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#   server.login(sender, password)
#   server.send_message(msg)
# print("Email Sent Successfully.")

#Virtual Assistant Program

# import datetime
# import webbrowser

# print("Hello! I'm your Virtual Assistant.")

# while True:
#   command = input("\nHow may I help you ").lower()

#   if "hello" in command or "hi" in command:
#     print("Hello Vikas! How are you?")
#   elif "time" in command:
#     time = datetime.datetime.now().strftime("%I:%M %p")
#     print("Current time is: ", time)
#   elif "date" in command:
#     date = datetime.datetime.now().strftime("%d-%m-%Y")
#     print("Today's date is: ", date)
#   elif "open google" in command:
#     webbrowser.open("https://www.google.com")
#     print("Opening Google....")
#   elif "your name" in command:
#     print("I am your Python Virtual Assistant")
#   elif "exit" in command or "bye" in command:
#     print("Goodbye! Have a nice day")
#     break
#   else:
#     print("Sorry, I don't understand that command.")

#shallow copy- Changing outer list- original doesn't change
# import copy
# original = [[10, 20], [30, 40]]
# copied = copy.copy(original)
# copied[0].append(99)
# print("original: ", original)
# print("copied: ", copied)

# Deep copy
