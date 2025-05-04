
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# load data
df = pd.read_csv('data/student_performance.csv')

# calculate the average score, average of  assignment, quiz, lab, mid and final exams
df['final_score'] = round(df[['assignment', 'quiz', 'lab', 'midterm_exam', 'final_exam']].sum(axis=1) / 5, 0)

# determine if the student has passed or failed the course
df['pass'] = (df['final_score'] >= 50).astype(int)

# features
X = df[ [ 'assignment', 'quiz', 'lab', 'midterm_exam', 'final_exam']]
y = df['pass']

# split your data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)

# create and train a model
model = RandomForestClassifier()
model.fit(x_train, y_train)

# evaluate model
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy}')


# How well is the model's prediction of pass or fail?
# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# How the features rank in terms of importance to predict student passing or failing?
# Feature importance
features = pd.Series(model.feature_importances_, index=X.columns)
features.sort_values(ascending=False).plot(kind='bar', title='Feature Importance')
plt.show()
