from flask import Flask, send_file
import random
from uuid import uuid4
import os
import re


app = Flask(__name__)


#constants
alphabet_list = 'abcdefghijklmnopqrstuvwxyz'
number_list = '1234567890'
alpha_numeric_list = ''.join([alphabet_list, number_list])
base_url = 'http://localhost:5000'
separator = ' ,'
real_number_pattern = re.compile(r"([0-9]+(?:\.[0-9]+)?)")


def generate_random_string():
    idx = random.randint(0, 3)
    if idx == 0:
        d = ''.join(random.choice(alphabet_list) for _ in range(0, 20))
    if idx == 1:
        d = random.randint(0, 999999)
    if idx == 2:
        d = random.uniform(0, 999999)
    if idx == 3:
        d = ''.join(random.choice(alpha_numeric_list) for _ in range(0, 20))


    return str(d)


@app.route('/', methods=['POST'])
def generate():
    try:
        os.mkdir('files')
    except:
        print('hehe')
        pass


    file_name = str(uuid4())
    limit = 2 * 1024 * 1024 # 2mb
    file_path = 'files/{name}.txt'.format(name=file_name)
    with open(file_path, 'w') as f:
        current_string = ''
        while(len(current_string) < limit):
            # continue to generate a string
            if current_string == '':
                current_string = generate_random_string()
            else:
                current_string = separator.join([current_string, generate_random_string()])


        f.write(current_string)


    return {"filename": file_path.replace('files/', ''), "url": "{base_url}/{path}".format(base_url=base_url, path=file_path)}


@app.route('/<string:filename>', methods=['GET'])
def get(filename):
    file_path = 'files/{name}'.format(name=filename)

    try:
        alphabet_count = 0
        real_number_count = 0
        integer_count = 0
        alpha_numeric_count = 0
        with open(file_path, 'r') as f:
            data = f.read()
            data_list = data.split(separator)
            for d in data_list:
                if d.isalnum():
                    alpha_numeric_count += 1


                if d.isalpha():
                    alphabet_count += 1


                if d.isnumeric():
                    integer_count += 1


                if real_number_pattern.match(d) is not None:
                    real_number_count += 1


        return {
            "count": {
                "alphabets": alphabet_count,
                "real_numbers": real_number_count,
                "integers": integer_count,
                "alpha_numerics": alpha_numeric_count
            }
        }
    except:
        return {"message": "filename not found"}, 404


@app.route('/files/<string:filename>', methods=['GET'])
def download(filename):
    try:
        return send_file('files/{name}'.format(name=filename), as_attachment=True)
    except:
        return {'message': 'File not found'}, 404


if __name__ == '__main__':
    app.run()