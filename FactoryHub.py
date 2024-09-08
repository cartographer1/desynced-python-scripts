def FactoryHub(Item, N_Slots):
  if not DataTypeSwitch__Item__Component(Item):
    WaitTicks(20)
  else:
    N_Slots = CountSlots()
    N_Slots -= 1

    product = 1
    for item in LoopRecipeIngredients(Item):
      stack_size = GetMaxStack(item)
      product *= stack_size

    weights = _
    total_weight = 0
    for item in LoopRecipeIngredients(Item):
      weight = item * product
      stack_size = GetMaxStack(item)
      weight /= stack_size

      ArrayPush(weight, weights)
      total_weight += weight
    

    idx = 1
    slot_range_start = 1
    for item in LoopRecipeIngredients(Item):
      weight = ArrayGet(weights, idx)
      idx += 1
      
      n_slots = Remap(weight, 0, total_weight, 1, N_Slots)
      slot_range_end = slot_range_start + n_slots
      slot_range_end -= 1
      range = CombineCoordinate(slot_range_start, slot_range_end)
      FixItemSlots(item, range)

      slot_range_start += n_slots

    FixItemSlots(Item, slot_range_start)
    
    Exit()
