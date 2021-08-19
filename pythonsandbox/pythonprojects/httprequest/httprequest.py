import requests

formData = {
    'userName':'jamal',
    'password':'xx@kk'
}
r = requests.post('https://httpbin.org/post',data=formData)
r_dictionary = r.json()
print(r_dictionary['form'])