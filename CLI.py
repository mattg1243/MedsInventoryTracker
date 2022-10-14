from typing import Dict
import sys


class CLI():
  # the constructor will take the inventory dict as an argument
  # and load it into a private isntance variable so it cant be tampered with
  def __init__(self, inventory: Dict[str, int], indices: Dict[int, str]):
    self.__inventory = inventory
    self.__indices = indices

  # standard setters and getters
  def getInventory(self) -> Dict[str, int]:
    return self.__inventory

  def setInventory(self, inventory: Dict[str, int]) -> None:
    self.__inventory = inventory

  def getIndices(self) -> Dict[int, str]:
    return self.__indices

  def setIndices(self, indices: Dict[int, str]) -> None:
    self.__indices = indices

  def inventoryScreen(self) -> None:
    # store a copy of the current state of the inventory
    inventory: Dict[str, int] = self.getInventory()
    # print header info
    print("""
---------------------
Medication inventory:
---------------------
## Name         Qty     ## Name         Qty     ## Name         Qty     ## Name         Qty"""
          )
    # initialize an index counter
    i: int = 0
    for med in inventory:
      # print the nicely formatted data
      print(f"{i+1:>2} {med:12} {inventory[med]:>3}", end="\t\t")
      # check if we need to start a new row
      if (i + 1) % 4 == 0 and i > 0:
        print("")
      # increment the index counters
      i += 1
    # print an empty line for formatting purposes
    print("")

  # method for adding medication
  def addMedication(self) -> None:
    # store a copy of the current state of the index dict
    inventory = self.getInventory()
    indices = self.getIndices()
    self.inventoryScreen()
    print("Which medication do you want to deposit?")
    while True:
      try:
        medNumber: int = int(input("Enter the mediction number:\n> ").strip())
      except ValueError:
        print("Please enter a number")
        continue
      break
    if medNumber not in [i for i in range(len(self.getInventory()))]:
      raise ValueError(
        "No medication with that number exists. Returning to menu")
    else:
      print(
        f"How many pills of {indices[medNumber - 1]} would you like to add?")
      while True:
        try:
          amountToAdd: int = int(input("> ").strip())
          if amountToAdd < 0:
            raise ValueError
        except ValueError:
          print("Please enter a positive number")
          continue
        # break out of loop once input is valid
        break
      # add to the inventory and update instance variable
      inventory[indices[medNumber - 1]] += amountToAdd
      self.setInventory(inventory)
      # display confirmation
      print(
        f"UPDATE: {indices[medNumber - 1]} new balance: {self.getInventory()[indices[medNumber - 1]]}"
      )
  # potential refactoring: this could be combined with the addMedication method with the use
  # of an add/subtract flag to keep the code dry, but no time for that now. copy and paste will do
  def removeMedication(self) -> None:
    # store a copy of the current state of the index dict
    inventory = self.getInventory()
    indices = self.getIndices()
    self.inventoryScreen()
    print("Which medication do you want to remove?")
    while True:
      try:
        medNumber: int = int(input("Enter the mediction number:\n> ").strip())
      except ValueError:
        print("Please enter a number")
        continue
      break
    if medNumber not in [i for i in range(len(self.getInventory()))]:
      raise ValueError(
        "No medication with that number exists. Returning to menu")
    else:
      print(
        f"How many pills of {indices[medNumber - 1]} would you like to remove?"
      )
      while True:
        try:
          amountToRemove: int = int(input("> ").strip())
          # check if theres enough inventory for the removal
          if amountToRemove > inventory[indices[medNumber - 1]] or amountToRemove < 0:
            raise ValueError
        except ValueError:
          print(
            "Please enter a positive number that is less than the current inventory"
          )
          continue
        # break out of loop once input is valid
        break
      # add to the inventory and update instance variable
      inventory[indices[medNumber - 1]] -= amountToRemove
      self.setInventory(inventory)
      # display confirmation
      print(
        f"UPDATE: {indices[medNumber - 1]} new balance: {self.getInventory()[indices[medNumber - 1]]}"
      )

  # method for displaying main menu
  def mainMenu(self) -> None:
    selection = input("""
  **** Main Menu ****
      Press 1: medication status
      2: add medication to inventory
      3: remove medication from inventory
      4: quit\n> """).strip()
    if selection not in '1234':
      raise ValueError("Invalid Input: enter a number between 1 and 4")
    else:
      # listen for each command
      if selection == '1':
        self.inventoryScreen()
      if selection == '2':
        self.addMedication()
      if selection == '3':
        self.removeMedication()
      if selection == '4':
        print("Program exiting, have a superior day!")
        sys.exit()

  # main function that runs the entire CLI
  def run(self) -> None:
    while True:
      try:
        self.mainMenu()
      except ValueError:
        print("Invalid input, try again")
        continue
