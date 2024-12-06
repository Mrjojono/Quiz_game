class Time:
    def __init__(self, time, label, root, stop_event, on_time_up):
        self.time = time
        self.label = label
        self.root = root
        self.stop_event = stop_event
        self.on_time_up = on_time_up
        self.update_time()

    def update_time(self):
        if self.time > 0 and not self.stop_event.is_set():
            mins, secs = divmod(self.time, 60)
            self.root.after(1000, self.update_time)  # Ensure GUI update happens in main thread
            if self.label.winfo_exists():
                self.label.config(text=f"{mins:02d}:{secs:02d}")
            self.time -= 1
        elif not self.stop_event.is_set():
            if self.label.winfo_exists():
                self.label.config(text="Time's up!")
            self.on_time_up()
