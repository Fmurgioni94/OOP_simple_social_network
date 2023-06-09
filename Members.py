"""
    Author: Francesco Murgioni
    
"""

class Member:
    """
    This is a class that represent the members, stores all the information about them.

    Attributes :

        > member_name : it stor the name of the member.

        > position : this attribute store the position of the member.

        > friend : this attribute store the list of fiends that a member has.

        > common friend : in this attribute is stored how many fiend a member has in common with the other members.

    Methods :

        > sort_friend_list : this method sort the list of friends.

        > member_creator : this method it's called in another class, it is used to create the instances for this class.

    """
    def __init__(self):

        self._member_name= "member_name"
        self._position = 0
        self._friend = []
        self._common_friends = []

    @property
    def member_name(self):
        """
        this is the getter of the private attribute _member_name
        :return: the value of that attribute

        the setter is used to change this value but before changing it, checks if the new value is a string
        """
        return self._member_name

    @member_name.setter
    def member_name(self, new_member_name):
        if isinstance(new_member_name, str):
            self._member_name = new_member_name
        else:
            print("ERROR, the value for this variable is not a string")

    @property
    def position(self):
        """
        this is the getter of the attribute _position
        :return: it return the value of this attribute

        the setter check if the new value is an integer if it is then the value will be change
        """
        return self._position

    @position.setter
    def position(self, new_position):
        if isinstance(new_position, int):
            self._position = new_position
        else:
            print("ERROR, the value for this variable is not a integer")

    @property
    def friend(self):
        """
        this is the getter of the attribute friend
        :return: the value of this attribute

        the setter check if the new value is a list and then if it is change the value
        """
        return self._friend

    @friend.setter
    def friend(self, new_list_of_friend):
        if isinstance(new_list_of_friend, list):
            self._friend = new_list_of_friend
        else:
            print("ERROR, the value for this variable is not a string")

    @property
    def common_friends(self):
        """
        this is the getter for the attribute _common_friends
        :return: the value of that attribute

        the setter checks if the new value is a list then it change it
        """
        return self._common_friends

    @common_friends.setter
    def common_friends(self, new_common_friend_list):
        if isinstance(new_common_friend_list, list):
            self._common_friends = new_common_friend_list
        else:
            print("ERROR, the value for this variable is not a string")

    def sort_friends_list(self):
        """
        this function is used to sort the list in the attribute _friend
        :return:
        """
        self.friend.sort()

    @staticmethod
    def member_creator(name, position):
        """
        this is a static method use as a part of function in the SocialNetwork class to create the Member objects
        :param name: this parameter is used to set the member_name attribute
        :param position: this parameter is used to set the position attribute
        :return: it returns the object created in this way
        """
        member = Member()
        member.member_name = name
        member.position = position
        return member



