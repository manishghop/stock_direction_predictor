# stock_direction_predictor
Stock Market Direction Predictor

## PACKAGES
<h1>You need to install following packages first</h1>
<ul><li> Pyqt5</li>
<li>sklearn </li>
<li>pandas </li>
<li> numpy </li>
<li> DBConnection</li>
</ul>
<p>Go ahead and pip install above packages.</p>

```
pip install pyqt5
pip install sklearn
pip install pandas
pip install numpy
pip install dbConnect
```


<h2>To run the file simply </h2>

Run 

```
python home.py
```



## DATA-GATHERING

We gathered data from the yahoo api which lets us access stock market data from any time-period.




## DATA PRE-PROCESSING
In this step we look for any discrepancies in the dataset. We performed standard scaling to ensure that we normalize the data-set.
There were no missing values as the yahoo api does it's job exceptionally well.




## FEATURE-ENGINEERING
As our problem was focussed on stock market direction prediction. We only chose the direction of stock market(Profit(-1) or Loss(1)) for two consecutive days. Rest all other features were found to be useless.


## MODEL SELECTION

Our problem was a binary classification, so we used Logistic Regression & Naive Bayes Model. 

## MODEL EVALUATION & COMPARISION

Out of these two, Naive Bayes Model preformed better.



## MODEL DEPLOYMENT
We used Flask framework to deploy our model as a web application. At the web application's front-end we added a textbox where, it asks the user the current day stock market value of the company choosen by the user and in the back-end it predicts the next day's stock market direction(Profit(1) or Loss(-1)).

<!--
## This below block is for school's requirememt.

In getdata file we are creating a table data and storing the values from the dataset
also we are creating a dataset table to store 3 fields that we are using for prediction 
along with profit/loss. 
Then in prediction file we use bernoulie naive bayes algorithm to perform a binary 
classification, load the data from the data set that we created(dynamically) and 
based on the details of user input match for the similiar data point in dataset
give result.-->
