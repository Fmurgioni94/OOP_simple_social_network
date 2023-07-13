"""
    Author: Francesco Murgioni
    
"""

from File_handler import FileHandler
from Member import Member


class SocialNetwork(Member):
    """
    The class Social Network is the one in charge to display the connection between the members

    Attributes:
         > file_handler :
         > updated_list :
         > member-list :
         > member_list_objects :

    Methods :

        > minor_value_after_zero : this is a static method used as part of another one,
                                   to find the smallest value after 0.

        > create_a_copy_of_a_list : this is a static method used to copy an existent list.

        > create_member_list : this is a  method  a list to store all the name of the member.

        > create_object_member : this is a method that create a list with all the member objects.

        > find_position : this is a method that from a given name find the position of that specific member.

        > find_name : this is a method that find the name of a specific member from a given position.

        > check_input_in_list : this is a method used to check if the given member name
                                is valid and present in the list of members.

        > check_member : this is a method from a given member name it returns the member object.

        > checking_input : this is a method check if the given input is valid e usable

        > count_how_many_friends_for_member : this is a method create a list of friends a given member has

        > creating_friends_list : this is a method create a list of friend for every member object created

        > display_friend_list : this is a method display all the member and for all of them display the friend/s

        > checking_common_friends : this is a method that compare all the member
                                    and find the friends in common for all the members

        > suggest_friend : this is a method that used the list of common friends to find
                           the member that are not friend yet with the selected member
                           and display those name as a suggested friend/s.

        > check_friends_of_friends : this is a method display all the friends of a given member
                                    and display also all of their friend excluding the given member name.

        > check_indirect_friend_for_member : this is a method is an upgrade of the previous one,
                                            it removes all the member that are already friends of the given member
                                            and display only the friends of friends that are not already friends
                                            with the given member.

        > single_member_friends_check : this is a method that display the name of the given user the number of friends
                                        and the list of the friend/s if applicable.

        > member_with_less_friend : this is a method display the member/s of the given file that has fewer friends
                                    and the one that has no friends if applicable.

    """
    input_saving = []
    check_input_loop_condition = True

    def __init__(self):
        super().__init__()
        self._file_handler = FileHandler()
        self._updated_list = self.file_handler.check_if_list_is_good()
        self._member_list = []
        self._member_list_objects = []
        # print(self._updated_list)

    @property
    def file_handler(self):
        return self._file_handler

    @property
    def updated_list(self):
        return self._updated_list

    @property
    def member_list(self):
        return self._member_list

    @member_list.setter
    def member_list(self, new_list):
        if isinstance(new_list, list):
            self._member_list = new_list
        else:
            print("ERROR! that value is not a list")

    @property
    def member_list_objects(self):
        return self._member_list_objects

    @member_list_objects.setter
    def member_list_objects(self, new_list):
        if isinstance(new_list, list):
            self._member_list = new_list
        else:
            print("ERROR! that value is not a list")

    # Static Method Section ---------------------------------------------------------------------
    # in this part of the program I collect all the static method that help other functions to work correctly

    @staticmethod
    def minor_value_after_zero(a_list):
        """
        this function is used to remove the value 0 from a list
        :param a_list: as parameter is taking a copy of the list created by the function
        count_how_many_friend_for_member()
        :return: the minimum value of the list after 0 has been removed
        """
        for value in a_list:
            if value == 0:
                a_list.remove(value)
        return min(a_list)

    @staticmethod
    def create_a_copy_of_a_list(name_of_the_list):
        """
        this function is made to create a copy of a list to avoid to change some crucial information in the main lists
        :param name_of_the_list:  take as a parameter a selected list
        :return: the copy of the selected list
        """
        new_list = []
        for value in name_of_the_list:
            new_list.append(value)
        return new_list

    # Create here a section for all the function that are part of the main features ----------------------------
    # In this section I collect all the functions that are used in one or more main function of the program

    def create_member_list(self):
        """
        this function check the information present in the updated list attribute and remove all the friends and the
        double names in order to have a correct and sorted list with all the member's name
        :return: a list that contains all the member's name
        """
        self.member_list = [*set(x for y in self.updated_list for x in y)]
        self.member_list.sort()
        return self.member_list

    def creating_objects_members(self):
        """
        this function run the create_member_list() function in order to create a list of all member's name
        and for each of the members in that list create an instance using the value of member_list as a name
         and the index of the iteration as a position.
        :return:
        """
        self.create_member_list()
        i = 0
        for members in self.member_list:
            self.member_list_objects.append(self.member_creator(members, i))
            i += 1

    def find_position(self, name):
        """
        this function convert the name of a member in its position
        :param name: as a parameter take the name of the given member
        :return: its position in the list
        """
        for member in self.member_list_objects:
            if name == member.member_name:
                return member.position

    def find_name(self, position):
        """
        this function use the position of the member inside the list to find its name
        :param position: take an integer as a position
        :return: the attribute member_name corresponding to that position
        """
        for member in self.member_list_objects:
            if position == member.position:
                return member.member_name

    def check_input_in_list(self, name):
        """
        this function is a check that make sure that the input is correct and that is inside the member_list
        if it is so, then change the value of the class attribute.
        :param name: this corresponds to the input name
        :return:
        """
        if name in self.member_list:
            SocialNetwork.check_input_loop_condition = False
        else:
            print()
            print(f" > ERROR .... the insert name is not in the list")
            print()

    def check_member(self, member_name):
        """
        this function is used to select a specific object by its attribute member_name
        :param member_name: attribute
        :return: object
        """
        for member in self.member_list_objects:
            if member_name == member.member_name:
                return member

    def checking_input(self):
        """
        this function use a class attribute as a condition for a loop, after taking the input call another function that
        change the value of the class attribute if it finds the input name in the list of members, breaking the loop.
        if the condition of the loop is false then the function check for each member in the list of objects if the last
        name that has been appended in the class attribute input_saving list correspond to one of the object attribute
        member_name
        :return: if member_name correspond to the last input appended in the list then return the objects
        """
        while SocialNetwork.check_input_loop_condition:
            selected_member = input(f" > Select one of the member:"
                                    f"\n\n  {', '.join(self.member_list)}\n\n > ").title()
            SocialNetwork.input_saving.append(selected_member)
            self.check_input_in_list(selected_member)
        else:
            SocialNetwork.check_input_loop_condition = True
            for member in self.member_list_objects:
                if SocialNetwork.input_saving[-1] == member.member_name:
                    return member

    def count_how_many_friend_for_member(self):
        """
        this function create for each member object a list in witch append all the length of the list of the
        object attribute friend
        :return: the list of lengths
        """
        list_of_friend_for_member = []
        for member in self.member_list_objects:
            list_of_friend_for_member.append(len(member.friend))
        return list_of_friend_for_member

    # Create here a section for all the main function of the program --------------------------------------
    # I collect in here all the main function that corresponds to the main features and sub_features of the program

    def creating_friends_list(self):
        """
        this function is the main function used to create the social network, for every member in the list of objects
        and for every value in the updated_list it checks the lengths of the value and if it found that it is equal to 2
        check if the name is equal to the value in index [0] and if it is appends the second value in the list of friends
        :return:
        """
        self.creating_objects_members()
        for member in self.member_list_objects:
            for name in self.updated_list:
                if len(name) == 2:
                    if member.member_name == name[0]:
                        member.friend.append(name[1])
            member.sort_friends_list()

    def display_friend_list(self):
        """
        this function just display the social network that has been created by creating_friend_list
        :return:
        """
        for member in self.member_list_objects:
            print(f"     > {member.member_name.ljust(10)} -> {', '.join(member.friend)}")

    def checking_common_friends(self):
        """
        this function for each member intersect the list of friend with the list of friend of a member of the
        object list and find all the common friends and append them in the list of common friends this creates a
        list of numbers for each member that correspond to a table with all the friend in common compare with all member
        :return:
        """
        for member in self.member_list_objects:
            for common_friends in self.member_list_objects:
                common_friends_list = list(set(member.friend).intersection(common_friends.friend))
                member.common_friends.append(len(common_friends_list))

    def suggest_friend(self):
        """
        this function take the table created with checking_common_friends() function and set to 0 the input given name
        from the list and the friends that the given member already has by checking the position of those friends
        so in the list of the particular user it only remains how many friends it has in common with a member/s that
        is not himself of a friend of him, then the function check witch of the number in this list is the highs one and
        convert the position of this number in the list in a name, and it appen this name in the suggested_friends list
        :return:
        """
        suggested_friends = []
        member = self.checking_input()
        if member is None:
            self.suggest_friend()
        else:
            if member.member_name == member.member_name:
                list_for_suggested_friend = self.create_a_copy_of_a_list(member.friend)
                self_position = int(member.position)
                member.common_friends[self_position] = 0
                for friends in list_for_suggested_friend:
                    position = int(self.find_position(friends))
                    member.common_friends[position] = 0
                if max(member.common_friends) > 0:
                    recommended_friend_position = 0
                    for all_position in member.common_friends:
                        if all_position == max(member.common_friends):
                            suggested_friends.append(self.find_name(recommended_friend_position))
                        recommended_friend_position += 1
                    print()
                    print(f" > The suggest friend/s for {member.member_name} --> {', '.join(suggested_friends)}")
                else:
                    print()
                    print(f" > {member.member_name} has no friends, so no one can be suggest as a friend...")

    def check_indirect_friend_for_member(self):
        """
        this function works very similar with the suggest_friend() function it checks the input at the beginning of the
        function after that if the input is correct from the common_friends list it set to 0 the position
        of the given member and the friends of the given member than append in a list of the names of the friends of the
        selected member friends, removing from the list the selected member name & the double names
        :return:
        """
        friends_of_friends = []
        member = self.checking_input()
        if member is None:
            self.check_indirect_friend_for_member()
        else:
            if member.member_name == member.member_name:
                list_for_indirect_friends = self.create_a_copy_of_a_list(member.friend)
                self_position = int(member.position)
                member.common_friends[self_position] = 0
                for friends in list_for_indirect_friends:
                    position = int(self.find_position(friends))
                    member.common_friends[position] = 0
                if max(member.common_friends) > 0:
                    position = 0
                    for all_position in member.common_friends:
                        if all_position > 0:
                            friends_of_friends.append(self.find_name(position))
                        position += 1
                    print()
                    print(f" > The indirect friend/s for {member.member_name} --> {', '.join(friends_of_friends)}")
                else:
                    print()
                    print(f" > The {member.member_name} has no friends, so has no indirect friend...")

    def check_friends_of_friends(self):
        """
        this function check the given input and if it is correct pick up of the friends that a user has and check their
        friends as well and print the list of friends,
        removing from this list the name of the selected member
        :return:
        """
        member = self.checking_input()
        print()
        if member is None:
            self.check_friends_of_friends()
        else:
            if not member.friend:
                print(f" > {member.member_name} has {len(member.friend)} friend/s")
            else:
                for friend in member.friend:
                    user = self.check_member(friend)
                    user.friend.remove(member.member_name)
                    print(f" > {user.member_name.ljust(10)} -> {', '.join(user.friend)}")
                    user.friend.append(member.member_name)

    def single_member_friends_check(self):
        """
        this function checks the given input if it is correct then find the list of friends and then print the length
        of the list and the value that has inside.
        :return:
        """
        member = self.checking_input()
        if member is None:
            self.single_member_friends_check()
        else:
            if member.member_name == member.member_name:
                if not member.friend:
                    print(f" > {member.member_name} has {len(member.friend)} friend/s")
                else:
                    print()
                    print(f" > {member.member_name} has {len(member.friend)} friend/s ---> {', '.join(member.friend)}")
            else:
                print()
                print(f" > ERROR.... The name is not in the file, please try again!")
                print()
                self.single_member_friends_check()

    def member_with_less_friend(self):
        """
        this function create two list one to append all the members with no friends and the other to appen the friends
        that has the least friends in the social network.
        To do so it runs a function that calculate all the lengths of a member_friend list for each of the member of the
        social network then took the value that is 0 and appen that member's name into the no_friend list
        than remove the value from the list and return the minimum value of the same list that correspond to the
        member with the least friend.

        :return:
        """
        member_with_no_friends = []
        member_with_less_friend = []
        self.count_how_many_friend_for_member()
        minor_value_after_0 =\
            self.minor_value_after_zero(self.create_a_copy_of_a_list(self.count_how_many_friend_for_member()))
        i = 0
        for x in self.count_how_many_friend_for_member():
            if x == minor_value_after_0:
                member_with_less_friend.append(self.find_name(i))
            elif x == 0:
                member_with_no_friends.append(self.find_name(i))
            i += 1
        print(f" > Member/s with less friend --> {', '.join(member_with_less_friend)}\n"
              f" > Member/s with no friends --> {' '.join(member_with_no_friends)}")
