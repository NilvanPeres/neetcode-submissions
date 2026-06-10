class Solution:
    def isValid(self, s: str) -> bool:
        ''' 1. Classificar caractere como: 'abertura' ou 'fechamento' 
            2. A ordem de dos que fecham devem ser o espelho dos que abrem:
                Equivalente a realizar sucessivos pops enquanto a lista não estiver vazia 
            
            3. Se lista de abertura for igual a pilha, deve retornar true
            '''

        stackOpen = []
  
        # Classificacao dos caracteres
        for char in s:
            if (char == '(' or char == '[' or char == '{'):
                stackOpen.append(char)
            elif (stackOpen):
                element_popped = stackOpen.pop() 
                if ( (element_popped == '(' and char != ')') or (element_popped == '[' and char != ']') or (element_popped == '{' and char != '}')):
                    return False
                else:
                    continue
            elif(not stackOpen):
                return False
        
        if(stackOpen):
            return False
        else:
            return True   
          

      
                



        # Comparar a partir de sucessivos pops (retornando true ou false em caso de não ter um match)
        # Se stackOpen[i] == '(' então stackClose.pop() == ')'

        # Atualmente tem uma falha na precedência (quando for espelhado dá certo)
        # Mas quando está na ordem exata: () [] {} está falhando
        # for i in range(len(stackOpen)):
        #     sequence_element = sta
        #     element_reversed = stackClose.pop()
        #     print("elementReversed: ", element_reversed)
        #     if ((stackOpen[i] == '(' and element_reversed == ')') 
        #         or (stackOpen[i] == '[' and element_reversed == ']') 
        #         or stackOpen[i] == '{' and element_reversed == '}'):
        #         # se vazia, retornar true
        #         if not stackClose:
        #             return True
        #         else:
        #             continue
        #     else:
        #         return False

             

        

