import pandas as pd

# Load dataset
df = pd.read_csv("Data/agriculture_data.csv")

# Remove duplicate rows
df = df.drop_duplicates()

# Clean column names
df.columns = df.columns.str.strip()

print("Rows after removing duplicates:", len(df))

# Convert numeric columns
for column in ["Area", "Production", "yield"]:
    df[column] = pd.to_numeric(df[column], errors="coerce")
    df[column] = df[column].fillna(df[column].median())

# Clean text columns
text_columns = ["State_Name", "District_Name", "Season", "Crop"]

for column in text_columns:
    df[column] = df[column].astype(str).str.strip()

print("\nText columns cleaned successfully!")

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())
# Save cleaned dataset
df.to_csv("Data/cleaned_agriculture_data.csv", index=False)

print("\nCleaned dataset saved successfully!")
# Check cleaned dataset
cleaned_df = pd.read_csv("Data/cleaned_agriculture_data.csv")

print("\nCleaned Dataset Shape:")
print(cleaned_df.shape)

print("\nCleaned Dataset Preview:")
print(cleaned_df.head())
# Crop-wise total production
crop_production = df.groupby("Crop")["Production"].sum().sort_values(ascending=False)

print("\nTop 10 Crops by Total Production:")
print(crop_production.head(10))
# State-wise total production
state_production = df.groupby("State_Name")["Production"].sum().sort_values(ascending=False)

print("\nTop 10 States by Total Production:")
print(state_production.head(10))
# Season-wise total production
season_production = df.groupby("Season")["Production"].sum().sort_values(ascending=False)

print("\nProduction by Season:")
print(season_production)
# Average yield by crop
crop_yield = df.groupby("Crop")["yield"].mean().sort_values(ascending=False)

print("\nTop 10 Crops by Average Yield:")
print(crop_yield.head(10))
# Area-wise total cultivation
crop_area = df.groupby("Crop")["Area"].sum().sort_values(ascending=False)

print("\nTop 10 Crops by Total Area:")
print(crop_area.head(10))
import matplotlib.pyplot as plt

# Top 10 crops by production
top_crops = df.groupby("Crop")["Production"].sum().sort_values(ascending=False).head(10)

# Create bar chart
plt.figure(figsize=(10, 6))
top_crops.plot(kind="bar")

plt.title("Top 10 Crops by Total Production")
plt.xlabel("Crop")
plt.ylabel("Total Production")
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart
plt.savefig("top_10_crop_production.png")

plt.show()
# Top 10 states by production
top_states = df.groupby("State_Name")["Production"].sum().sort_values(ascending=False).head(10)

# Create bar chart
plt.figure(figsize=(10, 6))
top_states.plot(kind="bar")

plt.title("Top 10 States by Total Production")
plt.xlabel("State")
plt.ylabel("Total Production")
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart
plt.savefig("top_10_state_production.png")

plt.show()
# Season-wise production
season_data = df.groupby("Season")["Production"].sum().sort_values(ascending=False)

# Create bar chart
plt.figure(figsize=(10, 6))
season_data.plot(kind="bar")

plt.title("Production by Season")
plt.xlabel("Season")
plt.ylabel("Total Production")
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart
plt.savefig("season_production.png")

plt.show()
# Top 10 crops by average yield
top_yield = df.groupby("Crop")["yield"].mean().sort_values(ascending=False).head(10)

# Create bar chart
plt.figure(figsize=(10, 6))
top_yield.plot(kind="bar")

plt.title("Top 10 Crops by Average Yield")
plt.xlabel("Crop")
plt.ylabel("Average Yield")
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart
plt.savefig("top_10_crop_yield.png")

plt.show()
# Bhoomi AI - Key Insights

top_production_crop = df.groupby("Crop")["Production"].sum().idxmax()
top_production_state = df.groupby("State_Name")["Production"].sum().idxmax()
top_yield_crop = df.groupby("Crop")["yield"].mean().idxmax()

print("\n===== Bhoomi AI Key Insights =====")

print("Highest Production Crop:", top_production_crop)
print("Highest Production State:", top_production_state)
print("Highest Average Yield Crop:", top_yield_crop)

print("=================================")