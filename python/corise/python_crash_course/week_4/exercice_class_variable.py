class StudentGrade:
  """Represents the grade for a student in a class
  and indicates when a grade is failing.
  For all students, 159 points is considered a failing grade.

  >>> grade1 = StudentGrade("Arfur Artery", 300)
  >>> grade1.is_failing()
  False
  >>> grade2 = StudentGrade("MoMo OhNo", 158)
  >>> grade2.is_failing()
  True
  >>> grade1.failing_grade
  159
  >>> grade2.failing_grade
  159
  >>> StudentGrade.failing_grade
  159
  >>>
  """
  failing_grade = 159
  def __init__(self, student_name, num_points):
    self.student_name = student_name
    self.num_points = num_points

  def is_failing(self):
    return self.num_points < StudentGrade.failing_grade





#####
import random

class Thneed:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    @classmethod
    def make_thneed(cls, size):
        """
        Returns a new instance of a Thneed with
        a random color and the given size.
        >>> rand_thneed = Thneed.make_thneed("small")
        >>> isinstance(rand_thneed, Thneed)
        True
        >>> rand_thneed.size
        'small'
        >>> isinstance(rand_thneed.color, str)
        True
        """
        color_list = ['blue', 'yellow', 'orange']
        rand_color = random.choice(color_list)
        return cls(rand_color, size)
    
    
    
import random

owner = "Ifeoma"

class Cat:
    def __init__(self, name, owner, lives=9):
        self.name = name
        self.owner = owner
        self.lives = lives

    @classmethod
    def adopt_random_cat(cls, owner = owner):
        """
        Returns a new instance of a Cat with the given owner,
        a randomly chosen name and a random number of lives.
        >>> randcat = Cat.adopt_random_cat("Ifeoma")
        >>> isinstance(randcat, Cat)
        True
        >>> randcat.owner
        'Ifeoma'
        """
        rand_name = random.choice(['leon', 'lucio', 'chachou'])
        rand_lives = random.randint(0,10)
        #adopt_owner = Cat.owner
        return cls(rand_name, owner, rand_lives)