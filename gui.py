
import tkinter as tk

class CounterApp:
    def __init__(self, root, data):
        self.data = data
        self.root = root
        self.root.title("Counter App")
        self.root.geometry("1500x700")
        self.root.resizable(False, False)
        
        # Initialize counter value
        self.counter = 0

        # -------------------------------------------
        color = {
            'main': '#2c3e50',
            'statusbar': '#566573',
            'toolbar': '#566573',
            'bg_dark': '#2c3e50',
            'bg_light': '#566573',
            'button_color': '#2c3e50',
            'darkest': '#0B2447',
        }

        frame_sizes = {
            'school_outer_w': 200,
            'school_inner_w':170,
            
            'ga_outer_w': 300,
            'ga_inner_w': 270,

            'main_inner_w': 1140,

            'inner_h': 650,

            'person_outer_h': 200,
            'person_inner_h': 170,
            'person_outer_w': 250,
            'person_inner_w': 240,
        }

        # region Frames
        # creating outer frame
        school_aside = tk.Frame(self.root, background=color['bg_dark'], width=frame_sizes['school_outer_w'])
        ga_aside = tk.Frame(self.root, background=color['bg_dark'], width=frame_sizes['ga_outer_w'])
        main = tk.PanedWindow(self.root, background=color['bg_dark'])

        # packing them
        school_aside.pack(side="left", fill="y")
        ga_aside.pack(side="right", fill="y")
        main.pack(side="top", fill="both", expand=True)


        # creating inner frame
        school_aside_frame = tk.Frame(school_aside, width=frame_sizes['school_inner_w'], height=frame_sizes['inner_h'], background = color['bg_light'])
        ga_aside_frame = tk.Frame(ga_aside, width=frame_sizes['ga_inner_w'], height=frame_sizes['inner_h'], background = color['bg_light'])
        main_frame = tk.Frame(main, width=frame_sizes['main_inner_w'], height=frame_sizes['inner_h'], background = color['bg_light'])

        # placing them
        school_aside_frame.place(in_=school_aside, anchor="c", relx=.5, rely=.5,)
        ga_aside_frame.place(in_=ga_aside, anchor="c", relx=.5, rely=.5)
        main_frame.place(in_=main, anchor="c", relx=.5, rely=.5)

        # setting some frame attributes
        school_aside_frame.pack_propagate(False)
        ga_aside_frame.grid_propagate(False)
        main_frame.pack_propagate(False)


        # inner ga child frames
        person_base = tk.Frame(ga_aside_frame, width=frame_sizes['person_outer_w'], height=frame_sizes['person_outer_h'], background = 'white')
        # person_base.place(in_=ga_aside_frame, anchor="c", relx=.5, rely=.5)
        person_padx = (frame_sizes['ga_inner_w'] - frame_sizes['person_outer_w']) / 2
        person_base.grid(row=0, padx=person_padx, pady=person_padx)




        # endregion

        # region Buttons
        # Function to create widgets with all options
        def create_widget(parent, widget_type, **options):
            return widget_type(parent, **options)

        # Create the main window
        def create_button(parent, text, fg):
            return create_widget(parent, tk.Button, text=text, fg=fg, bg=color['button_color'], bd=3, cursor='hand2',
                                highlightcolor='red', highlightthickness=2, highlightbackground='black')

        school_buttons_info = [self.data.school.item[instance].name for instance in self.data.school.item]

        for name in school_buttons_info:
            button = create_button(school_aside_frame, text=name, fg = 'white')
            button.pack(side=tk.TOP, fill= 'x')

        
        # endregion



        # -------------------------------------------

        
        # Create and pack the label
        self.label = tk.Label(self.root, text="Counter: 0", font=("Arial", 24))
        # self.label.pack(pady=20)
        
        # Create the increment button
        self.increment_button = tk.Button(self.root, text="Increment", font=("Arial", 14), command=self.increment)
        # self.increment_button.pack(pady=10)
        
        # Create the reset button
        self.reset_button = tk.Button(self.root, text="Reset", font=("Arial", 14), command=self.reset)
        # self.reset_button.pack(pady=10)
        
    def increment(self):
        """Increment the counter and update the label."""
        self.counter += 1
        self.update_label()
        
    def reset(self):
        """Reset the counter to 0 and update the label."""
        self.counter = 0
        self.update_label()
    
    def update_label(self):
        """Update the label with the current counter value."""
        self.label.config(text=f"Counter: {self.counter}")





