import requests
from bs4 import BeautifulSoup

vcard = ''

for i in range(0,5):
    URL = 'https://www.locatefamily.com/Street-Lists/Indonesia/index-395'+str(i)+'.html'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    contacts = soup.find_all('a', class_='phone-link')

    # Extract text from contacts
    for contact in range(len(contacts)):
        phone = contacts[contact].text.replace(' ', '')
        
        # Remove 62 in front number
        if phone[:2] == phone[2:4]:
            phone = phone[4:]
        if phone[:2] == '62':
            phone = phone[2:]

        vcard += 'BEGIN:VCARD' + '\n'
        vcard += 'VERSION:2.1' + '\n'
        vcard += 'N:' + '\n'
        vcard += 'FN:' + '\n'
        vcard += 'TEL;TYPE=CELL:' + phone + '\n'
        vcard += 'END:VCARD' + '\n\n'

# Save to file
with open('contact.vcf', 'w') as file:
    file.write(vcard)

# print(contact)