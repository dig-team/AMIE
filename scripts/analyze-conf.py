import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.inspection import permutation_importance

# Load data
data_file = 'miniamie_fb15k237_support_5_maxad3_realsupport.rules'  # Update with your actual filename
df = pd.read_csv(data_file)

# Drop specified columns
df = df.drop(columns=['rule', 'bodySelectivityAttributes'])

# Encode 'headRelation'
label_encoder = LabelEncoder()
df['headRelation'] = label_encoder.fit_transform(df['headRelation'].astype(str))

# Separate features and target
X = df.drop(columns=['realSupport', 'realHeadCoverage', 'realSupportNano'])
y = df['realSupport']

# Convert boolean columns to integers if any
X = X.applymap(lambda x: int(x) if isinstance(x, bool) else x)

# Handle any missing values
X = X.fillna(0)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the regressor
regressor = RandomForestRegressor(random_state=42)
regressor.fit(X_train, y_train)

# Predictions
y_pred = regressor.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")



r = permutation_importance(regressor, X_test, y_test, n_repeats=30, random_state=0)
for i in r.importances_mean.argsort()[::-1]:
    if r.importances_mean[i] - 2 * r.importances_std[i] > 0:
        print(f"{X.columns[i]:<8} "
              f"{r.importances_mean[i]:.3f}"
              f" +/- {r.importances_std[i]:.3f}")
