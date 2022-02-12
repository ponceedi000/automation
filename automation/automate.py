from asyncore import write
import re, os

def potential_contacts():
  file = open('assets/potential-contacts.txt', 'r')
  r_file = file.read()
  emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", r_file)
  emails = list(set(emails))
  emails.sort()
  
  phone = re.findall(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', r_file)
  phone = list(set(phone))
  phone.sort()
  file.close()
  phone_file = write_to_file('phone_numbers.txt', phone)
  email_file = write_to_file('emails.txt', emails)
  return(phone_file, email_file)

def write_to_file(file_name, data):
  with open(file_name, 'w+') as f:
    for line in data:
      f.write(line + '\n')
    f.close()
  return f


if __name__ == '__main__':
  test = potential_contacts()
  print(test)
