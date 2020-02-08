import argparse
from spread_sheet import get_list

class Guest():
  def __init__(self, name, reserve_name):
    self.name = name
    self.reserve_name = reserve_name

class Guests():
  def __init__(self):
    self.update()

  def get_guests(self):
    return self.__guests

  def get_guest(self, name):
    for guest in self.get_guests():
      if guest.name == name:
        return guest
    return


  def is_exist(self, name):
    for guest in self.get_guests():
      if guest.name == name:
        return True
    return False

  def update(self):
    self.__guests = []
    for i, data in enumerate(get_list()):
      if len(data) == 2 and data[0] == '':
        print('null name. check name column where row = {}. reserve_name is {}.'.format(i+2, data[1]))
        continue

      if len(data) == 1:
        self.__guests.append(Guest(data[0], ''))
      else:
        self.__guests.append(Guest(data[0], data[1]))

if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  parser.add_argument('--name', type=str, help='name to confirm reservation')
  args = parser.parse_args()

  confirm_name = args.name
  guests = Guests()

  if confirm_name is not None:
      print('confirm guest name : {}'.format(confirm_name))
      if guests.is_exist(confirm_name):
        guest = guests.get_guest(confirm_name)
        print('exist. name: {}, reserve_name: {}'.format(guest.name, guest.reserve_name))
      else:
        print('no exist.')
