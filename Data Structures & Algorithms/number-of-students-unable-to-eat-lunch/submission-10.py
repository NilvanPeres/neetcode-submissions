class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        result = len(students)
        cnt = {}

        # Dict para saber de match entre aluno e tipo de sanduiche
        for s in students:
            cnt[s] = cnt.get(s, 0) + 1
    
        # Itera sobre as comidas e vê se há aluno compatível na fila...
        for s in sandwiches:
            if cnt.get(s, 0) > 0:
                result -= 1 # Tira aluno da fila
                cnt[s] -= 1 #Atualiza 'value' da respectiva do key do dict
            else:
                return result #Early exit
        
        return result