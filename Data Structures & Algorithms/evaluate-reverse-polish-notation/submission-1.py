class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        
        for token in tokens:
            # If the token is not an operator, it must be a number
            if token not in {"+", "-", "*", "/"}:
                st.append(int(token))
            else:
                # Pop the top two elements
                a = st.pop()
                b = st.pop()
                
                # Perform the operation and push the result back
                if token == '+':
                    st.append(b + a)
                elif token == '-':
                    st.append(b - a)
                elif token == '*':
                    st.append(b * a)
                elif token == '/':
                    st.append(int(b / a)) # Truncates toward zero
                    
        return st[-1]
            




   	 		


            
        