# DSC17x2iWfkm0tR7wB3yTjrI3ONWCv0QmsKF3quwfA20UPOY0Y47b416ZSNB3OWt7M0EDelw120CZ50vQ21z08Y7hs2ahVpb31sUr01pFZP7234xPV0q6FiQ0yCdcI1F0hB20j6Vny0erhvy2hcPuQ0uoHYO0ydqK63UBVeI2VHPfT34jdd70UvqlN3RcNgS1OuIhQ0VFARN4DGHJY1ipXI74Maxl21Qxeyt3i3ixd0dySzm0hYx7c49KRWy3O6xYL0x98aT2sbmlT40rN9D3XmbGE0NuaY81pqRek2gmTQy3afYbR4Masmf2XHq3p3WNM8l1rUIsM3ckjxP0xzyn827Egxv0JG7ry1ZKpcm0FiLIz4ddWtU1TWRpq0zHtEl4KA7l63YEceI3qFmQj1NBDDy03uZyo3gyqb32iNubG11qBmp25Bmfv0sryWu4WIynX23douf37hrL51LB73h3jm00X0u4hpR0qKb0u2273yK27EOLx2FT9k742pY8d44tvDn4MkOnh1K9tD94SWErV17vRCb1Ak4ny0mO3oh3L7y9a1bq0Yx1wu3bO4VvRzX0IzrT62uKRE82r2Xku2ghzoJ1w7RRK178lfG3SC5EB4aeagS2IU1pk2iSrkP2gmfG82ps8uw3VC9jH09uDii0Q2dCk3HVvQf3WHQeG39Hnnj1rTU7i3l1b8L2xInvk4gedgT4A3EIn4WQhFv1TOGhA3h4zVP0JTJ670a5TG82rQPON2g8DNu48o9jH1PwqMp1VYnEi09GF91
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
    Ingredient1 = SetNumber(Ingredient1, n_slots_1 * stack_size_1)
    Ingredient2 = SetNumber(Ingredient2, n_slots_2 * stack_size_2)
    Ingredient3 = SetNumber(Ingredient3, n_slots_3 * stack_size_3)
    
    RequestItem(Ingredient1)
    if not CompareItem(Ingredient2, _):
      RequestItem(Ingredient2)
    if not CompareItem(Ingredient3, _):
      RequestItem(Ingredient3)

    WaitTicks(60)
