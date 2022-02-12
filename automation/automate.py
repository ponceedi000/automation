import re, os

def potential_contacts():
  file = open('assets/potential-contacts.txt', 'r')
  r_file = file.read()
  emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", r_file)
  emails = list(set(emails)).sort()
  phone = re.findall(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', r_file)
  phone.sort()
  file.close()
  with open('phone_numbers.txt', 'w+') as phone_file:
    for number in phone:
      phone_file.write(number + '\n')
    phone_file.close()
  with open('emails.txt', 'w+') as email_file:
    for email in emails:
      email_file.write(email + '\n')
    email_file.close()
  return(phone_file, email_file)

if __name__ == '__main__':
  test = potential_contacts()
  print(test)
