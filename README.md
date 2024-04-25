# Fin Tracker
- Deployed link: [Fin Tracker](https://fintracker-d91e74e9f79d.herokuapp.com/)
- [Screenshot of the running program "Fin Tracker"](assets/images/start.png)

<br>

Welcome to Fin Tracker – your personalized expense management tool!

Fin Tracker is a comprehensive expense tracking application designed to help individuals and households manage their finances effectively. Whether you're tracking your monthly expenses, setting budgets, or analyzing spending patterns, Fin Tracker has you covered.

With Fin Tracker, you can easily input your income and expenses, categorize transactions, and visualize your financial data. The intuitive user interface allows you to quickly add new transactions, set budgets for different expense categories, and monitor your spending in real-time.

Key features of Fin Tracker include:

- Income Tracking: Input your income details, including amount, description, and date, to keep track of your earnings.
- Expense Tracking: Record your expenses effortlessly by entering the amount, description, and date of each transaction.
- Budget Management: Set budgets for various expense categories such as groceries, utilities, and entertainment, and track your spending against these budgets.
- Expense Analysis: Analyze your spending patterns with detailed reports and visualizations, helping you identify areas where you can save money.
- Customizable Notifications: Receive alerts when your expenses exceed budget limits, helping you stay on track with your financial goals.

With Fin Tracker, managing your finances has never been easier. Say goodbye to the hassle of manual expense tracking and take control of your money today!

## User Stories
- As a first time user, I want the input system of the Fin Tracker to be intuitive and straightforward, guiding me through each step clearly.
- As a first time user, I expect the Fin Tracker to provide feedback and corrections if I make any mistakes during data entry, ensuring accuracy and helping me understand the system better.
- As a returning user, I aim to minimize my workload by only needing to input a few essential values into the Fin Tracker, streamlining the process of recording income, expenses, and budget information.
- As a returning user, I seek the ability to view and manage my financial data conveniently through a spreadsheet format provided by the Fin Tracker, allowing for easy tracking and analysis.
- As a returning user, I desire a quick and efficient method within the Fin Tracker to determine intervention strategies for my students based on their financial performance, enabling me to provide timely support and guidance as needed.

## Features
- Budget Setting and Tracking:
    - __Set budgets: For groceries, utilities, entertainment.__
    - __Validate input: Ensure positive numbers; provide error feedback.__
[Screenshot of budget entry and validation screen](assets/images/budget-validation.png)
    - __Track expenses: Notify if exceeding budget.__
[Screenshot of exceeded expense](assets/images/exceeded-expense.png)
    - __Data stored in "fin-tracker" Google Sheets.__
<br>

- Income Tracking:
    - __Input income data: Users input amount, description, and date.__
    - __Validate input: Ensure positive numbers; provide error feedback.__
[Screenshot of income input and validation screen](assets/images/income-validation.png)
    - __Data stored in "fin-tracker" Google Sheets.__
<br>

- Expense Tracking:
    - __Input expense data: Amount, description, date.__
    - __Validate input: Ensure positive numbers; provide error feedback.__
[Screenshot of expense input and validation screen](assets/images/expense-validation.png)
    - __Data stored in "fin-tracker" Google Sheets.__
- Financial Analysis:
    - __Summary: Total incomes, expenses.__
    - __Budget allocation: Summary of budget vs. actual expenses.__
    - __Calculate remaining amount.__
[Screenshot of remaining amount](assets/images/remaining-amount.png)
<br>

- User Interaction:
    - __Prompted options: Add income, expense, or exit.__
    - __Feedback on invalid inputs.__
<br>

- Data Visualization:
    - __Tabular display: Expense, income data.__
[Screenshot of data visualization](assets/images/display.png)
    - __Budget, expense summary tables.__
<br>

- Notification System:
    - __Alert on budget exceedance.__
[Screenshot of notification system](assets/images/notification.png)
<br>

## Flowchart
[First draft flowchart made before starting the project](assets/images/flowchart.png)
<br>

## Technologies used
### Languages
- [Python](https://www.python.org/doc/essays/blurb/)
<br>

### Library imports
- gspread 
- google.oauth2.service_account
- rich
- os
- datetime
<br>

### Other tools
- [Google sheets](https://www.google.co.uk/sheets/about/)
- [GitHub](https://github.com/)
- [GitPod](https://gitpod.io/)
- [Heroku](https://www.heroku.com/)
<br>

## Solved bug
I encountered an issue during deployment due to the failure of pip3 freeze > requirements.txt to install the required libraries automatically. Consequently, I manually searched for the missing libraries and their versions to resolve the issue.
<br>

## Testing
- I consistently tested the program throughout the development phase to guarantee its functionality.
- Employed the PEP8 Python Checker tool to evaluate my code, achieving a score of 68% - Good. See the screenshot of the PEP8 score here. [Screenshot of PEP8 score](assets/images/pep8.png)