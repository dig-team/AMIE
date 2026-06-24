import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.inspection import permutation_importance
from sklearn.neural_network import MLPRegressor

# Load data
data_file = 'miniamie_nations_support_5_maxad3_realsupport_full.rules'  # 'miniamie_fb15k237_support_5_maxad3_realsupport.rules'  # Update with your actual filename
df = pd.read_csv(data_file)

# Drop specified columns
df = df.drop(columns=['rule', 'bodySelectivityAttributes'])
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.inspection import permutation_importance

# Load data
def get_data(data_file, scaler_X=None, scaler_y=None):
    df = pd.read_csv(data_file)

    # Drop specified columns
    df = df.drop(columns=['rule', 'bodySelectivityAttributes', 'headRelation'])

    # Encode 'headRelation'
    # label_encoder = LabelEncoder()
    # df['headRelation'] = label_encoder.fit_transform(df['headRelation'].astype(str))

    # Separate features and target
    X = df.drop(columns=['realSupport', 'realHeadCoverage', 'realSupportNano', 'appSupportNano', 'headAtom', 'appSupport'])
    y = (df['realSupport'] / df['headAtom']).values.reshape(-1, 1)  # Reshape for scaler

    # Convert boolean columns to integers if any
    X = X.applymap(lambda x: int(x) if isinstance(x, bool) else x)

    # Handle any missing values
    X = X.fillna(0)
    
    # Z-normalization for features
    if scaler_X is None:
        scaler_X = StandardScaler()
    X_scaled = scaler_X.fit_transform(X)
    X_scaled = pd.DataFrame(X_scaled, columns=X.columns, index=X.index)

    # Z-normalization for target
    if scaler_y is None:
        scaler_y = StandardScaler()
    y_scaled = scaler_y.fit_transform(y).ravel()  # Flatten back to 1D

    return X_scaled, y, scaler_X, scaler_y

X, y, sX, sY = get_data(data_file = data_file)

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
              
Xp, yp, _, _ = get_data('miniamie_fb15k237_support_5_maxad3_realsupport.rules', sX, sY)
# Z-normalization for target
#Xp = sX.transform(Xp)
#Xp = pd.DataFrame(Xp, columns=X.columns, index=X.index)
#yp = sY.transform(yp).ravel()  # Flat

yp_pred = regressor.predict(Xp)

# Evaluation
mse = mean_squared_error(yp, yp_pred)
r2 = r2_score(yp, yp_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")
