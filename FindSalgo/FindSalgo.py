import pandas as pd

def find_s_algorithm(file_path):
    # Load the CSV data
    data = pd.read_csv(file_path)

    print("Training data:")
    print(data)

    # Get attribute columns and class label column
    attributes = data.columns[:-1]
    class_label = data.columns[-1]

    # Initialize hypothesis with the most specific values
    hypothesis = ['?' for _ in attributes]

    # Iterate over the training data
    for index, row in data.iterrows():
        if row[class_label] == 'Yes':
            for i, value in enumerate(row[attributes]):
                if hypothesis[i] == '?' or hypothesis[i] == value:
                    hypothesis[i] = value
                else:
                    hypothesis[i] = '?'

    return hypothesis

# Path to your CSV file
file_path = 'training_data.csv'

# Run the Find-S algorithm
hypothesis = find_s_algorithm(file_path)
print("\nThe final hypothesis is:", hypothesis)
