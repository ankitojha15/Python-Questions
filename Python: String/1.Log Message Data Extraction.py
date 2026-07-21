# Log Message Data Extraction

# Problem : Extract specific information from a log message. like : log_message = "2023-09-12 [INFO] User 'Alice' logged in. " should return ('2023-09-12', 'Alice')

# Solution

def extract_info(log_message): 
      
      date = log_message[:10]
      user = log_message.split("'")[1]

      print(f"{date}\n{user}")
