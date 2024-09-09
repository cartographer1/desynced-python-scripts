# DSCLw2gMTt20tMPi50EpPQS3yb4Js1KhvpT4HOf1A1dAd4Y2F6CEt0ZAe2h09QMOV3WQ4pC4PKfvI43iybB424kim4fWQFx4HT3x141pQha3ic6z34DvAC91skMgM4B4NnB2uaBnE4DtHD83f7vVb2TmpbL2kmd8B1sRBYv0uEAMc077ZIy1ipQ5o1D6zBr2R6lhC3fASOt2zuRhP4StCor35DlgK3kDbpk1b7fqz1I1BWw3wdqxv1RPULC3CtNtW1yu5VZ0vsidM1qO50n2kmdxD1OL6jo0Jvfid4XomX80X6x4N3rj3yJ27R74m4UExkl4R8UT03chWKR4TsIg43GR08K0chhBx31fwl90ZwWvA3zGxBc3b2uiF34S4mv1uI4S43mtM6o1dTmpz0yaEbO0ekMAf22ii3M4ZXiXb3msSjJ4467tC3ZC42D08jdIU0Nhegv0HoKyB49dapZ36Y7mu41TkYk2VTAWc1aA5Pb24OCEaFiRD
def DecodeItemTypes(Item, SignalType):
  Unlock()
  
  while CompareItem(Item, _):
    Item = FirstItem()
    WaitTicks(10)

  Item = SetNumber(Item, 0)
  
  code = ReadRadio(Item)
  while CompareItem(code, _):
    WaitTicks(1)
    code = ReadRadio(Item)

  Signal = SetNumber(SignalType, code)
  WaitTicks(10)