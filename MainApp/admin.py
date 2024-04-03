import tkinter as tk

class AdminPage:
    def __init__(self, root):
        self.root = root
        self.admin_window = tk.Toplevel(root)
        self.admin_window.title("Admin Page")

        # Initialize counts
        self.hard_plastic_count = 0
        self.soft_plastic_count = 0
        self.aluminum_count = 0
        self.cardboard_count = 0
        self.polyester_count = 0
        self.disposable_plates_count = 0
        self.iron_count = 0
        self.ceramics_count = 0

        # Set window size and make non-resizable
        self.admin_window.geometry("800x600")
        self.admin_window.resizable(False, False)

        # Create main frame to hold sidebar and content
        self.main_frame = tk.Frame(self.admin_window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Sidebar frame
        self.sidebar_frame = tk.Frame(self.main_frame, width=150, bg="#f0f0f0")
        self.sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Header frame
        self.header_frame = tk.Frame(self.main_frame, bg="#f0f0f0", height=50)
        self.header_frame.pack(fill=tk.X)

        # Label for "Admin Page" in header
        self.header_label = tk.Label(self.header_frame, text="Admin Page", font=("Arial", 24, "bold"), fg="black", bg="#f0f0f0")
        self.header_label.pack(side=tk.LEFT, padx=10, pady=10)

        # Circle on the right side
        self.circle_canvas = tk.Canvas(self.header_frame, width=50, height=50, bg="#f0f0f0", highlightthickness=0)
        self.circle_canvas.pack(side=tk.RIGHT, padx=10, pady=10)
        self.circle = self.circle_canvas.create_oval(5, 5, 45, 45, fill="white")

        # Remove border from sidebar
        self.sidebar_frame.configure(highlightthickness=0)

        # Content frame
        self.content_frame = tk.Frame(self.main_frame, bg="#ffffff")
        self.content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Frame to organize labels
        self.count_frame = tk.Frame(self.sidebar_frame, bg="#f0f0f0")
        self.count_frame.pack(pady=20)

        # Labels to display counts
        categories = [
            ("Hard Plastic", "#e6f7ff"),
            ("Soft Plastic", "#ffe6cc"),
            ("Aluminum", "#f0f0f0"),
            ("Cardboard", "#ccffcc"),
            ("Polyester", "#ffffcc"),
            ("Disposable Plates", "#ffb3b3"),
            ("Iron", "#d9d9d9"),
            ("Ceramics", "#ffccff")
        ]

        for category, color in categories:
            label = tk.Label(self.count_frame, text=f"{category}: 0", font=("Arial", 18), bg=color)
            label.pack(padx=20, pady=10, fill=tk.X)

        # Configure weights for resizing
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)


def open_admin_page(root):
    admin_page = AdminPage(root)


if __name__ == "__main__":
    root = tk.Tk()
    open_admin_page(root)
    root.mainloop()
