import message_logging, requests, json, time, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

with open("settings.json") as json_file:
    config = json.load(json_file)

alarm = {}
'''
Documenting which error is already detected and alarmed.
I do not use flag because I assert that this computer does not need to know which messages will be sent to it.
'''

def send_alarm_email(ip, key):
    '''
    Send alarm emails.
    '''
    content = MIMEMultipart()
    content["subject"] = "[實驗室]電腦異常"
    content["from"] = "labmail"
    recipient = config["email_list"][all] + config["email_list"][key]
    content["to"] = ", ".join(recipient)
    content.attach(MIMEText(ip + "出現異常錯誤" + key))
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(config["domain_mail_account"], config["domain_mail_password"])
            smtp.send_message(content)
        except Exception as e:
            print("Errpr message: ", e)

while True:
    for ip in config["ip_list"]:
        try:
            status = requests.get("http://" + ip + "/heartbeats").json()
        except:
            status = {"Computer":"Down"}
        for key in status.keys():
            message_logging.dtcsvlog(ip, key, status[key])
            if status[key] != "OK":
                if not alarm[key]:
                    send_alarm_email(ip, key)
                alarm[ip + " " + key] = True
    time.sleep(60)
    