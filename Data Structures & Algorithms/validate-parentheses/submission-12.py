class Solution:
    def isValid(self, s: str) -> bool:
        ''' 1. Classificar caractere como: 'abertura' ou 'fechamento' 
            2. A ordem de dos que fecham devem ser o espelho dos que abrem:
                Equivalente a realizar sucessivos pops enquanto a lista não estiver vazia 
            
            3. Se lista de abertura for igual a pilha, deve retornar true
            '''

        stackOpen = []
        pairs = { '(': ')', '[': ']', '{': '}' }

        for char in s:
            if char in pairs:
                stackOpen.append(char)
            elif not stackOpen:
                return False
            else:
                top = stackOpen.pop()
                if pairs[top] != char:
                    return False

        return not stackOpen
                




             

        

