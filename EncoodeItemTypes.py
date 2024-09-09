def EncodeItemTypes():
  Unlock()
  reg_idx = 1
  band_reg = CombineRegister(1, "c_radio_transmitter")
  value_reg = CombineRegister(2, "c_radio_transmitter")
  while 0 == 0:
    comp_idx = CombineRegister(reg_idx, "c_behavior")
    reg = GetFromComponent(comp_idx)
    if CompareItem(reg, _):
      Break()

    SetToComponent(SetNumber(reg, 0), band_reg)
    SetToComponent(reg)
    WaitTicks(1)
    
    reg_idx += 1
