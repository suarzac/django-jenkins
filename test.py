import unittest

# This is the class we want to test. So, we need to import it
import Person as Training

class Test(unittest.TestCase):

    student = Training.Students()
    user_id = []  
    user_name = [] 

    # test case function to check the Person.set_name function
    def test_0_set_name(self):
        #print("Start set_name test\n")
        for i in range(4):
            name = 'name' + str(i)
            self.user_name.append(name)
            user_id = self.student.set_name(name)
            self.assertIsNotNone(user_id)  # check if the obtained user id is null or not
            self.user_id.append(user_id)

    # test case function to check the Person.get_name function
    def test_1_get_name(self):
        length = len(self.user_id)  # total number of stored user information
        for i in range(6):
            if i < length:
                self.assertEqual(self.user_name[i], self.student.get_name(self.user_id[i])) # if the two name not matches it will fail the test case
            else:
                # print("Testing for get_name no user test")
                # if length exceeds then check the 'no such user' type message
                self.assertEqual('There is no such user', self.student.get_name(i))

if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()