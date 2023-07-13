"""
    Author: Francesco Murgioni

"""

from os.path import exists

class FileHandler:
    """
    This is a class that control and extract information about a given file

    Attributes:

        > filename (string) : input the name of the file to check

        > list (list) : data structure use to store all the information from the given file

    Methods :

        > check_if_file_exist : this method check if the file with the given name is present in the directory.

        > read_file : this method extract all the information from the file

        > updating_list : this method takes all the information given by the read_file method
                        and reorganize them in a specific way.

        > check_if_list_is_good : This method check if the file is empty, consistent or inconsistent.

        > inconsistent_case : if the file is inconsistent ( A friend with B, but B non friend with A)
                              it show an error message.

    """
    inconsistency = False
    def __init__(self):
        """
         Attributes:

        > filename (string) : the name of the file that needs to be checked.
        > list (list) : data structure use to store all the information from the given file.

        """
        self._filename = input("Input the name of the file that you want to open: ").lower()
        self._list = []

    @property
    def filename(self):
        """
        filename is the getter of the private attribute _filename
        :return
            the name of the file
        the setter makes sure that this specific attribute can be change only with a string
        """
        return self._filename

    @filename.setter
    def filename(self, new_file_name):
        if isinstance(new_file_name, str):
            self._filename = new_file_name
        else:
            print("ERROR the new value is not a list!")

    @property
    def list(self):
        """
        list is the getter of the private attribute _list
        :return: the list
        to change the value, the setter before check that the new value is a list then it change it
        """
        return self._list

    @list.setter
    def list(self, new_list):
        if isinstance(new_list, list):
            self._list = new_list
        else:
            print("ERROR the new value is not a list!")
        self._list = new_list
        self.list.sort()

    def check_if_file_exist(self):
        """
        this specific function check if the file is the current directory
        :return: a boolean value
        the user is able to input "n" to close the program at this stage
        if the file is not in the current directory an error message is display and the user have the possibility to
        try again with another file
        """
        if exists(self._filename):
            return
        elif self.filename == "n":
            exit()
        else:
            print()
            print(f"------------------------------------- Ops! -------------------------------------\n\n"
                  f"ERROR >>>> The selected file doesn't exist in the current directory...")
            self.filename = input("Try with another file name, or stop the program pressing n: ").lower()
            self.check_if_file_exist()

    def read_file(self):
        """
        this function open and read the file, and append each line as a list inside the list attribute

        """
        f = open(self.filename, "r")
        for lines in f:
            self.list.append(lines)
        f.close()

    def updating_list(self):
        """
        this function before running call the function to check the file if exist it call the function to read the file
        only then read the list starting after line [0].
        For all the item in the list it separates the string in single names and remove the "\n" present in the list
        :return: a list that the rest of the program can use without problems
        """
        self.check_if_file_exist()
        self.read_file()
        updated_list = []
        for item_list in self.list[1:]:
            updated_list.append(item_list.split())
        return updated_list

    def inconsistent_case(self, final_list):
        """
        this function runs only if the selected file is inconsistent, it gives some option to the user lik
        open the social network and see what is inside the file, or open another file
        :param final_list: this parameter is given by the check_if_is_good() function and represent the list update and
        ready to use
        :return: a ready to use list of members and friends of the inconsistent file
        """
        print()
        print(f"------------------------------------- Ops! -------------------------------------\n\n"
              f" > ERROR..... The selected file is inconsistent!")
        while True:
            input_inconsistent_file = input("You want to open it anyway? y/n ").lower()
            if input_inconsistent_file == "y":
                FileHandler.inconsistency = True
                return final_list

            elif input_inconsistent_file == "n":
                self.filename = input("Try with another file, or stop the program pressing n:\n").lower()
                self.list.clear()
                return self.check_if_list_is_good()

            else:
                print("Wrong input use 'y' for Yes, and 'n' for No")

    def check_if_list_is_good(self):
        """
        this function use the updating_list() function to correct the original list made from the file, and
        make sure that it is ready to use.
        it is also checking for all the value in the list if it's present its reverse value.
        the function use this method to check if a file is consistent or inconsistent.
        :return: the final list ready to use if the file is consistent or
         run another function if the file is inconsistent.
        """

        final_list = self.updating_list()
        true_false_list = []

        if not final_list:
            print()
            print(f"------------------------------------- Ops! -------------------------------------\n\n"
                  f"ERROR >>>> The selected file is empty!")
            self.filename = input("Try with another file...Or stop the program pressing n: ").lower()
            self.list.clear()
            return self.check_if_list_is_good()
        else:
            for value in final_list:
                if value[::-1] in final_list:
                    true_false_list.append(1)
                else:
                    true_false_list.append(0)

            if min(true_false_list) == 1:
                # return self.format_the_names(final_list)
                return final_list
            else:
                return self.inconsistent_case(final_list)
