## README.md

**oneAPI-powered Email Auto-Responder with Sentiment Analysis**

This project implements a sentiment analysis-driven email auto-responder system designed for email communication. It leverages Intel oneAPI toolkits (oneMKL and DAal) for optimized text pre-processing and explores advanced techniques for accurate sentiment classification. 

**Features:**

* **Sentiment Analysis:** Analyzes incoming emails to understand the sender's sentiment (positive, negative, neutral) using:
    * VADER: Simple and fast for basic sentiment analysis.
    * DistilBERT (Fine-tuned): Fine-tuned for email context, potentially providing more nuanced sentiment understanding.
* **oneAPI Integration:** Utilizes oneAPI for efficient text cleaning tasks (lowercasing, tokenization, etc.), accelerating pre-processing and enhancing scalability for large email volumes.
* **Automated Responses:** Based on the sentiment analysis, the system can generate pre-defined automated responses tailored to the sentiment of the incoming email. 
* **User Interface (Streamlit):** Provides a web application for managing configurations, viewing analysis results, and customizing response templates.

**Benefits:**

* **Improved Efficiency:** Automates responses to emails, saving time and resources.
* **Enhanced Customer Service:** Provides timely and appropriate responses based on sentiment analysis.
* **Streamlined Workflows:** Integrates with existing email systems to automate responses within workflows.
* **Data-Driven Insights:** Sentiment analysis from emails provides valuable insights into customer feedback or communication trends.

**Target Audience:**

* Businesses and organizations seeking to automate email responses and gain insights from customer sentiment.
* Developers interested in building sentiment analysis-based email auto-responders.

**Getting Started:**
1. **To clone this repository :** git clone https://github.com/Karan-Mishra-N/oneAPI-Email-AutoResponder.git
2. **Prerequisites:** Install the required libraries listed in `requirements.txt`.
3. **Running the Application:** Execute the `oneAPI_Email_AutoResponder_app.py` file to launch the web application.
4. **Code Structure:** Explore the code within the `oneAPI_Email_AutoResponder.ipynb` directory for functionalities related to text cleaning, sentiment analysis, and automated response generation.
5. **Data Preparation:** Create a labeled email dataset for DistilBERT fine-tuning.

**Demo Of The Project :**
![Screenshot 2024-04-06 114208](https://github.com/Karan-Mishra-N/oneAPI-Email-AutoResponder/assets/152774217/34fd39e6-961f-4e7b-b3b6-8b9f7b5093cb)
![Screenshot 2024-04-06 114250](https://github.com/Karan-Mishra-N/oneAPI-Email-AutoResponder/assets/152774217/df93c5c8-be70-448b-8484-389c8488f644)

**Benefits of using Intel oneAPI Toolkits:**

* **Performance:** oneAPI toolkits accelerate text cleaning tasks, enabling faster processing of email data, crucial for handling large volumes efficiently.
* **Scalability:** oneAPI's optimized libraries ensure the project scales well for bigger email datasets.
* **Customization:** DAal offers functionalities for advanced text pre-processing, allowing you to tailor the pre-processing pipeline to specific email data characteristics, potentially leading to more accurate sentiment classification.

**Contribute!**
This project is open-source. We welcome contributions to improve and expand its functionalities.
