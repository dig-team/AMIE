import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import permutation_importance

# === Step 1: Load the data
df = pd.read_csv("full_merged_fb15k237.tsv", sep="\t")

# === Step 2: Select relevant columns and drop rows with missing values
features = ["appSupport", "appJacquardSupport", "appAvgSupport", "headToBodySelectivity", "bodySelectivity", "closureFactor"]
target = "Pca Confidence"

df = df[features + [target]].dropna()

# === Step 3: Define features (X) and target (y)
X = df[features]
y = df[target]

# Optional: scale the input features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# === Step 4: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# === Step 5: Train the regressor
#model = RandomForestRegressor()
#model = LinearRegression()
model = Ridge()
model.fit(X_train, y_train)

# === Step 6: Evaluate
y_pred = model.predict(X_test)
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("R2 score:", r2_score(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

r = permutation_importance(model, X_test, y_test, n_repeats=30, random_state=0)
for i in r.importances_mean.argsort()[::-1]:
    if r.importances_mean[i] - 2 * r.importances_std[i] > 0:
        print(f"{X.columns[i]:<8} "
              f"{r.importances_mean[i]:.3f}"
              f" +/- {r.importances_std[i]:.3f}")

