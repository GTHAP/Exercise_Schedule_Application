from dataclasses import dataclass

@dataclass
class workout(object):

    wo1 = "Cardio"
    wo2 = "Strength And Conditioning"
    wo3 = "Weight Training"
    wo4 = "Freestyle Boxing"
    wo5 = "Core And Conditioning"

    def print_wo(self):
        print(self.wo1, " ", self.wo2, " ", self.wo3, " ", self.wo4, " ", self.wo5)

@dataclass
class cardio(workout):

    cardio_dict = { 1 : "Jogging", 2 : "Running", 3 : "Sprinting", 4 : "Walking" }

    def print_wo(self):

        print(self.cardio_dict)

@dataclass
class strength_and_conditioning(workout):

    sc_dict_1 = { 1 : "Push ups", 2 : "Squats", 3 : "Forward lunges", 4 : "Pulse push ups" }
    sc_dict_2 = { 1 : "Single arm dumbbell snatch", 2 : "Dumbbell hold", 
    3 : "Sumo deadlift with dumbbell", 4 : "Single arm dumbbell squat clean" }
    sc_dict_3 = { 1 : "Decline push ups", 2 : "Dips", 3 : "Reverse lunge", 4 : "Pulse squats" }
    sc_dict_4 = { 1 : "Side lunges", 2 : "Spiderman push ups", 3 : "Hindu push ups", 
    4 : "Quad rockers" }

    def print_wo(self, option):

        if option == 1 : print(self.sc_dict_1)
        if option == 2 : print(self.sc_dict_2)
        if option == 3 : print(self.sc_dict_3)
        if option == 4 : print(self.sc_dict_4)

@dataclass
class weight_training(workout):

    weight_dict_1 = { 1 : "Hammer curl", 2 : "Tricep press", 3 : "Single arm press", 
    4 : "Bicep curl" }
    weight_dict_2 = { 1 : "Chest press", 2 : "Lying dumbbell hold and bicycle", 
    3 : "Standing chest press", 4 : "Dumbbell row" }

    def print_wo(self, option):

        if option == 1 : print(self.weight_dict_1)
        if option == 2 : print(self.weight_dict_2)

@dataclass
class freestyle_boxing(workout):

    fb_dict_1 = { 1 : "Speed straight punches", 2 : "Speed hooks", 3 : "Speed uppercuts", 
    4 : "Speed Swing punches" }
    fb_dict_2 = { 1 : "4 Straight punches and Sprawls", 
    2 : "Jab cross left right hook left right uppercut", 3 : "Defence and movement",
    4 : "Jab cross" }
    fb_dict_3 = { 1 : "Straight punches with weights", 2 : "Uppercuts with weights",
    3 : "Jabs with weight", 4 : "Defence and movement with weights" }

    def print_wo(self, option):

        if option == 1 : print(self.fb_dict_1)
        if option == 2 : print(self.fb_dict_2)
        if option == 3 : print(self.fb_dict_3)

@dataclass
class core_and_conditioning(workout):

    cc_dict_1 = { 1 : "Bicycle crunches", 2 : "Leg raises", 3 : "Leg tuck ins", 
    4 : "Russian twist" } 
    cc_dict_2 = { 1 : "Elbow plank", 2 : "High plank", 2 : "Cobra to mountain", 
    4 : "Squat hold" }
    cc_dict_3 = { 1 : "V hold", 2 : "Boat hold", 3 : "Side plank", 4 : "Bridge hold" }
    cc_dict_4 = { 1 : "Crunches", 2 : "Butterfly sit ups", 3 : "Leg scissors", 
    4 : "Leg flutters" }
    cc_dict_5 = { 1 : "Jumping squats", 2 : "Split squat", 3 : "Curtsy lunge", 
    4 : "One and a half squat" }
    cc_dict_6 = { 1 : "Plank push ups", 2 : "Shoulder taps", 3 : "Beast load and unload",
    4 : "Beast hold" }
    cc_dict_6 = { 1 : "Beast shoulder tap", 2 : "Reverse crunch", 3 : "Jackknife",
    4 : "Superman hold" }
    cc_dict_7 = { 1 : "Grappler sit ups", 2 : "Bicycle crunches to sit ups",
    3 : "Push up hold", 4 : "Toe touch crunches" }
    cc_dict_8 = { 1 : "Bridges", 2 : "Bird dogs", 3 : "Mountain climber", 4 : "Warrior pose" }
    cc_dict_9 = { 1 : "Jumping squats", 2 : "Split squat", 3 : "Curtsy lunge", 
    4 : "One and a half squat" }

    def print_wo(self, option):

        if option == 1 : print(self.cc_dict_1)
        if option == 2 : print(self.cc_dict_2)
        if option == 3 : print(self.cc_dict_3)
        if option == 4 : print(self.cc_dict_4)
        if option == 5 : print(self.cc_dict_5)
        if option == 6 : print(self.cc_dict_6)
        if option == 7 : print(self.cc_dict_7)
        if option == 8 : print(self.cc_dict_8)
        if option == 9 : print(self.cc_dict_9)

wo_main_obj = workout()
wo_main_obj.print_wo()

wo_cardio_obj = cardio()
print(wo_cardio_obj.wo1)
wo_cardio_obj.print_wo()

wo_sc_obj = strength_and_conditioning()
print(wo_sc_obj.wo2)
wo_sc_obj.print_wo(1)

wo_weight_obj = weight_training()
print(wo_weight_obj.wo3)
wo_weight_obj.print_wo(2)

wo_fb_obj = freestyle_boxing()
print(wo_fb_obj.wo4)
wo_fb_obj.print_wo(3)

wo_cc_obj = core_and_conditioning()
print(wo_cc_obj.wo5)
wo_cc_obj.print_wo(7)
