import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
df = pd.read_csv("data/Loan.csv")
df = df.dropna()

y = df["default"]
X = df.drop("default", axis = 1)
print(df.corr()["default"].sort_values(ascending=False))
#These are crazy high correlations which aren't seen in real-world hence the model is so good and despite being no overfitting or data leakage


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify = y,random_state=42)
ran = RandomForestClassifier(n_estimators=500, random_state=42)
ran.fit(X_train,y_train)
loans_pr = ran.predict_proba(X_test)
loans_check = ran.predict(X_test)
print(classification_report(y_test,loans_check))

def expected_loss(loan, model, feature_cols, recovery_rate=0.10):
    x = pd.DataFrame([loan], columns=feature_cols)
    x = x.fillna(0) 
    pd_hat = model.predict_proba(x)[:, 1][0]
    pd_percent = round(pd_hat * 100, 2)
    lgd = 1 - recovery_rate
    ead = loan["loan_amt_outstanding"]
    el = pd_hat * lgd * ead
    return {"probability_of_default_%": pd_percent, "expected_loss": el}
feature_cols = X.columns.tolist()
loan_example = {
    "credit_lines_outstanding": 5,
    "loan_amt_outstanding": 10000,
    "total_debt_outstanding": 25000,
    "income": 52000,
    "years_employed": 2,
    "fico_score": 690
}


result = expected_loss(loan_example, ran, feature_cols, recovery_rate=0.10)
print(result)