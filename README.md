# Backend of Sample React JS

A simple service that runs in Python with Flask framework.

## Requirements
- [Python 3.8.5](https://www.python.org/downloads/release/python-385/)
- [Virtual environment](https://docs.python.org/3/library/venv.html)

## How to use
- Create a virtual environment
  - `python3 -m venv venv`
- Activate the virtual environment
  - `source venv/bin/activate`
- Install all the requirements
  - `pip install -r requirements.txt`
- Run application
  - `python app.py`


## API Enpoints

The API Endpoints are published in [Postman Documenter](https://documenter.getpostman.com/view/11811884/Tz5qbxZm)

- **Generate Data**
```
POST /
Response: application/json
type GenerateDataResponse ={
    filename: string,
    url: string
}
```
- **Get Data**
```
GET /<string:filename>
Response: application/json
type GetDataResponse = {
    count: Object<CountData> 
}
type CountData = {
    alpha_numerics: number,
    alphabets: number,
    integers: number,
    real_numbers: number
}
```
- **Download File**
```
GET /files/<string:filename>
Response: text/plain
```
