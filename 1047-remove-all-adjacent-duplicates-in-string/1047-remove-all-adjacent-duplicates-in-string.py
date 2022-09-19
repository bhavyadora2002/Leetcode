class Solution:
    def removeDuplicates(self, s: str) -> str:
        st,top=[],-1
        for i in s:
            if top==-1:
                st.append(i)
                top=0
            else:
                if st[top]==i:
                    st.pop()
                    top-=1
                else:
                    st.append(i)
                    top+=1
        return "".join(st)