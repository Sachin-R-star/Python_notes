# 🐍 Python Full Course for Interview 2026 (Jenny's Lectures CS IT)

> **YouTube Playlist Reference:** [Python Full Course - Jenny's Lectures](https://www.youtube.com/playlist?list=PLdo5W4Nhv31bZSiqiOL5ta39vSnBxpOPT)  
> **Course Coverage:** Total 126 Lectures / Videos covered completely with **0 missed concepts**.  
> **Explanations:** Brief & crisp **Hinglish comments** explaining "Ye kya hai", "Kyu use karte hain", aur "Interview me kya puchte hain", accompanied by 100% executable and tested Python code.

---

## 📁 Repository Structure Overview

```text
Python_for_interview_2026/
│
├── 01_basics_print_input_variables/
│   ├── 01_intro_history_first_program.py       # Lec 001 - 005 (Intro, History, First Program)
│   ├── 02_print_strings_comments.py            # Lec 006 - 007 (Print formatting, Escapes, Ex 1)
│   ├── 03_input_and_variables_swap.py          # Lec 008 - 011 (Input, Variables, Ex 2 Swap, Naming Rules)
│   └── 04_datatypes_typecasting_add_digits.py  # Lec 012 - 014 (Data types, Type casting, Ex 3 Add Digits)
│
├── 02_operators_and_math/
│   ├── 01_arithmetic_assignment_comparison.py  # Lec 015 - 016 (Arithmetic, PEMDAS, Relational)
│   ├── 02_logical_bitwise_identity_membership.py # Lec 017 - 020 (Logical, Bitwise, Identity 'is', Membership 'in')
│   └── 03_round_fstrings_bmi_life_weeks.py     # Lec 021 - 024 (round(), f-Strings, Ex 4 BMI, Ex 5 Life in Weeks)
│
├── 03_conditional_statements/
│   ├── 01_if_else_nested_bmi2_leap_year.py     # Lec 025 - 029 (if-else, Ex 6 Odd/Even, Ex 7 BMI 2.0, Ex 8 Leap Year)
│   └── 02_multiple_if_pizza_order_love_calc.py # Lec 030 - 032 (Multiple Ifs, Ex 9 Pizza Order, Ex 10 Love Calculator)
│
├── 04_data_structures_random_and_project1/
│   ├── 01_lists_methods_random_heads_tails.py  # Lec 033 - 036 (Lists, Methods, Random, Ex 11 Coin, Ex 12 Banker)
│   ├── 02_index_error_nested_lists_treasure_map.py # Lec 037 - 039 (IndexError, Nested Lists, Ex 13 Treasure Map)
│   ├── 03_project1_rock_paper_scissors.py      # Lec 040 (Project 1: Rock Paper Scissors Game)
│   ├── 04_tuples_immutable_packing_unpacking.py # Lec 041 (Tuples, Immutability, Packing, Unpacking)
│   └── 05_sets_operations_and_methods.py       # Lec 042 - 045 (Sets, Set Operations, Frozenset)
│
├── 05_loops_and_project2_project3/
│   ├── 01_for_loop_for_else_avg_height_max_score.py # Lec 046 - 049 (For loop, For-Else, Ex 14 Avg, Ex 15 Max)
│   ├── 02_range_function_sum_evens_fizzbuzz.py # Lec 050 - 052 (range(), Ex 16 Evens Sum, Ex 17 FizzBuzz)
│   ├── 03_project2_password_generator.py       # Lec 053 (Project 2: PyPassword Generator)
│   ├── 04_while_loop_break_continue_pass_indentation.py # Lec 054 - 056 (While loop, Break, Continue, Pass, Indentation)
│   └── 05_project3_hangman_game.py             # Lec 057 - 059 (Project 3: Hangman Game Complete)
│
├── 06_functions_and_project4/
│   ├── 01_functions_intro_paint_cans_calc.py   # Lec 060 - 063 (Functions intro, Ex 18-19, Ex 20 Paint Cans)
│   ├── 02_arguments_types_args_kwargs.py       # Lec 064 - 066 (Positional, Keyword, Default, *args, **kwargs)
│   ├── 03_prime_number_checker_exercises.py    # Lec 067 - 068 (Ex 21 & Ex 22: Prime Number Checker & Optimization)
│   └── 04_project4_caesar_cipher.py            # Lec 069 - 070 (Project 4: Caesar Cipher Complete)
│
├── 07_dictionaries_and_project5/
│   ├── 01_dictionary_basics_methods_grading.py # Lec 071 - 072 (Dictionaries, Methods, Ex 23 Grading Program)
│   ├── 02_nested_dictionaries_travel_log.py    # Lec 073 - 074 (Nested Dicts, Lists in Dicts, Ex 24 Travel Log)
│   └── 03_project5_silent_auction.py           # Lec 075 - 076 (Project 5: Secret Silent Auction)
│
├── 08_return_scope_debugging_projects/
│   ├── 01_return_multiple_returns_days_in_month_print_vs_return.py # Lec 077 - 080 (return, Ex 25 Days in Month, print vs return)
│   ├── 02_project6_calculator.py               # Lec 081 (Project 6: Calculator App)
│   ├── 03_local_global_scope_global_keyword.py # Lec 082 - 083 (LEGB rule, global keyword, nonlocal)
│   ├── 04_project7_guess_the_number.py         # Lec 084 (Project 7: Guess The Number Game)
│   ├── 05_debugging_tips_and_common_errors.py  # Lec 085 (Top 10 Errors & 4-Step Debugging)
│   ├── 06_project8_higher_lower_game.py        # Lec 086 (Project 8: Higher Lower Game)
│   └── 07_project9_coffee_machine.py           # Lec 087 (Project 9: Coffee Machine Simulator)
│
├── 09_oop_object_oriented_programming/
│   ├── 01_oop_intro_classes_objects_init_self_methods.py # Lec 088 - 091 (OOP Intro, Class, Object, __init__, self, @classmethod, @staticmethod)
│   ├── 02_exercise26_circle_bank_account.py    # Lec 092 (Ex 26: Circle Class + BankAccount)
│   ├── 03_inheritance_single_multiple_multilevel_hierarchical_hybrid.py # Lec 093 - 097 (All 5 Types of Inheritance, super())
│   └── 04_diamond_problem_mro_c3_linearization.py # Lec 098 (Diamond Problem, MRO, C3 Linearization)
│
├── 10_file_handling_and_project10/
│   ├── 01_file_handling_read_write_append_modes.py # Lec 099 (File Modes, seek, tell, with context manager)
│   └── 02_project10_quiz_game_oop.py           # Lec 100 (Project 10: Quiz Game MVC OOP)
│
├── 11_advanced_oop_modules_packages/
│   ├── 01_modules_packages_pip_dunder_name.py  # Lec 101, 112, 113, 114 (Modules, Packages, pip, PyPI, if __name__ == '__main__')
│   ├── 02_abstraction_abstract_class_methods.py # Lec 102 - 103 (Abstraction, abc module, ABC, @abstractmethod)
│   ├── 03_access_modifiers_encapsulation_getters_setters.py # Lec 104 - 105 (Public, Protected _, Private __, Name Mangling, @property)
│   ├── 04_polymorphism_duck_typing_operator_overloading_overriding.py # Lec 106 - 109 (Polymorphism, Duck Typing, Operator & Method Overloading/Overriding)
│   └── 05_magic_dunder_methods_exercise27.py   # Lec 110 - 111 (Dunder Methods: __str__, __repr__, __len__, __eq__, __call__, Ex 27)
│
└── 12_turtle_graphics_higher_order_colorgram/
    ├── 01_turtle_basics_shapes_spirograph.py   # Lec 115 - 121 (Turtle intro, Ex 28 Square, Ex 29 Dashed, Ex 30 Polygons, Ex 31 Walk, Ex 32 Spirograph)
    ├── 02_project11_turtle_race.py             # Lec 122 (Project 11: Turtle Race Project)
    ├── 03_higher_order_functions_event_listeners_sketch.py # Lec 123 - 125 (Higher Order Functions, Event Listeners, Ex 33 Etch-A-Sketch)
    └── 04_colorgram_rgb_extraction_hirst_painting.py # Lec 126 (Colorgram RGB extraction & Damien Hirst Spot Painting)
│
└── fastAPI/                                    # ⚡ TechSimPlus Learnings Complete FastAPI Backend Playlist (26 Tutorials)
    ├── 01_fastapi_introduction_and_architecture.py
    ├── 02_setup_environment_and_uvicorn.py
    ├── ... (26 in-depth conceptual files with detailed Hinglish comments)
    └── README.md                               # Complete FastAPI Course Syllabus & Guide
```

---

## 📑 Complete 126-Lecture Mapping & Syllabus Index

| # | Video Title (Jenny's Lectures) | Lecture # | Topic / Concepts Covered | Corresponding File |
|---|---|---|---|---|
| **001** | Introduction to Python Course | Intro | Overview, Syllabus & Setup | `01_basics_print_input_variables/01_intro_history_first_program.py` |
| **002** | Introduction to Python Programming | #lec1 | High-level, Interpreted, Dynamically Typed | `01_basics_print_input_variables/01_intro_history_first_program.py` |
| **003** | History of Python | #lec2 | Guido van Rossum, Monty Python origin, Python 2 vs 3 | `01_basics_print_input_variables/01_intro_history_first_program.py` |
| **004** | Download and Install Python & PyCharm | #lec3 | Python Installation, REPL vs Script execution | `01_basics_print_input_variables/01_intro_history_first_program.py` |
| **005** | Writing First Python Program | #lec4 | `print()`, basic execution | `01_basics_print_input_variables/01_intro_history_first_program.py` |
| **006** | Coding Exercises for Beginners - Exercise #1 | Ex #1 | Output formatting, exact console print matching | `01_basics_print_input_variables/02_print_strings_comments.py` |
| **007** | print() function & String concatenation | #lec6 | String `+` concatenation, escape sequences `\n`, `\t`, `sep`, `end` | `01_basics_print_input_variables/02_print_strings_comments.py` |
| **008** | Input function in Python | #lec7 | `input()` returns string, prompt message | `01_basics_print_input_variables/03_input_and_variables_swap.py` |
| **009** | Variables in Python | #lec8 | Memory references, object labels, `id()` function | `01_basics_print_input_variables/03_input_and_variables_swap.py` |
| **010** | Coding Exercises - Exercise #2 (Swap numbers) | Ex #2 | Swapping: Temp var, Tuple unpacking `a, b = b, a`, Arithmetic | `01_basics_print_input_variables/03_input_and_variables_swap.py` |
| **011** | Variable Naming Rules in Python | #lec10 | Identifiers rules, keywords, PEP 8 snake_case | `01_basics_print_input_variables/03_input_and_variables_swap.py` |
| **012** | Data Types in Python | #lec11 | int, float, complex, bool, str, binary/octal/hex prefixes | `01_basics_print_input_variables/04_datatypes_typecasting_add_digits.py` |
| **013** | Type Checking, Type Error & Type Conversion | #lec12 | `type()`, `isinstance()`, Implicit vs Explicit type casting, Truthy/Falsy | `01_basics_print_input_variables/04_datatypes_typecasting_add_digits.py` |
| **014** | Coding Exercises - Exercise #3 (Add digits) | Ex #3 | String indexing vs Mathematical `//` and `%` digit addition | `01_basics_print_input_variables/04_datatypes_typecasting_add_digits.py` |
| **015** | Operators in Python: Arithmetic Operators | #lec14 | `+`, `-`, `*`, `/` (always float), `//` (floor div), `%`, `**` | `02_operators_and_math/01_arithmetic_assignment_comparison.py` |
| **016** | Assignment and Comparison Operators | #lec15 | Compound assignments `+=`, Relational `==`, `!=`, `<`, `>`, Chained comparison | `02_operators_and_math/01_arithmetic_assignment_comparison.py` |
| **017** | Logical Operators in Python | #lec16 | `and`, `or`, `not`, Short-circuit evaluation | `02_operators_and_math/02_logical_bitwise_identity_membership.py` |
| **018** | Bitwise Operators in Python | #lec17 | `&`, `\|`, `^`, `~`, `<<`, `>>` bitwise mechanics | `02_operators_and_math/02_logical_bitwise_identity_membership.py` |
| **019** | Identity Operators in Python | #lec18 | `is`, `is not` vs `==` (Identity vs Value equality) | `02_operators_and_math/02_logical_bitwise_identity_membership.py` |
| **020** | Membership Operators in Python | #lec19 | `in`, `not in` across strings, lists, dict keys | `02_operators_and_math/02_logical_bitwise_identity_membership.py` |
| **021** | Coding Exercise #4 - BMI Calculator | #lec20 | Body Mass Index formula $weight / height^2$ | `02_operators_and_math/03_round_fstrings_bmi_life_weeks.py` |
| **022** | round() function in Python | #lec21 | Banker's Rounding (Round half to even), negative ndigits | `02_operators_and_math/03_round_fstrings_bmi_life_weeks.py` |
| **023** | f-Strings in Python | #lec22 | Formatted string literals, expression evaluation, padding | `02_operators_and_math/03_round_fstrings_bmi_life_weeks.py` |
| **024** | Coding Exercise #5 - Life in Weeks | #lec23 | Days, weeks, months remaining calculation | `02_operators_and_math/03_round_fstrings_bmi_life_weeks.py` |
| **025** | If & If Else Conditional Statements | #lec24 | Branching logic, indentation blocks | `03_conditional_statements/01_if_else_nested_bmi2_leap_year.py` |
| **026** | Coding Exercise #6 - Odd or Even | #lec25 | Modulo operator check for parity | `03_conditional_statements/01_if_else_nested_bmi2_leap_year.py` |
| **027** | Nested If Else & elif Statements | #lec26 | Multi-way branching, cascading conditions | `03_conditional_statements/01_if_else_nested_bmi2_leap_year.py` |
| **028** | Coding Exercise #7 - BMI 2.0 | #P_27 | Underweight, Normal, Overweight, Obese categories | `03_conditional_statements/01_if_else_nested_bmi2_leap_year.py` |
| **029** | Coding Exercise #8 - Leap Year Checker | #P_28 | Century rules (divisible by 4, not 100 unless 400) | `03_conditional_statements/01_if_else_nested_bmi2_leap_year.py` |
| **030** | Multiple if Statements in Python | #P_29 | Independent ifs vs mutually exclusive elif | `03_conditional_statements/02_multiple_if_pizza_order_love_calc.py` |
| **031** | Coding Exercise #9 - Pizza Order Program | #P_30 | Size selection, toppings add-ons accumulator pattern | `03_conditional_statements/02_multiple_if_pizza_order_love_calc.py` |
| **032** | Coding Exercise #10 - Love Calculator | #P_31 | `.lower()`, `.count()` character frequencies, 2-digit concat | `03_conditional_statements/02_multiple_if_pizza_order_love_calc.py` |
| **033** | List in Python and List Functions | #P_32 | Mutable sequence, indexing, slicing, append, extend, pop | `04_data_structures_random_and_project1/01_lists_methods_random_heads_tails.py` |
| **034** | Random Module in Python | #P_33 | `randint()`, `random()`, `choice()`, `shuffle()` | `04_data_structures_random_and_project1/01_lists_methods_random_heads_tails.py` |
| **035** | Coding Exercise #11 - Heads or Tails | #P_34 | Binary random simulation with `randint(0, 1)` | `04_data_structures_random_and_project1/01_lists_methods_random_heads_tails.py` |
| **036** | Coding Exercise #12 - Banker Roulette | #lec35 | Random bill payer selection from list | `04_data_structures_random_and_project1/01_lists_methods_random_heads_tails.py` |
| **037** | Fix Python IndexError: List Index Out of Range | #lec36 | Off-by-one errors, safe boundary checks | `04_data_structures_random_and_project1/02_index_error_nested_lists_treasure_map.py` |
| **038** | Nested List in Python | #lec37 | 2D matrices, `matrix[row][col]` coordinate access | `04_data_structures_random_and_project1/02_index_error_nested_lists_treasure_map.py` |
| **039** | Coding Exercise #13 - Treasure Map | #lec38 | 3x3 emoji grid coordinate replacement | `04_data_structures_random_and_project1/02_index_error_nested_lists_treasure_map.py` |
| **040** | Python Project 1 - Rock Paper Scissors Game | #lec39 | ASCII Art, decision logic, tie/win/loss resolution | `04_data_structures_random_and_project1/03_project1_rock_paper_scissors.py` |
| **041** | Tuples in Python | #lec40 | Immutability, trailing comma single item, packing/unpacking | `04_data_structures_random_and_project1/04_tuples_immutable_packing_unpacking.py` |
| **042** | Sets in Python (Part 1) | #lec41.1 | Unordered, unique elements, empty set `set()` vs `{}` | `04_data_structures_random_and_project1/05_sets_operations_and_methods.py` |
| **043** | Sets Methods in Python (Part 2) | #lec41.2 | `add()`, `update()`, `remove()` vs `discard()`, `pop()` | `04_data_structures_random_and_project1/05_sets_operations_and_methods.py` |
| **044** | Sets Methods in Python (Part 3) | #lec41.3 | Union `\|`, Intersection `&`, Difference `-`, Symmetric Diff `^` | `04_data_structures_random_and_project1/05_sets_operations_and_methods.py` |
| **045** | Sets Methods in Python (Part 4) | #lec41.4 | `issubset()`, `issuperset()`, `isdisjoint()`, `frozenset` | `04_data_structures_random_and_project1/05_sets_operations_and_methods.py` |
| **046** | For Loop in Python | #lec42 | Iterating over sequences, strings, lists | `05_loops_and_project2_project3/01_for_loop_for_else_avg_height_max_score.py` |
| **047** | For Else in Python | #lec43 | `else` with loops, executes when no `break` triggered | `05_loops_and_project2_project3/01_for_loop_for_else_avg_height_max_score.py` |
| **048** | Coding Exercise #14 - Average Height | #lec44 | Manual accumulator without `len()` or `sum()` | `05_loops_and_project2_project3/01_for_loop_for_else_avg_height_max_score.py` |
| **049** | Coding Exercise #15 - Max Score | #lec45 | Manual linear scan max finder without `max()` | `05_loops_and_project2_project3/01_for_loop_for_else_avg_height_max_score.py` |
| **050** | range() function in Python | #lec46 | start, stop (exclusive), step, reverse step | `05_loops_and_project2_project3/02_range_function_sum_evens_fizzbuzz.py` |
| **051** | Coding Exercise #16 - Sum of Even Numbers | #lec47 | Summing evens 1 to 100 via `range(2, 101, 2)` | `05_loops_and_project2_project3/02_range_function_sum_evens_fizzbuzz.py` |
| **052** | Coding Exercise #17 - FizzBuzz | #lec48 | Divisibility by 3, 5, and 15 (FizzBuzz trap) | `05_loops_and_project2_project3/02_range_function_sum_evens_fizzbuzz.py` |
| **053** | Python Project 2 - Password Generator | #lec49 | Easy sequential vs Hard shuffled password generation | `05_loops_and_project2_project3/03_project2_password_generator.py` |
| **054** | While Loop in Python | #lec50 | Condition controlled loops, infinite loop avoidance | `05_loops_and_project2_project3/04_while_loop_break_continue_pass_indentation.py` |
| **055** | Break, Continue, Pass | #lec51 | Loop controls, placeholders, skip iterations | `05_loops_and_project2_project3/04_while_loop_break_continue_pass_indentation.py` |
| **056** | Indentation in Python | #lec52 | PEP 8 4-space indentation rule, scope blocks | `05_loops_and_project2_project3/04_while_loop_break_continue_pass_indentation.py` |
| **057-059**| Python Project 3 - Hangman Game | #lec53-55 | Complete game: ASCII stages, lives system, letter guessing | `05_loops_and_project2_project3/05_project3_hangman_game.py` |
| **060-062**| Functions in Python Intro & Exercises 18-19 | #lec56-58 | `def`, calling, DRY principle, parameters | `06_functions_and_project4/01_functions_intro_paint_cans_calc.py` |
| **063** | Coding Exercise #20 - Paint Can Calculator | #lec59 | Wall area, fractional rounding with `math.ceil()` | `06_functions_and_project4/01_functions_intro_paint_cans_calc.py` |
| **064** | Functions with Arguments | #lec60 | Parameters (definition) vs Arguments (actual values) | `06_functions_and_project4/02_arguments_types_args_kwargs.py` |
| **065** | Types of Arguments | #lec61 | Positional, Keyword, Default arguments order rule | `06_functions_and_project4/02_arguments_types_args_kwargs.py` |
| **066** | *args and **kwargs | #lec62 | Arbitrary positional (tuple) & keyword (dict) args | `06_functions_and_project4/02_arguments_types_args_kwargs.py` |
| **067-068**| Exercises #21 & #22 - Prime Number Checker | #lec63-64 | Brute force $O(n)$ vs Optimized $O(\sqrt{n})$ prime check | `06_functions_and_project4/03_prime_number_checker_exercises.py` |
| **069-070**| Python Project 4 - Caesar Cipher | #lec65-66 | Cryptography, shift key, modulo 26 wrap-around | `06_functions_and_project4/04_project4_caesar_cipher.py` |
| **071** | Dictionaries in Python & Methods | #lec67 | Key-value mapping, `get()`, `keys()`, `values()`, `items()` | `07_dictionaries_and_project5/01_dictionary_basics_methods_grading.py` |
| **072** | Coding Exercise #23 - Student Grading | #lec68 | Mapping numerical scores to descriptive grades | `07_dictionaries_and_project5/01_dictionary_basics_methods_grading.py` |
| **073-074**| Nested Dictionaries & Exercise #24 (Travel Log) | #lec69-70 | Nested JSON-like dicts, dynamically adding records | `07_dictionaries_and_project5/02_nested_dictionaries_travel_log.py` |
| **075-076**| Python Project 5 - Silent Auction | #lec71-72 | Secret bidding system, max bidder algorithm, screen clear | `07_dictionaries_and_project5/03_project5_silent_auction.py` |
| **077** | Functions with Return Statement | #lec73 | Returning values vs default `None`, early exit | `08_return_scope_debugging_projects/01_return_multiple_returns_days_in_month_print_vs_return.py` |
| **078** | Return Multiple Values | #lec74 | Tuple packing on multiple returns, clean unpacking | `08_return_scope_debugging_projects/01_return_multiple_returns_days_in_month_print_vs_return.py` |
| **079** | Coding Exercise #25 - Days in Month | #lec75 | Month length lookup with leap year February handling | `08_return_scope_debugging_projects/01_return_multiple_returns_days_in_month_print_vs_return.py` |
| **080** | print() vs return | #lec76 | Displaying on console vs returning to memory caller | `08_return_scope_debugging_projects/01_return_multiple_returns_days_in_month_print_vs_return.py` |
| **081** | Python Project 6 - Calculator App | #lec77 | First-class functions dict mapping, recursion chaining | `08_return_scope_debugging_projects/02_project6_calculator.py` |
| **082-083**| Local and Global Scope, global keyword | #lec78-79 | LEGB rule, `UnboundLocalError`, `global`, `nonlocal` | `08_return_scope_debugging_projects/03_local_global_scope_global_keyword.py` |
| **084** | Python Project 7 - Guess The Number | #lec80 | Binary feedback (too high/low), difficulty turns | `08_return_scope_debugging_projects/04_project7_guess_the_number.py` |
| **085** | Debugging in Python & Debugging Tips | #lec81 | Top 10 Python errors, stack traces, `{var=}` syntax | `08_return_scope_debugging_projects/05_debugging_tips_and_common_errors.py` |
| **086** | Python Project 8 - Higher Lower Game | #lec82 | Dataset comparison game loop, score tracking | `08_return_scope_debugging_projects/06_project8_higher_lower_game.py` |
| **087** | Python Project 9 - Coffee Machine Simulator | #lec83 | Vending machine state, coin processing, resources check | `08_return_scope_debugging_projects/07_project9_coffee_machine.py` |
| **088-091**| OOP Intro, Classes, Objects, init, self, Methods | #lec84-87 | Blueprint, constructor, instance vs `@classmethod` vs `@staticmethod` | `09_oop_object_oriented_programming/01_oop_intro_classes_objects_init_self_methods.py` |
| **092** | Exercise #26 - Circle Class | #lec88 | Radius, area, circumference + BankAccount demo | `09_oop_object_oriented_programming/02_exercise26_circle_bank_account.py` |
| **093-097**| All 5 Types of Inheritance in Python | #lec89-93 | Single, Multiple, Multilevel, Hierarchical, Hybrid, `super()` | `09_oop_object_oriented_programming/03_inheritance_single_multiple_multilevel_hierarchical_hybrid.py` |
| **098** | Diamond Problem & MRO (C3 Linearization) | #lec94 | Deadly Diamond, `__mro__`, C3 algorithm, `super()` chain | `09_oop_object_oriented_programming/04_diamond_problem_mro_c3_linearization.py` |
| **099** | File Handling in Python | #lec95 | Modes `'r'`, `'w'`, `'a'`, `r+`, `seek()`, `tell()`, `with` context | `10_file_handling_and_project10/01_file_handling_read_write_append_modes.py` |
| **100** | Python Project 10 - Quiz Game Project | #lec96 | OOP Question model, QuizBrain controller, score loop | `10_file_handling_and_project10/02_project10_quiz_game_oop.py` |
| **101** | Modules in Python | #lec97 | Creating custom modules, `import`, `sys.path` | `11_advanced_oop_modules_packages/01_modules_packages_pip_dunder_name.py` |
| **102-103**| Abstraction, Abstract Classes & Methods | #lec98-99 | `abc` module, `ABC`, `@abstractmethod`, interface contracts | `11_advanced_oop_modules_packages/02_abstraction_abstract_class_methods.py` |
| **104-105**| Access Modifiers & Encapsulation | #lec100-101| Public, Protected `_`, Private `__`, Name Mangling, `@property` getters/setters | `11_advanced_oop_modules_packages/03_access_modifiers_encapsulation_getters_setters.py` |
| **106-109**| Polymorphism, Duck Typing, Overloading & Overriding | #lec102-105| Duck typing, Operator overloading (`__add__`), Overloading workaround | `11_advanced_oop_modules_packages/04_polymorphism_duck_typing_operator_overloading_overriding.py` |
| **110-111**| Magic/Dunder Methods & Exercise #27 | #lec106-107| `__str__`, `__repr__`, `__len__`, `__eq__`, `__call__`, Book class | `11_advanced_oop_modules_packages/05_magic_dunder_methods_exercise27.py` |
| **112-114**| pip, PyPI, Packages & if \_\_name\_\_ == '\_\_main\_\_' | #lec108-110| Package manager, `__init__.py`, execution vs import mode | `11_advanced_oop_modules_packages/01_modules_packages_pip_dunder_name.py` |
| **115-121**| Turtle Graphics & Exercises 28-32 | #lec111-118| Canvas, pen controls, Polygons, Random Walk, Spirograph | `12_turtle_graphics_higher_order_colorgram/01_turtle_basics_shapes_spirograph.py` |
| **122** | Python Project 11 - Turtle Race Project | #lec119 | Multi-turtle rainbow race, user betting, finish line check | `12_turtle_graphics_higher_order_colorgram/02_project11_turtle_race.py` |
| **123-125**| Higher Order Functions, Event Listeners & Ex 33 | #lec120-122| First-class functions, `screen.listen()`, `onkey()`, Etch-A-Sketch | `12_turtle_graphics_higher_order_colorgram/03_higher_order_functions_event_listeners_sketch.py` |
| **126** | Colorgram RGB Extraction (#lec117 in playlist) | #lec117/126| Extracting dominant RGB colors from images for Hirst spot painting | `12_turtle_graphics_higher_order_colorgram/04_colorgram_rgb_extraction_hirst_painting.py` |

---

## 🚀 How to Run the Files

Har file standalone executable hai. Terminal me kisi bhi file ko direct run kar sakte hain:

```bash
# Example 1: Run First Program & Basics
python 01_basics_print_input_variables/01_intro_history_first_program.py

# Example 2: Run The Diamond Problem & MRO demo
python 09_oop_object_oriented_programming/04_diamond_problem_mro_c3_linearization.py

# Example 3: Run Caesar Cipher Project
python 06_functions_and_project4/04_project4_caesar_cipher.py

# Example 4: Run Hangman Game Project
python 05_loops_and_project2_project3/05_project3_hangman_game.py
```
