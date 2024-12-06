# Outphish

![Banner](assets/banner.png)

A simple and effective application to detect phishing emails using artificial intelligence.

## Features
- Analyze emails to detect phishing characteristics.
- Use a logistic regression model to assess risks.
- Intuitive user interface to upload emails.

## Preview
![Preview of PhishDetector](assets/screenshot.png)

# Installation

You can clone the repository to your local machine and begin the installation process.  
Simply follow the instructions provided in the `README.txt` file.

This project is designed to work on Microsoft Azure, but you can also run it locally by following the steps outlined in `README.txt`. Both usage methods are detailed in the instructions.

## Usage
1. Fill in the text fields according to the labels (sender, subject, content).
2. Click "Envoyer"
3. View the prediction results (one prediction for the email content and another for the sender).

## Technical Overview
- The model is trained on labeled datasets of emails as "phishing" or "legitimate."
- Library used: `scikit-learn`.
- Algorithm: Logistic regression for binary classification.

## Datasets
The training data comes from:
- [Kaggle - Phishing Websites Dataset](https://www.kaggle.com/).
These datasets can be found within the project files.
