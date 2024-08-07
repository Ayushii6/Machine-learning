import smtplib
email="801852@gmail.com"
receiver_email="22cse017@gweca.ac.in"
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("aj801852@gmail.com","cdaqivenhehzrzkp")
message ="name:Ayushi jain\n college:government womens engineering college\n Branch:CSE\n"
s.sendmail(email,receiver_email,message)
print("mail sent")
s.quit()
