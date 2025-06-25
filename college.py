import tkinter as tk
from tkinter import ttk, messagebox
import json
import os


class StudentStatsManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Statistics Manager")
        self.root.geometry("1000x700")

        # Data file for persistence
        self.data_file = "student_data.json"

        # Student data storage
        self.students = []
        self.load_data()

        # Create GUI
        self.create_widgets()
        self.refresh_student_list()

    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)

        # Title
        title_label = ttk.Label(main_frame, text="Student Statistics Manager",
                                font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Left panel - Input form
        input_frame = ttk.LabelFrame(
            main_frame, text="Add New Student", padding="10")
        input_frame.grid(row=1, column=0, sticky=(
            tk.W, tk.E, tk.N, tk.S), padx=(0, 10))

        # Input fields
        ttk.Label(input_frame, text="First Name:").grid(
            row=0, column=0, sticky=tk.W, pady=2)
        self.first_name_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.first_name_var, width=25).grid(
            row=0, column=1, sticky=(tk.W, tk.E), pady=2)

        ttk.Label(input_frame, text="Last Name:").grid(
            row=1, column=0, sticky=tk.W, pady=2)
        self.last_name_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.last_name_var, width=25).grid(
            row=1, column=1, sticky=(tk.W, tk.E), pady=2)

        ttk.Label(input_frame, text="Major:").grid(
            row=2, column=0, sticky=tk.W, pady=2)
        self.major_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.major_var, width=25).grid(
            row=2, column=1, sticky=(tk.W, tk.E), pady=2)

        ttk.Label(input_frame, text="Age:").grid(
            row=3, column=0, sticky=tk.W, pady=2)
        self.age_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.age_var, width=25).grid(
            row=3, column=1, sticky=(tk.W, tk.E), pady=2)

        ttk.Label(input_frame, text="Dormitory:").grid(
            row=4, column=0, sticky=tk.W, pady=2)
        self.dormitory_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.dormitory_var, width=25).grid(
            row=4, column=1, sticky=(tk.W, tk.E), pady=2)

        ttk.Label(input_frame, text="Clubs (comma-separated):").grid(row=5,
                                                                     column=0, sticky=tk.W, pady=2)
        self.clubs_var = tk.StringVar()
        clubs_entry = tk.Text(input_frame, height=3, width=25)
        clubs_entry.grid(row=5, column=1, sticky=(tk.W, tk.E), pady=2)
        self.clubs_text = clubs_entry

        # Configure column weight for input frame
        input_frame.columnconfigure(1, weight=1)

        # Buttons
        button_frame = ttk.Frame(input_frame)
        button_frame.grid(row=6, column=0, columnspan=2, pady=10)

        ttk.Button(button_frame, text="Add Student",
                   command=self.add_student).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear Fields",
                   command=self.clear_fields).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Update Student",
                   command=self.update_student).pack(side=tk.LEFT, padx=5)

        # Right panel - Student list
        list_frame = ttk.LabelFrame(
            main_frame, text="Student List", padding="10")
        list_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)

        # Treeview for displaying students
        columns = ("Name", "Major", "Age", "Dormitory", "Clubs")
        self.tree = ttk.Treeview(
            list_frame, columns=columns, show="headings", height=15)

        # Define headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        # Scrollbars
        v_scrollbar = ttk.Scrollbar(
            list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(
            list_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=v_scrollbar.set,
                            xscrollcommand=h_scrollbar.set)

        # Grid the treeview and scrollbars
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        v_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        h_scrollbar.grid(row=1, column=0, sticky=(tk.W, tk.E))

        # Bind selection event
        self.tree.bind('<<TreeviewSelect>>', self.on_select)

        # Bottom buttons
        bottom_frame = ttk.Frame(list_frame)
        bottom_frame.grid(row=2, column=0, columnspan=2, pady=10)

        ttk.Button(bottom_frame, text="Delete Selected",
                   command=self.delete_student).pack(side=tk.LEFT, padx=5)
        ttk.Button(bottom_frame, text="View Details",
                   command=self.view_details).pack(side=tk.LEFT, padx=5)
        ttk.Button(bottom_frame, text="Save Data",
                   command=self.save_data).pack(side=tk.LEFT, padx=5)

        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(
            main_frame, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.grid(row=2, column=0, columnspan=2,
                        sticky=(tk.W, tk.E), pady=(10, 0))

    def add_student(self):
        """Add a new student to the database"""
        # Get values from input fields
        first_name = self.first_name_var.get().strip()
        last_name = self.last_name_var.get().strip()
        major = self.major_var.get().strip()
        age = self.age_var.get().strip()
        dormitory = self.dormitory_var.get().strip()
        clubs_text = self.clubs_text.get("1.0", tk.END).strip()

        # Validate required fields
        if not all([first_name, last_name, major, age]):
            messagebox.showerror(
                "Error", "Please fill in all required fields (Name, Major, Age)")
            return

        # Validate age
        try:
            age_int = int(age)
            if age_int < 0 or age_int > 150:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid age")
            return

        # Process clubs
        clubs = [club.strip()
                 for club in clubs_text.split(',') if club.strip()]

        # Create student record
        student = {
            "first_name": first_name,
            "last_name": last_name,
            "major": major,
            "age": age_int,
            "dormitory": dormitory,
            "clubs": clubs
        }

        # Add to list
        self.students.append(student)

        # Refresh display
        self.refresh_student_list()

        # Clear fields
        self.clear_fields()

        # Update status
        self.status_var.set(f"Added student: {first_name} {last_name}")

        # Auto-save
        self.save_data()

    def clear_fields(self):
        """Clear all input fields"""
        self.first_name_var.set("")
        self.last_name_var.set("")
        self.major_var.set("")
        self.age_var.set("")
        self.dormitory_var.set("")
        self.clubs_text.delete("1.0", tk.END)

    def refresh_student_list(self):
        """Refresh the student list in the treeview"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Add students to treeview
        for i, student in enumerate(self.students):
            name = f"{student['first_name']} {student['last_name']}"
            clubs_str = ", ".join(
                student['clubs']) if student['clubs'] else "None"

            self.tree.insert("", "end", iid=i, values=(
                name,
                student['major'],
                student['age'],
                student['dormitory'],
                clubs_str
            ))

        # Update status
        self.status_var.set(f"Total students: {len(self.students)}")

    def on_select(self, event):
        """Handle selection of a student in the treeview"""
        selection = self.tree.selection()
        if selection:
            item_id = selection[0]
            student_index = int(item_id)
            student = self.students[student_index]

            # Populate input fields with selected student data
            self.first_name_var.set(student['first_name'])
            self.last_name_var.set(student['last_name'])
            self.major_var.set(student['major'])
            self.age_var.set(str(student['age']))
            self.dormitory_var.set(student['dormitory'])

            self.clubs_text.delete("1.0", tk.END)
            if student['clubs']:
                self.clubs_text.insert("1.0", ", ".join(student['clubs']))

    def update_student(self):
        """Update the selected student"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning(
                "Warning", "Please select a student to update")
            return

        item_id = selection[0]
        student_index = int(item_id)

        # Get values from input fields
        first_name = self.first_name_var.get().strip()
        last_name = self.last_name_var.get().strip()
        major = self.major_var.get().strip()
        age = self.age_var.get().strip()
        dormitory = self.dormitory_var.get().strip()
        clubs_text = self.clubs_text.get("1.0", tk.END).strip()

        # Validate required fields
        if not all([first_name, last_name, major, age]):
            messagebox.showerror("Error", "Please fill in all required fields")
            return

        # Validate age
        try:
            age_int = int(age)
            if age_int < 0 or age_int > 150:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid age")
            return

        # Process clubs
        clubs = [club.strip()
                 for club in clubs_text.split(',') if club.strip()]

        # Update student record
        self.students[student_index] = {
            "first_name": first_name,
            "last_name": last_name,
            "major": major,
            "age": age_int,
            "dormitory": dormitory,
            "clubs": clubs
        }

        # Refresh display
        self.refresh_student_list()

        # Update status
        self.status_var.set(f"Updated student: {first_name} {last_name}")

        # Auto-save
        self.save_data()

    def delete_student(self):
        """Delete the selected student"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning(
                "Warning", "Please select a student to delete")
            return

        item_id = selection[0]
        student_index = int(item_id)
        student = self.students[student_index]

        # Confirm deletion
        if messagebox.askyesno("Confirm Delete",
                               f"Are you sure you want to delete {student['first_name']} {student['last_name']}?"):
            del self.students[student_index]
            self.refresh_student_list()
            self.clear_fields()
            self.status_var.set("Student deleted")
            self.save_data()

    def view_details(self):
        """View detailed information about the selected student"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning(
                "Warning", "Please select a student to view details")
            return

        item_id = selection[0]
        student_index = int(item_id)
        student = self.students[student_index]

        # Create details window
        details_window = tk.Toplevel(self.root)
        details_window.title(
            f"Student Details - {student['first_name']} {student['last_name']}")
        details_window.geometry("400x300")

        # Create text widget with student details
        text_widget = tk.Text(details_window, wrap=tk.WORD, padx=10, pady=10)
        text_widget.pack(fill=tk.BOTH, expand=True)

        # Format student information
        details = f"Name: {student['first_name']} {student['last_name']}\n"
        details += f"Major: {student['major']}\n"
        details += f"Age: {student['age']}\n"
        details += f"Dormitory: {student['dormitory']}\n"
        details += "Student Clubs:\n"

        if student['clubs']:
            for club in student['clubs']:
                details += f"  • {club}\n"
        else:
            details += "  • None\n"

        text_widget.insert(tk.END, details)
        text_widget.config(state=tk.DISABLED)

    def save_data(self):
        """Save student data to JSON file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.students, f, indent=2)
            self.status_var.set("Data saved successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {str(e)}")

    def load_data(self):
        """Load student data from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    self.students = json.load(f)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load data: {str(e)}")
                self.students = []


def main():
    root = tk.Tk()
    app = StudentStatsManager(root)
    root.mainloop()


if __name__ == "__main__":
    main()
