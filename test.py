"""import os

path='notebooks/research.ipynb'

dir,file=os.path.split(path)

os.makedirs(dir,exist_ok=True)

with open(path,"w")as f:
    pass"""

from src.InsurancePrediction.pipelines.prediction_pipeline import CustomData

custdataobj=CustomData(19,'female',27.9,0,'yes','southwest')

data=custdataobj.get_data_as_dataframe()

print(data)