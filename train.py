from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from joblib import dump

def train_model():
    # Load wine dataset
    data = load_wine(as_frame=True)
    X = data.data
    y = data.target
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train a Decision Tree classifier
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    
    # Save the model
    dump(clf, "model.pkl")

if __name__ == "__main__":
    train_model()
