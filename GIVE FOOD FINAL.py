import requests

Question1 = int(input("\nDo you want to:""\n1) GET Help OR  \n2) GIVE Help? \nSelect 1 OR 2\n"))


def get_help():
    post_code = input("\nInsert your Postcode: ")
    url = "https://www.givefood.org.uk/api/1/foodbanks/search/?address={}".format(post_code)
    response = requests.get(url)
    data = response.json()
    for name in data:
        print("------{}------".format(name['name']))
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
    donation = input("\nWhat would you like to donate?\n")
    result = give_help()
    counter = 0
    for i in range(len(result)):
        if donation.lower() in result[i]['needs'].lower():
            print("------{}------".format(result[i]['name']))
            print(result[i]['name'])
            print(result[i]['url'])
            print(result[i]["address"])
            print(result[i]["phone"])
            # print(result[i]['needs'])
            counter += 1
    if counter == 0:
        print("\nNo Food Banks in your area currently need that item.")


def needs():
    result = give_help()
    print("Find below the list of current Needs and details of the Food Banks closest to you: ")
    for results in result:
        print("------{}------".format(results['name']))
        # print ("data bank needed: ", results["name"])
        print("Donation Needed:", "\n", results["needs"])
        print("Address:", "\n", results["address"])
        print("Phone Number:", "\n", results["phone"])
        print("Email:", "\n", results["email"])
        print("Website:", "\n", results["url"])


if Question1 == 1:
    get_help()
else:
    Question2 = int(input("\nDo you want to:""\n3) DONATE an item? OR \n4) See a list of CURRENT NEEDS?"
                          "\nEnter 3 OR 4\n"))

    if Question2 == 3:
        donate()
    else:
        needs()
