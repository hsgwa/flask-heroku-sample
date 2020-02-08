import argparse
from spread_sheet import get_list

class User():
  def __init__(self, name, reserve_name):
    self.name = name
    self.reserve_name = reserve_name

class Users():
  def __init__(self):
    self.update()

  def get_users(self):
    return self.__users

  def is_exist(self, name):
    for user in users.get_users():
      if user.name == name:
        return True
    return False

  def update(self):
    self.__users = []
    for i, data in enumerate(get_list()):
      if len(data) == 2 and data[0] == '':
        print('null name. check name column where row = {}. reserve_name is {}.'.format(i+2, data[1]))
        continue

      if len(data) == 1:
        self.__users.append(User(data[0], ''))
      else:
        self.__users.append(User(data[0], data[1]))

if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  parser.add_argument('--name', type=str, help='name to confirm reservation')
  args = parser.parse_args()

  confirm_name = args.name
  users = Users()

  if confirm_name is not None:
      print('confirm user name : {}'.format(confirm_name))
      if users.is_exist(confirm_name):
        print('exist.')
      else:
        print('no exist.')
