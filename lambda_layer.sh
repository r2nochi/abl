mkdir -p ./lambda-layers/python
pip install -r requirements.txt -t ./lambda-layers/python/
cd ./lambda-layers
zip -r layer.zip python/*
