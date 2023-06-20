def validateStackSequences(pushed,popped):
    st=[]
    push_index=0
    pop_index=0
    while push_index < len(pushed):
        st.append(pushed[push_index])
        push_index+=1

        while st and st[-1] == popped[pop_index]:
            st.pop()
            pop_index+=1
    return True if len(st)==0 else False

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print(validateStackSequences(pushed,popped))