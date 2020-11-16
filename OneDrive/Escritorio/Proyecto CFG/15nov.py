import requests

question1= int(input ("Do you want 1.get help or 2.give help? 1/2 "))

def get_help():
    post_code= input ("insert a post code :")
    url = "https://www.givefood.org.uk/api/1/foodbanks/search/?address={}".format(post_code)
    response = requests.get (url)
    data = response.json()
    for name in data:
        print("name:", name["name"])
        print("address: ", name["address"])
        print("distance in meters: ", name["distance_m"])
        print("phone number:", name["phone"])
        print("district:", name["district"])
        print("email: ", name["email"])
        print("website: ", name ["url"])

if question1== 1:
    get_help()

def give_help():
    post_code= input ("insert a post code :")
    url = "https://www.givefood.org.uk/api/1/foodbanks/search/?address={}".format(post_code)
    response= requests.get(url)
    data2= response.json()
    return data2

def needs():
    donation = input("What would you like to donate?")
    result = give_help()

    for results in result:
        needs2 = results["needs"]
        # print (needs2)
        if donation in needs2:
            print("food bank which needs your product: ", results["name"])
            print(results["address"])
            print(results["phone"])
            print (results["url"])
            # else:
                 #print("This one does not need it: ", results["name"])
if question1 == 2:
    needs()