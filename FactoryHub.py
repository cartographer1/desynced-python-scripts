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

    weights_id = 1
    ArrayClear(weights_id)
    total_weight = 0
    for item in LoopRecipeIngredients(Item):
      weight = item * product
      stack_size = GetMaxStack(item)
      weight /= stack_size

      ArrayPush(weight, weights_id)
      total_weight += weight
    

    slot_range_start = 1
    for weight in LoopElements(weights_id):
      
      n_slots = Remap(weight, 0, total_weight, 1, N_Slots)
      slot_range_end = slot_range_start + n_slots
      slot_range_end -= 1
      i = slot_range_start
      while i <= slot_range_end:
        FixItemSlots(item, i)
        i += 1

      slot_range_start += n_slots

    FixItemSlots(Item, slot_range_start)
    
    Exit()
