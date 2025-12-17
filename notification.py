import requests
requests.post("https://ntfy.sh/your_topic_name", data="Your Message", headers={"Title": "Python Alert"})
