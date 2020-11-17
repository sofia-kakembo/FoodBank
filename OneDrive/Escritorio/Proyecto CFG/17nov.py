import requests

Question1 = int(input("Do you want  1) To Get Help or  2) To Give Help? Enter 1 OR 2 "))

def get_help():
    post_code = input("Insert your Postcode: ")
    url = "https://www.givefood.org.uk/api/1/foodbanks/search/?address={}".format(post_code)
    response = requests.get(url)
    data = response.json()
    for name in data:
        print("-------{}------".format(name['name']))
        print("Food Bank Name:", name["name"])
        print("Address: ", name["address"])
        print("Distance in Meters: ", name["distance_m"])
        print("Phone Number:", name["phone"])
        print("District:", name["district"])
        print("Email: ", name["email"])
        print("Website: ", name["url"])

def give_help():
    post_code = input("Insert your Postcode:")
    url = "https://www.givefood.org.uk/api/1/foodbanks/search/?address={}".format(post_code)
    response = requests.get(url)
    data2 = response.json()
    return data2

def donate():
    donation = input("What would you like to donate? ")
    result = give_help()
    counter = 0
    for i in range(len(result)):
        if donation.lower() in result[i]['needs'].lower():
            print("-------{}------".format(result[i]['name']))
            print(result[i]['name'])
            print(result[i]['url'])
            print(result[i]["address"])
            print(result[i]["phone"])
            #print(result[i]['needs'])
            counter += 1
    if counter == 0:
        print("No Food Banks in your area currently need that item")

def needs():
    result= give_help()
    print ("Find below the list of Needs and Details of the Food Banks closer to you: ")
    for results in result:
        print("-------{}------".format(results['name']))
        #print ("data bank needed: ", results["name"])
        print ("Donation Needed:", "\n", results["needs"])
        print("Address:", "\n", results["address"])
        print("Phone Number:", "\n", results["phone"])
        print("Email:", "\n", results["email"])
        print("Website:", "\n", results["url"])


if Question1 == 1:
    get_help()
else:
    Question2 = int(input("Do you want to 3) Donate something in particular? OR 4) See what is currently needed? Enter 3 OR 4 "))

    if Question2 == 3:
        donate()
    else:
        needs()