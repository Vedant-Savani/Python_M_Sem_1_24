import CSV_Handler as csvh
import UI as gui
import books as bk

class MissingDetailsError(Exception):
    def __init__(self) -> None:
        pass

class MembershipDoesNotExistError(Exception):
    def __init__(self) -> None:
        pass

class Members:

    memberDetails = {}

    #format of dict :  { 'RollNumber' : { 'name':<name> , 'password':<pass> } }

    def __init__(self) -> None:
        Members.memberDetails = csvh.CSV_Handler.loadMembers()

    def addMember(self, details : dict = {}) -> None:

        try:
            if details == {}: #if nothing is entered
                raise MissingDetailsError
            
            rollNo = list(details.keys())[0] #collects roll number
            memberInfo = details[rollNo] #collects name, password and books borrowed
            
            keys = ('name', 'password') #must be present

            for key in keys:
                if key not in list(memberInfo.keys()) or memberInfo[key] == None: #if any detail is missing
                    raise MissingDetailsError
                
            if rollNo not in list(Members.memberDetails.keys()): #if member is not already present
                Members.memberDetails[rollNo] = {
                    'name' : memberInfo['name'],
                    'password' : memberInfo['password'],
                }

                gui.GUI.success('Success!','Member Added!')

            else: #if member is already present
                gui.GUI.success('Info','Membership Already Exists!')

        
        except MissingDetailsError: #if any detail is missing
            gui.GUI.alert('Error!','Missing Details!')

        except TypeError:
            gui.GUI.alert('Error!','Wrong Information Entered!')

        finally: #after all errors/tasks have been handled
            csvh.CSV_Handler.updateMembers(Members.memberDetails) #update the CSV file

        
#**********************************************************************************


    def removeMember(self, rollNo : str = '') -> None:

        try:
            if rollNo == '': #if nothing is entered
                raise MissingDetailsError
            
            elif rollNo not in list(Members.memberDetails.keys()): #if membership does not exist
                raise MembershipDoesNotExistError
            
            else: #if membership exists
                del Members.memberDetails[rollNo]
                gui.GUI.success('Success!','Membership Removed!')

        except MissingDetailsError:
            gui.GUI.alert('Error!','Missing Details!')

        except MembershipDoesNotExistError:
            gui.GUI.alert('Error!','Membership does not exist!')

        except TypeError:
            gui.GUI.alert('Error!','Wrong Information Entered!')

        finally: #after all errors/tasks have been handled
            csvh.CSV_Handler.updateMembers(Members.memberDetails)


#*************************************************************************************

        
    def updateMember(self, rollNo : str = '', newPassword : str = '') -> None:

        try:
            if rollNo == '' or newPassword == '':
                raise MissingDetailsError
            
            elif rollNo not in list(Members.memberDetails.keys()): #if membership does not exist
                raise MembershipDoesNotExistError

            else:
                Members.memberDetails[rollNo]['password'] = newPassword
                gui.GUI.success('Success', 'Password Updated!')

        except MissingDetailsError:
            gui.GUI.alert('Error!','Missing Details!')

        except MembershipDoesNotExistError:
            gui.GUI.alert('Error!','Membership does not exist!')

        except TypeError:
            gui.GUI.alert('Error!','Wrong Information Entered!')    

        finally:
            csvh.CSV_Handler.updateMembers(Members.memberDetails)


#*************************************************************************************

    def __str__(self) -> str:
        return str(Members.memberDetails)


#*************************************************************************************


def main() -> int:
    members = Members()

    Members.memberDetails = {'IMT00' : {'name' : 'Anish', 'password' : 'a1'},
                          'IMT01' : {'name' : 'Teja', 'password' : 'b1'},
                          'IMT02' : {'name' : 'Bramha', 'password' : 'c1'}}
    
    members.addMember()
    members.addMember({'BT00' : {}})
    members.addMember({'BT00' : {'name' : 'A'}})
    members.addMember({'BT00' : {'name' : 'A' , 'password' : 'xyz'}})
    members.addMember({'IMT02' : {'name' : 'Bramha', 'password' : 'c1'}})

    print(members)

    members.removeMember()
    members.removeMember('BT01')
    members.removeMember('IMT01')

    print(members)

    members.updateMember()
    members.updateMember('BT01')
    members.updateMember('IMT01', 'abc')
    members.updateMember('IMT00', 'abc')

    print(members)


if __name__ == '__main__':
    main()
