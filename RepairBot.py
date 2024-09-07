def RepairBot(target):
  for target, _ in LoopSignalMatch("v_damaged"):
    SetToComponent(target, "c_repairer")
    if CheckHealth(target):
      WaitTicks(20)

  WaitTicks(20)
