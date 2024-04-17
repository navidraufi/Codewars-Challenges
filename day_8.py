import pyautogui as pg
import time


student_words = [
    "Intelligent", "Clever", "Brilliant", "Sharp", "Bright",
    "Smart", "Quick-witted", "Resourceful", "Knowledgeable", "Wise",
    "Savvy", "Astute", "Perceptive", "Analytical", "Insightful",
    "Educated", "Informed", "Erudite", "Well-read", "Intellectual",
    "Genius", "Gifted", "Talented", "Skilled", "Proficient",
    "Competent", "Adept", "Accomplished", "Expert", "Masterful",
    "Diligent", "Hardworking", "Industrious", "Persistent", "Dedicated",
    "Committed", "Focused", "Motivated", "Driven", "Ambitious",
    "Tenacious", "Resilient", "Persevering", "Goal-oriented", "Disciplined",
    "Self-motivated", "Self-disciplined", "Productive", "Efficient",
    "Effective", "Innovative", "Creative", "Imaginative", "Curious",
    "Inquisitive", "Problem-solver", "Critical thinker", "Analytical",
    "Logical", "Rational", "Strategic", "Adaptable", "Flexible",
    "Versatile", "Open-minded", "Reflective", "Self-aware", "Self-improving",
    "Self-assured", "Confident", "Optimistic", "Positive", "Hopeful",
    "Responsible", "Accountable", "Trustworthy", "Honest", "Ethical",
    "Inspirational", "Role model", "Exemplary", "Aspiring", "Successful",
    "Achiever", "Winner", "Triumphant", "Victorious", "Respected",
    "Esteemed", "Appreciated", "Valued", "Proud", "Satisfied"
]


good_words =  [
    "Knowledgeable", "Inspiring", "Dedicated", "Caring", "Supportive",
    "Encouraging", "Passionate", "Motivating", "Influential", "Patient",
    "Understanding", "Empathetic", "Inspirational", "Enthusiastic",
    "Compassionate", "Respectful", "Helpful", "Guiding", "Mentoring",
    "Nurturing", "Experienced", "Wise", "Brilliant", "Exceptional",
    "Talented", "Skilled", "Professional", "Hardworking", "Committed",
    "Devoted", "Generous", "Instructive", "Educational", "Informative",
    "Insightful", "Innovative", "Resourceful", "Effective", "Excellent",
    "Admirable", "Honorable", "Esteemed", "Valued", "Appreciated",
    "Grateful", "Thankful", "Indebted", "Responsible", "Reliable",
    "Approachable", "Friendly", "Approving", "Praiseworthy",
    "Well-prepared", "Organized", "Thorough", "Fair", "Impartial",
    "Consistent", "Constructive", "Progressive", "Dynamic", "Vibrant",
    "Eloquent",]

time.sleep(5)



for i in range(1,100):
    pg.write(f"Fuckw you {i} times.")
    pg.press("Enter")
    time.sleep(1)
