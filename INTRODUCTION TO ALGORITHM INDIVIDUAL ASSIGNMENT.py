print ("Enter 0 to 5 for the following options \n0 --> Issue new ticket number \n1 --> Assign ticket in queue for bill payment to Counter 1")
print ("2 --> Assign ticket in queue for bill payment to Counter 2 \n3 --> Assign ticket in queue for license renew to Counter 3 ")
print ("4 --> Assign ticket in queue for license renew to Counter 4 \n5 --> Quit program \n ")

#Definitions
bp_display = []
lr_display = []
bp_c1_queue = []
bp_c2_queue = []
lr_c1_queue = []
lr_c2_queue = []
#Queue for Bill Payment, License Renwal, Bill Payment Counter 1, Bill Payment Counter 2, License Renewal Counter 1, License Renewal Counter 2
bp_num = 1000  # Starting number for Bill Payment tickets
lr_num = 2000  # Starting number for License Renewal tickets

while True:
    if bp_display == []:
        bp_display = ("'No ticket'")
    if lr_display == []:
        lr_display = ("'No ticket'")
    if bp_c1_queue == []:
        bp_c1_queue = ("'No ticket'")
    if bp_c2_queue == []:
        bp_c2_queue = ("'No ticket'")
    if lr_c1_queue == []:
        lr_c1_queue = ("'No ticket'")
    if lr_c2_queue == []:
        lr_c2_queue = ("'No ticket'")

    print("Ticket in queue for bill payment:", bp_display)
    print("Ticket in queue for license renewal:", lr_display)
    print("'Counter 1' :", bp_c1_queue, ",", "'Counter 2' :", bp_c2_queue, ",", "'Counter 3' :", lr_c1_queue, ",", "'Counter 4' :", lr_c2_queue)
    print("")

    VG = input("Enter your option - ")
    print('')

    if VG == "0":  # Ticket counter
        print("Enter 0 or 1 for the following options:")
        print("0 -> New ticket for bill payment")
        print("1 -> New ticket for license renewal \n ")
        
        while True:
        
         TG = input("Enter your option: ")
         print("")

         if TG != "0" and TG != "1":
             print("Invalid option entered. Please enter 0 or 1.")
             print("")
             continue

         elif TG == "0":
             if bp_display == ("'No ticket'"):
              bp_display = []
              bp_num += 1
              bp_display.append(bp_num)
              break
             else:
              bp_num += 1
              bp_display.append(bp_num)
              break
    
         elif TG == "1":
             if lr_display == ("'No ticket'"):
              lr_display = []
              lr_num += 1
              lr_display.append(lr_num)
              break
             else:
              lr_num += 1
              lr_display.append(lr_num)
              break

    elif VG == "1":  # Bill Payment counter 1
        if    bp_display == ("'No ticket'"):
              print("Error, no new tickets in the ticket counter \n ")
        else:
              bp_c1_queue = bp_display.pop(0)
              print("Ticket assigned to queue for Bill Payment to counter 1 \n ")
              
    elif VG == "2":  # Bill Payment counter 2
        if    bp_display == ("'No ticket'"):
              print("Error, no new tickets in the ticket counter \n ")
        else:
              bp_c2_queue = bp_display.pop(0)
              print("Ticket assigned to queue for Bill Payment to counter 2 \n ")

    elif VG == "3":  # License Renewal Counter 1
        if    lr_display == ("'No ticket'"):
              print("Error, no new tickets in the ticket counter \n ")
        else:
              lr_c1_queue = lr_display.pop(0)
              print("Ticket assigned to queue for License Renewal to counter 1 \n ")

    elif VG == "4":  # License Renewal Counter 2
        if    lr_display == ("'No ticket'"):
               print("Error, no new tickets in the ticket counter \n ")
        else:
               lr_c2_queue = lr_display.pop(0)
               print("Ticket assigned to queue for License Renewal to counter 2 \n ")

    elif VG == "5":  # Exit the program
        print(" Quitting the program...")
        break
    
    else:
     print("Invalid option, try again… \n ")