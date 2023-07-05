import psutil
import pynvml  # GPU monitoring library
import tkinter as tk

class SystemMonitorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("System Monitor")

        self.cpu_label = tk.Label(self, text="CPU Usage: ")
        self.cpu_label.pack(pady=5)

        self.gpu_label = tk.Label(self, text="GPU Usage: ")
        self.gpu_label.pack(pady=5)

        self.memory_label = tk.Label(self, text="Memory Usage: ")
        self.memory_label.pack(pady=5)

        self.network_label = tk.Label(self, text="Network Usage: ")
        self.network_label.pack(pady=5)

        self.update_labels()

    def update_labels(self):
        cpu_percent = psutil.cpu_percent(interval=1)
        self.cpu_label.config(text=f"CPU Usage: {cpu_percent}%")

        gpu_percent = self.get_gpu_usage()
        self.gpu_label.config(text=f"GPU Usage: {gpu_percent}%")

        memory_usage = psutil.virtual_memory().percent
        self.memory_label.config(text=f"Memory Usage: {memory_usage}%")

        network_info = psutil.net_io_counters()
        network_usage = network_info.bytes_sent + network_info.bytes_recv
        self.network_label.config(text=f"Network Usage: {network_usage} bytes")

        self.after(1000, self.update_labels)  # Update labels every second

    def get_gpu_usage(self):
        pynvml.nvmlInit()
        handle = pynvml.nvmlDeviceGetHandleByIndex(0)
        info = pynvml.nvmlDeviceGetUtilizationRates(handle)
        gpu_percent = info.gpu
        pynvml.nvmlShutdown()
        return gpu_percent

# Creating an instance of SystemMonitorApp
app = SystemMonitorApp()
app.mainloop()


