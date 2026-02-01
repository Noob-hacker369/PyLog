import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the new dataset
df = pd.read_csv('Output/final_output.csv')

# 2. Define the Mapping for the labels based on your requirements
# This converts the numbers into readable text for the charts
label_names = {
    8: 'Command Injection',
    9: 'SQL Injection',
    5: 'XSS',
    0: 'Normal',
    -1: 'Undefined'
}

# Create a new column with the names
df['label_name'] = df['predicted_label'].map(label_names)

# --- 3. SINGLE BAR GRAPH: Count of each Attack Type ---

def bar_graph():
    plt.figure(figsize=(12, 6))
    # Order the bars by count size
    order = df['label_name'].value_counts().index

    sns.countplot(data=df, x='label_name', hue='label_name', palette='viridis', order=order, legend=False)

    plt.title('Frequency of Specific Security Events (Label Column)', fontsize=15)
    plt.xlabel('Attack Type', fontsize=12)
    plt.ylabel('Number of Instances', fontsize=12)
    plt.xticks(rotation=45) # Tilt text so long names like Command Injection fit
    plt.tight_layout()
    plt.show()

# --- 4. PIE CHART: Percentage Distribution ---
plt.figure(figsize=(10, 8))

# Get the data counts
label_counts = df['label_name'].value_counts()

# Plotting the pie chart
label_counts.plot.pie(autopct='%1.1f%%', startangle=140, cmap='Set3',pctdistance=0.85,explode=[0.05] * len(label_counts) )

# Optional: Make it a Donut Chart for professional look
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Percentage Distribution of Security Labels', fontsize=15)
plt.ylabel('') 
plt.tight_layout()
plt.show()

# 5. Summary Table (Optional: printed in your notebook)
print("--- Detailed Label Counts ---")
print(df['label_name'].value_counts())