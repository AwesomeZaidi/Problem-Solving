# class Solution:
def numUniqueEmails(emails):
#       Input: list of emails
#       Return: number of emails sent
    email_list = []
#       Go through each email
    for email in emails:
        emailArr = list(email)
        plus_index = len(email)
        at_index = email.index("@")
        for index, char in enumerate(emailArr):
            if index == at_index:
                break
            print('index:', index)
            if char == '+':
                plus_index = index
                
            if index > plus_index and index < at_index:
                emailArr.pop(index)
                    
            if char == '.':
                print('old email before .deletion:', email)
                emailArr.pop(index)
                print('email after .deletion:', email)

        email = ''.join(emailArr)
        print("cleaned Email: ", email)
        email_list.append(email)
    print("emails:", email_list)
    return email_list

print(numUniqueEmails(['asim@test.com', 'asim.zaidi@cool.com', 'as.im+zaidi.cool@test.com']))