def FactoryInputAutoRequest(Item, Ingredient1, Ingredient2, Ingredient3, N_Slots, Hub):
  if not DataTypeSwitch__Item__Component(Item):
    Item = ReadSignal(Hub)
  else:
    N_Slots = CountSlots()
    Ingredient1, Ingredient2, Ingredient3 = GetIngredients(Item)
    stack_size_1 = GetMaxStack(Ingredient1)
    stack_size_2 = GetMaxStack(Ingredient2)
    stack_size_3 = GetMaxStack(Ingredient3)

    product = stack_size_1
    if not CompareItem(Ingredient2, _):
      product *= stack_size_2
    if not CompareItem(Ingredient3, _):
      product *= stack_size_3
    
    weight_1 = Ingredient1 * product 
    weight_2 = Ingredient2 * product 
    weight_3 = Ingredient3 * product 
    weight_1 /= stack_size_1
    weight_2 /= stack_size_2
    weight_3 /= stack_size_3
    
    total_weight = weight_1
    total_weight += weight_2
    total_weight += weight_3
    
    n_slots_1 = Remap(weight_1, 0, total_weight, 1, N_Slots)
    n_slots_2 = Remap(weight_2, 0, total_weight, 1, N_Slots)
    n_slots_3 = Remap(weight_3, 0, total_weight, 1, N_Slots)
    Ingredient1 = SetNumber(Ingredient1, n_slots_1)
    Ingredient2 = SetNumber(Ingredient2, n_slots_2)
    Ingredient3 = SetNumber(Ingredient3, n_slots_3)
    
    
    
