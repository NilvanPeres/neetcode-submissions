class Solution:
    def __init__ (self):
        self.count_0 = 0
        self.count_1 = 0


    def count_zeros_and_ones(self, students: List[int]) -> None:
        for i in range(len(students)):
            if (students[i] == 0):
                self.count_0 += 1
            else:
                self.count_1 += 1

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        self.count_zeros_and_ones(students)
        #enquanto pilha não vazia e há aluno compatível:

        while (sandwiches and not (sandwiches[0] == 0 and self.count_0 == 0) and not (sandwiches[0] == 1 and self.count_1 == 0)):
            # Se for compatível remove da fila e da pilha:
            if (sandwiches[0] == students[0]):
                element = sandwiches[0]
                sandwiches.pop(0)
                students.pop(0)

                if (element == 0):
                    self.count_0 -= 1
                else:
                    self.count_1 -= 1
            # Aluno sai do começo e vai pro final da fila
            else:
                element = students[0]
                students.pop(0)
                students.append(element)

        return len(students)

        # Circular sandwiches = 0
        # Square sandwiches = 1

        # Number of sandwiches == number of students

        # Sandwitches in STACK students in QUEUE

        # Se aluno da fila quiser o sanduiche do topo da fila vai pegar e sair da fila
        # Se não, ele volta para o final da fila. 


        # students = [1,1,0,0], sandwiches = [0,1,0,1]

        '''
            Iteração 1:         
                Aluno 1: 1
                top stack: 0

                students = [1, 0, 0, 1]
                sandwiches = [0,1,0,1]

            Iteração 2:
                Aluno 2: 1
                top stack: 0

                students = [0, 0, 1, 1]
                sandwiches = [0,1,0,1] 

            Iteração 3:
                Aluno 3: 0
                top stack: 0

                students = [0, 1, 1]
                sandwiches = [1,0,1]  

            Iteração 4:
                Aluno 4: 1
                top stack: 0

                students = [1, 1, 0]
                sandwiches = [1,0,1]  

                            Iteração 1:         
                Aluno 1: 1
                top stack: 0

                students = [1, 0, 0, 1]
                sandwiches = [0,1,0,1]

            Iteração 2:
                Aluno 2: 1
                top stack: 0

                students = [0, 0, 1, 1]
                sandwiches = [0,1,0,1] 

            Iteração 3:
                Aluno 3: 0
                top stack: 0

                students = [0, 1, 1]
                sandwiches = [1,0,1]  

            Iteração 5:
                Aluno 5: 0
                top stack: 1

                students = [1, 1, 0]
                sandwiches = [1,0,1]  

            Iteração 6:
                Aluno 6: 1
                top stack: 1

                students = [1, 0]
                sandwiches = [0,1]  

            Iteração 7:
                Aluno 7: 1
                    top stack: 0

                    students = [0, 1]
                    sandwiches = [0,1]  


            Iteração 8:
                Aluno 8: 0
                top stack: 0

                students = [1]
                sandwiches = [1]  


            Iteração 9:
                Aluno 9: 1
                top stack: 1

                students = []
                sandwiches = []  
        '''



