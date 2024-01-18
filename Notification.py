import tkinter as tk
from tkinter import messagebox

class NotificationSystem:
    def __init__(self, root,):
        self.root = root
        self.root.title("Notification System")
        self.root.geometry("400x400")
        

        # Create and place widgets
        self.notification_label = tk.Label(self.root, text="", font=("Helvetica", 12), wraplength=300)
        self.notification_label.pack(pady=20)

        self.trigger_notification_button = tk.Button(self.root, text="Trigger Notification", command=self.trigger_notification)
        self.trigger_notification_button.pack()

    def trigger_notification(self):
        # Placeholder for triggering a notification
        notification_message = "Military alert: Match found!"
        self.show_notification(notification_message)

    def show_notification(self, message):
        # Display the notification using a messagebox
        messagebox.showinfo("Notification", message)
        # You can customize the display further, such as using a separate notification window or system tray.
    def trigger_notification_with_name(self, entered_name):
        notification_message = f"Notification: Hello, {entered_name}!"
        self.show_notification(notification_message)    
    def submit_name(self):
        entered_name = self.name_entry.get()
        if entered_name:
            self.status_label.config(text=f"Status: Hello, {entered_name}!")
            
    # Example of triggering a notification
        notification_message = f"Notification: Hello, {entered_name}!"
        self.notification_system.show_notification(notification_message)



if __name__ == "__main__":
    root = tk.Tk()
    notification_app = NotificationSystem(root)
    root.mainloop()
