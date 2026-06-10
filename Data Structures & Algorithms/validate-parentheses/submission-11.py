class Solution:
    def isValid(self, s: str) -> bool:
        ''' 1. Classificar caractere como: 'abertura' ou 'fechamento' 
            2. A ordem de dos que fecham devem ser o espelho dos que abrem:
                Equivalente a realizar sucessivos pops enquanto a lista não estiver vazia 
            
            3. Se lista de abertura for igual a pilha, deve retornar true
            '''

        stackOpen = []

        close_to_open = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
  
        # Classificacao dos caracteres

        for char in s:
            #Checar se é do tipo 'closing' - itera pela 'key' do 'map'   
            if char in close_to_open:
                # Stack não pode estar vazia
                if stackOpen and stackOpen[-1] == close_to_open[char]:
                    stackOpen.pop()
                else:
                    return False
            else:
                stackOpen.append(char)

        return True if not stackOpen else False
                




             

        

