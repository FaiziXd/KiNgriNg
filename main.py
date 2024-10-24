from flask import Flask, request
import requests
import time
from datetime import datetime

app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

def send_message_to_api(access_token, thread_id, message, retries=5):
    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
    parameters = {'access_token': access_token, 'message': message}
    
    for attempt in range(retries):
        try:
            response = requests.post(api_url, data=parameters, headers=headers)
            if response.status_code == 200:
                print(f"Message sent: {message}")
                return True
            else:
                print(f"Failed to send message: {response.status_code}. Retrying...")
                time.sleep(2 ** attempt)  # Exponential backoff
        except requests.RequestException as e:
            print(f"Request error: {e}. Retrying...")
            time.sleep(2 ** attempt)  # Exponential backoff
    print("All retries failed.")
    return False

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
            for message in messages:
                message_to_send = f"{mn} {message}"
                sent = send_message_to_api(access_token, thread_id, message_to_send)

                if sent:
                    print(f"Message sent successfully: {message_to_send}")
                else:
                    print(f"Failed to send message after retries: {message_to_send}")

                time.sleep(time_interval)  # Control sending rate

    return '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TH3 FA9ZI XD</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background-image: url('https://iili.io/2fTKrLg.jpg');
      background-size: cover; /* Fullscreen background image */
      background-position: center center;
      background-repeat: no-repeat;
    }
    .container {
      max-width: 500px;
      background-color: rgba(255, 255, 255, 0.9); /* Slightly transparent background */
      border-radius: 10px;
      padding: 20px;
      margin: 50px auto; /* Center the form */
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    }
    .header {
      text-align: center;
      padding-bottom: 20px;
    }
    .btn-submit {
      width: 100%;
      margin-top: 10px;
    }
    .footer {
      text-align: center;
      margin-top: 20px;
      color: #888;
    }
  </style>
</head>
<body>
  <header class="header mt-4">
    <h1 class="mb-3" style="color: palevioletred;">CONVO INVOX GROUP</h1>
    <h1 class="mt-3" style="color: palevioletred;">𝐎𝐖𝐍𝟑𝐑:: — Fʌɩzʋ  x3 wʌqʌs</h1>
  </header>

  <div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="accessToken">Enter Your vinthol Token:</label>
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
      <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
    </form>
  </div>
  <footer class="footer">
    <p>&copy; Developed by Fʌɩzʋ xd 2024. All Rights Reserved.</p>
    <p>Convo/Inbox Loader Tool</p>
    <p>Keep enjoying <a href="https://www.facebook.com/The.FaiZu.DonE">here</a></p>
  </footer>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
