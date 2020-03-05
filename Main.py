print ("--------------------------------------------------------------------------------")
print ("NORTON'S CALCULATOR FOR UNIT 3 (ENGINEERING SCIENCE) - ASSIGNMENT 3 - TASK 2A")
print ("--------------------------------------------------------------------------------")

V1 = float(input("Please enter a value for V1 (V): "))
V2 = float(input("Please enter a value for V2 (V): "))
R1 = int(input("Please enter a value for R1 (Ω): "))
R2 = int(input("Please enter a value for R2 (Ω): "))
R3 = int(input("Please enter a value for R3 (Ω): "))
R4 = int(input("Please enter a value for R4 (Ω): "))
R5 = int(input("Please enter a value for R5 (Ω): "))
R6 = int(input("Please enter a value for R6 (Ω): "))
R7 = int(input("Please enter a value for R7 (Ω): "))
R8 = int(input("Please enter a value for R8 (Ω): "))

print ("Calculating current and voltage through R8 using Norton's Theorom...")

print ("RTH = ((R1+R6)||R4)+R2||(R3+R7)")

RTH1 = (((R1+R6)*R4)/(R1+R4+R6))+R2
RTH2 = R7+R3
RTH = (RTH1*RTH2)/(RTH1+RTH2)
print ("RTH =",RTH)

print ("ResistanceLeftSide (RL) = (R1+R6)+((R2*R4)/(R2+R4))")
RL = (R1+R6)+((R2*R4)/(R2+R4))
print ("RL =",RL)

print ("CurrentLeftSide (IL) = V1/RL")
IL = V1/RL
print ("IL =",IL)

print ("CurrentSourceLeft (ISL) = IL*(R4/(R4+R2))")
ISL = IL*(R4/(R4+R2))
print ("ISL =",ISL)

print ("CurrentSourceRight (ISR) = V2\(R3+R7)")
ISR = V2/(R3+R7)
print ("ISR =",ISR)

print ("CurrentSourceOverall (ISO) = ISR+ISL")
ISO = ISR+ISL
print ("ISO =",ISO)

print ("Current through I8 = ISO*(RTH/(RTH+R8+R5))")
I8 = ISO*(RTH/(RTH+R8+R5))
print ("Current through I8 =",I8,"A")

print ("Voltage through V8 = I8*R8")
V8 = I8*R8
print ("Voltage through V8 =",V8,"V")
print ("--------------------------------------------------------------------------------")

print()
print()
print()
print ("--------------------------------------------------------------------------------")
print()
print()
print()

print ("--------------------------------------------------------------------------------")
print ("THEVENIN'S CALCULATOR FOR UNIT 3 (ENGINEERING SCIENCE) - ASSIGNMENT 3 - TASK 2B")
print ("--------------------------------------------------------------------------------")

V1 = float(input("Please enter a value for V1 (V): "))
V2 = float(input("Please enter a value for V2 (V): "))
R1 = int(input("Please enter a value for R1 (Ω): "))
R2 = int(input("Please enter a value for R2 (Ω): "))
R3 = int(input("Please enter a value for R3 (Ω): "))
R4 = int(input("Please enter a value for R4 (Ω): "))
R5 = int(input("Please enter a value for R5 (Ω): "))
R6 = int(input("Please enter a value for R6 (Ω): "))
R7 = int(input("Please enter a value for R7 (Ω): "))
R8 = int(input("Please enter a value for R8 (Ω): "))

print ("Calculating current and voltage through R2 using Thevenin's Theorom...")

print ("RTH=((R1+R6)||R4)+((R3+R7)||(R5+R8))")

RTH1 = ((R1+R6)*R4)/(R1+R4+R6)
print ("(R1+R6)||R4) =",RTH1)

RTH2 = ((R3+R7)*(R5+R8))/((R3+R7)+(R5+R8))
print ("((R3+R7)||(R5+R8)) =",RTH2)

RTH = (RTH1+RTH2)
print ("RTH =",RTH)

print ("CurrentLeftSide (IL) = V1\(R1+R4+R6)")
IL = V1/(R1+R4+R6)
print ("IL =",IL)

print ("VoltageLeftSide (VL) = IL1*R4")
VL = IL*R4
print ("VL =",VL)

print ("CurrentRightSide (IR) = V2\(R3+R5+R7+R8)")
IR = V2/(R3+R5+R7+R8)
print ("IR =",IR)

print ("VoltageRightSide (VR) = IR1*(R5+R8)")
VR = IR*(R5+R8)
print ("VR =",VR)

print ("VTH = VR-VL")
if VL>VR:
  VTH = VL-VR
elif VR>VL:
  VTH = VR-VL
else:
  print ("Error")
print ("VTH =",VTH)

print ("Current through I2=VTH/(RTH+R2)")
I2 = VTH/(RTH+R2)
print ("Current through I2 =",I2,"A")

print ("Voltage through V2=I2*R2")
V2 = I2*R2
print ("Voltage through V2 =",V2,"V")
print ("--------------------------------------------------------------------------------")
