import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree

def learn(a,b,c,d):
    df = pd.read_csv("titanic.csv")
    df.drop(['PassengerId','Name','SibSp','Parch','Ticket','Cabin','Embarked'], axis='columns',inplace=True)
    target = df['Survived']
    inputs=df.drop(["Survived"],axis='columns')
    inputs.Age = inputs.Age.fillna(inputs.Age.mean())
    le_sex=LabelEncoder()
    inputs['Sex_n'] = le_sex.fit_transform(inputs['Sex'])
    inputs.drop(['Sex'],axis='columns',inplace=True)
    model = tree.DecisionTreeClassifier()
    model.fit(inputs,target)
    print(model.score(inputs,target))
    res = model.predict([[a,b,c,d]])
    result={
        "survival_probabilty":str(res.tolist()[0]),
        "sex":"100.369.55",
        "age":"Mrinmay",
        "fare": str(d)
    }
    return (result)
