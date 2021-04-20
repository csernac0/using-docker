import pickle
import pandas as pd

loaded_model = pickle.load(open('cluster_model', 'rb'))
predictions = loaded_model.predict([[10, 0], [12, 3]])
print(predictions)
pd.DataFrame(predictions).to_csv('predictions.csv',index=False)


