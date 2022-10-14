from typing import List, Dict
# data given from test prompt
drugNames: List[str] = [
  'Aspirin', 'Tylenol', 'Lipitor', 'Prilosec', 'Glucophage', 'Zocor', 'Toprol',
  'Zithromax', 'Zoloft', 'Xanax', 'Wellbutrin', 'Flexeril', 'Prozac',
  'Effexor', 'Adderall'
]

drugQuantities: List[int] = [
  15, 20, 18, 24, 19, 29, 32, 42, 25, 42, 52, 19, 100, 40, 20
]

indices: List[int] = [i for i in range(14)]

# crafted dictionaries
nameQuantityDict: Dict[str, int] = {
  name: quantity
  for (name, quantity) in zip(drugNames, drugQuantities)
}
indexNameDict: Dict[int, str] = {
  index: name
  for (index, name) in zip(indices, drugNames)
}
