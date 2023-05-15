"""
    Author: Francesco Murgioni

"""
import File_handler
from Social_Network import SocialNetwork


def spaces_between_the_function():
    """
    this function has the purpose to display the all program more nicely and easy to read
    :return:
    """
    print()
    print("-------------------------------------------------------------------------------")
    print()


print()
print("------------------------ Welcome to the Social Network ------------------------")
print()
while True:
# the beginning of the main program
    social = SocialNetwork()
    spaces_between_the_function()

    if File_handler.FileHandler.inconsistency:
        """
        if the file is inconsistent then is going to be able only to display the social network and then the program
        will start again from the beginning.
        """

        social.creating_friends_list()
        social.display_friend_list()
        File_handler.FileHandler.inconsistency = False
        spaces_between_the_function()
    else:
        # if the file is consistent then it will run with all features
        while True:
            first_question = input(f" > Display the social network (y/n)? ").lower()
            if first_question == "y":
                print()
                social.creating_friends_list()
                # the display function is called only if the user input yes
                social.display_friend_list()
                break
            elif first_question == "n":
                social.creating_friends_list()
                break
            else:
                print()
                print(f" > ERROR....the input is incorrect, press 'y' for 'yes', and 'n' for 'no' ")
                print()
                continue

        spaces_between_the_function()
        # the checking_common_friends() function will run always because it is an important part of some main functions
        social.checking_common_friends()

        while True:
            bonus_question = input(f" > Do you want to recommend a friend to an User (y/n)? ")
            if bonus_question == "y":
                print()
                social.suggest_friend()
                while True:
                    print()
                    second_question = input(f" > Do you want to recommend friends to another user (y/n)? ")
                    if second_question == "y":
                        print()
                        social.suggest_friend()
                    elif second_question == "n":
                        break
                    else:
                        print()
                        print(f" > ERROR....the input is incorrect, press 'y' for 'yes', and 'n' for 'no' ")
                        spaces_between_the_function()
                break
            elif bonus_question == "n":
                break
            else:
                print(f" > ERROR....the input is incorrect, press 'y' for 'yes', and 'n' for 'no' ")

        spaces_between_the_function()

        while True:
            third_question = input(f" > Display how many friends a user has (y/n)? ")
            if third_question == "y":
                print()
                social.single_member_friends_check()
                while True:
                    print()
                    repeat_question = input(f" > Do you want to display how many friends another user has (y/n)? ")
                    if repeat_question == "y":
                        print()
                        social.single_member_friends_check()

                    elif repeat_question == "n":
                        break
                    else:
                        print()
                        print(f" > ERROR....the input is incorrect, press 'y' for 'yes', and 'n' for 'no' ")
                        spaces_between_the_function()
                break
            elif third_question == "n":
                break
            else:
                print(f" > ERROR....the input is incorrect, press 'y' for 'yes', and 'n' for 'no' ")

        spaces_between_the_function()

        while True:
            fourth_question = input(f" > Display the users with the least number of or have 0 friends (y/n)? ")
            if fourth_question == "y":
                print()
                social.member_with_less_friend()
                break
            elif fourth_question == "n":
                break
            else:
                print(f" > ERROR....the input is incorrect, press 'y' for 'yes', and 'n' for 'no' ")

        spaces_between_the_function()

        while True:
            fifth_question = input(f" > Display the friends of friends of a given user (y/n)? ")
            if fifth_question == "y":
                print()
                social.check_friends_of_friends()
                while True:
                    print()
                    repeat_question = input(f" > Display the friends of friends of another user (y/n)? ")
                    if repeat_question == "y":
                        print()
                        social.check_friends_of_friends()

                    elif repeat_question == "n":
                        break
                    else:
                        print()
                        print(f" > ERROR....the input is incorrect, press 'y' for 'yes', and 'n' for 'no' ")
                        spaces_between_the_function()
                break
            elif fifth_question == "n":
                break
            else:
                print(f" > ERROR....the input is incorrect, press 'y' for 'yes', and 'n' for 'no' ")

        spaces_between_the_function()
        while True:
            sixth_question = input(f" > Do you want to check the indirect friend of a given user (y/n)? ")
            if sixth_question == "y":
                print()
                social.check_indirect_friend_for_member()
                while True:
                    print()
                    repeat_question = input(f" > Do you want to check the indirect friend of another user (y/n)? ")
                    if repeat_question == "y":
                        print()
                        social.check_indirect_friend_for_member()

                    elif repeat_question == "n":
                        break
                    else:
                        print()
                        print(f" > ERROR....the input is incorrect, press 'y' for 'yes', and 'n' for 'no' ")
                        spaces_between_the_function()
                break
            elif sixth_question == "n":
                break
            else:
                print(f" > ERROR....the input is incorrect, press 'y' for 'yes', and 'n' for 'no' ")

        spaces_between_the_function()

        while True:
            re_start = input(f" > Do you want checking another file? y/n ").lower()
            if re_start == "y":
                print()
                break
            elif re_start == "n":
                print(f" > Thank you so much for using my program.")
                exit()
            else:
                print()
                print(f" > Wrong input use 'y' for Yes, and 'n' for No")
