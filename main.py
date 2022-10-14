# import custom modules
from data import nameQuantityDict, indexNameDict
from CLI import CLI

# load the inventory data and run the CLI
c = CLI(nameQuantityDict, indexNameDict)
c.run()