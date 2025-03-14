from abc import ABC, abstractmethod

#course behaviorları için abstract base sınıfı
class CourseBehavior(ABC):
  @abstractmethod
  def show_courses(self):
    pass
 #show_courses ın abstract method olma sebebi:
 #herhangi bir bölümün herhangi bir sınıfında kurs bilgilerini görmemiz gerekiyor.
  
  def calculus_info(self):
    pass  
  def physics_info(self):
    pass
  #calculus_info ve physics_info nun abstract method olmamasının sebebi :
  #her sınıf ya da her bölüm için kullanım gerekliliği yok.
###############################################################################################


#course behaviorlar
# 1.sınıf  ve 2.sınıf-compeng ve electeng bölümleri için
class CompEngFirstYear(CourseBehavior):
  def show_courses(self):
    print("dersler : calculus 1, physics 1, introduction to programming")
  def calculus_info(self):
    print("1.sinif comp eng için calculus : limit, türev temelleri")
  def physics_info(self):
    print("1.sinif comg eng için physics : mekanik ve elektrik ve manyetik alan temelleri")
class ElectricalEngFirstYear(CourseBehavior):
  def show_courses(self):
    print("dersler : calculus 1, physics 1, circuits")
  def calculus_info(self):
    print("1.sinif elect eng için calculus: matematik temelleri")
  def physics(self):
    print("1.sinif elect eng için physics: mekanik ve elektrik ve manyetik alan temelleri")

class CompEngSecondYear(CourseBehavior):
  def show_courses(self):
    print("dersler: calculus 2, data structres")
  def calculus_info(self):
    print("2.sinif comp eng için calculus: integral ve seriler")
class ElectricalEngSecondYear(CourseBehavior):
  def show_courses(self):
    print("dersler : physics 2, signal systems ")
  def physics_info(self):
    print("2.sinif elect eng için physics: termodinamik ve optik")
################################################################################################


#abstract öğrenci sınıfı
#student sınıfı, course behavior interface ini kullanır.
class Student(ABC):
  def __init__(self, course_isaretcisi : CourseBehavior) :
    self.course_isaretcisi = course_isaretcisi
  def uygula_show_courses(self):
    self.course_isaretcisi.show_courses()
  def uygula_calculus_info(self):
    self.course_isaretcisi.calculus_info()
  def uygula_physics_info(self):
    self.course_isaretcisi.physics_info()
  def set_course_isaretcisi(self, course_isaretcisi : CourseBehavior):
    print("sinif atlandi ")
    self.course_isaretcisi = course_isaretcisi

  @abstractmethod
  def display(self):
    pass
    #abstract method olan display i oluşturduk çünkü:
    #studentların, hangi bölüm öğrencisi oluğunu görmek istiyoruz.
################################################################################################


class CompEngStudent(Student):
  def display(self):
    print("\nben comp eng ögrencisiyim \n")
class ElectEngStudent(Student):
  def display(self):
    print("\nben electrical eng ögrencisiyim \n")
#################################################################################################


if __name__ == "__main__" :
  student1 = CompEngStudent(CompEngFirstYear())
  student1.display()
  student1.uygula_show_courses()
  student1.course_isaretcisi.calculus_info()
  student1.course_isaretcisi.physics_info()
  print("\n")
  #2.sınıfa geçerse
  student1.set_course_isaretcisi(CompEngSecondYear())
  student1.uygula_show_courses()
  student1.course_isaretcisi.calculus_info()