# import cv2
# from pyzbar.pyzbar import decode
#
# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# camera = True
#
#
# while camera == True:
#     success, frame = cap.read()


# import cv2
# from pyzbar.pyzbar import decode
# import time
#
# # Define a dictionary to map barcodes to their prices
# barcode_price_map = {
#     '123456789012': 17.00,  # Example barcode and price
#     '987654321098': 25.50,
#     '9789995001025': 18,# Another example
#     # Add more barcode-price mappings as needed
# }
#
#
# def get_book_price(barcode_data):
#
#     """Lookup the price of a book based on barcode data."""
#     return barcode_price_map.get(barcode_data, 'Price not found')
#
#
# # Initialize the webcam
# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)
# cap.set(cv2.CAP_PROP_FPS, 30)
# # camera = True
#
# cooldown_delay = 1.0  # 1 second
# last_detection_time = time.time() - cooldown_delay
#
# while camera:
#     success, frame = cap.read()
#
#     if not success:
#         print("Failed to grab frame")
#         break
#
#     # Decode barcodes in the frame
#     decoded_objects = decode(frame)
#
#     current_time = time.time()
#
#     barcode_detected = False
#
#     for obj in decoded_objects:
#         barcode_data = obj.data.decode('utf-8')
#         barcode_type = obj.type
#         price = get_book_price(barcode_data)
#
#         if current_time - last_detection_time >= cooldown_delay:
#
#             # Print barcode type, data, and price
#             print(f"Barcode Type: {barcode_type}")
#             print(f"Barcode Data: {barcode_data}")
#             print(f"Price: ${price}")
#
#         # Draw the barcode data on the frame
#             cv2.putText(frame, f"{barcode_data} - ${price}",
#                         (obj.rect.left, obj.rect.top - 10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
#             cv2.rectangle(frame, (obj.rect.left, obj.rect.top),
#                         (obj.rect.left + obj.rect.width, obj.rect.top + obj.rect.height),
#                         (0, 255, 0), 2)
#
#     # last_detection_time = current_time
#     barcode_detected = True
#
#     if barcode_detected:
#         last_detection_time = current_time
#
#     # Display the frame
#     cv2.imshow('Barcode Scanner', frame)
#
#     # Break the loop if 'q' is pressed
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break
#
# # Release the webcam and close windows
# cap.release()
# cv2.destroyAllWindows()

# for code in decode(frame):
#     print(code.type)
#     print(code.data.decode('utf-8'))
# cv2.imshow('Testing-code-scan', frame)
# cv2.waitKey(10)




# import cv2
# from pyzbar.pyzbar import decode
# import time
#
# # Define a dictionary to map barcodes to their prices
# barcode_price_map = {
#     '123456789012': 17.00,  # Example barcode and price
#     '987654321098': 25.50,
#     '9789995001025': 18,
#     '4977564000417': 25# Another example
#     # Add more barcode-price mappings as needed
# }
#
# def get_book_price(barcode_data):
#     """Lookup the price of a book based on barcode data."""
#     return barcode_price_map.get(barcode_data, 'Price not found')
#
# # Initialize the webcam
# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)
# cap.set(cv2.CAP_PROP_FPS, 30)
#
# cooldown_delay = 1.0  # 1 second
# last_detection_time = time.time() - cooldown_delay  # Initialize to ensure immediate detection
#
# scanned_items = []  # List to store scanned barcodes
# total_price = 0.0  # Variable to store the total price
#
# while True:
#     success, frame = cap.read()
#
#     if not success:
#         print("Failed to grab frame")
#         break
#
#     # Decode barcodes in the frame
#     decoded_objects = decode(frame)
#
#     current_time = time.time()
#
#     barcode_detected = False  # Flag to check if a barcode was detected
#
#     for obj in decoded_objects:
#         barcode_data = obj.data.decode('utf-8')
#         barcode_type = obj.type
#         price = get_book_price(barcode_data)
#
#         if price != 'Price not found':
#             if barcode_data not in scanned_items:
#                 scanned_items[barcode_data] = 1
#             else:
#                 scanned_items[barcode_data] += 1
#
#             total_price += price
#
#         # if price != 'Price not found':
#         #     if barcode_data not in scanned_items:
#         #         scanned_items.append(barcode_data)
#         #         total_price += price
#
#         if current_time - last_detection_time >= cooldown_delay:
#             # Print barcode type, data, and price
#             print(f"Barcode Type: {barcode_type}")
#             print(f"Barcode Data: {barcode_data}")
#             print(f"Price: ${price}")
#
#             # Draw the barcode data on the frame
#             cv2.putText(frame, f"{barcode_data} - ${price}",
#                         (obj.rect.left, obj.rect.top - 10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
#             cv2.rectangle(frame, (obj.rect.left, obj.rect.top),
#                           (obj.rect.left + obj.rect.width, obj.rect.top + obj.rect.height),
#                           (0, 255, 0), 2)
#
#             # Update the last detection time
#             last_detection_time = current_time
#             barcode_detected = True  # Set the flag to True if a barcode is detected
#
#     # Only update the last_detection_time if a barcode was detected
#     if barcode_detected:
#         last_detection_time = current_time
#
#     # Display the frame
#     cv2.imshow('Barcode Scanner', frame)
#
#     key = cv2.waitKey(10) & 0xFF
#
#     # # Break the loop if 'q' is pressed
#     # if cv2.waitKey(10) & 0xFF == ord('q'):
#     #     break
#
#     if key == ord('q'):
#         # Break the loop if 'q' is pressed
#         break
#
#     elif key == ord('p'):
#         # Print the total price and the scanned items if 'p' is pressed
#         print(f"Total Price: ${total_price:.2f}")
#         print("Scanned Items and Counts:")
#         for barcode, count in scanned_items.items():
#             print(f"Barcode Data: {barcode}, Count: {count}")
#
#     # elif key == ord('p'):
#     #     # Print the total price if 'p' is pressed
#     #     print(f"Total Price: ${total_price:.2f}")
#
# # Release the webcam and close windows
# cap.release()
# cv2.destroyAllWindows()


# import cv2
# from pyzbar.pyzbar import decode
# import time
# from playsound import playsound
#
# # Define a dictionary to map barcodes to their prices
# barcode_price_map = {
#     '123456789012': 17.00,  # Example barcode and price
#     '987654321098': 25.50,
#     '9789995001025': 18,
#     '4977564000417': 25  # Another example
#     # Add more barcode-price mappings as needed
# }
#
#
# def get_book_price(barcode_data):
#     """Lookup the price of a book based on barcode data."""
#     return barcode_price_map.get(barcode_data, 'Price not found')
#
#
# # Initialize the webcam
# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)
# cap.set(cv2.CAP_PROP_FPS, 30)
#
# cooldown_delay = 1.0  # 1 second
# barcode_last_seen = {}  # Dictionary to track last seen time for each barcode
# scanned_items = {}  # Dictionary to store scanned barcodes and their counts
# total_price = 0.0  # Variable to store the total price
#
# beep_sound = 'beep.wav'
#
# while True:
#     success, frame = cap.read()
#
#     if not success:
#         print("Failed to grab frame")
#         break
#
#     # Decode barcodes in the frame
#     decoded_objects = decode(frame)
#
#     current_time = time.time()
#
#     barcode_detected = False  # Flag to check if a barcode was detected
#
#     for obj in decoded_objects:
#         barcode_data = obj.data.decode('utf-8')
#         barcode_type = obj.type
#         price = get_book_price(barcode_data)
#
#         if price != 'Price not found':
#             # Check if this barcode was seen recently
#             if (barcode_data not in barcode_last_seen or
#                     current_time - barcode_last_seen[barcode_data] >= cooldown_delay):
#
#                 if barcode_data not in scanned_items:
#                     scanned_items[barcode_data] = 1
#                 else:
#                     scanned_items[barcode_data] += 1
#
#                 total_price += price
#
#                 # Update the last seen time for this barcode
#                 barcode_last_seen[barcode_data] = current_time
#
#                 barcode_detected = True
#
#         if barcode_detected:
#             # Print barcode type, data, and price
#             print(f"Barcode Type: {barcode_type}")
#             print(f"Barcode Data: {barcode_data}")
#             print(f"Price: ${price}")
#
#             # Draw the barcode data on the frame
#             cv2.putText(frame, f"{barcode_data} - ${price}",
#                         (obj.rect.left, obj.rect.top - 10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
#             cv2.rectangle(frame, (obj.rect.left, obj.rect.top),
#                           (obj.rect.left + obj.rect.width, obj.rect.top + obj.rect.height),
#                           (0, 255, 0), 2)
#
#     # Display the frame
#     cv2.imshow('Barcode Scanner', frame)
#
#     key = cv2.waitKey(10) & 0xFF
#
#     if key == ord('q'):
#         # Break the loop if 'q' is pressed
#         break
#     elif key == ord('p'):
#         # Print the total price and the scanned items if 'p' is pressed
#         print(f"Total Price: ${total_price:.2f}")
#         print("Scanned Items and Counts:")
#         for barcode, count in scanned_items.items():
#             price_per_item = get_book_price(barcode)
#             total_item_price = price_per_item * count if price_per_item != 'Price not found' else 0
#             print(f"Barcode Data: {barcode}, Count: {count}, Total Price for this item: ${total_item_price:.2f}")
#
# # Release the webcam and close windows
# cap.release()
# cv2.destroyAllWindows()




# import cv2
# from pyzbar.pyzbar import decode
# import time
# from playsound import playsound
#
# # Define a dictionary to map barcodes to their prices
# barcode_price_map = {
#     '123456789012': 17.00,  # Example barcode and price
#     '987654321098': 25.50,
#     '9789995001025': 18,
#     '4977564000417': 25  # Another example
#     # Add more barcode-price mappings as needed
# }
#
# def get_book_price(barcode_data):
#     """Lookup the price of a book based on barcode data."""
#     return barcode_price_map.get(barcode_data, 'Price not found')
#
# # Initialize the webcam
# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)
# cap.set(cv2.CAP_PROP_FPS, 30)
#
# cooldown_delay = 2.0  # 1 second
# barcode_last_seen = {}  # Dictionary to track last seen time for each barcode
# scanned_items = {}  # Dictionary to store scanned barcodes and their counts
# total_price = 0.0  # Variable to store the total price
#
# beep_sound = r'C:\Users\MSI-987\Downloads\cash_sound'  # Ensure this is the correct path to your sound file
#
# while True:
#     success, frame = cap.read()
#
#     if not success:
#         print("Failed to grab frame")
#         break
#
#     # Decode barcodes in the frame
#     decoded_objects = decode(frame)
#
#     current_time = time.time()
#     barcode_detected = False  # Flag to check if a barcode was detected
#
#     for obj in decoded_objects:
#         barcode_data = obj.data.decode('utf-8')
#         barcode_type = obj.type
#         price = get_book_price(barcode_data)
#
#         if price != 'Price not found':
#             # Check if this barcode was seen recently
#             if (barcode_data not in barcode_last_seen or
#                     current_time - barcode_last_seen[barcode_data] >= cooldown_delay):
#
#                 if barcode_data not in scanned_items:
#                     scanned_items[barcode_data] = 1
#                 else:
#                     scanned_items[barcode_data] += 1
#
#                 total_price += price
#
#                 # Update the last seen time for this barcode
#                 barcode_last_seen[barcode_data] = current_time
#
#                 barcode_detected = True
#
#                 # Play sound for a successful scan
#                 playsound(beep_sound)
#
#         if barcode_detected:
#             # Print barcode type, data, and price
#             print(f"Barcode Type: {barcode_type}")
#             print(f"Barcode Data: {barcode_data}")
#             print(f"Price: ${price}")
#
#             # Draw the barcode data on the frame
#             cv2.putText(frame, f"{barcode_data} - ${price}",
#                         (obj.rect.left, obj.rect.top - 10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
#             cv2.rectangle(frame, (obj.rect.left, obj.rect.top),
#                           (obj.rect.left + obj.rect.width, obj.rect.top + obj.rect.height),
#                           (0, 255, 0), 2)
#
#     # Display the frame
#     cv2.imshow('Barcode Scanner', frame)
#
#     key = cv2.waitKey(10) & 0xFF
#
#     if key == ord('q'):
#         # Break the loop if 'q' is pressed
#         break
#     elif key == ord('p'):
#         # Print the total price and the scanned items if 'p' is pressed
#         print(f"Total Price: ${total_price:.2f}")
#         print("Scanned Items and Counts:")
#         for barcode, count in scanned_items.items():
#             price_per_item = get_book_price(barcode)
#             total_item_price = price_per_item * count if price_per_item != 'Price not found' else 0
#             print(f"Barcode Data: {barcode}, Count: {count}, Total Price for this item: ${total_item_price:.2f}")
#
# # Release the webcam and close windows
# cap.release()
# cv2.destroyAllWindows()






# import cv2
# from pyzbar.pyzbar import decode
# import time
# from playsound import playsound
#
# # Define a dictionary to map barcodes to their prices
# barcode_price_map = {
#     '123456789012': 17.00,  # Example barcode and price
#     '987654321098': 25.50,
#     '9789995001025': 18.00,
#     '4977564000417': 25.00  # Another example
#     # Add more barcode-price mappings as needed
# }
#
# def get_book_price(barcode_data):
#     """Lookup the price of a book based on barcode data."""
#     return barcode_price_map.get(barcode_data, None)  # Return None if not found
#
# # Initialize the webcam
# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)
# cap.set(cv2.CAP_PROP_FPS, 30)
#
# cooldown_delay = 2.0  # 2 seconds
# barcode_last_seen = {}  # Dictionary to track last seen time for each barcode
# scanned_items = {}  # Dictionary to store scanned barcodes and their counts
# total_price = 0.0  # Variable to store the total price
#
# beep_sound = r'C:\Users\MSI-987\Downloads\cash_sound.wav'  # Ensure this is the correct path to your sound file
#
# while True:
#     success, frame = cap.read()
#
#     if not success:
#         print("Failed to grab frame")
#         break
#
#     # Decode barcodes in the frame
#     decoded_objects = decode(frame)
#
#     current_time = time.time()
#     barcode_detected = False  # Flag to check if a barcode was detected
#
#     for obj in decoded_objects:
#         barcode_data = obj.data.decode('utf-8')
#         barcode_type = obj.type
#         price = get_book_price(barcode_data)
#
#         if price is not None:
#             # Check if this barcode was seen recently
#             if (barcode_data not in barcode_last_seen or
#                     current_time - barcode_last_seen[barcode_data] >= cooldown_delay):
#
#                 if barcode_data not in scanned_items:
#                     scanned_items[barcode_data] = 1
#                 else:
#                     scanned_items[barcode_data] += 1
#
#                 total_price += price
#
#                 # Update the last seen time for this barcode
#                 barcode_last_seen[barcode_data] = current_time
#
#                 barcode_detected = True
#
#                 # Play sound for a successful scan
#                 playsound(beep_sound)
#
#         if barcode_detected:
#             # Print barcode type, data, and price
#             print(f"Barcode Type: {barcode_type}")
#             print(f"Barcode Data: {barcode_data}")
#             print(f"Price: ${price:.2f}")
#
#             # Draw the barcode data on the frame
#             cv2.putText(frame, f"{barcode_data} - ${price:.2f}",
#                         (obj.rect.left, obj.rect.top - 10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
#             cv2.rectangle(frame, (obj.rect.left, obj.rect.top),
#                           (obj.rect.left + obj.rect.width, obj.rect.top + obj.rect.height),
#                           (0, 255, 0), 2)
#
#     # Display the frame
#     cv2.imshow('Barcode Scanner', frame)
#
#     key = cv2.waitKey(10) & 0xFF
#
#     if key == ord('q'):
#         # Break the loop if 'q' is pressed
#         break
#     elif key == ord('p'):
#         # Print the total price and the scanned items if 'p' is pressed
#         print(f"Total Price: ${total_price:.2f}")
#         print("Scanned Items and Counts:")
#         for barcode, count in scanned_items.items():
#             price_per_item = get_book_price(barcode)
#             if price_per_item is not None:
#                 total_item_price = price_per_item * count
#                 print(f"Barcode Data: {barcode}, Count: {count}, Total Price for this item: ${total_item_price:.2f}")
#             else:
#                 print(f"Barcode Data: {barcode}, Count: {count}, Total Price for this item: Price not found")
#
# # Release the webcam and close windows
# cap.release()
# cv2.destroyAllWindows()





# import cv2
# from pyzbar.pyzbar import decode
# import time
# import pygame
# import sys
# import os
#
#
# # Define a dictionary to map barcodes to their prices
# barcode_price_map = {
#     '123456789012': 17.00,  # Example barcode and price
#     '987654321098': 25.50,
#     '9789995001025': 18.00,
#     '4977564000417': 25.00  # Another example
#     # Add more barcode-price mappings as needed
# }
#
# def get_book_price(barcode_data):
#     """Lookup the price of a book based on barcode data."""
#     return barcode_price_map.get(barcode_data, None)  # Return None if not found
#
# # Suppress pygame welcome message
# def suppress_pygame_welcome():
#     sys.stdout = open(os.devnull, 'w')
#
# def restore_stdout():
#     sys.stdout = sys.__stdout__
#
# # Suppress the pygame welcome message
# suppress_pygame_welcome()
# import pygame
# restore_stdout()
#
# # Initialize pygame for sound playback
# pygame.init()
# pygame.mixer.init()
# beep_sound = r'C:\Users\MSI-987\Downloads\cash_sound.wav'
#
# # Initialize the webcam
# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)
# cap.set(cv2.CAP_PROP_FPS, 30)
#
# cooldown_delay = 2.0  # 2 seconds
# barcode_last_seen = {}  # Dictionary to track last seen time for each barcode
# scanned_items = {}  # Dictionary to store scanned barcodes and their counts
# total_price = 0.0  # Variable to store the total price
#
# while True:
#     success, frame = cap.read()
#
#     if not success:
#         print("Failed to grab frame")
#         break
#
#     # Decode barcodes in the frame
#     decoded_objects = decode(frame)
#
#     current_time = time.time()
#     barcode_detected = False  # Flag to check if a barcode was detected
#
#     for obj in decoded_objects:
#         barcode_data = obj.data.decode('utf-8')
#         barcode_type = obj.type
#         price = get_book_price(barcode_data)
#
#         if price is not None:
#             # Check if this barcode was seen recently
#             if (barcode_data not in barcode_last_seen or
#                     current_time - barcode_last_seen[barcode_data] >= cooldown_delay):
#
#                 if barcode_data not in scanned_items:
#                     scanned_items[barcode_data] = 1
#                 else:
#                     scanned_items[barcode_data] += 1
#
#                 total_price += price
#
#                 # Update the last seen time for this barcode
#                 barcode_last_seen[barcode_data] = current_time
#
#                 barcode_detected = True
#
#                 # Play sound for a successful scan
#                 pygame.mixer.music.load(beep_sound)
#                 pygame.mixer.music.play()
#
#         if barcode_detected:
#             # Print barcode type, data, and price
#             print(f"Barcode Type: {barcode_type}")
#             print(f"Barcode Data: {barcode_data}")
#             print(f"Price: ${price:.2f}")
#
#             # Draw the barcode data on the frame
#             cv2.putText(frame, f"{barcode_data} - ${price:.2f}",
#                         (obj.rect.left, obj.rect.top - 10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
#             cv2.rectangle(frame, (obj.rect.left, obj.rect.top),
#                           (obj.rect.left + obj.rect.width, obj.rect.top + obj.rect.height),
#                           (0, 255, 0), 2)
#
#     # Display the frame
#     cv2.imshow('Barcode Scanner', frame)
#
#     key = cv2.waitKey(10) & 0xFF
#
#     if key == ord('q'):
#         # Break the loop if 'q' is pressed
#         break
#     elif key == ord('p'):
#         # Print the total price and the scanned items if 'p' is pressed
#         print(f"Total Price: ${total_price:.2f}")
#         print("Scanned Items and Counts:")
#         for barcode, count in scanned_items.items():
#             price_per_item = get_book_price(barcode)
#             if price_per_item is not None:
#                 total_item_price = price_per_item * count
#                 print(f"Barcode Data: {barcode}, Count: {count}, Total Price for this item: ${total_item_price:.2f}")
#             else:
#                 print(f"Barcode Data: {barcode}, Count: {count}, Total Price for this item: Price not found")
#
# # Release the webcam and close windows
# cap.release()
# cv2.destroyAllWindows()







# import cv2
# from pyzbar.pyzbar import decode
# import time
# import pygame
# import sys
# import os
#
# # Define a dictionary to map barcodes to their prices
# barcode_price_map = {
#     '123456789012': 17.00,  # Example barcode and price
#     '987654321098': 25.50,
#     '9789995001025': 18.00,
#     '4977564000417': 25.00  # Another example
#     # Add more barcode-price mappings as needed
# }
#
# def get_book_price(barcode_data):
#     """Lookup the price of a book based on barcode data."""
#     return barcode_price_map.get(barcode_data, None)  # Return None if not found
#
# # Suppress pygame welcome message
# def suppress_pygame_welcome():
#     sys.stdout = open(os.devnull, 'w')
#
# def restore_stdout():
#     sys.stdout = sys.__stdout__
#
# # Suppress the pygame welcome message
# suppress_pygame_welcome()
# import pygame
# restore_stdout()
#
# # Initialize pygame for sound playback
# pygame.init()
# pygame.mixer.init()
# beep_sound = r'C:\Users\MSI-987\Downloads\cash_sound.wav'
#
# # Initialize the webcam
# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)
# cap.set(cv2.CAP_PROP_FPS, 30)
#
# cooldown_delay = 2.0  # 2 seconds
# barcode_last_seen = {}  # Dictionary to track last seen time for each barcode
# scanned_items = {}  # Dictionary to store scanned barcodes and their counts
# total_price = 0.0  # Variable to store the total price
#
# while True:
#     success, frame = cap.read()
#
#     if not success:
#         print("Failed to grab frame")
#         break
#
#     # Decode barcodes in the frame
#     decoded_objects = decode(frame)
#
#     current_time = time.time()
#     barcode_detected = False  # Flag to check if a barcode was detected
#
#     for obj in decoded_objects:
#         barcode_data = obj.data.decode('utf-8')
#         barcode_type = obj.type
#         price = get_book_price(barcode_data)
#
#         if price is not None:
#             # Check if this barcode was seen recently
#             if (barcode_data not in barcode_last_seen or
#                     current_time - barcode_last_seen[barcode_data] >= cooldown_delay):
#
#                 if barcode_data not in scanned_items:
#                     scanned_items[barcode_data] = 1
#                 else:
#                     scanned_items[barcode_data] += 1
#
#                 total_price += price
#
#                 # Update the last seen time for this barcode
#                 barcode_last_seen[barcode_data] = current_time
#
#                 barcode_detected = True
#
#                 # Play sound for a successful scan
#                 pygame.mixer.music.load(beep_sound)
#                 pygame.mixer.music.play()
#
#         if barcode_detected:
#             # Print barcode type, data, and price
#             print(f"Barcode Type: {barcode_type}")
#             print(f"Barcode Data: {barcode_data}")
#             print(f"Price: ${price:.2f}")
#
#             # Draw the barcode data on the frame
#             cv2.putText(frame, f"{barcode_data} - ${price:.2f}",
#                         (obj.rect.left, obj.rect.top - 10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
#             cv2.rectangle(frame, (obj.rect.left, obj.rect.top),
#                           (obj.rect.left + obj.rect.width, obj.rect.top + obj.rect.height),
#                           (0, 255, 0), 2)
#
#     # Display the frame
#     cv2.imshow('Barcode Scanner', frame)
#
#     key = cv2.waitKey(10) & 0xFF
#
#     if key == ord('q'):
#         # Break the loop if 'q' is pressed
#         break
#     elif key == ord('p'):
#         # Print the total price and the scanned items if 'p' is pressed
#         print(f"Total Price: ${total_price:.2f}")
#         print("Scanned Items and Counts:")
#         for barcode, count in scanned_items.items():
#             price_per_item = get_book_price(barcode)
#             if price_per_item is not None:
#                 total_item_price = price_per_item * count
#                 print(f"Barcode Data: {barcode}, Count: {count}, Total Price for this item: ${total_item_price:.2f}")
#             else:
#                 print(f"Barcode Data: {barcode}, Count: {count}, Total Price for this item: Price not found")
#
# # Release the webcam and close windows
# cap.release()
# cv2.destroyAllWindows()







# import cv2
# from pyzbar.pyzbar import decode
# import time
# import pygame
# import sys
# import os
#
# # Define a dictionary to map barcodes to their prices
# barcode_price_map = {
#     '123456789012': 17.00,
#     '987654321098': 25.50,
#     '9789995001025': 18.00,
#     '4977564000417': 25.00
# }
#
# def get_book_price(barcode_data):
#     """Lookup the price of a book based on barcode data."""
#     return barcode_price_map.get(barcode_data)
#
# # Suppress pygame welcome message
# def suppress_pygame_welcome():
#     sys.stdout = open(os.devnull, 'w')
#
# def restore_stdout():
#     sys.stdout = sys.__stdout__
#
# suppress_pygame_welcome()
# import pygame
# restore_stdout()
#
# # Initialize pygame for sound playback
# pygame.init()
# pygame.mixer.init()
# beep_sound = pygame.mixer.Sound(r'C:\Users\MSI-987\Downloads\cash_sound.wav')  # Load the sound once
#
# # Initialize the webcam
# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# cap.set(cv2.CAP_PROP_FPS, 30)
#
# cooldown_delay = 2.0  # 2 seconds
# barcode_last_seen = {}  # Dictionary to track last seen time for each barcode
# scanned_items = {}  # Dictionary to store scanned barcodes and their counts
# total_price = 0.0  # Variable to store the total price
#
# while True:
#     success, frame = cap.read()
#
#     if not success:
#         print("Failed to grab frame")
#         break
#
#     # Decode barcodes in the frame
#     decoded_objects = decode(frame)
#
#     current_time = time.time()
#     barcode_detected = False  # Flag to check if a barcode was detected
#
#     for obj in decoded_objects:
#         barcode_data = obj.data.decode('utf-8')
#         barcode_type = obj.type
#         price = get_book_price(barcode_data)
#
#         if price is not None:
#             # Check if this barcode was seen recently
#             if (barcode_data not in barcode_last_seen or
#                     current_time - barcode_last_seen[barcode_data] >= cooldown_delay):
#
#                 if barcode_data not in scanned_items:
#                     scanned_items[barcode_data] = 1
#                 else:
#                     scanned_items[barcode_data] += 1
#
#                 total_price += price
#
#                 # Update the last seen time for this barcode
#                 barcode_last_seen[barcode_data] = current_time
#
#                 barcode_detected = True
#
#                 # Play sound for a successful scan
#                 beep_sound.play()
#
#         if barcode_detected:
#             # Print barcode type, data, and price
#             print(f"Barcode Type: {barcode_type}")
#             print(f"Barcode Data: {barcode_data}")
#             print(f"Price: ${price:.2f}")
#
#             # Draw the barcode data on the frame
#             cv2.putText(frame, f"{barcode_data} - {price: KHR}",
#                         (obj.rect.left, obj.rect.top - 10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
#             cv2.rectangle(frame, (obj.rect.left, obj.rect.top),
#                           (obj.rect.left + obj.rect.width, obj.rect.top + obj.rect.height),
#                           (0, 255, 0), 2)
#
#     # Display the frame
#     cv2.imshow('Barcode Scanner', frame)
#
#     key = cv2.waitKey(10) & 0xFF
#
#     if key == ord('q'):
#         # Break the loop if 'q' is pressed
#         break
#     elif key == ord('p'):
#         # Print the total price and the scanned items if 'p' is pressed
#         print(f"Total Price: {total_price: KHR}")
#         print("Scanned Items and Counts:")
#         for barcode, count in scanned_items.items():
#             price_per_item = get_book_price(barcode)
#             if price_per_item is not None:
#                 total_item_price = price_per_item * count
#                 print(f"Barcode Data: {barcode}, Count: {count}, Total Price for this item: {total_item_price: KHR}")
#             else:
#                 print(f"Barcode Data: {barcode}, Count: {count}, Total Price for this item: Price not found")
#
# # Release the webcam and close windows
# cap.release()
# cv2.destroyAllWindows()



# import cv2
# from pyzbar.pyzbar import decode
# import time
# import pygame
# import sys
# import os
#
# # Define a dictionary to map barcodes to their prices in Khmer Riel
# barcode_price_map = {
#     '123456789012': 68000,  # Example barcode and price in KHR
#     '987654321098': 102000,
#     '9789995001025': 72000,
#     '4977564000417': 100000  # Another example
# }
#
# def get_book_price(barcode_data):
#     """Lookup the price of a book based on barcode data."""
#     return barcode_price_map.get(barcode_data)
#
# # Suppress pygame welcome message
# def suppress_pygame_welcome():
#     sys.stdout = open(os.devnull, 'w')
#
# def restore_stdout():
#     sys.stdout = sys.__stdout__
#
# suppress_pygame_welcome()
# import pygame
# restore_stdout()
#
# # Initialize pygame for sound playback
# pygame.init()
# pygame.mixer.init()
# beep_sound = pygame.mixer.Sound(r'C:\Users\MSI-987\Downloads\cash_sound.wav')  # Load the sound once
#
# # Initialize the webcam
# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# cap.set(cv2.CAP_PROP_FPS, 30)
#
# cooldown_delay = 2.0  # 2 seconds
# barcode_last_seen = {}  # Dictionary to track last seen time for each barcode
# scanned_items = {}  # Dictionary to store scanned barcodes and their counts
# total_price = 0.0  # Variable to store the total price in Khmer Riel
#
# while True:
#     success, frame = cap.read()
#
#     if not success:
#         print("Failed to grab frame")
#         break
#
#     # Decode barcodes in the frame
#     decoded_objects = decode(frame)
#
#     current_time = time.time()
#     barcode_detected = False  # Flag to check if a barcode was detected
#
#     for obj in decoded_objects:
#         barcode_data = obj.data.decode('utf-8')
#         barcode_type = obj.type
#         price = get_book_price(barcode_data)
#
#         if price is not None:
#             # Check if this barcode was seen recently
#             if (barcode_data not in barcode_last_seen or
#                     current_time - barcode_last_seen[barcode_data] >= cooldown_delay):
#
#                 if barcode_data not in scanned_items:
#                     scanned_items[barcode_data] = 1
#                 else:
#                     scanned_items[barcode_data] += 1
#
#                 total_price += price
#
#                 # Update the last seen time for this barcode
#                 barcode_last_seen[barcode_data] = current_time
#
#                 barcode_detected = True
#
#                 # Play sound for a successful scan
#                 beep_sound.play()
#
#         if barcode_detected:
#             # Print barcode type, data, and price
#             print(f"Barcode Type: {barcode_type}")
#             print(f"Barcode Data: {barcode_data}")
#             print(f"Price: {price} KHR")  # Display price in KHR
#
#             # Draw the barcode data on the frame
#             cv2.putText(frame, f"{barcode_data} - {price} KHR",
#                         (obj.rect.left, obj.rect.top - 10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
#             cv2.rectangle(frame, (obj.rect.left, obj.rect.top),
#                           (obj.rect.left + obj.rect.width, obj.rect.top + obj.rect.height),
#                           (0, 255, 0), 2)
#
#     # Display the frame
#     cv2.imshow('Barcode Scanner', frame)
#
#     key = cv2.waitKey(10) & 0xFF
#
#     if key == ord('q'):
#         # Break the loop if 'q' is pressed
#         break
#     elif key == ord('p'):
#         # Print the total price and the scanned items if 'p' is pressed
#         print(f"Total Price: {total_price} KHR")  # Display total price in KHR
#         print("Scanned Items and Counts:")
#         for barcode, count in scanned_items.items():
#             price_per_item = get_book_price(barcode)
#             if price_per_item is not None:
#                 total_item_price = price_per_item * count
#                 print(f"Barcode Data: {barcode}, Count: {count}, Total Price for this item: {total_item_price} KHR")
#             else:
#                 print(f"Barcode Data: {barcode}, Count: {count}, Total Price for this item: Price not found")
#
# # Release the webcam and close windows
# cap.release()
# cv2.destroyAllWindows()







#




# import cv2
# from pyzbar.pyzbar import decode
# import time
# import pygame
# import sys
# import os
# import json
#
# # File to store barcode prices
# PRICE_FILE = 'barcode_prices.json'
#
# # Load barcode prices from a JSON file
# def load_prices():
#     if os.path.exists(PRICE_FILE):
#         with open(PRICE_FILE, 'r') as file:
#             return json.load(file)
#     return {
#         '123456789012': 68000,  # Example barcode and price in KHR
#         '987654321098': 102000,
#         '9789995001025': 72000,
#         '4977564000417': 100000  # Another example
#     }
#
# # Save barcode prices to a JSON file
# def save_prices(prices):
#     with open(PRICE_FILE, 'w') as file:
#         json.dump(prices, file, indent=4)
#
# # Define a dictionary to map barcodes to their prices
# barcode_price_map = load_prices()
#
# def get_book_price(barcode_data):
#     """Lookup the price of a book based on barcode data."""
#     return barcode_price_map.get(barcode_data)
#
# def update_book_price(barcode_data, new_price):
#     """Update the price of a book based on barcode data and save the change."""
#     barcode_price_map[barcode_data] = new_price
#     save_prices(barcode_price_map)
#     print(f"Price for barcode {barcode_data} updated to {new_price} KHR")
#
# def add_new_barcode(barcode_data):
#     """Prompt the user to add a new barcode and its price."""
#     try:
#         new_price = float(input(f"Barcode {barcode_data} not found. Enter the price in KHR: "))
#         barcode_price_map[barcode_data] = new_price
#         save_prices(barcode_price_map)
#         print(f"New barcode {barcode_data} added with price {new_price} KHR")
#         return True  # Indicate that the barcode was newly added
#     except ValueError:
#         print("Invalid price input. Please enter a valid number.")
#         return False  # Indicate that the barcode was not successfully added
#
# # Suppress pygame welcome message
# def suppress_pygame_welcome():
#     sys.stdout = open(os.devnull, 'w')
#
# def restore_stdout():
#     sys.stdout = sys.__stdout__
#
# suppress_pygame_welcome()
# import pygame
# restore_stdout()
#
# # Initialize pygame for sound playback
# pygame.init()
# pygame.mixer.init()
# try:
#     beep_sound = pygame.mixer.Sound(r'C:\Users\MSI-987\Downloads\cash_sound.wav')  # Load the sound once
# except pygame.error as e:
#     print(f"Error loading sound file: {e}")
#     sys.exit(1)
#
# # Initialize the webcam
# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# cap.set(cv2.CAP_PROP_FPS, 30)
#
# cooldown_delay = 2.0  # 2 seconds
# barcode_last_seen = {}  # Dictionary to track last seen time for each barcode
# scanned_items = {}  # Dictionary to store scanned barcodes and their counts
# total_price = 0.0  # Variable to store the total price in Khmer Riel
#
# try:
#     while True:
#         success, frame = cap.read()
#
#         if not success:
#             print("Failed to grab frame")
#             break
#
#         # Decode barcodes in the frame
#         decoded_objects = decode(frame)
#
#         current_time = time.time()
#         barcode_detected = False  # Flag to check if a barcode was detected
#
#         for obj in decoded_objects:
#             barcode_data = obj.data.decode('utf-8')
#             barcode_type = obj.type
#             price = get_book_price(barcode_data)
#
#             if price is not None:
#                 # Check if this barcode was seen recently
#                 if (barcode_data not in barcode_last_seen or
#                         current_time - barcode_last_seen[barcode_data] >= cooldown_delay):
#
#                     if barcode_data not in scanned_items:
#                         scanned_items[barcode_data] = 1
#                     else:
#                         scanned_items[barcode_data] += 1
#
#                     total_price += price
#
#                     # Update the last seen time for this barcode
#                     barcode_last_seen[barcode_data] = current_time
#
#                     barcode_detected = True
#
#                     # Play sound for a successful scan
#                     beep_sound.play()
#
#             else:
#                 # Handle unknown barcode
#                 if barcode_data not in barcode_last_seen:
#                     # Prompt user to add new barcode if not seen before
#                     if add_new_barcode(barcode_data):
#                         price = get_book_price(barcode_data)  # Retrieve the price after adding
#                         barcode_detected = True
#                         # Reset last seen time to avoid immediate re-prompt
#                         barcode_last_seen[barcode_data] = current_time
#
#             if barcode_detected:
#                 # Print barcode type, data, and price
#                 print(f"Barcode Type: {barcode_type}")
#                 print(f"Barcode Data: {barcode_data}")
#                 print(f"Price: {price if price is not None else 'Not Found'} KHR")
#
#                 # Draw the barcode data on the frame
#                 cv2.putText(frame, f"{barcode_data} - {price if price is not None else 'Not Found'} KHR",
#                             (obj.rect.left, obj.rect.top - 10),
#                             cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
#                 cv2.rectangle(frame, (obj.rect.left, obj.rect.top),
#                               (obj.rect.left + obj.rect.width, obj.rect.top + obj.rect.height),
#                               (0, 255, 0), 2)
#
#         # Display the frame
#         cv2.imshow('Barcode Scanner', frame)
#
#         key = cv2.waitKey(10) & 0xFF
#
#         if key == ord('q'):
#             # Break the loop if 'q' is pressed
#             break
#         elif key == ord('p'):
#             # Print the total price and the scanned items if 'p' is pressed
#             print(f"Total Price: {total_price} KHR")
#             print("Scanned Items and Counts:")
#             for barcode, count in scanned_items.items():
#                 price_per_item = get_book_price(barcode)
#                 if price_per_item is not None:
#                     total_item_price = price_per_item * count
#                     print(f"Barcode Data: {barcode}, Count: {count}, Total Price for this item: {total_item_price} KHR")
#                 else:
#                     print(f"Barcode Data: {barcode}, Count: {count}, Total Price for this item: Price not found")
#         elif key == ord('u'):
#             # Update the price of a barcode if 'u' is pressed
#             barcode_data = input("Enter the barcode to update: ")
#             try:
#                 new_price = float(input("Enter the new price in KHR: "))
#                 update_book_price(barcode_data, new_price)
#             except ValueError:
#                 print("Invalid price input. Please enter a valid number.")
# finally:
#     # Release the webcam and close windows
#     cap.release()
#     cv2.destroyAllWindows()





# import cv2
# from pyzbar.pyzbar import decode
# import time
# import pygame
# import sys
# import os
# import json
#
# # File to store barcode prices and names
# PRICE_FILE = 'barcode_data.json'
#
# # Load barcode data from a JSON file
# def load_data():
#     if os.path.exists(PRICE_FILE):
#         with open(PRICE_FILE, 'r') as file:
#             return json.load(file)
#     return {}
#
# # Save barcode data to a JSON file
# def save_data(data):
#     with open(PRICE_FILE, 'w') as file:
#         json.dump(data, file, indent=4)
#
# # Define a dictionary to map barcodes to their prices and names
# barcode_data_map = load_data()
#
# def get_book_info(barcode_data):
#     """Lookup the price and name of a book based on barcode data."""
#     return barcode_data_map.get(barcode_data, {"price": None, "name": None})
#
# def update_book_info(barcode_data, price, name):
#     """Update the price and name of a book based on barcode data and save the change."""
#     barcode_data_map[barcode_data] = {"price": price, "name": name}
#     save_data(barcode_data_map)
#     print(f"Updated barcode {barcode_data} with price {price} KHR and name '{name}'")
#
# def add_new_barcode(barcode_data):
#     """Prompt the user to add a new barcode, its price, and name."""
#     try:
#         new_price = float(input(f"Barcode {barcode_data} not found. Enter the price in KHR: "))
#         new_name = input("Enter the name of the item: ")
#         update_book_info(barcode_data, new_price, new_name)
#         print(f"New barcode {barcode_data} added with price {new_price} KHR and name '{new_name}'")
#         return True  # Indicate that the barcode was newly added
#     except ValueError:
#         print("Invalid price input. Please enter a valid number.")
#         return False  # Indicate that the barcode was not successfully added
#
# # Suppress pygame welcome message
# def suppress_pygame_welcome():
#     sys.stdout = open(os.devnull, 'w')
#
# def restore_stdout():
#     sys.stdout = sys.__stdout__
#
# suppress_pygame_welcome()
# import pygame
# restore_stdout()
#
# # Initialize pygame for sound playback
# pygame.init()
# pygame.mixer.init()
# try:
#     beep_sound = pygame.mixer.Sound(r'C:\Users\MSI-987\Downloads\cash_sound.wav')  # Load the sound once
# except pygame.error as e:
#     print(f"Error loading sound file: {e}")
#     sys.exit(1)
#
# # Initialize the webcam
# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# cap.set(cv2.CAP_PROP_FPS, 30)
#
# cooldown_delay = 2.0  # 2 seconds
# barcode_last_seen = {}  # Dictionary to track last seen time for each barcode
# scanned_items = {}  # Dictionary to store scanned barcodes and their counts
# total_price = 0.0  # Variable to store the total price in Khmer Riel
#
# try:
#     while True:
#         success, frame = cap.read()
#
#         if not success:
#             print("Failed to grab frame")
#             break
#
#         # Decode barcodes in the frame
#         decoded_objects = decode(frame)
#
#         current_time = time.time()
#         barcode_detected = False  # Flag to check if a barcode was detected
#
#         for obj in decoded_objects:
#             barcode_data = obj.data.decode('utf-8')
#             barcode_type = obj.type
#             book_info = get_book_info(barcode_data)
#             price = book_info["price"]
#             name = book_info["name"]
#
#             if price is not None:
#                 # Check if this barcode was seen recently
#                 if (barcode_data not in barcode_last_seen or
#                         current_time - barcode_last_seen[barcode_data] >= cooldown_delay):
#
#                     if barcode_data not in scanned_items:
#                         scanned_items[barcode_data] = 1
#                     else:
#                         scanned_items[barcode_data] += 1
#
#                     total_price += price
#
#                     # Update the last seen time for this barcode
#                     barcode_last_seen[barcode_data] = current_time
#
#                     barcode_detected = True
#
#                     # Play sound for a successful scan
#                     beep_sound.play()
#
#             else:
#                 # Handle unknown barcode
#                 if barcode_data not in barcode_last_seen:
#                     # Prompt user to add new barcode if not seen before
#                     if add_new_barcode(barcode_data):
#                         book_info = get_book_info(barcode_data)  # Retrieve updated info
#                         price = book_info["price"]
#                         name = book_info["name"]
#                         barcode_detected = True
#                         # Reset last seen time to avoid immediate re-prompt
#                         barcode_last_seen[barcode_data] = current_time
#
#             if barcode_detected:
#                 # Print barcode type, data, price, and name
#                 print(f"Barcode Type: {barcode_type}")
#                 print(f"Barcode Data: {barcode_data}")
#                 print(f"Name: {name if name else 'Not Named'}")
#                 print(f"Price: {price if price is not None else 'Not Found'} KHR")
#
#                 # Draw the barcode data on the frame
#                 cv2.putText(frame, f"{barcode_data} - {name if name else 'Not Named'} - {price if price is not None else 'Not Found'} KHR",
#                             (obj.rect.left, obj.rect.top - 10),
#                             cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
#                 cv2.rectangle(frame, (obj.rect.left, obj.rect.top),
#                               (obj.rect.left + obj.rect.width, obj.rect.top + obj.rect.height),
#                               (0, 255, 0), 2)
#
#         # Display the frame
#         cv2.imshow('Barcode Scanner', frame)
#
#         key = cv2.waitKey(10) & 0xFF
#
#         if key == ord('q'):
#             # Break the loop if 'q' is pressed
#             break
#         elif key == ord('p'):
#             # Print the total price and the scanned items if 'p' is pressed
#             print(f"Total Price: {total_price} KHR")
#             print("Scanned Items and Counts:")
#             for barcode, count in scanned_items.items():
#                 book_info = get_book_info(barcode)
#                 price_per_item = book_info["price"]
#                 name = book_info["name"]
#                 if price_per_item is not None:
#                     total_item_price = price_per_item * count
#                     print(f"Barcode Data: {barcode}, Name: {name}, Count: {count}, Total Price for this item: {total_item_price} KHR")
#                 else:
#                     print(f"Barcode Data: {barcode}, Name: {name}, Count: {count}, Total Price for this item: Price not found")
#         elif key == ord('u'):
#             # Update the price and name of a barcode if 'u' is pressed
#             barcode_data = input("Enter the barcode to update: ")
#             try:
#                 new_price = float(input("Enter the new price in KHR: "))
#                 new_name = input("Enter the new name of the item: ")
#                 update_book_info(barcode_data, new_price, new_name)
#             except ValueError:
#                 print("Invalid price input. Please enter a valid number.")
# finally:
#     # Release the webcam and close windows
#     cap.release()
#     cv2.destroyAllWindows()







# import cv2
# from pyzbar.pyzbar import decode
# import time
# import pygame
# import sys
# import os
# import json
#
# # File to store barcode prices and names
# PRICE_FILE = 'barcode_data.json'
#
# # Conversion rate from KHR to USD
# KHR_TO_USD_CONVERSION_RATE = 4100.0  # 1 USD = 4,100 KHR (example rate)
#
# # Load barcode data from a JSON file
# def load_data():
#     if os.path.exists(PRICE_FILE):
#         with open(PRICE_FILE, 'r') as file:
#             return json.load(file)
#     return {}
#
# # Save barcode data to a JSON file
# def save_data(data):
#     with open(PRICE_FILE, 'w') as file:
#         json.dump(data, file, indent=4)
#
# # Define a dictionary to map barcodes to their prices and names
# barcode_data_map = load_data()
#
# def get_book_info(barcode_data):
#     """Lookup the price and name of a book based on barcode data."""
#     return barcode_data_map.get(barcode_data, {"price": None, "name": None})
#
# def update_book_info(barcode_data, price, name):
#     """Update the price and name of a book based on barcode data and save the change."""
#     barcode_data_map[barcode_data] = {"price": price, "name": name}
#     save_data(barcode_data_map)
#     print(f"Updated barcode {barcode_data} with price {price} KHR and name '{name}'")
#
# def add_new_barcode(barcode_data):
#     """Prompt the user to add a new barcode, its price, and name."""
#     try:
#         new_price = float(input(f"Barcode {barcode_data} not found. Enter the price in KHR: "))
#         new_name = input("Enter the name of the item: ")
#         update_book_info(barcode_data, new_price, new_name)
#         print(f"New barcode {barcode_data} added with price {new_price} KHR and name '{new_name}'")
#         return True  # Indicate that the barcode was newly added
#     except ValueError:
#         print("Invalid price input. Please enter a valid number.")
#         return False  # Indicate that the barcode was not successfully added
#
# # Suppress pygame welcome message
# def suppress_pygame_welcome():
#     sys.stdout = open(os.devnull, 'w')
#
# def restore_stdout():
#     sys.stdout = sys.__stdout__
#
# suppress_pygame_welcome()
# import pygame
# restore_stdout()
#
# # Initialize pygame for sound playback
# pygame.init()
# pygame.mixer.init()
# try:
#     beep_sound = pygame.mixer.Sound(r'C:\Users\MSI-987\Downloads\cash_sound.wav')  # Load the sound once
# except pygame.error as e:
#     print(f"Error loading sound file: {e}")
#     sys.exit(1)
#
# # Initialize the webcam
# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# cap.set(cv2.CAP_PROP_FPS, 30)
#
# cooldown_delay = 2.0  # 2 seconds
# barcode_last_seen = {}  # Dictionary to track last seen time for each barcode
# scanned_items = {}  # Dictionary to store scanned barcodes and their counts
# total_price = 0.0  # Variable to store the total price in Khmer Riel
#
# try:
#     while True:
#         success, frame = cap.read()
#
#         if not success:
#             print("Failed to grab frame")
#             break
#
#         # Decode barcodes in the frame
#         decoded_objects = decode(frame)
#
#         current_time = time.time()
#         barcode_detected = False  # Flag to check if a barcode was detected
#
#         for obj in decoded_objects:
#             barcode_data = obj.data.decode('utf-8')
#             barcode_type = obj.type
#             book_info = get_book_info(barcode_data)
#             price = book_info["price"]
#             name = book_info["name"]
#
#             if price is not None:
#                 # Check if this barcode was seen recently
#                 if (barcode_data not in barcode_last_seen or
#                         current_time - barcode_last_seen[barcode_data] >= cooldown_delay):
#
#                     if barcode_data not in scanned_items:
#                         scanned_items[barcode_data] = 1
#                     else:
#                         scanned_items[barcode_data] += 1
#
#                     total_price += price
#
#                     # Update the last seen time for this barcode
#                     barcode_last_seen[barcode_data] = current_time
#
#                     barcode_detected = True
#
#                     # Play sound for a successful scan
#                     beep_sound.play()
#
#             else:
#                 # Handle unknown barcode
#                 if barcode_data not in barcode_last_seen:
#                     # Prompt user to add new barcode if not seen before
#                     if add_new_barcode(barcode_data):
#                         book_info = get_book_info(barcode_data)  # Retrieve updated info
#                         price = book_info["price"]
#                         name = book_info["name"]
#                         barcode_detected = True
#                         # Reset last seen time to avoid immediate re-prompt
#                         barcode_last_seen[barcode_data] = current_time
#
#             if barcode_detected:
#                 # Print barcode type, data, price, and name
#                 print(f"Barcode Type: {barcode_type}")
#                 print(f"Barcode Data: {barcode_data}")
#                 print(f"Name: {name if name else 'Not Named'}")
#                 print(f"Price: {price if price is not None else 'Not Found'} KHR")
#
#                 # Draw the barcode data on the frame
#                 cv2.putText(frame, f"{barcode_data} - {name if name else 'Not Named'} - {price if price is not None else 'Not Found'} KHR",
#                             (obj.rect.left, obj.rect.top - 10),
#                             cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
#                 cv2.rectangle(frame, (obj.rect.left, obj.rect.top),
#                               (obj.rect.left + obj.rect.width, obj.rect.top + obj.rect.height),
#                               (0, 255, 0), 2)
#
#         # Display the frame
#         cv2.imshow('Barcode Scanner', frame)
#
#         key = cv2.waitKey(10) & 0xFF
#
#         if key == ord('q'):
#             # Break the loop if 'q' is pressed
#             break
#         elif key == ord('p'):
#             # Print the total price and the scanned items if 'p' is pressed
#             total_price_usd = total_price / KHR_TO_USD_CONVERSION_RATE
#             print(f"Total Price: {total_price} KHR (${total_price_usd:.2f} USD)")
#             print("Scanned Items and Counts:")
#             for barcode, count in scanned_items.items():
#                 book_info = get_book_info(barcode)
#                 price_per_item = book_info["price"]
#                 name = book_info["name"]
#                 if price_per_item is not None:
#                     total_item_price = price_per_item * count
#                     total_item_price_usd = total_item_price / KHR_TO_USD_CONVERSION_RATE
#                     print(f"Barcode Data: {barcode}, Name: {name}, Count: {count}, Total Price for this item: {total_item_price} KHR (${total_item_price_usd:.2f} USD)")
#                 else:
#                     print(f"Barcode Data: {barcode}, Name: {name}, Count: {count}, Total Price for this item: Price not found")
#         elif key == ord('u'):
#             # Update the price and name of a barcode if 'u' is pressed
#             barcode_data = input("Enter the barcode to update: ")
#             try:
#                 new_price = float(input("Enter the new price in KHR: "))
#                 new_name = input("Enter the new name of the item: ")
#                 update_book_info(barcode_data, new_price, new_name)
#             except ValueError:
#                 print("Invalid price input. Please enter a valid number.")
# finally:
#     # Release the webcam and close windows
#     cap.release()
#     cv2.destroyAllWindows()




import cv2
from pyzbar.pyzbar import decode
import time
import pygame
import sys
import os
import json

# File to store barcode prices and names
PRICE_FILE = 'barcode_data.json'

# Conversion rate from KHR to USD
KHR_TO_USD_CONVERSION_RATE = 4100.0  # 1 USD = 4,100 KHR (example rate)


# Load barcode data from a JSON file
def load_data():
    if os.path.exists(PRICE_FILE):
        with open(PRICE_FILE, 'r') as file:
            return json.load(file)
    return {}


# Save barcode data to a JSON file
def save_data(data):
    with open(PRICE_FILE, 'w') as file:
        json.dump(data, file, indent=4)


# Define a dictionary to map barcodes to their prices and names
barcode_data_map = load_data()


def get_book_info(barcode_data):
    """Lookup the price and name of a book based on barcode data."""
    return barcode_data_map.get(barcode_data, {"price": None, "name": None})


def update_book_info(barcode_data, price, name):
    """Update the price and name of a book based on barcode data and save the change."""
    barcode_data_map[barcode_data] = {"price": price, "name": name}
    save_data(barcode_data_map)
    print(f"Updated barcode {barcode_data} with price {price} KHR and name '{name}'")


def add_new_barcode(barcode_data):
    """Prompt the user to add a new barcode, its price, and name."""
    try:
        new_price = float(input(f"Barcode {barcode_data} not found. Enter the price in KHR: "))
        new_name = input("Enter the name of the item: ")
        update_book_info(barcode_data, new_price, new_name)
        print(f"New barcode {barcode_data} added with price {new_price} KHR and name '{new_name}'")
        return True  # Indicate that the barcode was newly added
    except ValueError:
        print("Invalid price input. Please enter a valid number.")
        return False  # Indicate that the barcode was not successfully added


# Suppress pygame welcome message
def suppress_pygame_welcome():
    sys.stdout = open(os.devnull, 'w')


def restore_stdout():
    sys.stdout = sys.__stdout__


suppress_pygame_welcome()
import pygame

restore_stdout()

# Initialize pygame for sound playback
pygame.init()
pygame.mixer.init()
try:
    beep_sound = pygame.mixer.Sound(r'C:\Users\MSI-987\Downloads\cash_sound.wav')  # Load the sound once
except pygame.error as e:
    print(f"Error loading sound file: {e}")
    sys.exit(1)

# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

cooldown_delay = 2.0  # 2 seconds
barcode_last_seen = {}  # Dictionary to track last seen time for each barcode
scanned_items = {}  # Dictionary to store scanned barcodes and their counts
total_price = 0.0  # Variable to store the total price in Khmer Riel


def change_item_price():
    """Allow the user to change the price of an item by barcode."""
    barcode_data = input("Enter the barcode of the item to change the price: ")
    book_info = get_book_info(barcode_data)

    if book_info["price"] is not None:
        try:
            new_price = float(input(f"Current price is {book_info['price']} KHR. Enter the new price in KHR: "))
            new_name = input(f"Enter the new name of the item (or press Enter to keep '{book_info['name']}'): ") or \
                       book_info['name']
            update_book_info(barcode_data, new_price, new_name)
            print(f"Price updated for barcode {barcode_data}. New price: {new_price} KHR, New name: '{new_name}'")
        except ValueError:
            print("Invalid price input. Please enter a valid number.")
    else:
        print("Barcode not found in the database.")


try:
    while True:
        success, frame = cap.read()

        if not success:
            print("Failed to grab frame")
            break

        # Decode barcodes in the frame
        decoded_objects = decode(frame)

        current_time = time.time()
        barcode_detected = False  # Flag to check if a barcode was detected

        for obj in decoded_objects:
            barcode_data = obj.data.decode('utf-8')
            barcode_type = obj.type
            book_info = get_book_info(barcode_data)
            price = book_info["price"]
            name = book_info["name"]

            if price is not None:
                # Check if this barcode was seen recently
                if (barcode_data not in barcode_last_seen or
                        current_time - barcode_last_seen[barcode_data] >= cooldown_delay):

                    if barcode_data not in scanned_items:
                        scanned_items[barcode_data] = 1
                    else:
                        scanned_items[barcode_data] += 1

                    total_price += price

                    # Update the last seen time for this barcode
                    barcode_last_seen[barcode_data] = current_time

                    barcode_detected = True

                    # Play sound for a successful scan
                    beep_sound.play()

            else:
                # Handle unknown barcode
                if barcode_data not in barcode_last_seen:
                    # Prompt user to add new barcode if not seen before
                    if add_new_barcode(barcode_data):
                        book_info = get_book_info(barcode_data)  # Retrieve updated info
                        price = book_info["price"]
                        name = book_info["name"]
                        barcode_detected = True
                        # Reset last seen time to avoid immediate re-prompt
                        barcode_last_seen[barcode_data] = current_time

            if barcode_detected:
                # Print barcode type, data, price, and name
                print(f"Barcode Type: {barcode_type}")
                print(f"Barcode Data: {barcode_data}")
                print(f"Name: {name if name else 'Not Named'}")
                print(f"Price: {price if price is not None else 'Not Found'} KHR")

                # Draw the barcode data on the frame
                cv2.putText(frame,
                            f"{barcode_data} - {name if name else 'Not Named'} - {price if price is not None else 'Not Found'} KHR",
                            (obj.rect.left, obj.rect.top - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                cv2.rectangle(frame, (obj.rect.left, obj.rect.top),
                              (obj.rect.left + obj.rect.width, obj.rect.top + obj.rect.height),
                              (0, 255, 0), 2)

        # Display the frame
        cv2.imshow('Barcode Scanner', frame)

        key = cv2.waitKey(10) & 0xFF

        if key == ord('q'):
            # Break the loop if 'q' is pressed
            break
        elif key == ord('p'):
            # Print the total price and the scanned items if 'p' is pressed
            total_price_usd = total_price / KHR_TO_USD_CONVERSION_RATE
            print(f"Total Price: {total_price} KHR (${total_price_usd:.2f} USD)")
            print("Scanned Items and Counts:")
            for barcode, count in scanned_items.items():
                book_info = get_book_info(barcode)
                price_per_item = book_info["price"]
                name = book_info["name"]
                if price_per_item is not None:
                    total_item_price = price_per_item * count
                    total_item_price_usd = total_item_price / KHR_TO_USD_CONVERSION_RATE
                    print(
                        f"Barcode Data: {barcode}, Name: {name}, Count: {count}, Total Price for this item: {total_item_price} KHR (${total_item_price_usd:.2f} USD)")
                else:
                    print(
                        f"Barcode Data: {barcode}, Name: {name}, Count: {count}, Total Price for this item: Price not found")
        elif key == ord('u'):
            # Update the price and name of a barcode if 'u' is pressed
            barcode_data = input("Enter the barcode to update: ")
            try:
                new_price = float(input("Enter the new price in KHR: "))
                new_name = input("Enter the new name of the item: ")
                update_book_info(barcode_data, new_price, new_name)
            except ValueError:
                print("Invalid price input. Please enter a valid number.")
        elif key == ord('r'):
            # Allow the user to change the price of an item if 'r' is pressed
            change_item_price()

finally:
    # Release the webcam and close windows
    cap.release()
    cv2.destroyAll





# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.uix.button import Button
# from kivy.uix.image import Image
# from kivy.clock import Clock
# import cv2
# from pyzbar.pyzbar import decode
# import json
# import os
#
# # File to store barcode prices and names
# PRICE_FILE = 'barcode_data.json'
#
#
# # Load barcode data from a JSON file
# def load_data():
#     if os.path.exists(PRICE_FILE):
#         with open(PRICE_FILE, 'r') as file:
#             return json.load(file)
#     return {}
#
#
# # Save barcode data to a JSON file
# def save_data(data):
#     with open(PRICE_FILE, 'w') as file:
#         json.dump(data, file, indent=4)
#
#
# # Define a dictionary to map barcodes to their prices and names
# barcode_data_map = load_data()
#
#
# def get_book_info(barcode_data):
#     return barcode_data_map.get(barcode_data, {"price": None, "name": None})
#
#
# def update_book_info(barcode_data, price, name):
#     barcode_data_map[barcode_data] = {"price": price, "name": name}
#     save_data(barcode_data_map)
#
#
# class BarcodeScannerApp(App):
#     def build(self):
#         self.capture = cv2.VideoCapture(0)
#         self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#         self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#
#         self.image = Image()
#         self.label = Label(text="Scan a barcode", size_hint_y=None, height=50)
#         self.button = Button(text="Add New Barcode", size_hint_y=None, height=50)
#         self.button.bind(on_press=self.add_new_barcode)
#
#         layout = BoxLayout(orientation='vertical')
#         layout.add_widget(self.label)
#         layout.add_widget(self.image)
#         layout.add_widget(self.button)
#
#         Clock.schedule_interval(self.update, 1.0 / 30.0)  # Update at ~30 fps
#         return layout
#
#     def update(self, dt):
#         ret, frame = self.capture.read()
#         if ret:
#             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#             decoded_objects = decode(gray)
#             for obj in decoded_objects:
#                 barcode_data = obj.data.decode('utf-8')
#                 book_info = get_book_info(barcode_data)
#                 price = book_info["price"]
#                 name = book_info["name"]
#
#                 if price is not None:
#                     self.label.text = f"Barcode Data: {barcode_data}\nName: {name}\nPrice: {price} KHR"
#                 else:
#                     self.label.text = f"Barcode Data: {barcode_data}\nName: Not Found\nPrice: Not Found"
#
#                 # Draw bounding box
#                 for obj in decoded_objects:
#                     points = obj.polygon
#                     if len(points) == 4:
#                         pts = [(point.x, point.y) for point in points]
#                         cv2.polylines(frame, [np.array(pts, np.int32)], True, (0, 255, 0), 2)
#                     else:
#                         pts = [(point.x, point.y) for point in obj.polygon]
#                         cv2.polylines(frame, [np.array(pts, np.int32)], True, (0, 255, 0), 2)
#
#             # Convert image for Kivy
#             buf = frame.tobytes()
#             texture = self.image.texture
#             texture.blit_buffer(buf, colorfmt='bgr')
#             self.image.texture = texture
#
#     def add_new_barcode(self, instance):
#         barcode_data = self.label.text.split('\n')[0].replace('Barcode Data: ', '')
#         new_price = float(input("Enter the price in KHR: "))
#         new_name = input("Enter the name of the item: ")
#         update_book_info(barcode_data, new_price, new_name)
#         print(f"Added new barcode {barcode_data} with price {new_price} KHR and name '{new_name}'")
#
#
# if __name__ == '__main__':
#     BarcodeScannerApp().run()


# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.uix.image import Image
# from kivy.clock import Clock
# import cv2
# from pyzbar.pyzbar import decode
# import numpy as np
# import json
# import os
#
# # File to store barcode prices and names
# PRICE_FILE = 'barcode_data.json'
#
#
# # Load barcode data from a JSON file
# def load_data():
#     if os.path.exists(PRICE_FILE):
#         with open(PRICE_FILE, 'r') as file:
#             return json.load(file)
#     return {}
#
#
# # Save barcode data to a JSON file
# def save_data(data):
#     with open(PRICE_FILE, 'w') as file:
#         json.dump(data, file, indent=4)
#
#
# # Define a dictionary to map barcodes to their prices and names
# barcode_data_map = load_data()
#
#
# def get_book_info(barcode_data):
#     return barcode_data_map.get(barcode_data, {"price": None, "name": None})
#
#
# def update_book_info(barcode_data, price, name):
#     barcode_data_map[barcode_data] = {"price": price, "name": name}
#     save_data(barcode_data_map)
#
#
# class BarcodeScannerApp(App):
#     def build(self):
#         self.capture = cv2.VideoCapture(0)
#         self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#         self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#
#         self.image = Image()
#         self.label = Label(text="Scan a barcode", size_hint_y=None, height=50)
#
#         layout = BoxLayout(orientation='vertical')
#         layout.add_widget(self.label)
#         layout.add_widget(self.image)
#
#         Clock.schedule_interval(self.update, 1.0 / 30.0)  # Update at ~30 fps
#         return layout
#
#     def update(self, dt):
#         ret, frame = self.capture.read()
#         if ret:
#             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#             decoded_objects = decode(gray)
#             for obj in decoded_objects:
#                 barcode_data = obj.data.decode('utf-8')
#                 book_info = get_book_info(barcode_data)
#                 price = book_info["price"]
#                 name = book_info["name"]
#
#                 if price is not None:
#                     self.label.text = f"Barcode Data: {barcode_data}\nName: {name}\nPrice: {price} KHR"
#                 else:
#                     self.label.text = f"Barcode Data: {barcode_data}\nName: Not Found\nPrice: Not Found"
#
#                 # Draw bounding box
#                 for obj in decoded_objects:
#                     points = obj.polygon
#                     if len(points) == 4:
#                         pts = [(point.x, point.y) for point in points]
#                         cv2.polylines(frame, [np.array(pts, np.int32)], True, (0, 255, 0), 2)
#                     else:
#                         pts = [(point.x, point.y) for point in obj.polygon]
#                         cv2.polylines(frame, [np.array(pts, np.int32)], True, (0, 255, 0), 2)
#
#             # Convert frame to texture
#             buf = cv2.flip(frame, 0).tobytes()
#             texture = self.image.texture
#             if texture is None:
#                 texture = self.image.texture = self.image.texture.create(size=(frame.shape[1], frame.shape[0]),
#                                                                          colorfmt='bgr')
#             texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
#             self.image.texture = texture
#
#     def on_stop(self):
#         self.capture.release()
#
#
# if __name__ == '__main__':
#     BarcodeScannerApp().run()


# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.uix.image import Image
# from kivy.clock import Clock
# import cv2
# from pyzbar.pyzbar import decode
# import numpy as np
# import json
# import os
#
# # File to store barcode prices and names
# PRICE_FILE = 'barcode_data.json'
#
#
# # Load barcode data from a JSON file
# def load_data():
#     if os.path.exists(PRICE_FILE):
#         with open(PRICE_FILE, 'r') as file:
#             return json.load(file)
#     return {}
#
#
# # Save barcode data to a JSON file
# def save_data(data):
#     with open(PRICE_FILE, 'w') as file:
#         json.dump(data, file, indent=4)
#
#
# # Define a dictionary to map barcodes to their prices and names
# barcode_data_map = load_data()
#
#
# def get_book_info(barcode_data):
#     return barcode_data_map.get(barcode_data, {"price": None, "name": None})
#
#
# def update_book_info(barcode_data, price, name):
#     barcode_data_map[barcode_data] = {"price": price, "name": name}
#     save_data(barcode_data_map)
#
#
# class BarcodeScannerApp(App):
#     def build(self):
#         self.capture = cv2.VideoCapture(0)
#         self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#         self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#
#         # Create an Image widget and initialize its texture
#         self.image = Image(size=(640, 480))
#         self.label = Label(text="Scan a barcode", size_hint_y=None, height=50)
#
#         layout = BoxLayout(orientation='vertical')
#         layout.add_widget(self.label)
#         layout.add_widget(self.image)
#
#         Clock.schedule_interval(self.update, 1.0 / 30.0)  # Update at ~30 fps
#         return layout
#
#     def update(self, dt):
#         ret, frame = self.capture.read()
#         if ret:
#             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#             decoded_objects = decode(gray)
#
#             for obj in decoded_objects:
#                 barcode_data = obj.data.decode('utf-8')
#                 book_info = get_book_info(barcode_data)
#                 price = book_info["price"]
#                 name = book_info["name"]
#
#                 if price is not None:
#                     self.label.text = f"Barcode Data: {barcode_data}\nName: {name}\nPrice: {price} KHR"
#                 else:
#                     self.label.text = f"Barcode Data: {barcode_data}\nName: Not Found\nPrice: Not Found"
#
#                 # Draw bounding box
#                 for obj in decoded_objects:
#                     points = obj.polygon
#                     if len(points) == 4:
#                         pts = [(point.x, point.y) for point in points]
#                         cv2.polylines(frame, [np.array(pts, np.int32)], True, (0, 255, 0), 2)
#                     else:
#                         pts = [(point.x, point.y) for point in obj.polygon]
#                         cv2.polylines(frame, [np.array(pts, np.int32)], True, (0, 255, 0), 2)
#
#             # Convert frame to texture
#             buf = cv2.flip(frame, 0).tobytes()
#             if self.image.texture is None:
#                 self.image.texture = self.image.texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
#
#             self.image.texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
#             self.image.texture.flip_vertical()  # Ensure correct orientation
#             self.image.texture = self.image.texture
#
#     def on_stop(self):
#         self.capture.release()
#
#
# if __name__ == '__main__':
#     BarcodeScannerApp().run()


# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.uix.image import Image
# from kivy.clock import Clock
# import cv2
# from pyzbar.pyzbar import decode
# import numpy as np
# import json
# import os
#
# # File to store barcode prices and names
# PRICE_FILE = 'barcode_data.json'
#
# # Load barcode data from a JSON file
# def load_data():
#     if os.path.exists(PRICE_FILE):
#         with open(PRICE_FILE, 'r') as file:
#             return json.load(file)
#     return {}
#
# # Save barcode data to a JSON file
# def save_data(data):
#     with open(PRICE_FILE, 'w') as file:
#         json.dump(data, file, indent=4)
#
# # Define a dictionary to map barcodes to their prices and names
# barcode_data_map = load_data()
#
# def get_book_info(barcode_data):
#     return barcode_data_map.get(barcode_data, {"price": None, "name": None})
#
# def update_book_info(barcode_data, price, name):
#     barcode_data_map[barcode_data] = {"price": price, "name": name}
#     save_data(barcode_data_map)
#
# class BarcodeScannerApp(App):
#     def build(self):
#         self.capture = cv2.VideoCapture(0)
#         self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#         self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#
#         # Create an Image widget and initialize its texture
#         self.image = Image(size=(640, 480))
#         self.label = Label(text="Scan a barcode", size_hint_y=None, height=50)
#
#         layout = BoxLayout(orientation='vertical')
#         layout.add_widget(self.label)
#         layout.add_widget(self.image)
#
#         Clock.schedule_interval(self.update, 1.0 / 30.0)  # Update at ~30 fps
#         return layout
#
#     def update(self, dt):
#         ret, frame = self.capture.read()
#         if ret:
#             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#             decoded_objects = decode(gray)
#
#             for obj in decoded_objects:
#                 barcode_data = obj.data.decode('utf-8')
#                 book_info = get_book_info(barcode_data)
#                 price = book_info["price"]
#                 name = book_info["name"]
#
#                 if price is not None:
#                     self.label.text = f"Barcode Data: {barcode_data}\nName: {name}\nPrice: {price} KHR"
#                 else:
#                     self.label.text = f"Barcode Data: {barcode_data}\nName: Not Found\nPrice: Not Found"
#
#                 # Draw bounding box
#                 points = obj.polygon
#                 if len(points) == 4:
#                     pts = [(point.x, point.y) for point in points]
#                     cv2.polylines(frame, [np.array(pts, np.int32)], True, (0, 255, 0), 2)
#
#             # Convert frame to texture
#             buf = cv2.flip(frame, 0).tobytes()
#             if self.image.texture is None:
#                 self.image.texture = self.image.texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
#             else:
#                 self.image.texture.size = (frame.shape[1], frame.shape[0])
#
#             self.image.texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
#             self.image.texture.flip_vertical()  # Ensure correct orientation
#
#     def on_stop(self):
#         self.capture.release()
#
# if __name__ == '__main__':
#     BarcodeScannerApp().run()




# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.uix.image import Image
# from kivy.clock import Clock
# import cv2
# from pyzbar.pyzbar import decode
# import numpy as np
# import json
# import os
#
# # File to store barcode prices and names
# PRICE_FILE = 'barcode_data.json'
#
# # Load barcode data from a JSON file
# def load_data():
#     if os.path.exists(PRICE_FILE):
#         with open(PRICE_FILE, 'r') as file:
#             return json.load(file)
#     return {}
#
# # Save barcode data to a JSON file
# def save_data(data):
#     with open(PRICE_FILE, 'w') as file:
#         json.dump(data, file, indent=4)
#
# # Define a dictionary to map barcodes to their prices and names
# barcode_data_map = load_data()
#
# def get_book_info(barcode_data):
#     return barcode_data_map.get(barcode_data, {"price": None, "name": None})
#
# def update_book_info(barcode_data, price, name):
#     barcode_data_map[barcode_data] = {"price": price, "name": name}
#     save_data(barcode_data_map)
#
# class BarcodeScannerApp(App):
#     def build(self):
#         self.capture = cv2.VideoCapture(0)
#         self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#         self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#
#         # Create an Image widget
#         self.image = Image(size=(640, 480))
#         self.label = Label(text="Scan a barcode", size_hint_y=None, height=50)
#
#         layout = BoxLayout(orientation='vertical')
#         layout.add_widget(self.label)
#         layout.add_widget(self.image)
#
#         # Initialize the texture
#         self.texture = self.image.texture = self.image.texture if self.image.texture else self.image.texture.create(size=(640, 480), colorfmt='bgr')
#
#         Clock.schedule_interval(self.update, 1.0 / 30.0)  # Update at ~30 fps
#         return layout
#
#     def update(self, dt):
#         ret, frame = self.capture.read()
#         if ret:
#             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#             decoded_objects = decode(gray)
#
#             for obj in decoded_objects:
#                 barcode_data = obj.data.decode('utf-8')
#                 book_info = get_book_info(barcode_data)
#                 price = book_info["price"]
#                 name = book_info["name"]
#
#                 if price is not None:
#                     self.label.text = f"Barcode Data: {barcode_data}\nName: {name}\nPrice: {price} KHR"
#                 else:
#                     self.label.text = f"Barcode Data: {barcode_data}\nName: Not Found\nPrice: Not Found"
#
#                 # Draw bounding box
#                 points = obj.polygon
#                 if len(points) == 4:
#                     pts = [(point.x, point.y) for point in points]
#                     cv2.polylines(frame, [np.array(pts, np.int32)], True, (0, 255, 0), 2)
#
#             # Convert frame to texture
#             buf = cv2.flip(frame, 0).tobytes()
#
#             if not self.image.texture:
#                 self.image.texture = self.image.texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
#             self.image.texture.size = (frame.shape[1], frame.shape[0])
#
#             self.image.texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
#             self.image.texture.flip_vertical()  # Ensure correct orientation
#
#     def on_stop(self):
#         self.capture.release()
#
# if __name__ == '__main__':
#     BarcodeScannerApp().run()

