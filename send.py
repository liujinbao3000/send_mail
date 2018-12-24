import smtplib
    
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
dan='addressfrom'
giden='address2go'

file_path= 'C:\\yy.xlsx'
name='yy.xlsx'
msg=MIMEMultipart()
msg['Subject']='otomatik mail deneme'
msg['To']=giden
msg['From']=dan
msg.attach(MIMEText('heyy', 'plain'))

part = MIMEBase('application', "octet-stream")
part.set_payload(open(file_path, "rb").read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment', filename=name)
msg.attach(part)

attachment=MIMEBase('application',"octet-stream")


composed=msg.as_string()

#fp=open(file_path,'rb')
#attachment=MIMEBase('application',"octet-stream")
#attachment.set_payload(fp.read())
#encoders.encode_base64(attachment)
#attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_path)
#msg.attach(attachment)

s=smtplib.SMTP('smtp.office365.com',587)
s.starttls()
s.ehlo()
s.login('addressfrom','zxxxxx')

s.sendmail(dan,giden,composed)
s.close()
