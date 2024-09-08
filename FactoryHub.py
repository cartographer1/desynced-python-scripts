# DSC16m1Xxxd20tR7uN1ErN6i3IQ1Tl3Wi1yP2TxoaE3aTKzF0phnco0UdwBO0sFuMz08NC8a0hfe7806dME10kudBU0sfCcw27GXiK1hTyHP0025wL2YAQD14ArQPs1Zfm4l2OvEn73AQecB20ZONS2zeLaV3ijAQM43Udg01wbdse0JcxOn2THvcZ0VVNCG0pWD1E1KYFAM2ilZQu33JMov1f9Jib1dy6W61qG7ZO0Esal04El7xL4NSsKT19flA32gwtYa1K2O6b3QEHIY2JTeD81FMNQm131a3G1Q4Awl4cO6853NoRZg1y6YIq2apXcM4NVvul00wAhx0Eh5yz1YEJL70fdvWM22kXhZ2bDRwg3LtIe14gW5PL0eE2oJ0SyHH84evDgI1oovzz0RZsna0d8VvS2Qd5DV1iI5bp4ZYjk91HlDZX0odRlC48iEcd4O89TO0a2IgA3fqZEw3nT7yZ2rEFxo1la8Vi4RnduP1Cv5g52DA7cp3CnYD94KnDyx1Znz4K3NOX4124uJS72YHtM13bCSeB1bgIfY1vLsy44P1MKp0O3j0O1NEfLJ2b2RQA2lv7g41oVdqo0wcqT32lfwMG3gChNX0Xolgt1lBgnb3jJMmF1sLLcd11qxRw0VMUuA0wsjGX0nXPRr1872x12nanqo4S0TQ73A8bsk43pHd30lbckQ0vLMPX13SLjJ3fpaxr4XdNX226zkji0AqeJN2udGK32Ft2LL2hk8Fq1G0COR08qvQG2sRTbc2gaY5x03ZZDL0wSy9W
def FactoryHub(Item, N_Slots):
  Unlock()
  
  if not DataTypeSwitch__Item__Component(Item):
    WaitTicks(20)
  else:
    N_Slots = CountSlots()
    # N_Slots -= 1

    product = 1
    for item in LoopRecipeIngredients(Item):
      stack_size = GetMaxStack(item)
      product *= stack_size

    weights_id = 1
    ArrayClear(weights_id)
    total_weight = 0
    max_weight = 0
    for item in LoopRecipeIngredients(Item):
      weight = item * product
      stack_size = GetMaxStack(item)
      weight /= stack_size

      if weight >= max_weight:
        max_weight = weight

      ArrayPush(weight, weights_id)
      total_weight += weight
    

    slot_range_start = 1
    for weight in LoopElements(weights_id):
      
      n_slots = Remap(weight, 0, total_weight, 1, N_Slots)

      if CompareItem(weight, max_weight):
        n_slots -= 1
        FixItemSlots(Item, slot_range_start)
        slot_range_start += 1
      
      slot_range_end = slot_range_start + n_slots
      slot_range_end -= 1
      i = slot_range_start
      while i <= slot_range_end:
        FixItemSlots(weight, i)
        i += 1

      slot_range_start += n_slots
    
    Exit()
