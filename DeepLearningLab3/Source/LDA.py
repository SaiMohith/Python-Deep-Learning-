# Importing Libraries
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Loading Digits data into dig_data
dig_data = load_digits()
predictor = dig_data.data
response = dig_data.target
targets = dig_data.target_names  # Making a list of targets

# Applying LDA
lda = LinearDiscriminantAnalysis(n_components=2)
predictor = lda.fit(predictor, response).transform(predictor)  # transform the predictor

# Plotting the LDA on the graph. Different colors represent different targets
plt.figure()
colors = ['navy', 'turquoise', 'brown', 'red', 'blue', 'green', 'black', 'cyan', 'pink', 'purple']

# plotting Data
for color, i, target_name in zip(colors, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], targets):
    plt.scatter(predictor[response == i, 0], predictor[response == i, 1], alpha=.6, color=color,
                label=target_name)

# plotting labels
plt.legend(loc='best')
plt.title('LDA of Digits Dataset')
plt.xlabel('Predictor Values')
plt.ylabel('Response Values')
plt.show()