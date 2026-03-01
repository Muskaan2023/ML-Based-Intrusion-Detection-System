import pandas as pd
import numpy as np
column_names = [
'duration','protocol_type','service','flag','src_bytes','dst_bytes','land',
'wrong_fragment','urgent','hot','num_failed_logins','logged_in','num_compromised',
'root_shell','su_attempted','num_root','num_file_creations','num_shells',
'num_access_files','num_outbound_cmds','is_host_login','is_guest_login',
'count','srv_count','serror_rate','srv_serror_rate','rerror_rate','srv_rerror_rate',
'same_srv_rate','diff_srv_rate','srv_diff_host_rate','dst_host_count',
'dst_host_srv_count','dst_host_same_srv_rate','dst_host_diff_srv_rate',
'dst_host_same_src_port_rate','dst_host_srv_diff_host_rate',
'dst_host_serror_rate','dst_host_srv_serror_rate',
'dst_host_rerror_rate','dst_host_srv_rerror_rate',
'label','difficulty'
]

train_df = pd.read_csv("D:/ML/IDS_Project/KDDTrain+.txt", names=column_names)
test_df = pd.read_csv("D:/ML/IDS_Project/KDDTest+.txt", names=column_names)

print("Training shape:", train_df.shape)
print("Testing shape:", test_df.shape)

# Convert label to binary
train_df['label'] = train_df['label'].apply(lambda x: 0 if x == 'normal' else 1)
test_df['label'] = test_df['label'].apply(lambda x: 0 if x == 'normal' else 1)

print("Label distribution in training set:")
print(train_df['label'].value_counts())

# Drop difficulty column (not needed for prediction)
train_df = train_df.drop('difficulty', axis=1)
test_df = test_df.drop('difficulty', axis=1)

# Separate features and label
X_train = train_df.drop('label', axis=1)
y_train = train_df['label']

X_test = test_df.drop('label', axis=1)
y_test = test_df['label']

print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)

# One-hot encode categorical columns
categorical_columns = ['protocol_type', 'service', 'flag']

X_train = pd.get_dummies(X_train, columns=categorical_columns)
X_test = pd.get_dummies(X_test, columns=categorical_columns)

# Align test set columns with train set
X_train, X_test = X_train.align(X_test, join='left', axis=1, fill_value=0)

print("After encoding:")
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)

from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=500,
    max_depth=None,
    min_samples_split=5,
    min_samples_leaf=2,
    class_weight={0:1, 1:5},
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)

y_probs = model.predict_proba(X_test)[:,1]
y_pred = (y_probs > 0.22).astype(int)

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))