# GUI.py
import tkinter as tk
from tkinter import ttk


class MyApp:
    def __init__(self, root,notification_system):
        self.root = root
        self.root.title("Hybrid Application")
        self.root.geometry("800x600")
        self.notification_system = notification_system

        # Create and place widgets
        self.label = tk.Label(self.root, text="Welcome to Hybrid Application", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.button_start = tk.Button(self.root, text="Start Processing", command=self.start_processing)
        self.button_start.pack(pady=10)

        self.button_stop = tk.Button(self.root, text="Stop Processing", command=self.stop_processing)
        self.button_stop.pack(pady=10)

        self.progress_bar = ttk.Progressbar(self.root, length=300, mode="indeterminate")  # Use ttk.Progressbar
        self.progress_bar.pack(pady=20)

        self.status_label = tk.Label(self.root, text="Status: Idle")
        self.status_label.pack(pady=10)

        # Additional widgets
        self.separator = ttk.Separator(self.root, orient="horizontal")
        self.separator.pack(fill="x", pady=10)

        self.entry_label = tk.Label(self.root, text="Enter your name:")
        self.entry_label.pack()

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_name)
        self.submit_button.pack(pady=10)

    def start_processing(self):
        # Placeholder for the function to start processing
        self.status_label.config(text="Status: Processing...")
        self.progress_bar.start()

    def stop_processing(self):
        # Placeholder for the function to stop processing
        self.status_label.config(text="Status: Idle")
        self.progress_bar.stop()

    def submit_name(self):
        entered_name = self.name_entry.get()
        if entered_name:
            self.status_label.config(text=f"Status: Hello, {entered_name}!")
            self.notification_system.trigger_notification_with_name(entered_name)


if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
    
  


if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()